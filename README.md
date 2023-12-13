
# Web Scrapper

Web Scrapper is a Python tool designed to recursively extract and categorize links from web pages. This tool is built to streamline the process of collection and analysis of links, serving various purposes including web crawling, SEO analysis, link profiling, website enumeration or attack surface discovery.



## Features

- **Advanced Parsing:** The tool makes sure to extract all the available links by searching for attributes like *'src'*, *'href'* and strings like *'http://'* and *'https://'*, making it effective and more reliable
- **Recursive Link Extraction:** It seamlessly explores web pages in a recursive manner based on the given threshold, extracting links and providing a comprehensive view of the website's structure
- **Link Categorization:** It is smart enough to categorize the extracted links based on their filetype *(extension)*, providing a clear and organized output for further analysis
- **Sorting & Formation:** It makes sure that the output is complete and effective by removing any duplicates and appending Url to the incomplete relative path links 
- **Smart Recursiveness:** The recursive feature only applies to the extracted links that belongs to the same target, making result focused on specific target and help user stay in scope
- **Smart Output:** It provides two output files *(if Output Directory is specified)* named *'custom_output.txt'* *(customized output based on level of recursion and category of link)* and *'raw-output.txt'* *(raw output only contains extracted links)*, making easy for user to both read the output and integrate output to other tool or do further enumeration



## Installation

```bash
  git clone https://github.com/aboul3la/Sublist3r.git
  sudo pip install -r requirements.txt
```
    
## Usage

```bash
python webScrapper.py -u <URL> -t <Threshold/Depth> -o <OutputFolder>
```
The parameters can be conveniently specified via the command line.

The target URL `-u` *is mandatory*, recursion depth threshold `-t` *is optional (default value is 1)*, and output folder `-o` *is optional (if not provided it will just print the customised result to the output stream)*
## Example
```bash
python webScraper.py -u https://example.com -t 2 -o example_folder

```
This command will scrape/extract links from the specified URL *https://example.com* up to a depth of *2* and save the results in the *'output_folder'*

## Contributing

Contributions to the Web Scrapper are welcome! For bug reports, feature requests, or code contributions, please refer to our Contribution Guidelines.
## License

This Web Scrapper tool is open-source. Feel free to use, modify, and distribute it for your projects.

Happy Scrapping! 🕸️

