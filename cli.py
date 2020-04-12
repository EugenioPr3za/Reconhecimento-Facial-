# - * - codificação: utf-8 - * -
de __future__ import  print_function
 clique de importação
importação  os
importação  re
importação  scipy . misc
 avisos de importação
importar  face_recognition . API  como  face_recognition
 multiprocessamento de importação
 ferramentas de importação
 sys de importação


def  scan_known_people ( known_people_folder ):
    names_names  = []
    known_face_encodings  = []

    para o  arquivo  em  image_files_in_folder ( known_people_folder ):
        basename  =  os . caminho . splitext ( os . path . basename ( arquivo )) [ 0 ]
        img  =  face_recognition . load_image_file ( arquivo )
        codificações  =  face_recognition . face_encodings ( img )

        se  len ( codificações ) >  1 :
            clique . eco ( "AVISO: Mais de uma face encontrada em {}. Considerando apenas a primeira face." . formato ( arquivo ))

        se  len ( codificações ) ==  0 :
            clique . eco ( "AVISO: Não foram encontrados rostos em {}. Ignorando arquivo." . formato ( arquivo ))
        mais :
            names_names . anexar ( nome da base )
            known_face_encodings . acrescentar ( codificações [ 0 ])

    retornar  nomes_conhecidos , códigos_da_face_conhecidos


def  test_image ( image_to_check , names_names , known_face_encodings ):
    unknown_image  =  face_recognition . load_image_file ( image_to_check )

    # Reduza a imagem se for gigante, para que as coisas corram um pouco mais rápido
    se  imagem_ desconhecida . forma [ 1 ] >  1600 :
        fator_escala  =  1600.0  /  unknown_image . forma [ 1 ]
        com  avisos . catch_warnings ():
            avisos . filtro simples ( "ignorar" )
            unknown_image  =  scipy . misc . imresize ( unknown_image , fator_escala )

    unknown_encodings  =  face_recognition . face_encodings ( unknown_image )

    para  unknown_encoding  em  unknown_encodings :
        result  =  face_recognition . compare_faces ( known_face_encodings , unknown_encoding )

        se  True  no  resultado :
            [ print ( "{}, {}" . formato ( image_to_check , name )) para  is_match , nome  em  zip ( resultado , nome_nome ) se  is_match ]
        mais :
            print ( "{}, pessoa_ desconhecida " . formato ( imagem_para verificar ))


def  image_files_in_folder ( folder ):
    retornar [ os . caminho . join ( pasta , f ) para  f  em  os . listdir ( pasta ) se  re . match ( r '. * \. (jpg | jpeg | png)' , f , sinalizadores = re . I )]


def  process_images_in_process_pool ( images_to_check , names_name , known_face_encodings , number_of_cpus ):
    se  number_of_cpus  ==  - 1 :
        processos  =  nenhum
    mais :
        processos  =  número_de_cpus

    # O macOS travará devido a um erro no libdispatch se você não usar 'forkserver'
    contexto  =  multiprocessamento
    se  "forkserver"  no  multiprocessamento . get_all_start_methods ():
        contexto  =  multiprocessamento . get_context ( "servidor de forks" )

    pool  =  contexto . Pool ( processos = processos )
    function_parameters  =  zip ( images_to_check , itertools . repeat ( nomes_nome )), itertools . repeat ( nome_face_encodings ))

    piscina . starmap ( test_image , function_parameters )


@ clique . command ()
@ clique . argumento ( 'known_people_folder' )
@ clique . argumento ( 'image_to_check' )
@ clique . opção ( '--cpus' , padrão = 1 , help = 'número de núcleos de CPU para usar em paralelo (pode acelerar o processamento de muitas imagens). -1 significa "usar tudo no sistema"' )
def  main ( pasta_de_personagens_de_pessoas , imagem-para- verificação , cpus ):
    nomes_conhecidos , códigos_da_face_conhecida  =  pessoas_de_conhecidas-digitalização ( pasta_de_pessoas_conhecidas )

    # Processamento multinúcleo suportado apenas no Python 3.4 ou superior
    if ( sys . version_info  < ( 3 , 4 )) e  cpus  ! =  1 :
        clique . echo ( "AVISO: O suporte a multiprocessamento requer Python 3.4 ou superior. Voltando ao processamento de thread único!" )
        cpus  =  1

    se  os . caminho . isdir ( image_to_check ):
        se  cpus  ==  1 :
            [ Test_image ( image_file , known_names , known_face_encodings ) para  image_file  em  image_files_in_folder ( image_to_check )]
        mais :
            process_images_in_process_pool ( image_files_in_folder ( image_to_check ), known_names , known_face_encodings , CPUs )
    mais :
        test_image ( image_to_check , names_name , names_face_encodings )


se  __name__  ==  "__main__" :
