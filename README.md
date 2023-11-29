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