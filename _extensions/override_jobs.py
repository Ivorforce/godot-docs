# -*- coding: utf-8 -*-
import re
from docutils import nodes
from sphinx import addnodes
import multiprocessing

def setup(app):
    app.parallel = multiprocessing.cpu_count()

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
