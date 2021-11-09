#!/bin/bash

sudo apt install python3 python3-pip python3-venv gunicorn3 -y

#python3 -m venv venv
#source venv/bin/activate

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
cat - > /tmp/app.service << EOF
[Unit]
Description=Run flask app as systemd

[Service]
User=jenkins
Environment=db_uri=$db_uri
Environment=secretkey=$secretkey
Environment=GUNICORN_CMD_ARGS='--workers=4 --bind=0.0.0.0:5000'
ExecStart=/bin/sh -c "cd /home/jenkins/.jenkins/workspace/demo-proj && gunicorn3 app:app"

[Install]
WantedBy=multi-user.target
EOF

sudo cp /tmp/app.service /etc/systemd/system/app.service
sudo systemctl daemon-reload
sudo systemctl start app