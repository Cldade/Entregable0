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

#Bucle que guarda los datos en el csv según el personaje
while True:
  datos = obtenerPerso()

  my_dict = {'quote':datos['quote']}
  
  autor = datos['character']

  print(autor)

  if (autor == "Lisa Simpson"):
    with open("MaggieLevel/Lisa/Lisa.csv",'a' ) as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', lineterminator=';')
      wr.writerow(my_dict.values())

  if (autor == "Homer Simpson"):
    with open("MaggieLevel/Homer/Homer.csv",'a') as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', lineterminator=';')
      wr.writerow(my_dict.values())
      
  else:
   with open("MaggieLevel/Resto/Resto.csv", 'a') as csvfile:  
      wr = csv.writer(csvfile, dialect='excel', lineterminator=';')
      wr.writerow(my_dict.values())
  time.sleep(30)