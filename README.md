<img src="https://github.com/BALK-03/OCR/assets/145299162/5d580b38-8561-4e59-a8bc-b5c453a8aadf" width="900">

<br><br><br><br>
### Table of Contents


- [What is CNE-Reader?](#what-is-cne-reader)
- [How does it work?](#how-does-it-work)
- [How to run the project?](#how-to-run-the-project)
- [Model Process Overview](#model-process-overview)
- [References](#references)

<br><br><br><br>







### 1. What is CNE-Reader ?

*CNE-Reader* is a notebook that utilizes the [TensorFlow 2 Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) to train an *SSD-MobileNet* model and convert it to *TensorFlow Lite* format. Its purpose is to extract information from student ID cards issued by the [National Institute of Posts and Telecommunications - INPT](https://www.inpt.ac.ma/).

<br><br><br>
### 2. How does it work ?
*CNE-Reader* comprises two main steps. Firstly, we employ [Transfer Learning](https://www.ibm.com/topics/transfer-learning) to train a model capable of localizing **Matricule numbers** and **Full Names** on the student ID cards. Subsequently, we utilize the [PyTesseract](https://pypi.org/project/pytesseract/) library to extract text from the localized zones. For further details on the model, refer to the *ocr_model* notebook.
<br><br><br>
### 3. How to run the project ?
If you only intend to use the model, download requirements.txt and upload it to Colab. Then, execute `!pip install -r requirements.txt`. Alternatively, if you plan to run the model's source code, there is no need to install the requirements.

    3. 1. Download the custom_model_lite folder.
    3. 2. Open the model_test.ipynb notebook on Google Colab.
    3. 3. Follow the steps outlined in the notebook.

<br><br><br>
### 4. Model Process Overview  

### 4.1. Image Preprocessing  
  The input images go through several preprocessing steps such as resizing, normalization and color correction before being fed into the model.  
 
### 4.2. Localizing Zones of Interest

<img src="https://github.com/BALK-03/OCR/assets/145299162/8dbbe0b9-8db3-4c68-87b0-c72ff1f06bf6" width="650">


### 4.3. Text Recognition
  Utilizing OpenCV to process the localized images before feeding them to PyTesseract to read the text.


<br><br><br>
### 5. References
	
[TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
	
[TensorFlow models repository](https://github.com/tensorflow/models)
	
[TensorFlow Lite Object Detection](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)
	
[Colah](chat.openai.com)









