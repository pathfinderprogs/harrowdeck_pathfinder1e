import csv
import numpy as np
from classRollTable import RollTable

with open('harrowdeck_noweights.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    c = list(csv_reader)


with open('harrowdeck_weightsonly.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    w = list(csv_reader)

cards = np.array(c)
weights = np.array(w, dtype=float)
table_harrow = RollTable(cards, weights)

def draw_a_card():
    for _ in range(1):
        result = table_harrow.get_item()
        return result
        
print(draw_a_card())

