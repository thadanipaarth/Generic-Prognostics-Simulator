# Generic-Prognostic-Simulator

This repository contains an application that predicts the breakdown time using Reliablity Analysis by simulating the component at various speeds and recoding the reading through an accelerometer. 

This project was presented at **International Conference on Precision, Meso, Micro & Nano Engineering**.

The project poster can be viewed [here](./Project_Poster.pdf) and demo video of the application can be viewed [here](https://youtu.be/w2jPJMDxUsw).

<ins><strong>NOTE:</strong> This repository only contains demo application displaying the functionality using sample documents. The final application is yet to be made Open-Source. However, the functionality and user-interface will remain the same. Stay updated for the same!</ins>

### Directory Overview
1. [main.py](./main.py) contains the backend of the application. '/enter' route is used for running the model and fetching the required readings, other roots are self-explainatory. Refer [main.py](./main.py) for further information.
2. [./static/RMS_MOTOR1/](./static/RMS_MOTOR1) contains the sample files simulated using the model (Principled on Reliablity Analysis).
3. [./static/js/rms_graph.js](./static/js/rms_graph.js) contains the code for ploting of the graphs bootstrapped using [Chart.js](https://github.com/chartjs/Chart.js)
4. [./static/download.xlsx](./static/download.xlsx) contains the sample analysis file that will be available for download after the simulation is completed for further research.

### Steps To Run
1. `pip install -r requirments.txt `
2. `python main.py`
