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

## Interactive Design Space Exploration
The reader is also provided HTML files that summarize all the surrogate modeling and effect screening efforts for both the PEGASUS and the [TBW](Interactive Design Space Exploration/TBW.htm). At the top of each of the files, the main actual by predicted plot shows how the model performs with respect to the trained data, providing some useful quantities such as the root mean squared error (RMSE), R^2 of the fit, and the Pvalue of the fit.

In addition, the complete effect summary is given for each of the trained design variables an interactions, highlighting their contribution to the estimation in the surrogate model.

Within the HTML file, more information is also provided in the general residual by predicted plot, and a second section with further information regarding the fit.

Next, the actual parameter estimates are given for each of the design variables and their interactions, as well as the leverage plots of each of them, minimized to save screen space.

In the final section, a complete prediction profiler is provided for each of the main design variables (user interactive), as well as the interaction profiles of each of the design variables (static). The interaction plots are all arranged in a grid that organizes all the different variables and their interactions in the horizontal and vertical axis. 

With the profiler, the reader can check the impact of every design variable independently, actively changing both the response (wingbox weight) and the different single-variable trends by using dials in the file.

## Surrogate Model Functions
In addition to the aforementioned files, fully usable trained python surrogate models for the PEGASUS and TBW configurations are provided. These surrogates can be used by the reader for many-query applications such as uncertainty quantification, or to aid as a weight etimation model in an integrated design environment.

The provided file structure is as follows:
- Surrogate function. The inputs and the bounds where the surrogate is valid are specified in Tables~\ref{tab:pegasus_dse_dvs} and~\ref{tab:tbw_dse_dvs} for the PEGASUS and TBW concepts respectively.
- Main running block, where sample inputs and execution are provided.