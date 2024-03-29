#!/usr/bin/env python
from optparse import make_option

from builder.api.blueprint import Blueprint

class PythonBlueprint(Blueprint):
    """ 
    :synopsis: Class ScriptBase
    """
    
    options = Blueprint.options + [
        make_option('-f', '--filename', action='store')
    ]
    
    def validate(self, context, args):
        if not context.get('filename', None) and not args:
            self.addError('-f/--filename option or filename argument missing')
        
        if self.errors:
            return False
        return True
    # end def validate
# end class PythonBlueprint