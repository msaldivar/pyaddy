# pyaddy
A Python CLI to interact with addy.io


## Installing
* In your python environment install the package - e.g. using poetry
* `poetry add pyaddy`
* `addy --help`
* You must first run the `load-key` cmd otherwise all other cmds will fail
* Note requires 3.11+ 

## Basic Usage - see command section for example output
```
Usage: addy <command> <subcommand> [options & parameters]

  CLI tool to interact with addy.io api:

  Run load_key first to add api key:

  addy load_ley <key goes here>

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  load-key  Load api key.
  api       Invoke details about the provided api key
  alias     Invoke alias commands: --help for details
  bulk      Invoke bulk alias commands: --help for details
```

## Commands
### load-key
```
addy load-key addy_io_key 

Key saved
```

### api
```
Usage: addy api [OPTIONS] COMMAND [ARGS]...

  Invoke details about the provided api key

Options:
  --help  Show this message and exit.

Commands:
  account-details  Get all account details associated with api key
  api-details      Check the details of the api key

```


### alias
```
Usage: addy alias [OPTIONS] COMMAND [ARGS]...

  Invoke alias commands: --help for details

  addy alias <subcommand>

Options:
  --help  Show this message and exit.

Commands:
  activate    Activate alias ID
  deactivate  Deactivate alias ID
  delete      Delete alias ID
  forget      Forget alias ID
  get         Get ID details
  get-all     Get details about all ACTIVE aliases SORTED by CREATED_AT.
              OPTION: --only-ids
  new         Create a new alias. --help for all options
  restore     Restore alias ID
  update      Update alias "descprition" and "from_name
```

## bulk
```
Usage: addy bulk [OPTIONS] COMMAND [ARGS]...

  Invoke bulk alias commands: --help for details

  addy bulk <subcommand>

Options:
  --help  Show this message and exit.

Commands:
  activate     Bulk activate list of aliases. Supply a comma-seperated list of
               alias IDs -e.g. ID1,ID2. --help for more info
  deactivate   Bulk deactivate list of aliases. Supply a comma-seperated list
               of alias IDs -e.g. ID1,ID2. --help for more info
  delete       Bulk delete list of aliases. Supply a comma-seperated list of
               alias IDs -e.g. ID1,ID2. --help for more info
  get-aliases  Get detailed info on aliases. Supply a comma-seperated list of
               alias IDs -e.g. ID1,ID2. --help for more info
  restore      Bulk restore list of aliases. Supply a comma-seperated list of
               alias IDs -e.g. ID1,ID2. --help for more info
```


## Testing
From source run:
```
pytest tests/
```  

## Development
Feel free to open a pr or file an issue. I'm working on adding new features and plan regular releases! 