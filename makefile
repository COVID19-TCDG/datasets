install:
	conda env create -f environment.yml
	yarn install

build: datasets/thstat.csv datasets/5lab.csv

datasets/thstat.csv:
	python scripts/thstat.py preprocess ~/Downloads

datasets/5lab.csv:
	python scripts/5lab.py download
	yarn 5lab
	python scripts/5lab.py preprocess

clean:
	rm -rf datasets/*

# https://github.com/psf/requests-html/issues/305
fix:
	python -c 'import pyppeteer; pyppeteer.chromium_downloader.download_chromium()'