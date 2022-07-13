#!/usr/bin/env python

from bprofile import BProfile

import tempfile
from solve import solve
from factory import SolverFactory

methods = [
    "breadthfirst",
    "depthfirst",

]

def profile():
    for m in methods:
        for i in inputs:
            with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
                solve(SolverFactory(), m, "examples/%s.png" % i, tmp.name)

profiler = BProfile('profiler.png')
with profiler:
    profile()
