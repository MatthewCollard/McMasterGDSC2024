from PyQt6.QtWidgets import QMainWindow,QListView, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QLabel, QGridLayout, QListWidget, QListWidgetItem
from PyQt6.QtGui import QPalette, QColor, QGuiApplication
from PyQt6.QtCore import QDir, QRect, Qt,QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont
from tkinter.filedialog import askdirectory, askopenfilename
import tkinter as tk
#import tensorflow as tf
#import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential
from tensorflow.keras.models import load_model
#from tensorflow import keras
#from keras.layers import Dense
#import matplotlib.pyplot as plt
import numpy as np
import PIL
#from tensorflow.keras.layers import Rescaling
#from tensorflow.keras import layers
#from tensorflow.keras.models import load_model#Sequential, load_model
#from tensorflow.keras import backend
import pathlib
from PIL import Image, ImageQt
from tensorflow.keras.preprocessing import image
import sys
import random
import glob
import os

#include <QRect>


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GDSC Marine Garbage Detection")
        self.screen_size = QGuiApplication.primaryScreen().availableGeometry()#QDesktopWidget().screenGeometry(0)
        print(self.screen_size.width())
        screen_height = self.screen_size.height()
        screen_width = self.screen_size.width()
        x_pos = 0
        y_pos = 0
        self.setGeometry(x_pos, y_pos, screen_width, screen_height)
        self.showMaximized()
        #self.root=tk.Tk()
        


        #self.stacklayout = QStackedLayout()
        if(1):
            
            #mainLayout=QGridLayout()
            self.mainLayout=QStackedLayout()
            if(1):
                
                self.buttonLayout=QHBoxLayout()
                #self.setFixedHeight(300)
                self.button1 = QPushButton("Import Trash")
                #button1.pressed.connect(self.close)
                self.button1.pressed.connect(self.changeToImportImages)
                #button1.resize(200,50)
                self.button2 = QPushButton("Import Model")
                #self.button2.pressed.connect(self.close)
                self.button2.pressed.connect(self.changeToImportDataSet)

                self.button1.setMinimumSize(50,100)
                self.button2.setMinimumSize(50,100)

                #button2.resize(200,50)
                self.buttonLayout.addWidget(self.button1)
                self.buttonLayout.addWidget(self.button2)
                self.buttonLayout.setSpacing(100)
                buttonLayoutSize=QRect(50,100,50,100)
                self.buttonLayout.setContentsMargins(100,10,100,10)
                self.buttonLayout.setGeometry(buttonLayoutSize)
                self.button1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
                self.button2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
            #w=WidgetButton()
        #mainLayout.addLayout(self.stacklayout)
            if(1):
                self.importImageLayout=QVBoxLayout()
                self.importImageListLayout=QHBoxLayout()
                self.findImageLayout=QHBoxLayout()

                self.imageListView=QListWidget()
                self.imageListView.setIconSize(QSize(416,416))
                self.importButton=QPushButton("Import images")
                self.importButton.setMinimumSize(200,150)
                self.importButton.pressed.connect(self.importImages)
                self.importButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
                self.imageListView.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
                
                self.findButton=QPushButton("Find Trash")
                self.findButton.setMinimumSize(50,100)
                self.findButton.setMaximumSize(500,100)
                self.findButton.pressed.connect(self.classify)
                self.findButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')

                self.importImageListLayout.addWidget(self.importButton)
                self.importImageListLayout.addWidget(self.imageListView)

                self.findImageLayout.addWidget(self.findButton)
                tempWidget=QWidget()
                tempWidget.setLayout(self.importImageListLayout)
                tempWidget2=QWidget()
                tempWidget2.setLayout(self.findImageLayout)
                self.importImageLayout.addWidget(tempWidget)
                self.importImageLayout.addWidget(tempWidget2)
                self.importImageLayout.setSpacing(50)
                self.importImageLayout.setContentsMargins(100,10,100,10)

            if(1):
                self.resultsLayout=QVBoxLayout()
                widgetFont = QFont()
                widgetFont.setWeight(40)
                widgetFont.setPointSize(24)
                self.resultsSubLayout=QHBoxLayout()
                self.resultsListView=QListWidget()
                #self.originalListView=QListWidget()
                self.resultsListView.setIconSize(QSize(416,416))
                self.resultsSubLayout.addWidget(self.resultsListView)
                self.resultsListView.setFont(widgetFont)
                #self.resultsSubLayout.addWidget(self.originalListView)
                self.resultsLayout.setSpacing(100)
                self.importImageLayout.setContentsMargins(100,10,100,10)
                tempWidget3=QWidget()
                tempWidget3.setLayout(self.resultsSubLayout)
                self.resultsLayout.addWidget(tempWidget3)

                self.resultsLayout.setSpacing(100)



            mainMenuWidget=QWidget()
            #p=mainMenuWidget.palette()
            #p.setColor(w.backgroundRole(), QColor('red'))
            #mainMenuWidget.setAutoFillBackground(True)
            #mainMenuWidget.setPalette(p)
           

            #background = QPixmap('GarbageBackgroundPhoto.jpg').scaledToWidth(screen_width)
            #stylesheet = 'border-image: url("GarbageBackgroundPhoto.jpg");'
            #mainMenuWidget.setStyleSheet(stylesheet)
            #mainMenuWidget.setPixmap(QPixmap('GarbageBackgroundPhoto.jpg'))
            #mainLayout.addWidget(Color('blue'))
        #layout.addWidget(Color('red'))
            #label2 = QLabel("I want this text to appear on top of background image")
            #buttonLayout.addWidget(label2)
            #mainLayout.addLayout(w)
            #w.show()
            self.buttonWidget=QWidget()
            self.buttonWidget.setLayout(self.buttonLayout)
            self.mainLayout.addWidget(self.buttonWidget)

            self.imageImportWidget=QWidget()
            self.imageImportWidget.setLayout(self.importImageLayout)
            self.mainLayout.addWidget(self.imageImportWidget)

            self.resultsWidget=QWidget()
            self.resultsWidget.setLayout(self.resultsLayout)
            self.mainLayout.addWidget(self.resultsWidget)
            
            #mainLayout.addWidget(Color('blue'))
            self.mainLayout.setContentsMargins(0,0,0,0)
            self.mainLayout.setSpacing(0)

            mainMenuWidget.setLayout(self.mainLayout)
        
            self.setCentralWidget(mainMenuWidget)
        #widget = QWidget()
        #self.setCentralWidget(widget)
        #stylesheet = 'border-image: url("GarbageBackgroundPhoto.jpg");'
        #widget.setStyleSheet(stylesheet)
    
        #layout2 = QHBoxLayout()
        #button1 = QPushButton("Import Trash")
        #button1.pressed.connect(self.close)
        #layout2.addWidget(button1)
        #label2 = QLabel("I want this text to appear on top of background image")
        #layout2.addWidget(label2)
        #widget.setLayout(layout2)
        #self.image = QLabel()
        #self.image.setPixmap(background)
        #layout.addWidget(self.image)
        #lay = QHBoxLayout(self)

        #for letter in "ABCDEFG":
        #    label = QLabel(letter)
        #    color = QColor(*[random.randint(0, 255) for _ in range(3)])
        #    label.setStyleSheet("background-color: {}".format(color.name()))
        #    lay.addWidget(label)


        #self.show()
    def changeToImportImages(self):
        self.mainLayout.setCurrentIndex(1)
        #print('hi')
    
    def changeToImportDataSet(self):
        #print('hi')
        self.keras=askopenfilename(filetypes=[("Keras Files","*.h5")])
        print(self.keras)
        self.loaded_model = load_model(self.keras)
        #self.mainLayout.setCurrentIndex(3)

    def changeToMainMenu(self):
        self.mainLayout.setCurrentIndex(0)

    def importImages(self):
        folderPath = askdirectory()
        self.image_list = []
        self.imageNameList=[]
        print(folderPath)
        for filename in glob.glob(folderPath+'/*.jpg'): #assuming gif        
            filename=str(pathlib.PureWindowsPath(filename).as_posix())
            picture = Image.open(filename)
            self.image_list.append(picture)
            self.imageNameList.append(filename)
            picture.thumbnail((416, 416), Image.LANCZOS)
            icon = QIcon(QPixmap(filename))#QIcon(QPixmap.fromImage(ImageQt.ImageQt(picture)))
            item = QListWidgetItem(os.path.basename(filename)[:20] + "...", self.imageListView)
            item.setStatusTip(filename)
            item.setIcon(icon)
            #print(filename)
            #self.imageNameList.append(filename)
            #im=Image.open(filename)
            #self.image_list.append(im)
            #im.thumbnail((72,72),Image.Resampling.LANCZOS)
            #icon=QIcon(QPixmap.fromImage(ImageQt.ImageQt(im)))
            #item=QListWidgetItem(filename,self.imageListView)
            #item.setStatusTip(filename)
            #item.setIcon(icon)
        #print(self.imageNameList)
        #self.root.mainloop()
        #self.imageListView.addItems(self.imageNameList)
        #self.image_list = image.img_to_array(img)
        #self.image_list = np.expand_dims(img_array, axis=0)
        #self.image_list/=255.0

    def classify(self):
        print("Classify")
        for i in self.imageNameList:
            img = image.load_img(i, target_size=(416, 416)) 
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            
            #img_array /= 255.0  # Normalize the image pixel values
            icon = QIcon(QPixmap(i))#QIcon(QPixmap.fromImage(ImageQt.ImageQt(picture)))
            widgetFont = QFont()
            widgetFont.setWeight(40)
            widgetFont.setPointSize(24)
            predictions=self.loaded_model.predict(img_array)
            print("Source Image: "+i)
            print("Predicted Probabilites:")
            print(predictions)
            predicted_class_index = np.argmax(predictions)
            if(predicted_class_index==0):
                print("Predicted Class: Clean")
                item = QListWidgetItem("Predicted Class: Clean \n"+i, self.resultsListView)
                item.setFont(widgetFont)
            else:
                print("Predicted Class: Dirty")
                item = QListWidgetItem("Predicted Class: Dirty \n"+i, self.resultsListView)
                item.setFont(widgetFont)
                


            
            item.setStatusTip(i)
            item.setIcon(icon)
            #self.resultsListView
            #print("Predicted Class Index:", predicted_class_index)


        self.mainLayout.setCurrentIndex(2)

    #def pictureDropped(self, imageList,imageNameList):
	#    for i in range(len(imageList)):
    #            img=imageList[i]
    #            path=imageNameList[i]
		        #img.thumbnail((72, 72), Image.ANTIALIAS)
			    #icon = QIcon(QPixmap.fromImage(ImageQt.ImageQt(img)))
			    #item = QListWidgetItem(os.path.basename(path)[:20] + "...", self.imageListView)
			    #item.setStatusTip(path)
			    #item.setIcon(icon)

class Color(QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        
        palette=self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class WidgetButton(QWidget):
    def __init__(self, parent=None):
        super(WidgetButton, self).__init__(parent)
        buttonLayout=QHBoxLayout()
        self.setFixedHeight(300)
        button1 = QPushButton("Import Trash")
        button1.pressed.connect(self.close)
        button1.setStyleSheet("background-color: green; color: white;")
        #button1.resize(200,50)
        button2 = QPushButton("Import Model")
        button2.pressed.connect(self.close)
        #button2.resize(200,50)
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.setSpacing(30)
        #buttonLayoutSize=QRect(50,100,50,100)
        buttonLayout.setContentsMargins(10,10,10,10)
        #buttonLayout.setGeometry(buttonLayoutSize)

        




stylesheet = """
    MainWindow {
        background-image: url("AnimatedOcean.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

custom_font = QFont()
custom_font.setWeight(26);
#QApplication.setFont(custom_font, "QLabel")
app = QApplication(sys.argv)
app.setFont(custom_font)
app.setStyleSheet(stylesheet)
w = MainWindow()
w.show()
app.exec()