Aviation 2022 - Wingbox Weight Data
==============

This repository contains the supplementary data for the following paper

Darshan Sarojini, Heriberto D. Solano, Jason A. Corman, and Dimitri N. Mavris. "Parametric Wingbox Structural Weight Estimation of the CRM, PEGASUS and Truss-Braced Wing Concepts." AIAA Aviation Forum 2022. 

```
@inproceedings{SarojiniParametric2022,
  title={Parametric Wingbox Structural Weight Estimation of the CRM, PEGASUS and Truss-Braced Wing Concepts},
  author={Sarojini, Darshan and Solano, Heriberto D and Corman, Jason A and Mavris, Dimitri N},
  booktitle={AIAA Aviation Forum 2022},
  year={2022}
}
```

# Data in the repository
The data is broadly categorized into three types:
1. Aircraft files: geometry as OpenVSP files, aerodynamic model as AVL files, and structural model as Nastran .bdf files
2. HTML files that allow for interactive visualization of the design space
3. Surrogate model of the structural weight as a function of the design variables provided as python functions

## Aircraft Files
Geometry in the form of [OpenVSP](http://openvsp.org/) files representing the Outer Mold Line (OML) of the baseline aircraft are provided for the Common Research Model (CRM), the PEGASUS concept, and the Truss-Braced Wing (TBW) concept. All OML design variables can be modified using the OpenVSP GUI to visualize the changes. 

Aerodynamic models are provided as Athena Vortex Lattice (AVL) files for the three concepts. [AVL](https://web.mit.edu/drela/Public/web/avl/) is an open-source tool that implements Vortex Lattice Method (VLM)  where the lifting surfaces are modeled as discretized vortex panels following Biot-Savart Law and Kutta-Joukwski Theorem, while the non-lifting bodies are modeled as sources/sinks or doublets to enforce the non-penetrating condition.
The AVL models can be run by the reader to obtain the trim conditions at cruise and static maneuver conditions. 
The NASTRAN bdf files can be run by the reader to obtain element deflections, rotations, stresses, and other specifics such as material layouts and structural meshes of the PEGASUS wing and the TBW wing, strut and spar.