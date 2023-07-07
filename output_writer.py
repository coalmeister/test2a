```python
import csv

def write_output(output_filename, energy, residue_interaction_energies):
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['ligand_index', 'total_energy'] + [f'residue_{i}_interaction' for i in range(len(residue_interaction_energies[0]))]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i, (total_energy, residue_energies) in enumerate(zip(energy, residue_interaction_energies)):
            row_dict = {'ligand_index': i, 'total_energy': total_energy}
            row_dict.update({f'residue_{j}_interaction': energy for j, energy in enumerate(residue_energies)})
            writer.writerow(row_dict)
```