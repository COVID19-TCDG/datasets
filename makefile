install:
	conda env create -f environment.yml
	yarn install

build: datasets/5lab.csv

generate: clean/5lab datasets/5lab.csv

prep/conda:
	conda activate covid

datasets/thstat.csv:
	python scripts/thstat.py preprocess ~/Downloads

datasets/5lab.csv:
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