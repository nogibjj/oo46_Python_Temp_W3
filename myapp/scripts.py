import polars as pl


def read_csv():
    df = pl.read_csv("./dsets/automobiles.csv")
    return df
    


def mpg_cat(mpg):
    if mpg < 15:
        return "Low"
    elif mpg < 25:
        return "Moderate"
    else:
        return "High"
    


def my_stats(df):
    # my_df = read_csv()
    car_dataset = df.select("mpg", "cyl", "displ", "hp", "weight", "accel")
    return car_dataset.describe()
    
