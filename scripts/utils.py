def export_dataframe(df, name):
    csv_path = f"datasets/{name}.csv"
    df_there = pd.read_csv(csv_path)
    if df.shape != df_there.shape:
        df.to_csv(csv_path, index=False)
        df.to_excel(f"datasets/{name}.xlsx", index=False)
        df.to_json(f"datasets/{name}.json", orient="records")
