## How to use this module
In order to use this module, you need to have a 2Captcha account with funds. Also, if you want to see the help in the table, you need to open the captcha web page with a Rocketbot browser.

How to use reCaptcha:
1. Open the captcha web page with a Rocketbot browser.
2. Execute the command Resolve reCaptcha.
3. Wait for the captcha to be solved.
4. Get the response token.
5. Execute the following JavaScript code in the captcha web page. This will execute the captcha callback function and send the response token completing the captcha.

```
function findRecaptchaClients() {
  // eslint-disable-next-line camelcase
  if (typeof (___grecaptcha_cfg) !== 'undefined') {
    // eslint-disable-next-line camelcase, no-undef
    return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {
      const data = { id: cid, version: cid >= 10000 ? 'V3' : 'V2' };
      const objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

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
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => `['${key}']`).join('');
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
6. Continue with the workflow.


---

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
      const objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

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
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => `['${key}']`).join('');
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

---


## Como usar este módulo
Para usar este módulo, você precisa ter uma conta no 2Captcha com créditos. Além disso, se você quiser ver a tabela com dados adicionais, você precisa ter a página do captcha aberta com um navegador controlado pelo Rocketbot.

Como usar o reCaptcha:
1. Abra a página do captcha com um navegador controlado pelo Rocketbot.
2. Execute o comando Resolver reCaptcha.
3. Aguarde o captcha ser resolvido.
4. Obtenha o token de resposta.
5. Execute o seguinte código JavaScript na página do captcha. Isso executará a função de retorno de chamada do captcha e enviará o token de resposta completando o captcha.

```
function findRecaptchaClients() {
  // eslint-disable-next-line camelcase
  if (typeof (___grecaptcha_cfg) !== 'undefined') {
    // eslint-disable-next-line camelcase, no-undef
    return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {
      const data = { id: cid, version: cid >= 10000 ? 'V3' : 'V2' };
      const objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

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
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => `['${key}']`).join('');
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
6. Continue com o fluxo de trabalho.

