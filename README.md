# Passive permeability based on simulations

Using Coarse Grained (CG) models, where several atoms are aggregated into a single bead, the authors obtain a set of 500,000 compounds with their simulated permeability across a single-component DOPC lipid bilayer. With this approach, the authors are able to cover a large and representative portion of the chemical space. We have used the data generated in this publication to train a simple regression model to predict compound permeability.

## Identifiers

* EOS model ID: `eos2hbd`
* Slug: `passive-permeability`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Permeability coefficient (P). Cut-off: 6

## References

* [Publication](https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended)
* [Source Code](https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/full/10.1021/acscentsci.8b00718?ref=recommended) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!