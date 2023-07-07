```python
import os
from rdkit import Chem

class LigandReader:
    def __init__(self, ligand_file):
        self.ligand_file = ligand_file
        self.ligand_data = None

    def read_ligand_file(self):
        if not os.path.exists(self.ligand_file):
            raise FileNotFoundError(f"Ligand file {self.ligand_file} not found.")
        self.ligand_data = Chem.SDMolSupplier(self.ligand_file)

    def get_ligand_data(self):
        if self.ligand_data is None:
            self.read_ligand_file()
        return self.ligand_data

if __name__ == "__main__":
    ligand_reader = LigandReader("ligand.sdf")
    ligand_data = ligand_reader.get_ligand_data()
```