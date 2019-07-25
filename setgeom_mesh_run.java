// STAR-CCM+ macro: setgeom_mesh_run.java
// Written by STAR-CCM+ 14.02.012
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;
import star.meshing.*;
import star.cadmodeler.*;
import star.vis.*;

public class setgeom_mesh_run extends StarMacro {

  public void execute() {

    //exec_chg_curves();
    //exec_remesh_run();
    //exec_save();
    exec_plot_scenes();
  }

  private void exec_chg_curves() {

    String pwd = "/home/flyntga/git/optuna/";
    String skname1 = "Sketch3D 1";
    String skname2 = "Sketch3D 2";
    String cf_fy   = "fy_curve.csv";
    String cf_fz   = "fz_curve.csv";

    replace_splines( skname1, pwd+cf_fy);
    replace_splines( skname2, pwd+cf_fz);
  }

  private void exec_remesh_run() {

    // remesh
    Simulation sim =  getActiveSimulation();
    MeshPipelineController meshPipelineController_0 = sim.get(MeshPipelineController.class);
    meshPipelineController_0.generateVolumeMesh();

    // run
    sim.getSimulationIterator().runAutomation();
  }

  private void exec_save() {

    Simulation sim = getActiveSimulation();
    sim.saveState("/home/flyntga/git/optuna/ncT009.sim");
  }

  private void exec_plot_scenes() {

    String pwd = "/home/flyntga/git/optuna/";
    String prob = "ncT002_";

    plot_scene( "alpha_xy"     , pwd+prob+  "alpha_xy"      +".png"  );
    plot_scene( "beta_xy"      , pwd+prob+  "beta_xy"       +".png"  );
    plot_scene( "velocity_nep" , pwd+prob+  "velocity_nep"  +".png"  );
    plot_scene( "velocity_xy"  , pwd+prob+  "velocity_xy"   +".png"  );
  }

  void plot_scene(String scene_name, String save_name)
  {
    Simulation sim = getActiveSimulation();
    Scene sc1 = sim.getSceneManager().getScene( scene_name );
    sc1.printAndWait(resolvePath( save_name ), 1, 1167, 670, true, false);
  }

  void replace_splines(String skname, String fcurve)
  {
    Simulation sim = getActiveSimulation();
    CadModel cm = ((CadModel) sim.get(SolidModelManager.class).getObject("3D-CAD Model 1"));

    Sketch3D sk2 = ((Sketch3D) cm.getFeature(  skname  ));
    cm.getFeatureManager().rollBack(sk2);
    cm.getFeatureManager().startSketch3DEdit(sk2);
    SplineSketchPrimitive3D spline2 = ((SplineSketchPrimitive3D) sk2.getSketchPrimitive3D("Spline 1"));
    sk2.replaceSketchPrimitive3d(spline2, resolvePath(  fcurve  ));
    cm.getFeatureManager().stopSketch3DEdit(sk2, false);
    cm.getFeatureManager().markDependentNotUptodate(sk2);
    cm.getFeatureManager().rollForwardToEnd();
  }
}
