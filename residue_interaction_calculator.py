```python
from openmm import app
from openmm import unit

def calculate_residue_interaction(protein_ligand_complex, parameters, topology):
    residue_interaction_energies = []
    for residue in protein_ligand_complex.topology.residues():
        for ligand in protein_ligand_complex.topology.residues():
            if ligand != residue:
                system = parameters.createSystem(topology, nonbondedMethod=app.NoCutoff, constraints=None)
                force = system.getForce(0)
                for i in range(force.getNumParticles()):
                    if i in [atom.index for atom in residue.atoms()]:
                        force.setParticleParameters(i, charge=0.0, sigma=1.0, epsilon=0.0)
                for i in range(force.getNumParticles()):
                    if i in [atom.index for atom in ligand.atoms()]:
                        force.setParticleParameters(i, charge=0.0, sigma=1.0, epsilon=0.0)
                integrator = openmm.VerletIntegrator(1.0*unit.femtoseconds)
                simulation = app.Simulation(topology, system, integrator)
                simulation.context.setPositions(protein_ligand_complex.positions)
                state = simulation.context.getState(getEnergy=True)
                energy = state.getPotentialEnergy()
                residue_interaction_energies.append((residue, energy))
    return residue_interaction_energies
```