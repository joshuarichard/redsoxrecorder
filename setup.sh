#!/bin/bash

# setup audiodevice
echo "Installing audiodevice..."
wget http://whosawhatsis.com/paraphernalia/audiodevice.zip
unzip audiodevice.zip
mv Audiodevice/audiodevice /usr/local/bin/

# install sox
echo "Installing sox..."
brew install sox

# install lame
echo "Installing lame..."
curl -L -O http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
tar -zxvf lame-3.99.5.tar.gz
rm -r lame-3.99.5.tar.gz
cd lame-3.99.5
./configure
make
sudo make install

# wget chromedriver and PATH it
echo "Installing chromedriver..."
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
mkdir webdriver
mv chromedriver webdriver/
PATH=$PATH:/$PWD/webdriver/

echo "Done!"
