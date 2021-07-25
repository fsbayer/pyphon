"""
This is a mess and will need cleaned up.
"""

import xml.etree.ElementTree as ElementTree
import pathlib

libpath = pathlib.Path(__file__).parent.resolve()

errorfile = str(libpath) + '\\errors.xml'
errortree = ElementTree.parse(errorfile)
errors = errortree.getroot()


def ordinal(n): return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


def codecheck(code):
    errtype = errors[code].attrib['code']
    if isinstance(code, int) and code >= 0:
        if int(errtype) == int(code):
            return
        else:
            message = "Mismatch" + str(errtype) + str(code)
    else:
        message = "Not an integer"
    return message


def failmsg(code):
    return codecheck(code)
#    if codecheck(code) == 0:
#        return
#    elif codecheck(code) == 1:
#        msg1 = 'Pyphon tried to handle an internal error with code '
#        msg2 = '. Pyphon error codes must be positive integers (or zero).'
#        message = msg1 + str(code) + msg2
#    elif codecheck(code) == 2:
#        msg1 = 'Malformed error definition file (\'errors.xml\'): Error code '
#        msg2 = ' is not the '
#        msg3 = ' error defined in the file. Errors must be defined in order!'
#        message = msg1 + str(code) + msg2 + ordinal(code + 1) + msg3
#    else:
#        message = 'Error code check failed in error.py[35].'
#    return message


class Error(Exception):
    def __init__(self, code=0):
        self.code = code
        self.message = ''
        fail = failmsg(code)
        if fail is None:
            msg1 = "Internal error "
            msg2 = ": "
            errtitle = errors[code].attrib['title']
            errmsg = errors[code].text
            self.message = msg1 + str(code) + msg2 + errtitle + errmsg
        else:
            raise RuntimeError(fail)
