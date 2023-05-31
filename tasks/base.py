DATA_PATH = './data'


class Task:
    def __init__(self):
        self.data = []
        self.value_cache = {}
        self.steps = 0
        self.stops = []

    def __len__(self) -> int:
        pass

    def get_input(self, idx: int) -> str:
        pass

    def test_output(self, idx: int, output: str):
        pass

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        pass

    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        pass

    @staticmethod
    def propose_prompt_wrap(x: str, y:str='') -> str:
        pass
