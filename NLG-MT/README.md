## NLG+MT method

We used the ControlPrefixes model to generate outputs in English and then translated the generated English text  with selected MT models. This directory contains instructions and configuration files used to run the ControlPrefixes model. 

We used  the official [ControlPrefixes repository](https://github.com/jordiclive/ControlPrefixes/tree/main) and their docker image.

First, follow instructions in the original repository for training using `webnlg17_config.yaml`. After obtaining a checkpoint trained on English WebNLG data, you can use `transform_json_into_cp.py` script to transform the json data test sets that are in evaluation/graph-input into ControlPrefixes format. 

After updating the data.zip file present in [ControlPrefixes repository](https://github.com/jordiclive/ControlPrefixes/tree/main)  with that data, you can run a script to get ControlPrefixes outputs in English, which afterwards can be translated in any language by a chosen model in the MT-Selection directory of this repository.

We have modified the original ControlPrefixes `finetune.py` file to properly handle checkpoints, the modified version is included in this repository.

The example script `run_docker_emnlp.sh` shows how to run the model on the 500 instances test set introduced in our paper (which is located in evaluation/graph-input). It uses a docker image, a `teston_test500.yaml` configuration file, as well as a presaved checkpoint, the modified `data.zip` and the modified `finetune.py` file. 

The output is produced in a pickled format which later can be transformed into plain txt files using `process_pickled_outputs_cp.py` script. 

