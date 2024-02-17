import PySimpleGUI as sg
from draw_a_card import draw_a_card

layout = [[sg.Text("Hello")], [sg.Button("OK")], [sg.Button("Draw a card...")]]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "Draw a card...":
        print(draw_a_card())
        
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
window.close()
