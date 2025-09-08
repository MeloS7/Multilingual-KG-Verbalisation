## NLG+MT method

We used ControlPrefixes model to generate outputs in English and then translated them with MT choden MT models. This directory contains instructions and configuration files used to run the ControlPrefixes model. 

We used official [ControlPrefixes repository](https://github.com/jordiclive/ControlPrefixes/tree/main) and their docker image.

First, follow instructions in the original repository for training using `webnlg17_config.yaml`. After obtaining a checkpoint trained on English WebNLG data, you can use `transform_json_into_cp.py` script to transform our json data test sets into ControlPrefixes format. 

After updating data.zip with that data, you can run a script to get ControlPrefixes outputs in English, which afterwards can be translated in any language by a chosen model in the MT part of the repository.

We have modified an original ControlPrefixes `finetune.py` file to properly handle checkpoints, the modified version is included in this repository.

The example script `run_docker_emnlp.sh` shows how to run the model on a 500 instances test set introduced in our paper. It uses a docker image, a `teston_test500.yaml` configuration file, as well as a presaved checkpoint, modified `data.zip` and a modified `finetune.py` file. 

The output is retrieved in a pickled format which later can be transformed into plain txt files using `process_pickled_outputs_cp.py` script. 

