# requestCrypto
script para obtener el precio actual de una criptomoneda

# ejecución
desde la línea de comandos especificar por argumento el tipo de criptomoneda de la que deseamos buscar el precio actual en USD

$ python requestCrypto.py <criptomoneda>

# ayuda
el script permite una ayuda desde la línea de comandos con uno de los siguientes párametros: 

-h, -help, --help, -?, --?

# ejemplos
$ python requestCrypto.py bitcoin

 - PARÁMETRO de búsqueta de crytomoneda: ripple
 - URL de llamada al microservicio: https://api.coingecko.com/api/v3/coins/ripple
 - llamada al microservicio correcto: status code 200

 ** El precio actual de 1 bitcoin es 0.849125 dólares **

----------------------------------------------------------------
  
$ python requestCrypto.py litecoin

 - PARÁMETRO de búsqueta de crytomoneda: litecoin
 - URL de llamada al microservicio: https://api.coingecko.com/api/v3/coins/litecoin
 - llamada al microservicio correcto: status code 200

 ** El precio actual de 1 bitcoin es 121.7 dólares **

----------------------------------------------------------------
  
$ python requestCrypto.py ripple

 - PARÁMETRO de búsqueta de crytomoneda: ripple
 - URL de llamada al microservicio: https://api.coingecko.com/api/v3/coins/ripple
 - llamada al microservicio correcto: status code 200

 ** El precio actual de 1 bitcoin es 0.849125 dólares **

 # control de errores
 en caso de error, el script devuelve el tipo de error HTTP que se haya producido en la llamada al microservicio
 
 
