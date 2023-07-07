```python
import Bio.PDB

def read_protein_structure(pdb_filename):
    parser = Bio.PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_filename)
    return structure

pdb_filename = 'protein.pdb'
protein_structure = read_protein_structure(pdb_filename)
```