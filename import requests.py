import requests

def consultar_api():
    
    url="https://cl.dolarapi.com/v1/cotizaciones/usd"
    response=requests.get(url)

    if response.status_code==200:
        print('solicitud exitosa')
        print('Data:',response.json())

    else:
        print('error en lasolicitud, detalles:',response.text)    
