#!/usr/bin/env python

import sys
import os

from .base import PythonBlueprint

class CommandLineScript(PythonBlueprint):
    """ 
    :synopsis: Class ScriptBase
    """
    
    class Meta:
        name = "command_line_script"
        namespace = 'python'
        aliases = ("cls",)
        version = (1,0,0)
        usage = '%prog python.command_line_script -n/--filename filename\n%prog python.command_line_script filename'
    # end class Meta
        
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
    def run(self, context, args):
        filename = context.get('filename') or args[0]
        context['filename'] = filename
        file_path = os.path.join(context['working_dir'], filename)
        output_fd = open(file_path, 'w')
        output_fd.write(self.renderTemplate('cmdline_script.txt', context))
        output_fd.close()
        print "Generated: %s" % file_path
    
# end class CommandLineScript