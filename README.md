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
```
Commands:
 \
  **activate-alias:** \
  Activate an alias. Pass ID of alias to activate

  **api:**\
  Invoke details about the provided api key

  **bulk-activate-aliases:** \
  Bulk activate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2

  **bulk-deactivate-aliases:** \
  Bulk deactivate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2

  **bulk-delete-aliases:** \
  Bulk delete list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2

  **bulk-restore-aliases:** \
  Bulk restore list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2

  **create-new-alias:** \
  see --help for all options

  **deactivate-alias:** \
  Deactivate alias. Pass ID of alias to activate

  **delete-specific-alias:** \
  Delete an alias. Pass ID of alias to delete

  **forget-specific-alias:** \
  Forget an alias. Pass ID of alias to forget

  **get-all-aliases:** \
  Default: Get details about all ACTIVE aliases SORTED by CREATED_AT. --help to see all options and filtering

  **get-bulk-aliases:** \
  Get detailed info on aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2

  **get-specific-alias:** \ 
  Get details about a specific alias

  **load-key:** \
  Load api key.

  **update-specific-alias:** \
  Update a specific alias descprition and from_name. Pass ID of alias


## Commands
### load-key
```
addy load-key addy_io_key 

Key saved
```

### active-alias
```
addy activate-alias 50c9e585-e7f5-41c4-9016-9014c15454bc

 {
    "data": {
        "id": "50c9e585-e7f5-41c4-9016-9014c15454bc",
        "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
        "aliasable_id": null,
        "aliasable_type": null,
        "local_part": "pyaddy",
        "extension": null,
        "domain": "addymail.com",
        "email": "py.addy@addymail.com",
        "active": true,
        "description": "pyaddy email",
        "from_name": null,
        "emails_forwarded": 1,
        "emails_blocked": 0,
        "emails_replied": 0,
        "emails_sent": 1,
        "recipients": [],
        "created_at": "2023-10-31 16:10:06",
        "updated_at": "2023-11-11 22:17:30",
        "deleted_at": null
    }
}
```

### bulk-activate-aliases
```
addy bulk-activate-aliases 50c9e585-e7f5-41c4-9016-9014c15454bc,c549db7d-5fac-4b09-9443-9e47f644d29f

Bulk Activated Aliases Info: 
 {
    "message": "2 aliases activated successfully",
    "ids": [
        "50c9e585-e7f5-41c4-9016-9014c15454bc",
        "c549db7d-5fac-4b09-9443-9e47f644d29f"
    ]
}
```

### bulk-deactivate-aliases
```
addy bulk-deactivate-aliases c549db7d-5fac-4b09-9443-9e47f644d29f,50c9e585-e7f5-41c4-9016-9014c15454bc7
Bulk Deactivated Aliases Info: 
 {
    "message": "2 aliases deactivated successfully",
    "ids": [
        "c549db7d-5fac-4b09-9443-9e47f644d29f",
        "50c9e585-e7f5-41c4-9016-9014c15454bc"
    ]
}
```

### bulk-delete-aliases
```
addy bulk-delete-aliases c549db7d-5fac-4b09-9443-9e47f644d29f,50c9e585-e7f5-41c4-9016-9014c15454bc
Bulk Deactivated Aliases Info: 
 {
    "message": "2 aliases deactivated successfully",
    "ids": [
        "c549db7d-5fac-4b09-9443-9e47f644d29f",
        "50c9e585-e7f5-41c4-9016-9014c15454bc"
    ]
}
```

### bulk-restore-aliases
```
addy bulk-restore-aliases c549db7d-5fac-4b09-9443-9e47f644d29f,50c9e585-e7f5-41c4-9016-9014c15454bc
Bulk Restore Aliases Info: 
 {
    "message": "2 aliases restored successfully",
    "ids": [
        "c549db7d-5fac-4b09-9443-9e47f644d29f",
        "50c9e585-e7f5-41c4-9016-9014c15454bc"
    ]
}
```

### create-new-alias
```
addy create-new-alias
Create New Alias Info: 
 {
    "data": {
        "id": "8401cb92-05b0-4fc6-95a0-1e892d50d9a4",
        "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
        "aliasable_id": null,
        "aliasable_type": null,
        "local_part": "frayed.jacket4",
        "extension": null,
        "domain": "addymail.com",
        "email": "frayed.jacket4@addymail.com",
        "active": true,
        "description": null,
        "from_name": null,
        "emails_forwarded": 0,
        "emails_blocked": 0,
        "emails_replied": 0,
        "emails_sent": 0,
        "recipients": [],
        "created_at": "2023-11-12 19:27:26",
        "updated_at": "2023-11-12 19:27:26",
        "deleted_at": null
    }
}
```

### deactivate-alias
```
addy deactivate-alias 8401cb92-05b0-4fc6-95a0-1e892d50d9a4

