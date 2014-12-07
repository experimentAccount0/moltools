.. image:: https://coveralls.io/repos/fishstamp82/dalton_tools/badge.png :target: https://coveralls.io/r/fishstamp82/dalton_tools 

pyclasses
=========

Main files used daily is:

read_dal.py
molecules.py


The file 

template.py

contains templates for molecule properties derived analytically for water modeles, and is used by the class
Molecule to add the class Property to all atomic sites to a molecule.

right now only water molecules are implemented.



read_dal.py is used to generate qmmm input files for dalton. Right now used with Water molecules.
