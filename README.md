# Explainable Anomaly Detection in Spacecraft Telemetry
As spacecraft missions become more complex and ambitious, it becomes increasingly important to track the status and health of the spacecraft in real-time to ensure mission success. Anomaly detection is a crucial part of spacecraft telemetry analysis, allowing engineers to quickly identify unexpected or abnormal behaviour in spacecraft data and take appropriate corrective action. Anomaly detection on spacecraft telemetry data presents particular challenges due to the complex and dynamic nature of spacecraft systems, as well as the limited and noisy data available. Traditional statistical methods \textcolor{red}{based on threshold setting} are often inadequate for detecting anomalies in this context, requiring the development of more sophisticated techniques that can handle the high-dimensional, non-linear, and non-stationary nature of spacecraft telemetry such as machine learning-based techniques. This article presents an approach for anomaly detection using machine-learning techniques for spacecraft telemetry. The identification of anomaly types present on two real telemetry datasets from NASA is performed to incorporate information of magnitude, frequency, and waveform from known anomalies into the feature extraction process. The proposed approach was tested on unknown real data and results outperform the obtained on the existing related works. \textcolor{red}{Finally, an explainability analysis is performed to understand why a particular data instance has been identified as anomalous, proving the effectiveness of the feature extraction process.

# Data Description
The raw data available for download represents real spacecraft telemetry data and anomalies from the Soil Moisture Active Passive satellite (SMAP) and the Curiosity Rover on Mars (MSL), provided by Hundman, K., Constantinou, V., Laporte, C., Colwell, I., & Soderstrom, T. (2018, July). Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding. In Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining (pp. 387-395): https://github.com/khundman/telemanom.

# Contents:
- LSTM_bychannel.ipynb: Training LSTM neural network for each telemetry channel.
- featuresbyChannel.ipynb: Feature extraction process for each telemetry channel.
- classifier.ipynb: Classification model training, validation and explanation.
- anom_types_.csv: Analysis of types of anomalies.

# Authors:
Sara Cuéllar
PhD. Candidate at Pontificia Universidad Católica de Valparaíso
https://www.researchgate.net/profile/Sara-Cuellar-Carrillo-2
