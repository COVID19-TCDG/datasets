def export_dataframe(df, name):
    df.to_csv(f"datasets/{name}.csv", index=False)
    df.to_excel(f"datasets/{name}.xlsx", index=False)
    df.to_json(f"datasets/{name}.json", orient="records")
