// STAR-CCM+ macro: setgeom_mesh_run.java
// Written by STAR-CCM+ 14.02.012
package macro;

import java.util.*;
import java.io.*;


import star.common.*;
import star.base.neo.*;
import star.meshing.*;
import star.cadmodeler.*;
import star.vis.*;

public class setgeom_mesh_run extends StarMacro {

  public void execute() {

    exec_read_case_num();
    exec_chg_curves();
    exec_remesh_run();
    exec_plot_scenes();
    //exec_sudoSave();
    exec_save();
  }

  String pwd = "/home/flyntga/git/optuna/";
  int prob_num = 0;
  String caseName = "ncT"+String.format("%03d", prob_num);  // "ncT003"

  private void exec_read_case_num() {
    //Simulation sim = getActiveSimulation();

    // read case number into global variable "prob_num"
    try {
        //BufferedReader br = new BufferedReader(new FileReader("/home/flyntga/git/optuna/prob_num"));
        BufferedReader br = new BufferedReader(new FileReader(pwd+"prob_num"));
        String line = br.readLine();
        prob_num = Integer.parseInt(line);
        caseName = "ncT"+String.format("%03d", prob_num);
        //System.out.println("got problem number: " + prob_num);
        //System.out.println("case name is: " + caseName);
        br.close();
    }
    catch (Exception e) {
        System.out.println("file not found!");
        //sim.println("file not found!");
    }
  }

  private void exec_chg_curves() {

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
    sim.saveState(pwd+caseName+".sim");
  }

  private void exec_sudoSave() {
     System.out.println("sudo saving case as: "+pwd+caseName+".sim");
  }


  private void exec_plot_scenes() {

    plot_scene( "alpha_xy"     , pwd + caseName + "_" + "alpha_xy"     + ".png"  );
    plot_scene( "beta_xy"      , pwd + caseName + "_" + "beta_xy"      + ".png"  );
    plot_scene( "velocity_nep" , pwd + caseName + "_" + "velocity_nep" + ".png"  );
    plot_scene( "velocity_xy"  , pwd + caseName + "_" + "velocity_xy"  + ".png"  );
    plot_scene( "Vector"       , pwd + caseName + "_" + "vector"       + ".png"  );
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
