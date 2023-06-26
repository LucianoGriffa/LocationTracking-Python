import requests

def obtener_ubicacion(ip):
  url = f"http://ip-api.com/json/{ip}"
  respuesta = requests.get(url)
  datos = respuesta.json()
  if datos['status'] == 'success':
    print("Información de ubicación:")
    print(f"IP: {datos['query']}")
    print(f"País: {datos['country']}")
    print(f"Región: {datos['regionName']}")
    print(f"Ciudad: {datos['city']}")
    print(f"Código postal: {datos['zip']}")
    print(f"Proveedor de servicios de internet: {datos['isp']}")
  else:
    print("No se pudo obtener la ubicación.")

# Ejemplo de uso
ip = input("Ingrese la dirección IP o URL: ")
obtener_ubicacion(ip)
