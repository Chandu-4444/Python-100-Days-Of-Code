import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrel = len(data[data["Primary Fur Color"]=='Cinnamon'])
black_squirrel = len(data[data["Primary Fur Color"]=='Black'])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrel, black_squirrel]
}
d_frame = pd.DataFrame(data_dict)
d_frame.to_csv("Stats.csv", header="")
