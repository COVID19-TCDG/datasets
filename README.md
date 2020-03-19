> Updated 19 March 2020: 19:42

# datasets
a ready-to-use datasets and API around COVID-19 for Thai

## Stats
Statistic about numbers over time
 * **Format**: csv, excel and json
 * **Source**: <https://covid19.th-stat.com/>
 * **Updated**: 19 March 2020 19:42
 * **Extract/Provide**: click download `csv` in the website to `~/Downloads` and run `make datasets/thstat.csv`

| Column                    | Type  | Example      | Detail                                |
| ------------------------- | ----- | ------------ | ------------------------------------- |
| Date                      | `str` | "2020-01-05" | Date                                  |
| CumCase                   | `int` | 14           | Cumulative Case Since 01-01-20        |
| CurrentlyInfectedPatients | `int` | 104          | Number of Currently Infected Patients |
| Recovered                 | `int` | 9            | Number of Recovered Case              |
| Deaths                    | `int` | 1            | Number of Death                       |

### Download
[csv](datasets/thstat.csv) | [excel](datasets/thstat.xlsx) | [json](datasets/thstat.json)

## Cases
Information about each infected cases
 * **Format**: csv, excel and json
 * **Source**: <https://covidtracker.5lab.co/>
 * **Updated**: 19 March 2020 19:42
 * **Extract/Provide**: `make datasets/5lab.csv`

| Column | Type  | Example | Detail           |
| ------ | ----- | ------- | ---------------- |
| #WIP   | `str` | ""      | Work in Progress |



### Download
[csv](datasets/5lab.csv) | [excel](datasets/5lab.xlsx) | [json](datasets/5lab.json)