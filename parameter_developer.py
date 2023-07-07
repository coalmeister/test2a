```python
import pybel
from openforcefield.topology import Molecule, Topology
from openforcefield.typing.engines.smirnoff import ForceField

def develop_parameters(protein_file, ligand_file):
    # Read protein structure
    protein = pybel.readfile('pdb', protein_file).next()

    # Read ligand structure
    ligand = pybel.readfile('sdf', ligand_file).next()

    # Convert ligand to openforcefield molecule
    ligand_mol = Molecule.from_smiles(ligand.write('can'))

    # Create topology
    topology = Topology.from_molecules([protein, ligand_mol])

    # Load forcefields
    forcefield = ForceField('amber99sb.xml', 'gaff-2.11.xml')

    # Develop parameters
    system = forcefield.create_openmm_system(topology)

    return system
```