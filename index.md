---
layout: page
title: PANAMA/LIMMI
tagline: 
---
{% include JB/setup %}

PANAMA and LIMMI are probabilistic models that account for confounding/environmental factors in eQTL studies.

### PANAMA
Hidden confounding factors, such as unobserved covariates or unknown subtle environmental perturbations can create spurious false associations or mask real genetic association signals. In contrast to previous methods, PANAMA learns hidden factors jointly with the effect of prominent genetic regulators. As a result, this new model can more accurately distinguish true genetic association signals from confounding variation.

[N. Fusi,O. Stegle and N. D. Lawrence, _"Joint modelling of confounding factors and prominent genetic regulators provides increased accuracy in genetical genomics studies"_, PLoS Computational Biology, 2012](http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1002330)


### LIMMI
LIMMI is a novel approach to detect genotype-environment interactions with unmeasured environmental
factors, and is able to recover the unmeasured environmental state solely from gene expression data.
Once learnt, these variables can be used in genetic analyses to investigate interactions between environmental factors and genotype with a regulatory effect on gene expression levels.

**PANAMA and LIMMI share the same codebase, and it's possible to switch between them by passing the --limmi command line argument**


* * *

## Installation

#### Prerequisites:
* Python
* Numpy and Scipy 
* Matplotlib 
* Ipython 
* Cython 
* pandas 
* pygp 
* sphinx

If you already have Python and pip installed, probably pip will take care of installing all the dependencies. *If you don't know how to install these libraries, perhaps the easiest way is to download the Entougth Python Distribution*. 

#### Installing PANAMA and LIMMI
There are two options:
1. Running `pip install panama` (easiest)
2. Download panama and pygp, extract them, and then run 
`sudo python setup.py install` in the "pygp" directory first, and then in the "panama" directory.

* * *

## Data

This is the simulated data we used in the paper:
[simulated.zip](http://ml.sheffield.ac.uk/qtl/panama/data/simulated.zip)

Thanks to Leonid Kruglyak, Erin Smith and Rachel Brem we can also provide the yeast dataset we used for most of our experiments
[yeast_data.zip](http://ml.sheffield.ac.uk/qtl/panama/data/yeast.zip)