flags = [
    {
        "name": "--csv",
        "description": "Create Comma-Separated Values (CSV) File.",
    },{
        "name": "--xlsx",
        "description": "Create the standard file for the modern Microsoft Excel spreadsheet (xslx)."
    }, {
        "name": "--print-all",
        "description": "Output sites where the username was not found."
    }, {
        "name": "--print-found",
        "description": "Output sites where the username was found."
    }, {
        "name": "--folderoutput",
        "description": "If using multiple usernames, the output of the results will be saved to this folder.",
        "text": True,
        "text_label": "Folder Name:"
    }, {
        "name": "--output",
        "description": "If using single username, the output of the result will be saved to this file.",
        "text": True,
        "text_label": "File Name:"
    }, {
        "name": "--no-color",
        "description": "Don't color terminal output",
    }, {
        "name": "--browse",
        "description": "Browse to all results on default browser."
    }, {
        "name": "--local",
        "description": "Force the use of the local data.json file."
    }, {
        "name": "--nsfw",
        "description": "Include checking of NSFW sites from default list."
    }, {
        "name": "--tor",
        "description": "Make requests over Tor; increases runtime; requires Tor to be installed and in system path."
    }, {
        "name": "--unique-tor",
        "description": "Make requests over Tor with new Tor circuit after each request; increases runtime; requires Tor to be installed and in system path."
    }, {
        "name": "--proxy",
        "description": "Make requests over a proxy. e.g. socks5://127.0.0.1:1080",
        "text": True,
        "text_label": "Proxy URL:"
    }, {
        "name": "--json",
        "description": "Load data from a JSON file or an online, valid, JSON file.",
        "text": True,
        "text_label": "Json:"
    }, {
        "name": "--timeout",
        "description": "Time (in seconds) to wait for response to requests (Default: 60)",
        "text": True,
        "text_label": "Timeout:"
    }
]