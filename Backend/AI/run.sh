#!/bin/bash
#cd machine_learning_model/Answering_questions/
#
#python3 setup.py develop
#
#cd ../..

cd server/

export FLASK_APP=api.py

flask run --host=0.0.0.0
