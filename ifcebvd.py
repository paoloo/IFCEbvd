# -*- coding: utf-8 -*-
#    _ ____       Instituto Federal de
#   (_) __/        Educação, Ciência e
#  / / _/          Tecnologia do Ceará
# /_/_/  BIBLIOTECA VIRTUAL DOWNLOADER

from selenium import webdriver
import urllib, md5, os, sys

def _baixa(_url,_nome):
  try:
    urllib.urlretrieve(_url, _nome)
  except:
    print 'problemas ao baixar %s' % _nome
  else:
    print '%s baixado' % _nome

_hash = lambda(_mat): 'login=%s&token=%s' % (_mat, md5.new('%sQJEkJM2iLJiAj6LScxsZivml54SmzSy0' % _mat).hexdigest())

def _dump(matricula, id_livro):
  b=webdriver.PhantomJS()
  print 'gerando cookie de login para matricula %s...' % matricula
  b.get('http://ifce.bv3.digitalpages.com.br/user_session/authentication_gateway?%s' % _hash(matricula))
  print 'inicializando...'
  b.get('http://ifce.bv3.digitalpages.com.br/users/publications/%s' % id_livro)
  print 'obtendo informacoes para o livro %s...' % id_livro
  p_1 = 0
  while(p_1 == 0):
    try:
      p_1 = b.execute_script("if ($('.backgroundImg')[0]) { return 1 } else { return 0 }")
    except:
      p_1 = 0
  num_pag = int(b.execute_script("return RDP.options.pageSetLength")) - 2
  print 'preparando para baixar livro id=%s com %d paginas...' % (id_livro, num_pag)
  _baixa(b.execute_script("return $('.backgroundImg')[0].src"), "%s-00000.jpg" % id_livro)
  print 'baixando livro...'
  b.execute_script("navigate.next_page()")
  _v_p1, _v_p2 = '' , ''
  for i in range(1, num_pag, 2):
    # loop para esperar a pagina carregar
    p_1 , p_2 = 0 , 0
    while ((p_1==0) or (p_2==0)):
      try:
        p_1 = b.execute_script("if ($('.backgroundImg')[0]) { return 1 } else { return 0 }")
        p_2 = b.execute_script("if ($('.backgroundImg')[1]) { return 1 } else { return 0 }")
      except:
        p_1 , p_2 = 0 , 0
    # carregou, pegar endereco
    _p1 = b.execute_script("return $('.backgroundImg')[0].src")
    _p2 = b.execute_script("return $('.backgroundImg')[1].src")
    # checa se ainda não carregou a nova pagina
    while((_p1 == _v_p1) or (_p2 == _v_p2)):
      try:
        _p1 = b.execute_script("return $('.backgroundImg')[0].src")
        _p2 = b.execute_script("return $('.backgroundImg')[1].src")
      except:
        pass
    # carregou nova, baixar...
    _baixa(_p1, "%s-%05d.jpg" % (id_livro, i))
    _baixa(_p2, "%s-%05d.jpg" % (id_livro, i+1))
    # ajusta os novos valores
    _v_p1 , _v_p2 = _p1 , _p2
    b.execute_script("navigate.next_page()")
    print 'baixadas %d/%d paginas...' % (i,num_pag)
  print 'fim do dump'
  b.quit()

def _gerapdf(_livro):
  # usando a ferramenta convert do ImageMagick
  print 'convertendo para PDF...'
  os.system('convert *.jpg %s.pdf' % livro)
  print 'limpando os jpgs residuais...'
  os.system('rm *.jpg')

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "\033[91mifcebvd.py -- IFCE Biblioteca Virtual Downloader  \033[0m"
    print "\033[91msintaxe: ./ifcebvd.py [matricula] [id do livro]   \033[0m"
    sys.exit(1)
  else:
    matricula = sys.argv[1]
    livro = sys.argv[2]
    _dump(matricula , livro)
    _gerapdf(livro)
    print '\033[92moperacao finalizada.\033[0m'
