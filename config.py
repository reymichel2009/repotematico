import os
import ProxyCloud

BOT_TOKEN = '5735357680:AAFA6dXjr6MuZ2gR7dSHJgz3Oi1Te7gbMow' #Aqui va el token del bot
API_ID =  13233271 #Tu api id de telegram
API_HASH = 'e3ce8145aa657c2a4cc5cf0f7183e476' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Hiyabo').split(';')

static_proxy = ''
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['az9az999999'] = 0

