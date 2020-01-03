FROM continuumio/miniconda3

WORKDIR /app

ADD . /app

RUN conda create -n fastai_v1 python=3.6

RUN activate fastai_v1

RUN conda install fastai pytorch=1.0.0 -c fastai -c pytorch -c conda-forge

RUN conda install pip

RUN pip install google_images_download

RUN pip install Flask

EXPOSE 5000

CMD ["python","app.py"]