# Passive permeability based on simulations

Using Coarse Grained (CG) models, where several atoms are aggregated into a single bead, the authors obtain a set of 500,000 compounds with their simulated permeability across a single-component DOPC lipid bilayer. With this approach, the authors are able to cover a large and representative portion of the chemical space. We have used the data generated in this publication to train a simple regression model to predict compound permeability.

This model was incorporated on 2021-11-10.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2hbd`
- **Slug:** `passive-permeability`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Permeability`, `ADME`, `Papp`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Permeability coefficient (P). Cut-off: 6

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| log10_permcoeff | float | high | Log10 of permeability coefficient |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2hbd](https://hub.docker.com/r/ersiliaos/eos2hbd)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2hbd.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2hbd.zip)

### Resource Consumption
- **Model Size (Mb):** `7`
- **Environment Size (Mb):** `1722`


### References
- **Source Code**: [https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended](https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended)
- **Publication**: [https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended](https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2hbd
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2hbd
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
