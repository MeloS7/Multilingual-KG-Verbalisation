docker run --name controlprefixes --gpus '"all"' --rm -id jordiclive/controlprefixes:main-latest
docker cp teston_test500.yaml controlprefixes:/app/src/datatotext/configs/

docker exec -i controlprefixes sh -c "mkdir src/output_dir"
docker cp "cp_docker_save/output_dir/output_dir/checkpoint_name.ckpt" controlprefixes:/app/src/
docker cp finetune.py controlprefixes:/app/src/datatotext/finetune.py
docker cp data.zip controlprefixes:/app/src/data.zip
docker exec -i controlprefixes sh -c "unzip src/data.zip"
docker exec -i controlprefixes sh -c "unzip src/datatotext/utils.zip"

docker exec -i controlprefixes sh -c "cd src/datatotext && python read_yaml.py configs/teston_test500.yaml" > cp_test_500test_logs
mkdir cp_eval_res
mkdir cp_eval_res/500test
docker cp controlprefixes:/app/src/output_dir/val_outputs cp_eval_res/500test
docker cp controlprefixes:/app/src/datatotext/outputs_all_testsets.pkl cp_eval_res/500test

docker stop controlprefixes
