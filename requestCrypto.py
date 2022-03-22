import sys
import requests

print("")

def help():
    print(" INFO")
    print("   script para obtener el precio actual de una criptomoneda\n\n")
    print(" EJECUCION")
    print("   desde la línea de comandos especificar por argumento el tipo de criptomoneda de la que deseamos buscar el precio actual en USD\n\n")
    print("     python requestCrypto.py <criptomoneda>\n")

#argumentos = len(sys.argv) - 1
argumentos = sys.argv

# sin parámetros
if (len(argumentos) - 1) == 0:
    print(" ERROR - falta el parámetro de la crytomoneda a buscar")
    quit()

# más de 1 parámetro
if (len(sys.argv) - 1) > 1:
    print(" ERROR - especifique sólo un parámetro que indique la crytomoneda a buscar")
    quit()

if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-?" or sys.argv[1] == "--?":
    help()
    quit()

scriptParam = sys.argv[0]
cryptoParam = sys.argv[1]

uri = "https://api.coingecko.com/api/v3/coins/"
url = uri + cryptoParam

print(" - PARÁMETRO de búsqueta de crytomoneda:", cryptoParam)
print(" - URL de llamada al microservicio:", url)

try:
    res = requests.get(url,timeout=3)
    res.raise_for_status()

    if res.status_code == 200:
        print(" - llamada al microservicio correcto: status code",res.status_code)

        resJson = res.json()

        jsonMarketData = (resJson['market_data'])

        usdCurrency = resJson["market_data"]["current_price"]["usd"]

        print("\n----------------------------------------------------------------\n")

        print(" ** El precio actual de 1 bitcoin es",usdCurrency,"dólares **")
        quit()

except requests.exceptions.HTTPError as errh:
    print("\n----------------------------------------------------------------\n")
    print(" ERROR: no existe valor para la criptomoneda indicada:", cryptoParam)
    print(" ERROR HTTP:\n", errh)

except requests.exceptions.ConnectionError as errc:
    print("\n----------------------------------------------------------------\n")
    print(" ERROR de Conexión:\n", errc)

except requests.exceptions.Timeout as errt:
    print("\n----------------------------------------------------------------\n")
    print(" ERROR de Timeout:\n", errt)

except requests.exceptions.RequestException as err:
    print("\n----------------------------------------------------------------\n")
    print(" ERROR Desconocido: Se ha producido un error en la llamada al servidor\n",err)
