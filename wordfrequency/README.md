# Top Wikipedia Page Word Frequency Counter

![version-image][version-image]

Python based Module to get any Wikipedia page by it's Page ID and return the **top N words** that appear in that page.

## Sample

### Input

Wikipedia Page ID: 21721040
Top Words to Display: 5 

### Output

Top 5 words:
- 19 questions
- 16 Stack, Overflow
- 11 that
- 10 site, users
- 9 question

## Installation

### Prerequisites
* Python3
* PIP3
* Download the repo package wordfrequency.zip and unzip. You should have a directory named wordfrequency

### Running Instructions

1. Install the pip module into your python library.

   pip3 install wordfrequency/

2. Export your PATH env to pick up the alias wiki when running the python module form your machine

   export PATH=~/.local/bin:$PATH

3. Run the wiki command

   wiki --page_id=21721040 --n=5

OR

1. Run the python module command. Navigate into wordfrequency and Run.

   python3 -m wordfrequency.main --page_id=21721040 --n=5

## Uninstall

pip3 uninstall wiki-page-work-frequency

### Parameters
*page_id* - wikipedia page id

*n* - the top number of words to display

## Development

Use you preferred IDE and import Python module.

### Testing

#### Running Unit Tests
python3 -m pytest wordfrequency/wordfrequency/test/

## Features
* 0.0.1 Bla bla bla

## Contributing
This is info on how you can contribute bla bla bla

[version-image]: https://img.shields.io/badge/version-0.0.1-green.svg?style=plastic
