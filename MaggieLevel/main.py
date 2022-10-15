import time
import csv
import requests

#Difinición de la función que obtiene datos del API
def obtenerPerso():
  URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
  respuesta = requests.get(url = URL)
  datos = respuesta.json()
  # Obtenemos valor en la clave 'character' del JSON que nos interesa
  dic:str = datos[0]
  return dic
'''
#Definición de cabecera de los csv
cabecera = ["quote", "character", "image", "characterDirection"]
with open("/Homer/Homer.csv", "a+", newline ='') as csvfile:
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(cabecera)
with open("/Lisa/Lisa.csv", "a+", newline ='') as csvfile:
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(cabecera)
with open("/Resto/Resto.csv", "a+", newline ='') as csvfile:
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(cabecera)
'''

#Bucle que guarda los datos en el csv según el personaje
while True:
  datos = obtenerPerso()
  print(datos['character'])
  print(datos)
  lst = []
  lst.extend(datos.values())
  if (datos['character'] == "Lisa Simpson"):
    with open("MaggieLevel/Lisa/Lisa.csv", "a+", newline ='') as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(lst)
  if (datos['character'] == "Homer Simpson"):
    with open("MaggieLevel/Homer/Homer.csv", "a+", newline ='') as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(lst)
  else:
   with open("MaggieLevel/Resto/Resto.csv", "a+", newline ='') as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator=';')
      wr.writerow(lst)
  time.sleep(30)