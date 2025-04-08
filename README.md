# DICOM-to-NIfTI Converter for Cancer Detection

This repository hosts tools dedicated to converting DICOM medical imaging files from PET and CT scans into NIfTI format, focusing on applications in cancer detection, particularly for analyzing metastasis to lymph nodes.

## Introduction

Medical imaging is crucial in diagnosing and monitoring various diseases, with significant emphasis on cancer. DICOM (Digital Imaging and Communications in Medicine) is the standard format used across medical imaging equipment and software. Converting these images into the NIfTI format allows for more advanced processing and analysis, especially using automated machine learning and deep learning techniques, which can significantly aid in the detection and monitoring of cancer progression.

## Project Aim

To facilitate the conversion of medical imaging data from DICOM to NIfTI format to enable advanced analysis for cancer detection. This project specifically focuses on PET and CT scans used in the identification and evaluation of metastasis to lymph nodes and other tissues.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python installed. If not, download and install it from [Python's official site](https://www.python.org/).

### Installation

Clone this repository to your local machine
```
git clone https://github.com/yourusername/DICOM-to-NIfTI-Converter.git
cd DICOM-to-NIfTI-Converter
```
Install the necessary Python packages
```
pip install -r requirements.txt
```
Running the Project
Convert DICOM files by running the following command in the terminal:
```
python src/main.py
```
For visualization of the NIfTI files, use:
```
python src/visualize_nifti.py
```


Built With
- **Python**: Primary programming language used.
- **Nibabel**: For reading and writing NIfTI files.
- **Pydicom**: For handling DICOM files.
- **Matplotlib**: For visualizing medical images.
- **3D Slicer**: Recommended for viewing NIfTI files. [3D Slicer](https://www.slicer.org/)

