#!/bin/bash

sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

while getopts "c" options; do
  case ${options} in
    c) create=true;;
  esac
done

if [ ${create} ]; then
  python3 create.py
fi

echo 'TESTING:'
python3 -m pytest --cov=application --cov-report html

#python3 app.py
gunicornpath=$(pwd)/venv/lib/python3.6/site-packages
cat - > /tmp/app.service << EOF
[Unit]
Description=Run flask app as systemd

[Service]
User=jenkins
Environment=db_uri=$db_uri
Environment=secretkey=$secretkey
Environment=path=$gunicornpath
ExecStart=/bin/sh -c "$path/gunicorn --workers=4 --bind=0.0.0.0:5000 app:app --daemon"

[Install]
WantedBy=multi-user.target
EOF

sudo cp /tmp/app.service /etc/systemd/system/app.service
sudo systemctl daemon-reload
sudo systemctl start app