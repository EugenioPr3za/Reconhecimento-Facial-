#! / usr / bin / env python
# - * - codificação: utf-8 - * -

de  setuptools  import  setup

com  open ( 'README.rst' ) como  readme_file :
    readme  =  readme_file . read ()

com  open ( 'HISTORY.rst' ) como  arquivo_de_história :
    history  =  history_file . read ()

requisitos  = [
    'face_recognition_models' ,
    'Clique> = 6.0' ,
    «dlib> = 19.3.0» ,
    'numpy' ,
    "Almofada" ,
    'scipy> = 0.17.0'
]

test_requirements  = [
    'tox' ,
    'flake8'
]

configuração (
    name = 'face_recognition' ,
    version = '0.2.0' ,
    description = "Reconhecer faces do Python ou da linha de comando" ,
    long_description = leia-me  +  ' \ n \ n '  +  histórico ,
    author = "Adam Geitgey" ,
    author_email = 'ageitgey@gmail.com' ,
    url = 'https://github.com/ageitgey/face_recognition' ,
    packages = [
        'face_recognition' ,
    ],
    package_dir = { 'face_recognition' : 'face_recognition' },
    package_data = {
        'face_recognition' : [ 'modela / *. dat' ]
    }
    entry_points = {
        'console_scripts' : [
            'face_recognition = face_recognition.cli: main'
        ]
    }
    install_requires = requisitos ,
    license = "licença MIT" ,
    zip_safe = False ,
    keywords = 'face_recognition' ,
    classificadores = [
        'Status do desenvolvimento :: 4 - Beta' ,
        'Público-alvo :: Desenvolvedores' ,
        'Licença :: OSI Aprovado :: Licença MIT' ,
        'Natural Language :: English' ,
        "Linguagem de programação :: Python :: 2" ,
        'Linguagem de programação :: Python :: 2.6' ,
        'Linguagem de programação :: Python :: 2.7' ,
        'Linguagem de programação :: Python :: 3' ,
        'Linguagem de programação :: Python :: 3.3' ,
        'Linguagem de programação :: Python :: 3.4' ,
        'Linguagem de programação :: Python :: 3.5' ,
        'Linguagem de programação :: Python :: 3.6' ,
    ],
    test_suite = 'testes' ,
    tests_require = test_requirements
