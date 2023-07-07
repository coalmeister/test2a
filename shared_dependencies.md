1. Shared Variables:
   - `protein_structure`: The protein structure data read from the PDB file.
   - `ligand_structures`: The list of ligand structures read from the SDF file.
   - `parameters`: The parameters developed for both protein and ligand using AMBER and GAFF forcefields.
   - `topology`: The topology developed for both protein and ligand using AMBER and GAFF forcefields.
   - `protein_ligand_complex`: The combined protein-ligand object.
   - `energy`: The energy of the protein-ligand complex evaluated using openmm forcefield.
   - `residue_interaction_energies`: The list of interaction energies of each residue from the protein with the ligand.
   - `output_filename`: The filename supplied as a command-line argument for output.

2. Data Schemas:
   - `ProteinStructure`: The schema for the protein structure data.
   - `LigandStructure`: The schema for the ligand structure data.
   - `Parameters`: The schema for the parameters data.
   - `Topology`: The schema for the topology data.
   - `ProteinLigandComplex`: The schema for the combined protein-ligand object.
   - `Energy`: The schema for the energy data.
   - `ResidueInteractionEnergy`: The schema for the interaction energy data.

3. Function Names:
   - `read_protein_structure`: Function to read protein structure file in PDB format.
   - `read_ligand_structure`: Function to read ligand structure file in SDF format.
   - `generate_parameters_topology`: Function to develop parameters and topology for both protein and ligand.
   - `combine_protein_ligand`: Function to combine protein into a single object with ligand.
   - `evaluate_energy`: Function to evaluate the energy of the protein-ligand complex.
   - `calculate_residue_interaction`: Function to compute the energy of interaction of each residue from the protein with the ligand.
   - `write_output`: Function to write the output data to a file.

Note: As the prompt does not mention any JavaScript or DOM elements, they are not included in the shared dependencies.