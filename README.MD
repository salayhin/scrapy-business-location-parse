# Location Data scrapper
Scrap location data from different sites

## Project Setup
1. Clone https://github.com/salayhin/scrapy_business_location_parse.git

2. Create a seperate `config.py` file. Where, you'll put the `SITE_URL`

3. Go to project directory and install dependencies
 Command: `pip install -r requirements.txt`

4. To run Category spider go to project folder and run on terminal:
    `scrapy crawl seven_eleven -o data/seven_eleven.json`
    This will create a **seven_eleven.json** file which contains the scrap data.


