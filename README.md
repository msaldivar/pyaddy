# pyaddy
A Python cli to interact with addy.io


## How to use
* In your python environment install the package - e.g. using poetry
* `poetry add pyaddy`
* `addy --help`
* You must first run the `load-key` cmd otherwise all other cmds will fail 

## Example output

Usage: addy [OPTIONS] COMMAND [ARGS]...

&nbsp;&nbsp;&nbsp;  Entry point for the cli

Options: \
&nbsp;&nbsp;&nbsp;--version  Show the version and exit. \
&nbsp;&nbsp;&nbsp;--help     Show this message and exit.

Commands: \
  &nbsp;&nbsp;&nbsp; get-acount-details  Get all account details associated with api key \
  &nbsp;&nbsp;&nbsp; get-api-details     Get api details to confirm key is valid \
  &nbsp;&nbsp;&nbsp; load-key            Supply your addy api-key \