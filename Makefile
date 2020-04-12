.PHONY : documentação limpa-teste limpo-pyc clean-build docs ajuda
.DEFAULT_GOAL : = ajuda
definir  BROWSER_PYSCRIPT
import os, navegador da web, sys
experimentar:
	de urllib import pathname2url
exceto:
	de urllib.request import pathname2url

webbrowser.open ("file: //" + nome do caminho2url (os.path.abspath (sys.argv [1])))
endef
exportar  BROWSER_PYSCRIPT

definir  PRINT_HELP_PYSCRIPT
import re, sys

para linha em sys.stdin:
	match = re.match (r '^ ([a-zA-Z _-] +):. *? # # (. *) $$', linha)
	se corresponder:
		target, help = match.groups ()
		print ("% - 20s% s"% (destino, ajuda))
endef
exportar  PRINT_HELP_PYSCRIPT
NAVEGADOR : = python3 -c "$$ BROWSER_PYSCRIPT"

ajuda :
	@ python3 -c " $$ PRINT_HELP_PYSCRIPT "  <  $ ( MAKEFILE_LIST )

clean : clean-build clean-pyc clean-test # # remove todos os artefatos de compilação, teste, cobertura e Python


clean-build : # # remove artefatos de build
	rm -fr build /
	rm -fr dist /
	rm -fr .eggs /
	encontrar . -name ' * .egg-info ' -exec rm -fr {} +
	encontrar . -name ' * .egg ' -exec rm -f {} +

clean-pyc : # # remove artefatos de arquivo Python
	encontrar . -name ' * .pyc ' -exec rm -f {} +
	encontrar . -name ' * .pyo ' -exec rm -f {} +
	encontrar . -name ' * ~ ' -exec rm -f {} +
	encontrar . -name ' __pycache__ ' -exec rm -fr {}

clean-test : # # remove artefatos de teste e cobertura
	rm -fr .tox /
	rm -f .coverage
	rm -fr htmlcov /

lint : # # verifique o estilo com o flake8
	flake8 face_recognition tests

test : # # execute testes rapidamente com o Python padrão

		teste python3 setup.py

test-all : # # executa testes em todas as versões do Python com tox
	tox

cobertura : # # verifique a cobertura do código rapidamente com o Python padrão

		execução da cobertura --source face_recognition setup.py test

		relatório de cobertura -m
		cobertura html
		$ (BROWSER) htmlcov / index.html

docs : # # gera documentação em HTML do Sphinx, incluindo documentos da API
	sphinx-apidoc -o docs / face_recognition
	Documentos $ ( MAKE ) -C limpos
	$ ( MAKE ) -C docs html
	$ ( BROWSER ) docs / _build / html / index.html

servidoocs : docs # # compila os documentos observando alterações
	watchmedo shell-command -p ' * .rst ' -c ' $ (MAKE) -C docs html ' -R -D .

release : limpe o pacote # # e faça o upload de um release
	upload python3 setup.py sdist
	upload python3 setup.py bdist_wheel

dist : clean # # cria pacote fonte e roda
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	ls -l dist

install : clean # # instala o pacote nos pacotes de sites ativos do Python
	instalação do python3 setup.py
