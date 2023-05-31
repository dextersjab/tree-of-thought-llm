def get_complex_task(task_name, data_file=None):
    if task_name == 'game24':
        from .game24 import Game24Task
        return Game24Task(data_file)
    elif task_name == 'creativewriting':
        from .creativewriting import CreativeWritingTask
        return CreativeWritingTask(data_file)
    elif task_name == 'crosswords':
        from .crosswords import MiniCrosswordsTask
        return MiniCrosswordsTask(data_file)
    else:
        raise NotImplementedError