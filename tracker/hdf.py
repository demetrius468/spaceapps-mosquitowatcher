import csv
import pyhdf
from pyhdf.SD import *

file_name = "C:\\Users\\Demetrius\\Desenvolvimento\\spaceapps-mosquitowatcher\\tracker\\data\\AIRS.2019.10.10.L3.RetSup_IR008.v6.0.31.1.G19291181914.hdf"
file = SD(file_name, SDC.READ)

var_names = ['Latitude', 'Longitude', 'SurfSkinTemp_Forecast_A', 'IR_Precip_Est_A']

for v in var_names:
    with open(v + '.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=';')
        for r in file.select(v)[:]:
            wr.writerow(r)
