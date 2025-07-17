import joblib
import csv
import os, sys
import numpy as np

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rd
sys.path.append("../code/")
from chemeleon_descriptor import CheMeleonFingerprint


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

# Calculate CheMeleon embeddings
chemeleon_fingerprint = CheMeleonFingerprint()
batch_size, count = 5000, 0
X = []
while count < len(smiles):
    df = chemeleon_fingerprint(smiles[count:count+batch_size])
    X.extend(df)
    count += batch_size
X = np.array(X)

# Load model
mdl = joblib.load(os.path.join(checkpoints_dir, "RF_REG.joblib"))
preds = mdl.predict(X)

# Print output
with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["log10_permcoeff"])
    for r in preds:
        if r is None:
            writer.writerow(["None"])
        else:
            writer.writerow([r])
