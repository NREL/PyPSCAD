# PyPSCAD

UPDATED - October 2025.

This repository holds test netowrks configured to operate in the PSCAD software, along with generic three-phase averaged switching GFL/GFM models that are scalable and have all parameters exposed for tuning. These models were assembled by Rick Wallace Kenyon during his time at the National Renewable Energy Laboratory and the University of Colorado Boulder. They were built and tuned using a variety of resources that are noted in the publications listed below. The most up to date library of models can be found in Droope/lib.

These models are made freely available to anyone who would like to use them, whether as is or modified to whatever extent is desired. Please simply cite the publication relevant to the work you're doing to give credit to Wallace

The 'Droope' directory holds the test networks used in Sections 5.1 and 5.2 of the most recent publication:
'Autonomous grid-forming inverter exponential droop control for improved frequency stability', IJEPES, 2025
https://www.sciencedirect.com/science/article/pii/S0142061525007082
 
The 39 bus system found in the 'Interactive' directory has been split to operate on 7 cores and was used for the following publication:
 'Frequency Dynamics with Grid Forming Inverters: A New Stability Paradigm', IEEE Systems Journal, 2023
https://ieeexplore.ieee.org/abstract/document/10092276/

The 'Controller_Order' directory has a .zip of the 3_bus model used in the publication:
'Criticality of Inverter Controller Order in Power System Dynamic Studies – Case Study: Maui Island', Electric Power Systems Research, 2023
https://www.sciencedirect.com/science/article/abs/pii/S0378779622008434

The 'GFM-GFL Models' directory are described in the following publication:
'Open-Source PSCAD Grid-Following and Grid-Forming Inverters and A Benchmark for Zero-Inertia Power System Simulations', 2021 Kansas Power and Energy Conference.
https://www.osti.gov/biblio/1780982

Fun Fact - even though this repo is titled 'PyPSCAD', indicating a linking between Python and PSCAD, there is minimal such linking code found in the repo. Although such code was extensively employed during the time of constructing these models, it was deemed not general enough to be helpful to the broader community.

Contact - Wallace Kenyon, wallace@encoord.com, rike4641@colorado.edu