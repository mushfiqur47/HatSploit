"""
MIT License

Copyright (c) 2020-2023 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pex.proto.ssh import SSHClient
from hatsploit.lib.option import *


class SSH(object):
    """ Subclass of hatsploit.lib.module.proto module.

    This subclass of hatsploit.lib.module.proto module is a representation
    of a wrapper of SSH client for a module.
    """

    def __init__(self) -> None:
        super().__init__()

        self.timeout = IntegerOption(10, "Connection timeout.", False)
        self.host = IPv4Option(None, "SSH host.", True)
        self.port = PortOption(22, "SSH port.", True)
        self.username = Option(None, "SSH username.", True)
        self.password = Option(None, "SSH password.", True)

    def open_ssh(self) -> SSHClient:
        """ Open SSH client.

        :return SSHClient: SSH client
        """

        return SSHClient(
            host=self.host.value,
            port=self.port.value,
            username=self.username.value,
            password=self.password.value,
            timeout=self.timeout.value
        )
