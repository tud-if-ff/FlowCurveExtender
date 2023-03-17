# FlowCurveExtender

**Analysing tensile test beyond the necking point.**  

Standard tensile test enable the computation of the hardening curve only+
up to the necking point. This software enable the computation of the strain-stress value for 
higher strain, based of local DIC information for more information see "future link to EFB merkblatt"

# Instalation

Before using or installing the software please inform yourself about the license in the corresponding section.
If you wish only to use the gui and you are a Windows user, you can download the latest
compiled release (.exe) of this software [here](https://github.com/tud-if-ff/FlowCurveExtender/releases/latest).

Otherwise, please install the python packet DIC_Exchange first.
Then download the latest wheel (.whl) [here](https://github.com/tud-if-ff/FlowCurveExtender/releases/latest).
You can install the wheel with the following:
 
`pip install <name>.whl`

# Usage

To use the software you need to have your DIC information stored in an hdf5 data,
for more information see here.  
A conversion tool is provided for xml export of GOM Aramis Data.
For an Aramis script to export data in xml, see the script folder of this repository.  
Further documentation is available here.

# License

Copyright (c) 2022. Chair of Forming and Machining Processes, TU Dresden  

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

This program make use of the following library:

* [NumPy](https://numpy.org/doc/stable/license.html) 
* [SciPy](https://projects.scipy.org/scipylib/license.html)
* [tqdm](https://pypi.org/project/tqdm/)
* [PySide6](https://pypi.org/project/PySide6/)
* [Matplotlib](https://matplotlib.org/stable/users/project/license.html)

the software is provided as is,


# Devellopement and financing

## Devellopers
This software was developed at the chair of forming and machining processes
of the technical university of Dresden.

This following persons taked part in the software development:

* Prof. Alexander Brosius (project management)
* Rémi Lafarge (main developer)
* Robert König  
* Felix Hackenbeck


## Grant information
This work was part of the project "Auswertungserweiterung Zugversuch" 
supported by the [EFB](https://www.efb.de) under project number 08/120
financed by the [AIF](https://www.aif.de) under grant number 21358BR.



