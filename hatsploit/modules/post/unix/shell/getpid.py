"""
This module requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.module.basic import *


class HatSploitModule(Module):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': "post",
            'Name': "Unix Shell Get PID",
            'Module': "post/unix/shell/getpid",
            'Authors': [
                'Ivan Nikolsky (enty8080) - module developer',
            ],
            'Description': "Get current session process id.",
            'Platform': OS_UNIX,
            'Rank': "medium",
        })

        self.session = SessionOption(None, "Session to run on.", True,
                                     platforms=[OS_UNIX],
                                     type='shell')

    def run(self):
        pid = self.session.session.send_command("printf $$", True).strip()

        if pid:
            self.print_information(f"PID: {pid}")
