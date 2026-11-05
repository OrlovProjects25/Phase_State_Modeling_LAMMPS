Theme: Modeling Phases of Metals with LAMMPS

Created by: Aleksandr Orlov

The project focuses on calculating the melting point of aluminum using LAMMPS, through simulating its behaviour when it changes phases. The coexistence method is used:
two groups of atoms are put next to each other - the first one is the aluminum liquid at high temperature (3000 K); the second one is aluminum at the currently observed temperature. These two groups are then made to reach the required temperature together, eventually either becoming a solid or a liquid.
Using the probabilities at different temperatures for the material to become a liquid, I calculate the melting pont of aluminum at 925.6K.

The code is written on LAMMPS internal language and Python.

To get the files for specific temperatures (how system's energy per atom changes over time), run 'runMod.sh'

The files for specific temperatures can be viewed in "results"

The graphs for the simulations of temperatures can be viewed in "results/Graphs"
To get the graphs, run "Get_graphs.py"

The code ("in.eim") for modeling the potential energies for the lines and the lines themselves can be viewed in "Lines"

The formula derived from the Boltzmann distribution that is used to get a line of best fit is in "Probabilities_over_temperature.pdf"

The code for getting a line of best fit for Probabilities(Temp) is in "Curve_fit.py"

The graph of Probabilities(Temp) along with the value of the melting point is in "Plot_Probabilities(Temp).png"

