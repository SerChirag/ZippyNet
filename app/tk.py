import PySimpleGUI27 as sg
import datetime
import os
import numpy as np
from keras.models import load_model

layout = [[sg.Text('Download files or folders')],      
          [sg.Text('Url', size=(15, 1)), sg.InputText('', key='_url_')], 
          [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
            sg.InputText('Current Folder', key='_dir_'), sg.FolderBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Download Files or Folders', layout)

event, values = window.Read()

print(values['_url_'],values['_dir_'])
import requests 
# image_url = "https://www.python.org/static/img/psf-logo.png"
image_url = "https://cloud.iitmandi.ac.in/f/abcfb9a692/?raw=1"
image_url = values['_url_']
r = requests.get(image_url) # create HTTP response object 

filepath=values['_dir_']
if(filepath=='Current Folder'):
    filepath=os.getcwd()
print(filepath)
with open(filepath+"/bin.npy",'wb') as f:
    f.write(r.content) 
# sg.Popup('The GUI returned:', event, values)
import subprocess
subprocess.call(os.getcwd()+'/script.sh')

y = np.load(filepath+"/bin.npy")
decu = load_model('de.h5')
sg.Popup('Decoding downloaded file.')
yd = decu.predict(y)*255
cv2.imwrite(filepath+"/downloaded.jpg",yd[0])