# -*- coding: utf-8 -*-
#
# archmage -- CHM decompressor
# Copyright (c) 2003 Eugeny Korekin <aaaz@users.sourceforge.net>
# Copyright (c) 2005-2009 Basil Shubin <bashu@users.sourceforge.net>
# Copyright (c) 2015 Mikhail Gusarov <dottedmag@dottedmag.net>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
__all__ = ['CHM']
__version__ = '0.4.0-pre'

import sys, os, pkg_resources

# Global variables
EXTRACT = 1        # Extract CHM content
DUMPHTML = 3    # Dump CHM file as plain text
CHM2TXT = 4        # Convert CHM file into Single Text file
CHM2HTML = 5    # Convert CHM file into Single HTML file
CHM2PDF = 6        # Convert CHM file into PDF Document
#CHM2PS = 7        # Convert CHM file into PDF Document

# what config file to use - local or a system wide?
user_config = os.path.join(os.path.expanduser('~'), '.arch.conf')
if os.path.exists(user_config):
    config = user_config
else:
    config = pkg_resources.resource_filename('archmage', 'arch.conf')

def file2dir(filename):
    """Convert file filename.chm to filename_html directory"""
    dirname = filename.rsplit('.', 1)[0] + '_' + 'html'
    return dirname

def output_format(mode):
    if mode == 'text':
        return CHM2TXT
    elif mode == 'html':
        return CHM2HTML
    elif mode == 'pdf':
        return CHM2PDF
#    elif mode == 'ps':
#        return CHM2PS
    else:
        sys.exit('Invalid output file format: %s' % mode)

def output_file(filename, mode):
    """Convert filename.chm to filename.output"""
    if mode == CHM2TXT:
        file_ext = 'txt'
    elif mode == CHM2HTML:
        file_ext = 'html'
    elif mode == CHM2PDF:
        file_ext = 'pdf'
#    elif mode == CHM2PS:
#        file_ext = 'ps'
    else:
        file_ext = 'output'
    output_filename = filename.rsplit('.', 1)[0] + '.' + file_ext
    return output_filename
