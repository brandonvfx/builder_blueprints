#!/usr/bin/env python

import os
import sys
from optparse import make_option

from builder.api.blueprint import Blueprint

class TestPlugin(Blueprint):
    class Meta:
        name = 'test_script'
        namespace = 'testing'
        version = (1,0,0)
    # end class Meta
    
    options = Blueprint.options + [
        make_option('--testing', action='store', default='test'),
    ]

    def run(self, context, args):
        self.logger.info("Context: %s", context) 

