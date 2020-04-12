# - * - codificação: utf-8 - * -

importação  scipy . misc
importar  dlib
importar  numpy  como  np

tente :
    importar  face_recognition_models
exceto :
    print ( "Instale` face_recognition_models` com este comando antes de usar `face_recognition`:" )
    print ()
    print ( "pip install git + https: //github.com/ageitgey/face_recognition_models" )
    quit ()

face_detector  =  dlib . get_frontal_face_detector ()

predictor_model  =  face_recognition_models . pose_predictor_model_location ()
pose_predictor  =  dlib . shape_predictor ( preditor_model )

face_recognition_model  =  face_recognition_models . face_recognition_model_location ()
face_encoder  =  dlib . face_recognition_model_v1 ( face_recognition_model )


def  _rect_to_css ( rect ):
    "" "
    Converter um objeto dlib 'rect' em uma tupla simples na ordem (superior, direita, inferior, esquerda)
    : param rect: um objeto dlib 'rect'
    : return: uma representação simples da tupla do ret na ordem (superior, direita, inferior, esquerda)
    "" "
    return  rect . superior (), ret . direita (), ret . inferior (), ret . esquerda ()


def  _css_to_rect ( css ):
    "" "
    Converter uma tupla em ordem (superior, direita, inferior, esquerda) em um objeto dlib `rect`
    : param css: representação simples da tupla do ret na ordem (superior, direita, inferior, esquerda)
    : return: um objeto dlib `rect`
    "" "
    retornar  dlib . retângulo ( css [ 3 ], css [ 0 ], css [ 1 ], css [ 2 ])


def  _trim_css_to_bounds ( css , image_shape ):
    "" "
    Verifique se uma tupla na ordem (superior, direita, inferior, esquerda) está dentro dos limites da imagem.
    : param css: representação simples da tupla do ret na ordem (superior, direita, inferior, esquerda)
    : param image_shape: forma numpy da matriz de imagens
    : return: uma representação de tupla simples aparada do ret (ordem superior, direita, inferior, esquerda)
    "" "
    retorno  max ( css [ 0 ], 0 ), min ( css [ 1 ], forma da imagem [ 1 ]), min ( css [ 2 ], forma da imagem [ 0 ]), max ( css [ 3 ], 0 )


def  face_distance ( face_encodings , face_to_compare ):
    "" "
    Dada uma lista de codificações de face, compare-as com uma codificação de face conhecida e obtenha uma distância euclidiana
    para cada face de comparação. A distância mostra como os rostos são semelhantes.
    : param faces: lista de codificações de faces para comparar
    : param face_to_compare: uma codificação de face para comparar
    : return: um ndarray numpy com a distância de cada face na mesma ordem que a matriz 'faces'
    "" "
    se  len ( face_encodings ) ==  0 :
        return  np . vazio (( 0 ))

    return  np . linalg . norma ( codificações_frontais  -  face_para_comparar , eixo = 1 )


def  load_image_file ( nome do arquivo , mode = 'RGB' ):
    "" "
    Carrega um arquivo de imagem (.jpg, .png, etc) em uma matriz numpy
    : param filename: arquivo de imagem a ser carregado
    : param mode: format para converter a imagem. Apenas 'RGB' (RGB de 8 bits, 3 canais) e 'L' (preto e branco) são suportados.
    : return: conteúdo da imagem como matriz numpy
    "" "
    devolver  scipy . misc . imread ( nome do arquivo , mode = mode )


def  _raw_face_locations ( img , number_of_times_to_upsample = 1 ):
    "" "
    Retorna uma matriz de caixas delimitadoras de rostos humanos em uma imagem
    : param img: uma imagem (como uma matriz numpy)
    : param number_of_times_to_upsample: quantas vezes para aumentar a amostra da imagem procurando rostos. Números mais altos encontram rostos menores.
    : return: Uma lista de objetos dlib 'rect' dos locais de face encontrados
    "" "
    retornar  face_detector ( img , number_of_times_to_upsample )


