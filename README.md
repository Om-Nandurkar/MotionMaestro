# MotionMaestro
Motion Maestro is a web-based application designed to detect and translate American Sign Language(ASL) 
hand gestures into text in real-time. Utilizing a Convolutional Neural Network (CNN) model, the system 
processes video input from a webcam, classifies the gestures, and displays the corresponding text on 
the screen.

Set up for ASL Detection Project

Create a new PyCharm Project

Select the Python Interpreter as Python 3.11.x

Click Create project
A virtual environment(venv) will be created it will get activated by default
If it does not activate automatically, activate it manually with the below code:

  .\venv\Scripts\activate


Now, into the Project directory 
Create a Directory Structure as follows

asl_detection_project
     -Model
         -keras_model.h5
         -label.txt
     -static
         -style.css
     -templates
         -index.html
     -app.py
     -asl_logic.py
     -dataCollection.py
     -test.py
     -requirements.txt

Copy the files According to the above directory structure

Once the Directory structure is and all the files are ready, install the required packages and libraries in the project.

The required packages and libraries for this are:
CVZone (1.6.1)
MediaPipe (0.10.14)
TensorFlow (2.12.1)
Flask (3.0.3)

Run this command to install the packages:
    
    pip install -r requirements.txt


To install these packages manually into the project:

Go to settings in pycharm
On the right side menu select project
In project click on python interpreter
Click on '+' icon in interpreter
On search bar type the names of the packages
Select the package
Select specify version and install the specified versions of these packages

Now to run the project

On PyCharm terminal type command "python app.py"
Terminal will give you the links of the localhost
Click on the links or copy and paste the links on your browser

The Project is done setting up and ready for use.
