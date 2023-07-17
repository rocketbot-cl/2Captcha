# 2Captcha
  
Módulo para resolver recatpchas com o 2Captcha  

*Read this in other languages: [English](Manual_2Captcha.md), [Português](Manual_2Captcha.pr.md), [Español](Manual_2Captcha.es.md)*
  
![banner](imgs/Banner_2Captcha.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  




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
      const objects = 
Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

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


## Descrição do comando

### Resolver ReCaptcha
  
Resolva o ReCaptcha com a API https://2captcha.com Mais informações https://2captcha.com/2captcha-api#solving_recaptchav2_new
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dados importantes|||
|Key 2Captcha|Chave fornecida pelo 2Captcha|Key|
|Url da página que tem ReCaptcha \| pageurl|Url da página que tem ReCaptcha|Url da página|
|Token ReCaptcha \| sitekey||Token|
|Variável onde o resultado do 2Captcha é armazenado|Variável onde salvar o resultado|Variable|

### Resolver Captcha Imagen
  
Resolva um Captcha de imagem com a API https://2captcha.com mais informações https://2captcha.com/2captcha-api
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Key 2Captcha|Key fornecida pelo 2Captcha|Key|
|Caminho para a imagem no seu computador|Caminho onde a imagem do captcha está localizada|C:/Users/User/Desktop/captcha.png|
|Variável onde o resultado do 2Captcha é armazenado|Variável para salvar o resultado|Variable|
