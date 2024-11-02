# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from zip_extractor import extract

label1 = sg.Text("Select files to extract : ")
input1 = sg.Input(key='text1')
choose_button1=sg.FileBrowse('Choose',key='archive')
label2 = sg.Text("Select destination folder : ")
input2 = sg.Input(key='text2')
choose_button2=sg.FolderBrowse('Choose',key='folder')
exit_button=sg.Button('Exit')
extract_button = sg.Button("Extract")
output_label=sg.Text(key='output',text_color='black')
window = sg.Window("Files Extractor",
                   layout=[[label1, input1,choose_button1],
                           [label2, input2,choose_button2],
                           [extract_button,exit_button,output_label]])

while True:
    event,values=window.read()
    archive_path=values['archive']
    folder=values['folder']
    extract(archive_path,folder)
    window['output'].update(value='Extraction completed !')
    if event=='Exit':
        break
window.close()