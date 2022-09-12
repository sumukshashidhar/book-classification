# BookBub Take Home

## Run Instructions

### Dependencies

This program is designed to be run without additional package installation. Base Python, version 3.5+ is sufficient.

### Usage

```shell
python main.py <path to list of books> <path to keywords / phrases file>
```

#### Compatability Mode

Sometimes, due to variations in path configurations with python, there may be an error, where python is not able to locate the subroutines / src folder, which causes the program to halt before execution. 

As a failsafe against this, I have provided a `compatability.py` file which can be run on most systems. It can be run as follows

```bash
python compatability.py <path to list of books> <path to keywords / phrases file>
```

## Running Tests

I've developed this program with TDD. As such, there is an included test bench for the following code, which can be run / executed as follows

```bash
python -m unittest discover tests/
```


# Project Notes

## Tradeoffs

### Ensuring Compatability

I initially planned on using pandas to read the keyword files, to make for quick and easy processing of the csv file. However, to ensure compatability and forgo installation time, I ended up deciding to use the Python included csvreader.

### Being liberal with the space complexity



## Functionality

All functionality is complete. However, there is a list of improvements that I can make

### Refinements

1. **Storage of books as CSV instead of JSON:** The JSON file format is only particularly useful if the keys in the JSON are variable. However, in this case, the title / description are constant keys for each book. Hence, storing large sets of books as a csv saves considerable space. If there is an API transmission of this data, I would rather it be transmitted as a CSV file or CSV string, rather than as a JSON. _This is for this particular use case of genre classification only. I recognize that for other usecases, the JSON format is advantageous_

## Time Taken

I took approximately 2 hours to code, test and extensively document my solution.