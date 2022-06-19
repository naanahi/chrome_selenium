FROM python:3

RUN apt-get update && apt-get install -y unzip wget vim

# google-chrome 変更部分①
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
wget http://dl.google.com/linux/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_93.0.4577.18-1_amd64.deb && \
apt-get install -y -f ./google-chrome-unstable_93.0.4577.18-1_amd64.deb

# ChromeDriver 変更部分②
ADD https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip

# python package
RUN pip install selenium && \
pip install bs4 && \
pip install oauth2client

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome