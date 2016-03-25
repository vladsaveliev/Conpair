#!/usr/bin/env python2.7

#
# Version 1.0 2016-02-29
# Ewa Grabowska (egrabowska@nygenome.org)
# New York Genome Center
#

# New York Genome Center
# SOFTWARE COPYRIGHT NOTICE AGREEMENT
# This software and its documentation are copyright (2014) by the New York
# Genome Center. All rights are reserved. This software is supplied without
# any warranty or guaranteed support whatsoever. The New York Genome Center
# cannot be responsible for its use, misuse, or functionality.
# Version: 1.0
# Author: Ewa A Grabowska (egrabowska@nygenome.org)


import numpy as np
from math import log10



def phred2prob(Q):
    return(np.float64(10.0**(-float(Q)/10)))

def log10p(f):
    
    if f < 1e-323:
	return(-324)
    else:
	return(np.log10(f))