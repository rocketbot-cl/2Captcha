# 2Captcha
  
Module to solve recatpchas with 2Captcha  

*Read this in other languages: [English](Manual_2Captcha.md), [Português](Manual_2Captcha.pr.md), [Español](Manual_2Captcha.es.md)*
  
![banner](imgs/Banner_2Captcha.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

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



## Description of the commands

### Resolve ReCaptcha
  
Resolve ReCaptcha with an API of https://2captcha.com mas información https://2captcha.com/2captcha-api#solving_recaptchav2_new
|Parameters|Description|example|
| --- | --- | --- |
|Important Data|||
|Key 2Captcha|Key provided by 2Captcha|Key|
|Url de la página que tiene ReCaptcha \| pageurl|Url of the page that has ReCaptcha|Page url|
|Token ReCaptcha \| sitekey||Token|
|Variable where the result of 2Captcha is stored|Variable where to save the result|Variable|

### Resolve Image Captcha
  
Resolve a Image Captcha with an API of https://2captcha.com more information https://2captcha.com/2captcha-api
|Parameters|Description|example|
| --- | --- | --- |
|Key 2Captcha|Key provided by 2Captcha|Key|
|Path to the image on your computer|Path where the captcha image is located|C:/Users/User/Desktop/captcha.png|
|Variable where the result of 2Captcha is stored|Variable to save the result|Variable|
