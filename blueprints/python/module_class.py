#!/usr/bin/env python

import os
import sys

from builder.utils import camelcase

from .base import PythonBlueprint

class ClassModule(PythonBlueprint):
    """ 
    :synopsis: Class Module blueprint
    """
    
    class Meta:
        name = "class"
        namespace = 'python'
        aliases = ("cls",)
        version = (1,0,0)
        usage = '%prog python.module -n/--filename filename\n%prog python.module filename'
    # end class Meta
        
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
    def run(self, context, args):
        filename = context.get('filename') or args[0]
        context['filename'] = filename
        context['class'] = camelcase(os.path.splitext( os.path.basename(filename))[0])
        context['inherit'] = 'object'
        file_path = os.path.join(context['working_dir'], filename)
        output_fd = open(file_path, 'w')
        output_fd.write(self.renderTemplate('class_module.txt', context))
        output_fd.close()
        self.log.info("Generated: %s", file_path)
    # end def run
    
# end class CommandLineScript