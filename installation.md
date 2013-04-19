---
layout: page
title: Installation
tagline: 
group: navigation
---
{% include JB/setup %}

## Installation and Data

#### Prerequisites:

* python
* numpy and scipy
* matplotlib
* ipython
* cython
* pandas
* pygp
* sphinx

If you already have Python and pip installed, probably pip will take care of installing all the dependencies. *If you don't know how to install these libraries, perhaps the easiest way is to download the Entougth Python Distribution*. 

#### Installing PANAMA and LIMMI

There are two options:

1. Running `pip install panama` (easiest)
2. Download [panama](http://pypi.python.org/pypi/panama) and [pygp](http://pypi.python.org/pypi/pygp), extract them, and then run  

`sudo python setup.py install` 

in the "pygp" directory first, and then in the "panama" directory.

* * *

## Data

This is the simulated data we used in the paper: [simulated.zip](http://ml.sheffield.ac.uk/qtl/panama/data/simulated.zip)



Thanks to Leonid Kruglyak, Erin Smith and Rachel Brem we can also provide the yeast dataset we used for most of our experiments: [yeast_data.zip](http://ml.sheffield.ac.uk/qtl/panama/data/yeast.zip)
