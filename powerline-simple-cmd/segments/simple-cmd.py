from __future__ import absolute_import
# vim:fileencoding=utf-8:noet

import string
import subprocess


def cmd(pl, segment_info):
    """Returns a unicode sock, and either an up or down arrow
    """
    output = subprocess.run(cmd,stdout=subprocess.PIPE).output
    return output.decode('utf-8').strip('\n')
