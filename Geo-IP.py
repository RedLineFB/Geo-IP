import urllib.request
import json 

def main():
	
	print("\n\nCreado por: RedLineFB")
	print("\nInstagram: facundo_betancur97\n")
	print("\n\nBIENVENIDO A Geo-IP\n")
	IP = input("Ingrese una IP: ")	
	scanner="https://ipinfo.io/{}/json".format(IP)  #Le pasamos la página con la ip cargada por el usuario
	urllibx=urllib.request.urlopen(scanner) #Función de de librería "urllib.request" urllib.request.urlopen() le pasamos la variable que tiene la página 
	jsonx=json.load(urllibx) #Función de la librería "json" json.load() que se usa para leer una cadena json en la página

	for f in jsonx:
		print(f + " : " + jsonx[f]) #"for" para recorrer cada fila y mostrar por pantalla cada json

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
