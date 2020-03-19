>  Updated 19 March 2020: 19:42

#  datasets


a ready-to-use datasets and API around COVID-19 for Thai.


## ข้อมูลสถานะการณ์การแพรระบาด

### TH-STAT

ข้อมูลทางสถิติอนุกรมเวลาของจำนวนผู้ติดเชื้อ


Timeseries data about numbers over time

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

#### Download
[csv](datasets/thstat.csv) | [excel](datasets/thstat.xlsx) | [json](datasets/thstat.json)

### 5Lab's CovidTracker
Information about each infected cases
 * **Format**: csv, excel and json
 * **Source**: <https://covidtracker.5lab.co/>
 * **Updated**: 19 March 2020 19:42
 * **Extract/Provide**: `make datasets/5lab.csv`

| Column | Type  | Example | Detail           |
| ------ | ----- | ------- | ---------------- |
| #WIP   | `str` | ""      | Work in Progress |


#### Download
[csv](datasets/5lab.csv) | [excel](datasets/5lab.xlsx) | [json](datasets/5lab.json)

### Daily Capture DDC
Screenshot of <https://ddc.moph.go.th/viralpneumonia/index.php> since 16 March 2020
 * **Format**: png
 * **Source**: @CircleOnCircles
 * **Updated**: Every Midnight
 * **Extract/Provide**: He uses Stillio.

### Download
[Google Drive](https://drive.google.com/drive/folders/1a4Qzn-DA7yWpGwIAPa23VXgh3qwwT3t0?usp=sharing)

### Numbers of Tested Case
Information about Tested Case
 * **Format**: csv, excel and json
 * **Source**: @CircleOnCircles
 * **Updated**: 19 March 2020 19:42
 * **Extract/Provide**: `make datasets/5lab.csv`

| Column | Type  | Example | Detail           |
| ------ | ----- | ------- | ---------------- |
| #WIP   | `str` | ""      | Work in Progress |

## API

### NoobLearning Big Query

## GeoData
 - [POI COVID19](https://drive.google.com/open?id=19ycfK9oxidH9Ozgcd0kl8qNr_hh_OYe6) - [ref](https://www.facebook.com/thaivaluer/posts/2494014620821845)
 - [ข้อมูลพิกัดจุดบริการของรัฐจากระบบ CITIZENinfo](https://data.go.th/dataset/citizeninfo_location_mar2563) - [ref](https://data.go.th/blog/covid-19-citizeninfo)

## Medical Power
 - [ICU Staff Ventalator](http://gishealth.moph.go.th/healthmap/report.php) - [ref post Mar 12](https://www.facebook.com/pg/thaivaluer)