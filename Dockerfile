# Este é um exemplo de arquivo Docker que você pode modificar para implantar seu próprio aplicativo com base no reconhecimento de rosto

FROM python: 3.4-slim

RUN apt-get update -y
RUN apt-get install -y --fix-faltando \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    ondulação \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-propriedades-comuns \
    fecho eclair \
    && apt-get clean && rm -rf / tmp / * / var / tmp / *

EXECUTAR CD ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.4' - único ramo https://github.com/davisking/dlib.git dlib / && \
    cd dlib / && \
    instalação do python3 setup.py - sim USE_AVX_INSTRUCTIONS


# O restante deste arquivo apenas executa um script de exemplo.

# Se você quiser usar este Dockerfile para executar seu próprio aplicativo, talvez faça o seguinte:
# COPY. / root / your_app_or_whatever
# EXECUTAR cd / root / your_app_or_whatever && \
#      pip3 install -r requirements.txt
# EXECUTAR what_command_you_run_to_start_your_app

COPY . / root / face_recognition
EXECUTAR cd / root / face_recognition && \
    instalação do pip3 -r requirements.txt && \
    instalação do python3 setup.py

CD do CMD / root / face_recognition / examples && \
    python3 accept_faces_in_pictures.py
