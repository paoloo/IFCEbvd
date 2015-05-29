# IFCEbvd
### IFCE Biblioteca Virtual Downloader

Ferramenta de download de livros da biblioteca virtual do IFCE.
Baixa página a página como imagem e depois converte para pdf.
É necessário uma matricula válida do IFCE.

### Dependências
Caso o browser a ser interagido seja o phantomJS

**$ sudo apt-get install phantomjs**

Senão, mudar a linha 21 para:

**b=webdriver.Firefox()**

Biblioteca Selenium, para automatizar a interação com a página web.

**$ pip install -U selenium**

Para juntar as imagens e montar o PDF, escolha o pacote de seu agrado. No linux, minha escolha foi o convert do pacote Imagemagick

Para instalá-lo:

**$ sudo apt-get install imagemagick**

Outras opções podem ser utilizada, apenas mudando o comando de saida na linha 70 do script.
