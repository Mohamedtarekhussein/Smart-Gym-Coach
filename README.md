# Yoga Posture Detection and Correction Using YOLOv8 with Keypoints

## About Dataset
This project focuses on the detection and correction of yoga postures using YOLOv8 with keypoint annotations. The dataset was systematically collected and annotated for training and validation purposes.

### Dataset Creation Process:
1. **Data Collection**: Collected 500-600 images of various yoga poses, with each pose category represented by around 100 images.
2. **Data Split**: Divided into training and validation sets to evaluate model generalization.
3. **Annotation Tool**: Used **CVAT.ai** to annotate keypoints relevant to yoga poses, ensuring detailed pose descriptions.
4. **Skeleton Creation**: Defined a 5-skeleton structure for key body joints, including shoulders, elbows, wrists, hips, and knees.
5. **Annotation Application**: Applied the defined skeleton annotations consistently across images.
6. **Export Format**: Annotations were exported in **COCO Keypoint 1.0 format** for standardization.
7. **Data Conversion**: Converted COCO keypoint JSON files into **YOLO format text files** for compatibility with YOLOv8.
8. **Final Dataset**: The dataset was processed and formatted for training the YOLOv8 model for posture detection and correction.

This structured dataset allows for robust machine learning model training to detect and correct yoga postures effectively.

## Project Requirements

### Python Environment
- Python serves as the primary programming language for implementing deep learning and computer vision tasks.
- Popular libraries used in this project:
  - **NumPy, OpenCV, TensorFlow, PyTorch** for deep learning and image processing.
  - **Ultralytics** for YOLOv8 implementation.
  - **Streamlit** for building an interactive web-based system.

### Development Tools
- **PyCharm** (Recommended IDE) with a **Conda environment** for dependency management.
- **Conda Environment** ensures a reproducible and consistent setup across different machines.
- **Ultralytics** provides state-of-the-art implementations of YOLOv8 for object detection and keypoint analysis.
- **Streamlit** enables interactive visualization and integration of ML models into a web-based interface.

## YOLOv8 Implementation
- YOLOv8 from **Ultralytics** was used for training and inference.
- Model training, evaluation, and visualization were performed using Ultralytics' YOLO tools.
- The model predicts **keypoints for yoga poses** and identifies posture correctness.

## Performance Analysis
### Training Results
Below are some key performance metrics and training results:
- **Loss Curves**: Displaying training/validation loss trends.
- **Precision-Recall Curves**: Evaluating model performance.
- **Confusion Matrix**: Understanding classification accuracy.

### Sample Training Results:
![Training Results](https://github.com/Mohamedtarekhussein/Smart-Gym-Coach/blob/main/train/BoxPR_curve.png?raw=true)

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/yoga-posture-detection.git
   cd yoga-posture-detection
   ```
2. Create and activate a Conda environment:
   ```bash
   conda create --name yoga_env python=3.8 -y
   conda activate yoga_env
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit web application:
   ```bash
   streamlit run app.py
   ```

## Conclusion
This project demonstrates how **YOLOv8 with keypoint annotations** can be effectively used for **yoga posture detection and correction**. The structured dataset and model training provide a foundation for developing intelligent fitness applications.

