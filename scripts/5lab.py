import re
import pandas as pd
from requests_html import HTMLSession
import fire
import json
from pathlib import Path


def export_dataframe(df, name):
    csv_path = f"datasets/{name}.csv"
    df_there = pd.read_csv(csv_path)
    if df.shape != df_there.shape:
        df.to_csv(csv_path, index=False)
        df.to_excel(f"datasets/{name}.xlsx", index=False)
        df.to_json(f"datasets/{name}.json", orient="records")


def download():
    session = HTMLSession()
    r = session.get("https://covidtracker.5lab.co/")
    r.html.render()
    scripts = r.html.find("body > script")
    data = scripts[0].text
    match = re.search(r"(function.*)\);", data)

    path = Path("tmp/data.js")
    path.parent.mkdir(exist_ok=True)

    with open("tmp/data.js", "w") as f:
        f.write("module.exports.data = ")
        f.write(match.group(1))


def preprocess():
    with open("tmp/raw_5lab.json") as f:
        data = json.load(f)
    cases = data["cases"]
    df = pd.DataFrame(cases)
    export_dataframe(df, "5lab")


if __name__ == "__main__":
    fire.Fire()
