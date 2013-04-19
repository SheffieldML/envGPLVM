---
layout: page
title: Usage
tagline: 
group: navigation
---
{% include JB/setup %}

## Usage 

### Basic usage
PANAMA includes a script that lets you access the basic functionalities without too much pain.

After installing PANAMA, from a terminal, run:

`$ panama expression_data.csv snp_data.csv`

Where expression_data.csv is a Comma Separated Values file containing the gene expression data in the following format

                sample1, sample2, ..., sampleN
         gene1  value ,  value , ...,  value
         gene2  value ,  value , ...,  value
         ...
         geneN

and snp_data.csv contains the SNP data encoded as [0,1,2] in the following format

              sample1, sample2, ..., sampleN 
        SNP1  value ,  value , ...,  value
        SNP2  value ,  value , ...,  value
        ...
        SNPQ

If you need to load data in another format, just contact us.

##### Optional arguments: 
* *-p num_processes*
in order to facilitate the analysis of larger datasets, PANAMA implements a cluster interface that can work seamlessly on the local machine, on a group of machines on the local network (via SSH), on a local cluster (via SunGrid), or on Amazon EC2 (Elastic Cloud Computing). In order to use this feature, you need to have an ipcluster instance running. If you have Ipython 0.12 installed on your machine, running PANAMA on multiple cores on the local machine just requires a ipcluster start from the command line.
For ipython 0.10, the equivalent command would be ipcluster local -n num_processes. PANAMA automatically detects the Ipython version, so no further input is necessary. Read the Ipython documentation for more informations on how to run on networked machines, on clusters and on Amazon EC2

* *-d output_directory*
specify an output directory (default: the current directory)

* *-l logging_level*
how much output do you want from PANAMA? There are 4 possible choices: debug, info, warning, error. The default level is "info", so you will get a good idea of what PANAMA is actually doing in any given moment.



### Advanced usage
Some of the features of PANAMA can't be accessed using the simple panama script provided or need further setup. Here's a list of features that have been implemented and can be accessed through the python API:

imputation of missing genotypes (available from panama.utilities.imputation)
threading configuration for the Intel Math Kernel Library ™(available from panama.utilities.MKL)
reading/writing files in HDF5 (available from panama.utilities.io_wrapper)
storing intermediate results in HDF5 (available from panama.core.testing)
If you want to call PANAMA directly from python, just take a look at the PANAMA function in panama.core.run. The expected arguments are:

expr (required) an NxD numpy array, where N is the number of samples and D is the number of genes.
snps (required) an NxQ numpy array, where N is the number of samples and Q is the number of SNPs.
tf_correction = False [True|False] remove broad genetic effects? This will result in more uniform pvalues, but it will also results in an overcorrection of the data (see the paper for a more extended explanation).
pop_struct = False [True|NxN numpy array] if pop_struct = True, a population structure covariance matrix will be calculated using the genotypes. You can explicitly pass your own population structure covariance matrix as a NxN numpy array.
parallel = True [True|False] run PANAMA in parallel. If True, please also pass the desired number of jobs to run as jobs = num_jobs.
statistics = False [True|False] print some statistics like genomic control, number of significant qvalues, and so on..
If you don't want to hack your way around python, just contact us. We can make some functionalities available from the main script.
