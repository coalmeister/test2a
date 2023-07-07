```python
import sys
import argparse
from protein_structure_reader import read_protein_structure
from ligand_structure_reader import read_ligand_structure
from parameter_topology_generator import generate_parameters_topology
from protein_ligand_combiner import combine_protein_ligand
from energy_evaluator import evaluate_energy
from residue_interaction_calculator import calculate_residue_interaction
from output_writer import write_output

def main():
    parser = argparse.ArgumentParser(description='Evaluate the energy of protein-ligand complex.')
    parser.add_argument('protein_file', help='Protein structure file in PDB format.')
    parser.add_argument('ligand_file', help='Ligand structure file in SDF format.')
    parser.add_argument('-o', '--output', help='Output filename.', required=True)

    args = parser.parse_args()

    protein_structure = read_protein_structure(args.protein_file)
    ligand_structures = read_ligand_structure(args.ligand_file)

    for ligand_structure in ligand_structures:
        parameters, topology = generate_parameters_topology(protein_structure, ligand_structure)
        protein_ligand_complex = combine_protein_ligand(protein_structure, ligand_structure, parameters, topology)
        energy = evaluate_energy(protein_ligand_complex)
        residue_interaction_energies = calculate_residue_interaction(protein_structure, ligand_structure, protein_ligand_complex)
        write_output(args.output, energy, residue_interaction_energies)

if __name__ == "__main__":
    main()
```