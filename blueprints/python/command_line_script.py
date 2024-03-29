#!/usr/bin/env python

import os
import sys

from .base import PythonBlueprint

class CommandLineScript(PythonBlueprint):
    """ 
    :synopsis: Class ScriptBase
    """
    
    class Meta:
        name = "command_line_script"
        namespace = 'python'
        aliases = ("cli",)
        version = (1,0,0)
        usage = '%prog python.command_line_script -f/--filename filename\n%prog python.command_line_script filename'
    # end class Meta
        
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
    def run(self, context, args):
        filename = context.get('filename') or args[0]
        context['filename'] = filename
        context['std_libs'] = ['from optparse import OptionParser']
        file_path = os.path.join(context['working_dir'], filename)
        output_fd = open(file_path, 'w')
        output_fd.write(self.renderTemplate('cmdline_script.txt', context))
        output_fd.close()
        self.log.info("Generated: %s", file_path)
    # end def run
    
# end class CommandLineScript