python run.py \
    --task_name creativewriting \
    --task_data_file data_100_random_text.txt \
    --task_start_index 0 \
    --task_end_index 1 \
    --naive_run \
    --prompt_sample cot \
    --n_generate_sample 10 \
    --temperature 1.0 \
    "${@}"

# 0.03 dollars per line ->  3 dollars for 100 lines?