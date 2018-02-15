# IFCEbvd
### IFCE Biblioteca Virtual Downloader

Ferramenta de download de livros da biblioteca virtual do IFCE. Baixa página a página como imagem e depois converte para pdf. **É necessário uma matricula válida do IFCE.**

### sintaxe:
**$ python ifcebvd.py [matricula] [id do livro]**

### Dependências
1. Biblioteca Selenium, para automatizar a interação com a página web.

**$ pip install -U selenium**

2. Para juntar as imagens e montar o PDF, escolha o pacote de seu agrado. No linux, minha escolha foi o *convert* do pacote Imagemagick. Para instalá-lo:

**$ sudo apt-get install imagemagick**

Outras opções podem ser utilizada, apenas mudando o comando de saida na linha **71** do script.

3. Caso o browser a ser interagido seja o phantomJS

**$ sudo apt-get install phantomjs**

Senão, mudar a linha **21** para:

**b=webdriver.Firefox()**

```
As versões do selenium a partir do v4.0.0-alpha.1 deprecaram o suporte a phantomJS, ao inves
disto, pedem para que se user o chrome ou firefox em modo headless, conforme demonstrado a seguir:
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
```

**OSX**
Todos os passos de instalação previamente descritos são, considerando que o brew estaá instalado:
```
pip install -U selenium
brew install phantomjs
brew install imagemagick
```