Deactivated 8401cb92-05b0-4fc6-95a0-1e892d50d9a4
```

### delete-specific-alias
```
addy delete-specific-alias 8401cb92-05b0-4fc6-95a0-1e892d50d9a4

Deleted 8401cb92-05b0-4fc6-95a0-1e892d50d9a4
```

### forget-specific-alias
```
addy forget-specific-alias 50c9e585-e7f5-41c4-9016-9014c15454bc

Forgot 50c9e585-e7f5-41c4-9016-9014c15454bc
```

### get-account-details
```
addy api account-details

Account Details:
{
    "data": {
           "id": "50c9e585-e7f5-41c4-9016-9014c15454bc",
            "username": "johndoe",
            "from_name": "John Doe",
            "email_subject": "Private Subject",
            "banner_location": "off",
            "bandwidth": 10485760,
            "username_count": 2,
            "username_limit": 3,
            "default_recipient_id": "46eebc50-f7f8-46d7-beb9-c37f04c29a84",
            "default_alias_domain": "anonaddy.me",
            "default_alias_format": "random_words",
            "subscription": "pro",
            "subscription_ends_at": null,
            "bandwidth_limit": 0,
            "recipient_count": 12,
            "recipient_limit": 20,
            "active_domain_count": 4,
            "active_domain_limit": 10,
            "active_shared_domain_alias_count": 50,
            "active_shared_domain_alias_limit": 0,
            "active_rule_count": 4,
            "active_rule_limit": 5,
            "total_emails_forwarded": 488,
            "total_emails_blocked": 6,
            "total_emails_replied": 95,
            "total_emails_sent": 17,
            "total_aliases": 529,
            "total_active_aliases": 481,
            "total_inactive_aliases": 19,
            "total_deleted_aliases": 29,
            "created_at": "2019-10-01 09:00:00",
            "updated_at": "2019-10-01 09:00:00"
    }
}
```

### get-all-aliases
```
addy get-all-aliases

