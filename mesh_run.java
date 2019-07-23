// STAR-CCM+ macro: mesh_run.java
// Written by STAR-CCM+ 14.02.012
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;
import star.meshing.*;

public class mesh_run extends StarMacro {

  public void execute() {
    execute0();
    execute1();
    // /home/flyntga/git/optuna/ncT002.sim
  }

  private void execute0() {

    // remesh
    Simulation simulation_0 =  getActiveSimulation();
    MeshPipelineController meshPipelineController_0 = simulation_0.get(MeshPipelineController.class);
    meshPipelineController_0.generateVolumeMesh();

    // run
    simulation_0.getSimulationIterator().runAutomation();
  }

  private void execute1() {

    // save simfile
    Simulation simulation_0 = getActiveSimulation();
    simulation_0.saveState("/home/flyntga/git/optuna/ncT002.sim");
  }
}
