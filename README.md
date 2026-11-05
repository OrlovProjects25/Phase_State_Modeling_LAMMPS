Theme: Modeling Phases of Metals with LAMMPS

Created by: Aleksandr Orlov

The project focuses on calculating the melting point of aluminum using LAMMPS, through simulating its behaviour when it changes phases. The coexistence method is used:
two groups of atoms are put next to each other - the first one is the aluminum liquid at high temperature (3000 K); the second one is aluminum at the currently
observer temperature. These two groups are then made to reach the required temperature together, eventually either becoming a solid or a liquid.
Using the probabilities at different temperatures for the material to become a liquid, I calculate the melting pont of aluminum at 925.6K.

The code is written on LAMMPS internal language.

To get the files for specific temperatures (how system's energy per atom changes over time), run 'runMod.sh'
The files for specific temperatures can be viewed in "Temperatures"
The graphs for the simulations of temperatures can be viewed in "Graphs"
The code for modeling the potential energies for the lines and the excel table can be seen

To get the graphs, run Make_graphs.py

