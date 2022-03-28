
# PaperDownloader

A tool for information extraction from paper which get pdf file from internet using doi.


This tool requires [DocumentCollector](https://github.com/brillience/DocumentCollector) .

DocumentCollector‘s output file `db.sqlite` is this tool's input file.



## Run Locally

1. Clone the project

```bash
  git clone https://github.com/brillience/PaperDownloader.git
```

2. Go to the project directory

```bash
  cd PaperDownloader
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```

4. Run DocumentCollector
  - Click [here](https://github.com/brillience/DocumentCollector).

5. Copy `db.sqlite` to the root path of this Project.
```bash
cp DocumentCollector/db.sqlite PaperDownloader/
```
6. Run this Projiect
```bash
python runSpider.py
```
7. Synchronize the PDF to the database (so that the obtained PDF is no longer submitted to the task)
```bash
cd wos_crawl
python updateFilesToDb.py
```
8. Perform Steps 7 and 8 several times to ensure that more PDFS are obtained.


## Authors

- [@brillience](https://github.com/brillience)

