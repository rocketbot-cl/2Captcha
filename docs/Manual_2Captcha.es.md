# 2Captcha
  
Módulo para resolver recatpchas con 2Captcha  

*Read this in other languages: [English](Manual_2Captcha.md), [Português](Manual_2Captcha.pr.md), [Español](Manual_2Captcha.es.md)*
  
![banner](imgs/Banner_2Captcha.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este módulo
Para usar este módulo, tienes que tener una cuenta en 2Captcha con créditos. También, si deseas ver la tabla con datos adicionales, tienes que tener abierta la página del captcha con un navegador controlado por Rocketbot.

Método de uso de reCaptcha:
1. Abrir la página del captcha con un navegador controlado por Rocketbot.
2. Ejecutar el comando Resolver reCaptcha.
3. Esperar a que se resuelva el captcha.
4. Obtener el token de respuesta.
5. Ejecutar el siguiente código JavaScript en la página del captcha. Esto hará que se ejecute la función de callback del captcha y se envíe el token de respuesta completando el captcha.

```
function findRecaptchaClients() {
  // eslint-disable-next-line camelcase
  if (typeof (___grecaptcha_cfg) !== 'undefined') {
    // eslint-disable-next-line camelcase, no-undef
    return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {
      const data = { id: cid, version: cid >= 10000 ? 'V3' : 'V2' };
      const 
objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

      objects.forEach(([toplevelKey, toplevel]) => {
        const found = Object.entries(toplevel).find(([_, value]) => (
          value && typeof value === 'object' && 'sitekey' in value && 'size' in value
        ));
     
        if (typeof toplevel === 'object' && toplevel instanceof HTMLElement && toplevel['tagName'] === 'DIV'){
            data.pageurl = toplevel.baseURI;
        }
        
        if (found) {
          const [sublevelKey, sublevel] = found;

          data.sitekey = sublevel.sitekey;
          const callbackKey = data.version === 'V2' ? 'callback' : 'promise-callback';
          const callback = sublevel[callbackKey];
          if (!callback) {
            data.callback = null;
            data.function = null;
          } else {
            data.function = callback;
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => 
`['${key}']`).join('');
            data.callback = `___grecaptcha_cfg.clients${keys}`;
          }
        }
      });
      return data;
    });
  }
  return [];
}

document.querySelector("#g-recaptcha-response").value = "{token}"
document.querySelector("#g-recaptcha-response").innerText = "{token}"

eval(findRecaptchaClients()[0]["callback"])("{token}")

```
6. Continuar con el flujo de trabajo.


## Descripción de los comandos

### Resolver ReCaptcha
  
Resuelve ReCaptcha con API de https://2captcha.com mas información https://2captcha.com/2captcha-api#solving_recaptchav2_new
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos importantes|||
|Key 2Captcha|Key provista por 2Captcha|Key|
|Page url that has ReCaptcha \| pageurl|Url de la página que tiene ReCaptcha|Url de la página|
|Token ReCaptcha \| sitekey||Token|
|Variable donde se almacena el resultado de 2Captcha|Variable donde guardar el resultado|Variable|

### Resolver hCaptcha
  
Resuelve hCaptcha con API de https://2captcha.com mas información https://2captcha.com/2captcha-api#solving_hcaptcha
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos importantes|||
|Key 2Captcha|Key provista por 2Captcha|Key|
|Page url that has hCaptcha \| pageurl|Url de la página que tiene hCaptcha|Url de la página|
|Token hCaptcha \| sitekey||Token|
|Variable donde se almacena el resultado de 2Captcha|Variable donde guardar el resultado|Variable|

### Resolver Captcha Imagen
  
Resuelve un Captcha tipo imagen con API de https://2captcha.com mas información https://2captcha.com/2captcha-api
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Key 2Captcha|Key provista por 2Captcha|Key|
|Ruta a la imagen en su equipo|Ruta donde se encuentra la imagen del captcha|C:/Users/User/Desktop/captcha.png|
|Variable donde se almacena el resultado de 2Captcha|Variable donde guardar el resultado|Variable|
