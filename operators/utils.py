import pandas as pd


class Utils:
    def listToCsv(objects: list, current_path: str, filename: str):
        df = pd.DataFrame(objects)
        df.to_csv(f"{current_path}/{filename}", index=False)
