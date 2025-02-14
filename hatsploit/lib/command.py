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

from hatsploit.core.cli.badges import Badges
from hatsploit.core.cli.colors import Colors
from hatsploit.core.cli.fmt import FMT
from hatsploit.core.cli.tables import Tables


class Command(FMT, Badges, Colors, Tables):
    """ Subclass of hatsploit.lib module.

    This subclass of hatsploit.lib module is intended for providing
    wrapper for a command.
    """

    def __init__(self) -> None:
        super().__init__()

        self.details = {
            'Category': "",
            'Name': "",
            'Authors': [
                ''
            ],
            'Description': "",
            'Usage': "",
            'MinArgs': 0
        }

    def run(self, argc: int, argv: list) -> None:
        """ Run this command.

        :param int argc: number of arguments
        :param list argv: arguments
        :return None: None
        """

        pass
