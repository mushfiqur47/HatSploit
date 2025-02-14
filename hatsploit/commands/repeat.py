"""
This command requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.command import Command
from hatsploit.lib.commands import Commands


class HatSploitCommand(Command):
    def __init__(self):
        super().__init__()

        self.commands = Commands()

        self.details.update({
            'Category': "developer",
            'Name': "repeat",
            'Authors': [
                'Ivan Nikolsky (enty8080) - command developer',
            ],
            'Description': "Repeat specified command.",
            'Usage': "repeat <times> <command>",
            'MinArgs': 2,
        })

    def run(self, argc, argv):
        if argv[1].isdigit():
            commands = self.format_commands(argv[2])

            for _ in range(int(argv[1])):
                self.commands.execute_command(commands)
        else:
            self.print_error("Times expected!")
