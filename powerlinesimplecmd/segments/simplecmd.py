from __future__ import absolute_import
# vim:fileencoding=utf-8:noet

import string
import subprocess


def cmd(pl, command):
    """Returns a unicode sock, and either an up or down arrow
    """
    result = subprocess.run(command,stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip('\n')
