FROM nvcr.io/nvidia/pytorch:22.12-py3

LABEL maintainer="utmech26koike@gmail.com"

ARG USER_NAME

ENV DEBIAN_FRONTEND=noninteractive
ENV HOME /root

WORKDIR $HOME

# 
RUN \
apt-get update && \
apt-get upgrade -y && \
apt-get install -y sudo git openssh-server libgl1-mesa-dev && \
apt-get clean
# 
RUN \
sudo chmod 777 -R /root && \
useradd --user-group --create-home --shell /bin/false ${USER_NAME} && \
echo "${USER_NAME} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER ${USER_NAME}

# install libralies
ENV PATH $PATH:/root/.local/bin
COPY requirements.txt .
RUN \
pip install --upgrade pip setuptools --no-cache-dir --user && \
pip install --no-cache-dir -r requirements.txt --user