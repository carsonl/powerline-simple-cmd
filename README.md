## Powerline extension for running a simple command

(Templated from: https://github.com/DamnWidget/powerline-segment-vengo)

Just a simple segment extension to run a simple command,
and add the output to a segment (stripped of newline characters)

### Install
Install using pip:
`pip install git+https://github.com/carsonl/powerline-simple-cmd.git`

### Configure

Add to your tmux (or shell, I guess) theme a new section containing:

```json
{
    "function": "powerline-simple-cmd.segments.simple-cmd.cmd",
    "args": [
	"cmd": "your_cmd_here"
    ]
    "priority": 50
}
 ```
