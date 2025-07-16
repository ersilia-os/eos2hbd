FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

#RUN pip install rdkit==2023.3.1
#RUN pip install scikit-learn==0.24.2
RUN pip install tqdm==4.67.1
RUN pip install matplotlib==3.10.3
# RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@main
RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@main#egg=lazyqsar[full]

WORKDIR /repo
COPY . /repo
