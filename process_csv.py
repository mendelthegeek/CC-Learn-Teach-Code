import pandas as pd

df = pd.read_csv("Mock_user_data.csv")
df.to_json("Json_output.json", orient="records")