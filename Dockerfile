FROM python:3

RUN apt-get update && apt-get install -y unzip wget vim

# google-chrome 変更部分
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
wget http://dl.google.com/linux/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_93.0.4577.18-1_amd64.deb && \
apt-get install -y -f ./google-chrome-unstable_93.0.4577.18-1_amd64.deb

# ChromeDriver 変更部分
ADD https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

# 以下から追記
WORKDIR /usr/src/app/
RUN mkdir db
RUN mkdir csv
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt