FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

RUN pip install rdkit==2023.09.5
RUN pip install scikit-learn==1.6.1
RUN pip install tqdm==4.67.1
RUN pip install matplotlib==3.10.3
RUN pip install chemprop==2.2.0

WORKDIR /repo
COPY . /repo
