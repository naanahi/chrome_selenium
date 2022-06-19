FROM ubuntu:latest

RUN apt-get update && apt-get install -y unzip wget vim && apt-get install -y python3 python3-pip

# google-chrome 変更部分
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
wget http://dl.google.com/linux/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_93.0.4577.18-1_amd64.deb && \
apt-get install -y -f ./google-chrome-unstable_93.0.4577.18-1_amd64.deb

# ChromeDriver 変更部分
ADD https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

# 追加設定
WORKDIR /opt/chrome/
COPY requirements.txt /opt/chrome/
COPY *.py /opt/chrome/
RUN mkdir csvdata
RUN pip3 install -r requirements.txt