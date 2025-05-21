import joblib
import csv
import os, sys
import numpy as np

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rd


PATH = os.path.dirname(os.path.abspath(__file__))

checkpoints_dir = os.path.join(PATH, "../../checkpoints/")

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

mols = []
idxs = []
for i, smi in enumerate(smiles):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        continue
    idxs += [i]
    mols += [mol]

RADIUS = 3
NBITS = 2048
DTYPE = np.int8


def clip_sparse(vect, nbits):
    l = [0]*nbits
    for i,v in vect.GetNonzeroElements().items():
        l[i] = v if v < 127 else 127
    return l


class Descriptor(object):

    def __init__(self):
        self.nbits = NBITS
        self.radius = RADIUS

    def calc(self, mol):
        v = rd.GetHashedMorganFingerprint(mol, radius=self.radius, nBits=self.nbits)
        return clip_sparse(v, self.nbits)

X = np.zeros((len(mols), NBITS), dtype=np.int8)

desc = Descriptor()
for i, mol in enumerate(mols):
    X[i,:] = desc.calc(mol)

mdl = joblib.load(os.path.join(checkpoints_dir, "flaml.joblib"))
preds = mdl.predict(X)

y = [None]*len(smiles)
for i, p in zip(idxs, preds):
    y[i] = p

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["log10_permcoeff"])
    for r in y:
        if r is None:
            writer.writerow(["None"])
        else:
            writer.writerow([r])
