python run.py \
    --task_name game24 \
    --task_data_file 24.csv \
    --task_start_index 900 \
    --task_end_index 1000 \
    --naive_run \
    --prompt_sample cot \
    --n_generate_sample 100 \
    "${@}"