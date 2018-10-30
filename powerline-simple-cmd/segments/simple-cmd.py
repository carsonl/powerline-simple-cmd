from __future__ import absolute_import
# vim:fileencoding=utf-8:noet

import string
import subprocess

from powerline.theme import requires_segment_info


@requires_segment_info
def cmd(pl, cmd=true):
    """Return back the vengo environment prompt
    """

    vengo_env = segment_info['environ'].get('VENGO_ENV')
    if vengo_env is not None:
        return os.path.basename(vengo_env)
from __future__ import absolute_import



@requires_segment_info
def cmd(pl, segment_info):
    """Returns a unicode sock, and either an up or down arrow
    """
    output = subprocess.run(cmd,stdout=subprocess.PIPE).output
    return output.decode('utf-8').strip('\n')
