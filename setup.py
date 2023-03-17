#  Copyright (c) 2023. Chair of Forming and Machining Processes, TU Dresden
#   FlowCurveExtender, analysing tensile test beyond necking point
#   This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU Affero General Public License as
#       published by the Free Software Foundation, either version 3 of the
#       License, or (at your option) any later version.
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU Affero General Public License for more details.
#       You should have received a copy of the GNU Affero General Public License
#       along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='FlowCurveExtender',
    version='',
    packages=['gui', 'core'],
    package_dir={'': 'FlowCurveExtender'},
    url='https://github.com/tud-if-ff/FlowCurveExtender',
    license='AGPL v3.0',
    author='Chair of Forming and Machining Processes, TU Dresden',
    author_email='remi.lafarge@tu-dresden.de',
    description='',
    classifiers=['Private :: Do Not Upload',
                 'Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)'],
    install_requires=[
        'matplotlib~=3.6.2',
        'PySide6~=6.4.2',
        'numpy~=1.23.4',
        'scipy~=1.9.3',
        'shapely~=2.0.1',
        'setuptools~=67.2.0',
        'DIC_Exchange~=0.1a'
    ],
)
