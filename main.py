from flask import Flask,render_template, jsonify, send_file
import os
from random import sample
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

app = Flask(__name__)

## Route for the main home page ##
@app.route('/') 
def home():
    return render_template('index.html')

## Route for running the model ##
@app.route('/enter')  
def submit():    
    #import Model
    return '', 205

## Route for downloading the analysis file ##
@app.route('/download')
def download():
    # The file path below ideally should be the blob url created by the Model. However, 
    # for demo purposes it has been provided with a demo file path   
    return send_file(os.path.join('static/', 'download.xlsx'), as_attachment=True, attachment_filename='Result.xlsx')
    
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)