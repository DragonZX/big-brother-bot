#
# BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright (C) 2005 Michael "ThorN" Thornton
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# $Id: setup.py 103 2006-04-14 16:23:10Z thorn $
#
# Example:
# setup.py dev sdist
# setup.py dev bdist_egg

__author__  = 'ThorN'
__version__ = '1.0.0'


import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

import sys

# use 'register upload' to upload to pypi
if len(sys.argv) == 1:
	sys.argv += ['dev', 'bdist_egg']

setup(
    name = "b3",
    version = "1.1.2",
    packages = find_packages(),
	extras_require = { 'mysql' : 'MySQL-python', 'elementtree' : 'elementtree' },
	package_data = {
		'': ['conf/*.xml', 'extplugins/conf/*.xml', 'docs/*', 'README']
	},
    zip_safe = False,
    #download_url = 'http://b3.python-hosting.com/browser/releases/',
	author = 'Michael Thornton (ThorN), Tim ter Laak (ttlogic)',
    author_email = "bigbrotherbot@gmail.com",
    description = "BigBrotherBot (B3) is a cross-platform, cross-game game administration bot. Features in-game administration of game servers, multiple user access levels, and database storage. Currently include parsers for Call of Duty (CoD) and Call of Duty 2 (CoD2)",
    long_description = """\
Big Brother Bot B3 is a complete and total server administration package for online games. B3 is designed primarily to keep your server free from the derelicts of online gaming, but offers more, much more. With the stock configuration files, B3 will will keep your server free from offensive language, and team killers alike. A completely automated and customizable warning system will warn the offending players that this type of behavior is not allowed on your server, and ultimately kick, and or ban them for a predetermined time limit.

B3 was designed to be easily ported to other online games. Currently, B3 is in production for Call of Duty and Call of Duty: United Offensive and Call of Duty 2. Since these games are based on the Quake III Arena engine, conversion to any game using the engine should be easy.

Plugins provide much of the functionality for B3. These plugins can easily be configured. An SDK will be provided to make your own plugins.
""",
    license = "GPL",
    url = "http://www.bigbrotherbot.com",
	entry_points = {
		'console_scripts': [
			'b3_run = b3.run:main',
		]
	},
    classifiers = [
		'Development Status :: 4 - Beta',
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: System :: Logging',
		'Topic :: Utilities'
	]
)