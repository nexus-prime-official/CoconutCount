

# Coconut Trees Detection and Segmentation

This repository provides an implementation of the paper **"Coconut Trees Detection and Segmentation in Aerial Imagery using Mask R-CNN"**. The project focuses on using deep learning techniques to identify and segment coconut trees in aerial imagery, crucial for rapid assessment of food resources in disaster-stricken areas.

## Abstract

Food resources often face significant damage in the wake of natural catastrophes such as earthquakes, cyclones, and tsunamis. In these scenarios, rapid assessment of agricultural resources is vital to support aid efforts. This work introduces a deep learning-based method for detecting and segmenting coconut trees in aerial images. Using Mask R-CNN, a popular object detection and segmentation framework, we achieve over 90% confidence in coconut tree detection. The implementation leverages both ResNet50 and ResNet101 architectures, with our final model utilizing ResNet101.

## Key Features

- **Mask R-CNN**: A state-of-the-art model for object detection and segmentation.
- **ResNet101 Backbone**: Used for feature extraction to enhance model accuracy.
- **High Performance**: Achieves 91% mean average precision (mAP) for coconut tree detection.

## Setup and Installation

To get started with this project, follow these steps:

### Clone the Repository

First, clone the repository:

```bash
git clone https://github.com/agkavin/CoconutCount.git
cd CoconutCount
```

### Install Dependencies

Create and activate a virtual environment (optional but recommended), then install the required packages:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```
