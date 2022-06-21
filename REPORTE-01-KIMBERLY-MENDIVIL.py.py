from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

#Log in de usuario-administrador
#usuario = input("Ingrese el usuario:")
#contraseña = input("Ingrese la contraseña:")
repetir = 0
'''
if usuario == 'emtech' and contraseña == 'caso1':
  repetir = 0
  acceso = 1
else: 
  print('Usuario y/o contraseña incorrectos')
  repetir = 1
  acceso = 0
'''
while repetir<3:
  usuario = input("Ingrese el usuario:")
  contraseña = input("Ingrese la contraseña:")

  if usuario == 'emtech'and contraseña == 'caso1':
    repetir = 5
    acceso = 1
  else: 
    print('Usuario y/o contraseña incorrectos')
    repetir = repetir+1
    acceso = 0
     
if acceso == 1:
  print('Bienvenido, seleccione una opción:\n')
  print('A) 5 productos con mayor ventas')
  print('B) 10 productos con mayores busquedas')
  print('C) 5 productos con menor ventas')
  print('D) 10 productos con menores busquedas')
  opcion = input(' Ingrese la opción deseada: ')



#Numero de ventas por producto
contador = 0
ventas_ordenadas_max = []
for producto in lifestore_products:

  for venta in lifestore_sales:
    if producto[0] == venta [1]:
      contador +=1
  ventas_actuales = [producto[0],producto[1], contador]
  ventas_ordenadas_max.append(ventas_actuales)
  contador = 0

def sorter (item):
  return(item[2], item [0])
  
ventas_ordenadas_max2 = sorted(ventas_ordenadas_max, key= sorter, reverse=True)
#print(ventas_ordenadas_max2)     

ventas_ordenadas_min = sorted(ventas_ordenadas_max, key= sorter, reverse= False)
#print(ventas_ordenadas_min)




#Numero de buquedas por producto
contador = 0
busquedas_ordenadas_max = []
for producto in lifestore_products:

  for busqueda in lifestore_searches:
    if producto[0] == busqueda [1]:
      contador +=1
  busquedas_actuales = [producto[0],producto[1], contador]
  busquedas_ordenadas_max.append(busquedas_actuales)
  contador = 0

def sorter (item):
  return(item[2], item [0])
  
busquedas_ordenadas_max2 = sorted(busquedas_ordenadas_max, key= sorter, reverse=True)
#print(busquedas_ordenadas_max2)     

busquedas_ordenadas_min = sorted(busquedas_ordenadas_max, key= sorter, reverse= False)
#print(busquedas_ordenadas_min)



if opcion == "A":
  for i in range (5):
    print(ventas_ordenadas_max2[i])
elif opcion == "B":
  for i in range (10):
    print(busquedas_ordenadas_max2)
elif opcion == "C":
  for i in range (5):
    print(ventas_ordenadas_min)
elif opcion == "D":
  for i in range (10):
    print(busquedas_ordenadas_min)




