#!/usr/bin/env python3

#
# This command requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

import readline

from hatsploit.lib.config import Config
from hatsploit.lib.storage import GlobalStorage
from hatsploit.lib.command import Command


class HatSploitCommand(Command):
    config = Config()

    history = config.path_config['history_path']
    storage_path = config.path_config['storage_path']

    global_storage = GlobalStorage(storage_path)

    usage = ""
    usage += "history <option>\n\n"
    usage += "  -l, --list   List all history.\n"
    usage += "  -c, --clear  Clear all history.\n"
    usage += "  on/off       Turn history on/off.\n"

    details = {
        'Category': "developer",
        'Name': "history",
        'Authors': [
            'Ivan Nikolsky (enty8080) - command developer'
        ],
        'Description': "Manage HatSploit history.",
        'Usage': usage,
        'MinArgs': 1
    }

    def run(self, argc, argv):
        option = argv[0]
        if option == "on":
            self.global_storage.set("history", True)
            self.output_information("HatSploit history: on")
        elif option == "off":
            self.global_storage.set("history", False)
            self.output_information("HatSploit history: off")
        elif option in ['-c', '--clear']:
            readline.clear_history()
            with open(self.history, 'w') as history:
                history.write("")
        elif option in ['-l', '--list']:
            if readline.get_current_history_length() > 0:
                self.output_information("HatSploit history:")

                for index in range(1, readline.get_current_history_length()):
                     self.output_empty("    * " + readline.get_history_item(index))
            else:
                self.output_warning("HatSploit history empty.")
        else:
            self.output_usage(self.details['Usage'])
