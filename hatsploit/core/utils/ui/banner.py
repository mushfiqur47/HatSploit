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

import os
import random

from colorscript import ColorScript

from hatsploit.core.cli.badges import Badges
from hatsploit.core.cli.colors import Colors
from hatsploit.lib.config import Config


class Banner(object):
    """ Subclass of hatsploit.core.utils.ui module.

    This subclass of hatsploit.core.utils.ui module is intended for
    providing tools for printing banners in UI.
    """

    def __init__(self) -> None:
        super().__init__()

        self.config = Config()
        self.badges = Badges()
        self.colors = Colors()

        self.color_script = ColorScript()

    def print_random_banner(self) -> None:
        """ Print random banner.

        :return None: None
        """

        if os.path.exists(self.config.path_config['banners_path']):
            banners = []
            all_banners = os.listdir(self.config.path_config['banners_path'])

            for banner in all_banners:
                banners.append(banner)

            if banners:
                banner = ""

                while not banner:
                    random_banner = random.randint(0, len(banners) - 1)
                    banner = self.color_script.parse_file(
                        self.config.path_config['banners_path'] + banners[random_banner]
                    )

                self.badges.print_empty(f"%newline%end{banner}%end%newline")
            else:
                self.badges.print_warning("No banners detected.")
        else:
            self.badges.print_warning("No banners detected.")
