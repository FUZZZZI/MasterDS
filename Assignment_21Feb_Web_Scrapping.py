# Q1. What is Web Scraping? Why is it Used? Give three areas where Web Scraping 
#     is used to get data.
# Ans.
# Web scraping is the process of extracting data from websites by automated 
# means, typically using software tools called web scrapers or web crawlers. 
# Web scraping involves sending requests to web pages, parsing the HTML or 
# other markup languages in the responses, and extracting the desired data 
# from the page.

# Web scraping is used for a variety of purposes, such as data analysis, 
# market research, price monitoring, and content aggregation. It enables 
# users to extract large amounts of data quickly and easily, without the need 
# for manual copying and pasting.

# Three areas where web scraping is commonly used to get data are:

# E-commerce: Web scraping can be used to gather product information and 
# pricing data from e-commerce websites such as Amazon, eBay, and Walmart 
# (Flipkart). This information can be used for market research, competitor 
# analysis, and price monitoring.

# Social media: Web scraping can be used to extract data from social media 
# platforms such as Facebook, Twitter, and Instagram. This data can be used 
# for sentiment analysis, social media monitoring, and marketing research.

# Research: Web scraping can be used to gather data for academic or scientific 
# research. For example, researchers might use web scraping to collect data on 
# online behavior, news articles, or weather patterns. This data can be used 
# to analyze trends, make predictions, and develop models.

# Q2. What are the different methods used for Web Scraping?
# Ans.
# There are various methods used for web scraping, ranging from manual scraping 
# to automated scraping using specialized software or programming languages. 
# Some of the most common methods are:

# Manual scraping: This involves manually copying and pasting data from websites 
# into a spreadsheet or database. It is time-consuming and labor-intensive, but 
# can be useful for small-scale data extraction or for websites that are not 
# easily scraped using automated methods.

# Web scraping software: This includes specialized software tools that can 
# automate the process of web scraping. Examples of web scraping software 
# include Octoparse, ParseHub, and WebHarvy.

# Programming languages: Many programmers prefer to use programming languages 
# such as Python, Ruby, or JavaScript for web scraping. They can write custom 
# scripts or use existing libraries such as Beautiful Soup, Scrapy, or 
# Puppeteer to automate the process of scraping websites.

# =============================================================================
# HTML Parsing HTML parsing involves the use of JavaScript to target a linear 
# or nested HTML page. It is a powerful and fast method for extracting text and 
# links (e.g. a nested link or email address), scraping screens and pulling resources.
# 
# DOM Parsing The Document Object Model (DOM) defines the structure, style and 
# content of an XML file. Scrapers typically use a DOM parser to view the 
# structure of web pages in depth
# 
# XPath XPath is short for XML Path Language, which is a query language for 
# XML documents. XML documents have tree-like structures, so scrapers can use XPath
# =============================================================================

# APIs: Some websites offer APIs (application programming interfaces) that 
# allow users to access their data in a structured way. This can be a more 
# reliable and efficient way to extract data than web scraping, but it requires 
# knowledge of programming and API integration.

# Headless browsers: These are web browsers that can be used for automated web 
# scraping. They allow users to interact with web pages programmatically and 
# extract data in a more flexible way than traditional web scrapers. Examples 
# of headless browsers include Puppeteer, Selenium, and Playwright.

# Q3. What is Beautiful Soup? Why is it used?
# Ans.
# Beautiful Soup is a Python library used for web scraping. It is a popular 
# tool among web developers and data scientists because it provides an easy-to-use 
# interface for parsing HTML and XML files.

# Beautiful Soup is used to extract data from web pages by parsing the HTML or 
# XML markup in the pages. It provides a set of functions and methods for 
# navigating the parse tree, searching for specific elements or attributes, 
# and extracting data from those elements.

# One of the main advantages of Beautiful Soup is its flexibility. It can handle 
# poorly formatted or invalid HTML, and can be used to extract data from a wide 
# range of websites, from simple blogs to complex e-commerce sites. It can also 
# be integrated with other Python libraries such as Pandas, Numpy, and 
# Matplotlib, making it a powerful tool for data analysis and visualization.

# In summary, Beautiful Soup is a popular Python library for web scraping that 
# provides an easy-to-use interface for parsing HTML and XML files, and 
# extracting data from web pages. Its flexibility and versatility make it a 
# valuable tool for web developers and data scientists who need to extract data 
# from websites for research or analysis purposes.

# Q4. Why is flask used in this Web Scraping project?
# Ans.
# Flask is a lightweight web framework for Python that is commonly used in web 
# scraping projects. Flask provides a simple and flexible interface for building 
# web applications, making it easy to create custom web scrapers and web 
# applications for data visualization and analysis.

# Here are some reasons why Flask is commonly used in web scraping projects:

# Easy to use: Flask is easy to set up and use, even for beginners. Its 
# lightweight design and minimalistic approach make it a good choice for 
# small and medium-sized projects.

# Flexible: Flask is a flexible framework that can be customized to fit a wide 
# range of web scraping projects. It provides a wide range of extensions and 
# libraries that can be used to build custom web scrapers and data analysis tools.

# Scalable: Flask is designed to be scalable, making it a good choice for 
# projects that require scraping large amounts of data from multiple sources. 
# It can handle high traffic and large amounts of data with ease.

# Integration with other tools: Flask can be easily integrated with other Python 
# libraries and tools such as Beautiful Soup, Scrapy, and Pandas, making it a 
# versatile tool for web scraping and data analysis.

# RESTful API development: Flask can be used to develop RESTful APIs that can be 
# used to extract data from web pages and integrate with other applications.

# Q5. Write the names of AWS services used in this project. Also, explain the 
#     use of each service.
# Ans.
# AWS Elastic Beanstalk is an orchestration service offered by Amazon Web Services 
# for deploying applications which orchestrates various AWS services, including 
# EC2, S3, Simple Notification Service, CloudWatch, autoscaling, and Elastic Load

# AWS CodePipeline is a fully managed continuous delivery service that helps 
# you automate your release pipelines for fast and reliable application and 
# infrastructure updates.