# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('16641929'))
    API_HASH = str(getenv('af33474aed591a271d342070515e1fab'))
    BOT_TOKEN = str(getenv('5077201853:AAEcwtNbeeEyjmhQ4SeYE3GFeLO-ltNHFiw'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AafuSam013'))
    SLEEP_THRESHOLD = str(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = str(getenv('WORKERS', '4'))
    BIN_CHANNEL = str(getenv('-1001606422438'))
    PORT = str(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = str(getenv('2075300611'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('aafusam_directlinkkk'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('mongodb+srv://afiqsam:afiqsam@cluster0.0wb1c.mongodb.net/afiqsam?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    
