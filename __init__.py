# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import requests
from time import sleep


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "ReCaptchaV2":
    key = GetParams("key")
    token = GetParams("token")
    url = GetParams("url")
    var_ = GetParams("result")

    if key and token:
        try:
            # Add these values
            API_KEY = key  # Your 2captcha API KEY
            site_key = token  # site-key, read the 2captcha docs on how to get this
            #url = 'http://somewebsite.com'  # example url
            proxy = None #'127.0.0.1:6969'  # example proxy

            #proxy = {'http': 'http://' + proxy, 'https': 'https://' + proxy}

            s = requests.Session()

            # here we post site key to 2captcha to get captcha ID (and we parse it here too)
            url_captcha  = "http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url)
            print(url_captcha)
            captcha_id = s.get(url_captcha, proxies=proxy).text.split('|')[1]
            # then we parse gresponse from 2captcha response
            recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
            print("solving ref captcha...")
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
                sleep(5)
                recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
                print(recaptcha_answer)
            recaptcha_answer = recaptcha_answer.split('|')[1]
            s.close()
            print(recaptcha_answer)
            SetVar(var_, str(recaptcha_answer))
        except Exception as e:
            PrintException()
            raise Exception(e)
"""
    Resuelvo captcha tipo imagen
"""

if module == "captchaimagen":

    key = GetParams("key")
    path_ = GetParams("path")
    var_ = GetParams("result")
    print(var_)
    if key and path_:
        # Add these values
        API_KEY = key  # Your 2captcha API KEY

        #url = 'http://somewebsite.com'  # example url
        proxy = None #'127.0.0.1:6969'  # example proxy

        #proxy = {'http': 'http://' + proxy, 'https': 'https://' + proxy}

        s = requests.Session()

        # here we post site key to 2captcha to get captcha ID (and we parse it here too)
        url = 'http://2captcha.com/in.php'
        file_ = open(path_, 'rb')
        files = {'file': file_}
        data = {'key': key, 'method': 'post'}
        captcha_id = s.post(url, files=files, data=data).text.split('|')[1]
        # then we parse gresponse from 2captcha response
        recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
        print("solving ref captcha...")
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            sleep(5)
            recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
            print(recaptcha_answer)
        recaptcha_answer = recaptcha_answer.split('|')[1]
        s.close()
        file_.close()
        print(recaptcha_answer)
        try:
            SetVar(var_, str(recaptcha_answer))
        except Exception as e:
            print(e)
