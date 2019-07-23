// STAR-CCM+ macro: chg_curves.java
// Written by STAR-CCM+ 14.02.012
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;
import star.cadmodeler.*;

public class chg_curves extends StarMacro {

  public void execute() {
    execute0();
  }

  private void execute0() {

    String pwd = "/home/flyntga/git/rhino3dm/samples/python/";
    String skname1 = "Sketch3D 1";
    String skname2 = "Sketch3D 2";
    String cf_fy   = "fy_curve.csv";
    String cf_fz   = "fz_curve.csv";

    replace_splines( skname1, pwd+cf_fy);
    replace_splines( skname2, pwd+cf_fz);
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