def  face_locations ( img , number_of_times_to_upsample = 1 ):
    "" "
    Retorna uma matriz de caixas delimitadoras de rostos humanos em uma imagem
    : param img: uma imagem (como uma matriz numpy)
    : param number_of_times_to_upsample: quantas vezes para aumentar a amostra da imagem procurando rostos. Números mais altos encontram rostos menores.
    : return: Uma lista de tuplas de locais de face encontrados em ordem css (superior, direita, inferior, esquerda)
    "" "
    retornar [ _trim_css_to_bounds ( _rect_to_css ( face ), forma img . ) para face em _raw_face_locations ( img , número_de_times_to_upsample )]   


def  _raw_face_landmarks ( face_image , face_locations = None ):
    se  face_locations  for  None :
        face_locations  =  _raw_face_locations ( face_image )
    mais :
        face_locations  = [ _css_to_rect ( face_location ) para  face_location  em  face_locations ]

    retornar [ pose_predictor ( face_image , face_location ) para  face_location  em  face_locations ]


def  face_landmarks ( face_image , face_locations = None ):
    "" "
    Dada uma imagem, retorna um ditado dos locais dos recursos do rosto (olhos, nariz etc.) para cada rosto na imagem
    : param face_image: imagem para pesquisa
    : param face_locations: opcionalmente, forneça uma lista dos locais das faces a serem verificadas.
    : return: Uma lista de dictos de locais de rosto (olhos, nariz, etc)
    "" "
    marcos  =  _raw_face_landmarks ( face_image , face_locations )
    landmarks_as_tuples  = [[( p . x , p . y ) para  p  no  ponto de referência . parts ()] para  ponto  de referência em  pontos de referência ]

    # Para obter uma definição de cada índice de pontos, consulte https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png
    retornar [{
        "queixo" : pontos [ 0 : 17 ],
        "left_eyebrow" : pontos [ 17 : 22 ],
        "right_eyebrow" : pontos [ 22 : 27 ],
        "nose_bridge" : pontos [ 27 : 31 ],
        "nose_tip" : pontos [ 31 : 36 ],
        "left_eye" : pontos [ 36 : 42 ],
        "right_eye" : pontos [ 42 : 48 ],
        "top_lip" : pontos [ 48 : 55 ] + [ pontos [ 64 ]] + [ pontos [ 63 ]] + [ pontos [ 62 ]] + [ pontos [ 61 ]] + [ pontos [ 60 ]],
        "lábio inferior" : pontos [ 54 : 60 ] + [ pontos [ 48 ]] + [ pontos [ 60 ]] + [ pontos [ 67 ]] + [ pontos [ 66 ]] + [ pontos [ 65 ]] + [ pontos [ 64 ]]
    } para  pontos  em  marcos_com_tuplos ]


def  face_encodings ( face_image , local_face_locations = Nenhum , num_jitters = 1 ):
    "" "
    Dada uma imagem, retorne a codificação de face de 128 dimensões para cada face da imagem.
    : param face_image: a imagem que contém uma ou mais faces
    : param known_face_locations: Opcional - as caixas delimitadoras de cada face, se você já as conhece.
    : param num_jitters: Quantas vezes para amostrar novamente a face ao calcular a codificação. Maior é mais preciso, mas mais lento (ou seja, 100 é 100x mais lento)
    : return: Uma lista de codificações de face de 128 dimensões (uma para cada face na imagem)
    "" "
    raw_landmarks  =  _raw_face_landmarks ( face_image , known_face_locations )

    retornar [ np . array ( face_encoder . compute_face_descriptor ( face_image , raw_landmark_set , num_jitters )) para  raw_landmark_set  em  raw_landmarks ]


def  compare_faces ( codificação_face_da_conhecida , codificação_da_verdadeiro_de_ verificação , tolerância = 0,6 ):
    "" "
    Compare uma lista de codificações de face com uma codificação candidata para ver se elas correspondem.
    : param known_face_encodings: Uma lista de codificações de face conhecidas
    : param face_encoding_to_check: uma única codificação de face para comparar com a lista
    : param tolerance: Quanta distância entre as faces é considerada uma correspondência. Menor é mais rigoroso. 0,6 é o melhor desempenho típico.
    : return: Uma lista de valores Verdadeiro / Falso indicando quais codificações_face_conhecidas correspondem à codificação de face para verificar
    "" "
     lista de retorno ( face_distance ( face_encodings_conhecidas , face_encoding_to_check ) <=  tolerância )
