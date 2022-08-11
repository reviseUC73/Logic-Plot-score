import pandas as pd


class Data:

    def __init__(self, data_file_name):
        file = pd.read_csv(data_file_name)
        self.data = pd.DataFrame(file)
