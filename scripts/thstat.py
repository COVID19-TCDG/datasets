import pandas as pd
import fire
from pathlib import Path


def export_dataframe(df, name):
    df.to_csv(f"datasets/{name}.csv", index=False)
    df.to_excel(f"datasets/{name}.xlsx", index=False)
    df.to_json(f"datasets/{name}.json", orient="records")


def preprocess(path):
    path = Path(path)

    df = pd.read_csv(path / "timeline_summary.csv")
    df.columns = ["Date", "CumCase"]

    df1 = pd.read_csv(path / "timeline.csv")
    df1.columns = ["Date", "Recovered", "CurrentlyInfectedPatients", "Deaths"]
    df1 = df1[["Date", "CurrentlyInfectedPatients", "Recovered", "Deaths"]]
    df1 = df1.drop_duplicates()

    out = pd.merge(df, df1, left_on="Date", right_on="Date")
    out["Date"] = pd.to_datetime(out.Date)
    # out = out.set_index("Date")
    export_dataframe(out, "thstat")


if __name__ == "__main__":
    fire.Fire()