All Aliases: 
 {
    "data": [
        {
            "id": "ff27c17f-b94b-4752-9233-7004a9f53357",
            "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
            "aliasable_id": null,
            "aliasable_type": null,
            "local_part": "campus.proclaim40",
            "extension": null,
            "domain": "addymail.com",
            "email": "campus.proclaim40@addymail.com",
            "active": true,
            "description": "ayg screenshot",
            "from_name": null,
            "emails_forwarded": 1,
            "emails_blocked": 0,
            "emails_replied": 0,
            "emails_sent": 1,
            "created_at": "2023-09-21 16:10:06",
            "updated_at": "2023-11-12 19:17:14",
            "deleted_at": null
        },
        {
            "id": "8eb05144-d0a4-4650-8999-5f078b394907",
            "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
            "aliasable_id": null,
            "aliasable_type": null,
            "local_part": "aim.entire33",
            "extension": null,
            "domain": "addymail.com",
            "email": "aim.entire33@addymail.com",
            "active": true,
            "description": "kobe post three specials at once",
            "from_name": null,
            "emails_forwarded": 0,
            "emails_blocked": 0,
            "emails_replied": 0,
            "emails_sent": 1,
            "created_at": "2023-09-19 18:03:57",
            "updated_at": "2023-11-12 19:17:14",
            "deleted_at": null
        },
        {
            "id": "efe6a55a-d145-4936-af1b-437ce3dc463d",
            "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
            "aliasable_id": null,
            "aliasable_type": null,
            "local_part": "canopy.stamina198",
            "extension": null,
            "domain": "addymail.com",
            "email": "canopy.stamina198@addymail.com",
            "active": true,
            "description": "golden tickets three specials at once",
            "from_name": null,
            "emails_forwarded": 0,
            "emails_blocked": 0,
            "emails_replied": 0,
            "emails_sent": 0,
            "created_at": "2023-09-19 17:59:44",
            "updated_at": "2023-09-19 17:59:44",
            "deleted_at": null
        },
        "meta": {
        "current_page": 1,
        "from": 1,
        "last_page": 1,
        "links": [
            {
                "url": null,
                "label": "&laquo; Previous",
                "active": false
            },
            {
                "url": "https://app.addy.io/api/v1/aliases?filter%5Bactive%5D=true&sort=-created_at&page%5Bnumber%5D=1",
                "label": "1",
                "active": true
            },
            {
                "url": null,
                "label": "Next &raquo;",
                "active": false
            }
        ],
        "path": "https://app.addy.io/api/v1/aliases",
        "per_page": 100,
        "to": 3,
        "total": 3
    }
}
```

### get-api-details
```
addy api api-details
API details: {
    "name": "Firefox Extension",
    "created_at": "2019-10-01 09:00:00",
    "expires_at": null
}
```

### get-bulk-aliases
```
addy get-bulk-aliases 50c9e585-e7f5-41c4-9016-9014c15454bc c549db7d-5fac-4b09-9443-9e47f644d29f

Detailed Aliases Info:
{
    "data": [
        {
            "id": "50c9e585-e7f5-41c4-9016-9014c15454bc",
            "user_id": "ca0a4e09-c266-4f6f-845c-958db5090f09",
            "aliasable_id": null,
            "aliasable_type": null,
            "local_part": "first",
            "extension": null,
            "domain": "johndoe.anonaddy.com",
            "email": "first@johndoe.anonaddy.com",
            "active": true,
            "description": null,
            "from_name": null,
            "emails_forwarded": 5,
            "emails_blocked": 0,
            "emails_replied": 0,
            "emails_sent": 0,
            "recipients": [],
            "created_at": "2019-10-01 09:00:00",
            "updated_at": "2019-10-01 09:00:00",
            "deleted_at": null
        },
        {
            "id": "c549db7d-5fac-4b09-9443-9e47f644d29f",
            "user_id": "ca0a4e09-c266-4f6f-845c-958db5090f09",
            "domain_id": null,
            "local_part": "second",
            "extension": null,
            "domain": "johndoe.anonaddy.com",
            "email": "second@johndoe.anonaddy.com",
            "active": true,
            "description": null,
            "from_name": null,
            "emails_forwarded": 2,
            "emails_blocked": 1,
            "emails_replied": 0,
            "emails_sent": 0,
            "recipients": [],
            "created_at": "2019-10-01 09:00:00",
            "updated_at": "2019-10-01 09:00:00",
            "deleted_at": null
        }
    ]
}
```

### get-specific-alias
```
addy get-specific-alias

Alias Info: 
 {
    "data": {
        "id": "8eb05144-d0a4-4650-8999-5f078b394907",
        "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
        "aliasable_id": null,
        "aliasable_type": null,
        "local_part": "aim.entire33",
        "extension": null,
        "domain": "addymail.com",
        "email": "aim.entire33@addymail.com",
        "active": true,
        "description": "kobe post three specials at once",
        "from_name": null,
        "emails_forwarded": 0,
        "emails_blocked": 0,
        "emails_replied": 0,
        "emails_sent": 1,
        "recipients": [],
        "created_at": "2023-09-19 18:03:57",
        "updated_at": "2023-11-12 19:17:14",
        "deleted_at": null
    }
}
```

### update-specific-alias
```
addy update-specific-alias 8eb05144-d0a4-4650-8999-5f078b394907 --description "PyAddy Cli"

Updated 8eb05144-d0a4-4650-8999-5f078b394907 Info: 
 {
    "data": {
        "id": "8eb05144-d0a4-4650-8999-5f078b394907",
        "user_id": "7944df11-09bf-48e9-a78f-13585c923bf3",
        "aliasable_id": null,
        "aliasable_type": null,
        "local_part": "aim.entire33",
        "extension": null,
        "domain": "addymail.com",
        "email": "aim.entire33@addymail.com",
        "active": true,
        "description": "PyAddy Cli",
        "from_name": null,
        "emails_forwarded": 0,
        "emails_blocked": 0,
        "emails_replied": 0,
        "emails_sent": 1,
        "recipients": [],
        "created_at": "2023-09-19 18:03:57",
        "updated_at": "2023-11-12 20:51:49",
        "deleted_at": null
    }
}
```

## Testing
From source run:
```
pytest tests/
```  

## Development
Feel free to open a pr or file an issue. I'm working on adding new features and plan regular releases! 