```python
import Bio.PDB

def read_protein_structure(protein_file):
    parser = Bio.PDB.PDBParser(QUIET=True)
    protein_structure = parser.get_structure('protein', protein_file)
    return protein_structure
```