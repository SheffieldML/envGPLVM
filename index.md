---
layout: page
title: PANAMA/LIMMI
tagline: 
---
{% include JB/setup %}


PANAMA and LIMMI are probabilistic models that account for confounding and environmental factors in eQTL studies.

### PANAMA

<div style="float: left; margin-right:15px"><img src="assets/images/expr_cov.png" /></div> 

Hidden confounding factors, such as unobserved covariates or unknown subtle environmental perturbations can create spurious false associations or mask real genetic association signals. In contrast to previous methods, PANAMA learns hidden factors jointly with the effect of prominent genetic regulators. As a result, this new model can more accurately distinguish true genetic association signals from confounding variation.

[N. Fusi,O. Stegle and N. D. Lawrence, _"Joint modelling of confounding factors and prominent genetic regulators provides increased accuracy in genetical genomics studies"_, PLoS Computational Biology, 2012](http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1002330)


### LIMMI

<div style="float: left; margin-right:15px"><img src="assets/images/limmi.png" /></div> 

LIMMI is a novel approach to detect genotype-environment interactions with unmeasured environmental
factors, and is able to recover the unmeasured environmental state solely from gene expression data.
Once learnt, these variables can be used in genetic analyses to investigate interactions between environmental factors and genotype with a regulatory effect on gene expression levels.

**PANAMA and LIMMI share the same codebase, and it's possible to switch between them by passing the --limmi command line argument**