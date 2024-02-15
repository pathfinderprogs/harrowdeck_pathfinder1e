import PySimpleGUI as sg
from classRollTable import RollTable

layout = [[sg.Text("Hello")], [sg.Button("OK")]]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
window.close()
