install:
	conda env create -f environment.yml
	yarn install

build: datasets/5lab.csv

generate:  datasets/5lab datasets/thstat

prep/conda:
	conda activate covid

datasets/thstat.csv: datasets/thstat

datasets/thstat:
	python scripts/thstat.py preprocess raw_data

datasets/5lab.csv: datasets/5lab

datasets/5lab:
	python scripts/5lab.py download
	yarn 5lab
	python scripts/5lab.py preprocess

clean: clean/5lab clean/thstat


clean/thstat:
	rm -rf datasets/thstat.*

clean/5lab:
	rm -rf datasets/5lab.*

# https://github.com/psf/requests-html/issues/305
fix:
	python -c 'import pyppeteer; pyppeteer.chromium_downloader.download_chromium()'