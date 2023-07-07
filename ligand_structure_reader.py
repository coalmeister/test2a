```python
import os
from rdkit import Chem

def read_ligand_structure(sdf_filename):
    ligand_structures = []
    supplier = Chem.SDMolSupplier(sdf_filename)
    for mol in supplier:
        if mol is not None:
            ligand_structures.append(mol)
    return ligand_structures

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Read ligand structures from SDF file.')
    parser.add_argument('-i', '--input', required=True, help='Input SDF file.')
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        raise FileNotFoundError(f"{args.input} does not exist.")

    ligand_structures = read_ligand_structure(args.input)
```