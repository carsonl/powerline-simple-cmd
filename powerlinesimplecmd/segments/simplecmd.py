# vim:fileencoding=utf-8:noet
from __future__ import absolute_import

import string
import subprocess
import powerline.lib.shell


def cmd(pl=None, command="/bin/echo None"):
    """Returns a unicode sock, and either an up or down arrow
    """
    result = subprocess.getoutput(command)
    return [{"contents":result.strip('\n'),"highlight_groups":["window"]}]

if __name__ == '__main__':
    print(cmd(command="/bin/echo test"))
