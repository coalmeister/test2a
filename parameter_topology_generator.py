```python
from openmm import app
from openmm import ForceField

def generate_parameters_topology(protein_structure, ligand_structures):
    # Load AMBER and GAFF forcefields
    forcefield = ForceField('amber14-all.xml', 'gaff.xml')

    parameters = []
    topology = []

    # Generate parameters and topology for protein
    protein_parameters, protein_topology = forcefield.generateTemplates(protein_structure)
    parameters.append(protein_parameters)
    topology.append(protein_topology)

    # Generate parameters and topology for each ligand
    for ligand_structure in ligand_structures:
        ligand_parameters, ligand_topology = forcefield.generateTemplates(ligand_structure)
        parameters.append(ligand_parameters)
        topology.append(ligand_topology)

    return parameters, topology
```