import pandas as pd
import fire
from pathlib import Path


def export_dataframe(df, name):
    df.to_csv(f"datasets/{name}.csv", index=False)
    df.to_excel(f"datasets/{name}.xlsx", index=False)
    df.to_json(f"datasets/{name}.json", orient="records")


def preprocess(path):
    path = Path(path)

    df = pd.read_csv(path / "timeline.csv")
    df.columns = [
        "Date",
        "CumCase",
        "Recovered",
        "CurrentlyInfectedPatients",
        "Deaths",
    ]
    df = df[["Date", "CurrentlyInfectedPatients", "Recovered", "Deaths"]]
    df = df.drop_duplicates()

    # out = pd.merge(df, df1, left_on="Date", right_on="Date")
    df["Date"] = pd.to_datetime(df.Date)
    # out = out.set_index("Date")
    export_dataframe(df, "thstat")


if __name__ == "__main__":
    fire.Fire()
