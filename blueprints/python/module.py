#!/usr/bin/env python
import os
import sys

from .base import PythonBlueprint

class Module(PythonBlueprint):
    """ 
    :synopsis: Class ScriptBase
    """
    
    class Meta:
        name = "module"
        namespace = 'python'
        aliases = ("mod",)
        version = (1,0,0)
        usage = '%prog python.module -n/--filename filename\n%prog python.module filename'
    # end class Meta
        
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
    def run(self, context, args):
        filename = context.get('filename') or args[0]
        context['filename'] = filename
        file_path = os.path.join(context['working_dir'], filename)
        output_fd = open(file_path, 'w')
        output_fd.write(self.renderTemplate('module.txt', context))
        output_fd.close()
        self.log.info("Generated: %s", file_path)
    # end def run
    
# end class CommandLineScript