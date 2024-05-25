Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy


Steps :

    scrapy - help
   14  scrapy
   15  scrapy startproject spider_tutorial
   16  cd spider_tutorial
   17  scrapy genspider worldmeters www.worldometers.info/world-population/population-by-country
       scrapy crawl worldmeters
       scrapy crawl worldmeters -o population_2.json

user agents
https://explore.whatismybrowser.com/useragents/explore/


available templates: 
scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed


# crwal 
scrapy genspider -t crawl transcripts subslikescript.com











generate new spider using pre-defined templates

Optional Arguments
==================
  -h, --help            show this help message and exit
  -l, --list            List available templates
  -e, --edit            Edit spider after creating it
  -d TEMPLATE, --dump TEMPLATE
                        Dump template to standard output
  -t TEMPLATE, --template TEMPLATE
                        Uses a custom template.
  --force               If the spider already exists, overwrite it with the template

Global Options
--------------
  --logfile FILE        log file. if omitted stderr will be used
  -L LEVEL, --loglevel LEVEL
                        log level (default: DEBUG)
  --nolog               disable logging completely
  --profile FILE        write python cProfile stats to FILE
  --pidfile FILE        write process ID to FILE
  -s NAME=VALUE, --set NAME=VALUE
                        set/override setting (may be repeated)
  --pdb                 enable pdb on failure

### countries gdp spider 
scrapy startproject countries_gdp
cd countries_gdp
scrapy genspider gdp wikipedia.org


workspace_vscode/explore-scrapy/countries_gdp
    scrapy crawl gdp

scrapy crawl gdp -o gdp.csv
scrapy crawl gdp -O gdp.csv ==> capital O means overwrite 
