# webscraping_2023

pip install scrapy


## Scrapy's Commands
https://docs.scrapy.org/en/latest/intro/tutorial.html

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command

## Startproject

scrapy startproject <name_project>

website to practice
https://www.worldometers.info/world-population/population-by-country/

# Difference between Scrapy Template and Crawler Template

# Making a request
scrapy shell
r = scrapy.Request(url='https://www.worldometers.info/world-population/population-by-country/')
fetch(r)

another way
scrapy shell "https://www.worldometers.info/world-population/population-by-country/"

response.xpath('//h1') >>> return complete html element
for only text
response.xpath('//h1/text()') >>> return data without tag html
response.xpath('//h1/text()').get() >>> return only the text
response.xpath('//td/a/text()').getall()

## Running script
into folder with name project <spider_tutorial> run in terminal the command
scrapy crawl worldometers

## Save in json
scrapy crawl worldometer -o population.json

## Libraries to use MongoDB
pymongo dnspython

about database, remember change the file pipelines.py to correscpond with your class configuration