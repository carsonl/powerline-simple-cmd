# vim:fileencoding=utf-8:noet
from __future__ import absolute_import

import string
import subprocess
import powerline.lib.shell


def cmd(pl=None, command="/bin/echo None"):
    """Returns a the output of a command, or nothing if the output is also nothing
    """
    result = subprocess.getoutput(command)
    stripped_result = result.strip('\n')
    if len(stripped_result) == 0:
        return None
    else:
        return [{"contents":stripped_result,"highlight_groups":["window"]}]

if __name__ == '__main__':
    print(cmd(command="/bin/echo test"))
