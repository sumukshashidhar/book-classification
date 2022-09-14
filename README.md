# Book Classification

This is a proof of concept for classifying large sets of books into different genres based on certain keywords.

P.S: This is also an indication of how I write code for larger projects :)

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

## Design Choices

### Use of Typing

One thing that I've always disliked and have found to bite me in larger projects is the dynamic typing of python.
Therefore, to facilitate rapid future development, I've included function typing, so we know exactly
what function arguments are, and what it returns, without having to peruse the code underneath.

## Tradeoffs

### Readability instead of Code Golfing

I've made various design choices, where I've written readable code, instead of writing "slick" code. For example, I've
written the following in my CSV read input function

```python
if key not in dictionary:
    dictionary[key] = value
else:
    dictionary[key] += value
```

However, one way that I particularly like, but chose not to include, is the "get" function
```python
dictionary[key] = value + dictionary.get(key, 0)
```

Both pieces of code accomplish the same thing, but many programmers may not be familiar with the latter, as it is 
unintuitive. 

### Ensuring Compatability

I initially planned on using pandas to read the keyword files, to make for quick and easy processing of the csv file. However, to ensure compatability and forgo installation time, I ended up deciding to use the Python included csvreader.

### Being liberal with the space complexity

After thinking about the problem for a while, I realized that speed would be of paramount importance, and that the list
of keywords would not grow linearly with the number of books, but would rather have a high initial y-intercept, and then
proceed to taper off. This is why I was quite liberal with space complexity and decided to optimize for time.

### Choosing to group by genre

With the storage of the keyword list, there were essentially two ways that I could have gone about it.

1. Group by keywords first, associate each keyword with a genre and point score

```json
{
  "fast paced": [["action", 5], ["sci-fi", 2]]
}
```
2. Group by genre and associate each genre with a list of keywords

```json
{
  "action": [["fast paced", 5]],
  "sci-fi": [["fast paced", 2]]
}
```

I ended up picking option #2, because of something that I learned recently in a class I'm taking (CS483 -> Applied 
Parallel Programming). With option #2, we can run our textual analysis on different threads / different cores (perhaps)
not in Python because of the global interpreter lock, but in other parallel programming languages, as each genre can now
be evaluated independently. In option #1, while this is still possible by having a separate count, and then summing them
together, it is more cumbersome.

Also, another issue with hashing, is that you would need an extremely large hash table to hash that many keywords. However,
this also depends on how these keywords are chosen, and how much random access we have to work with, and how fast genre
classification needs to be done. I took the liberty of assuming that genre classification is a backend task, and need 
not happen real time.

### Performance

Storage and manipulation of the keyword list and the associated scores pose an interesting problem that can be solved 
in a multitude of ways. Had this been C++, where there is minimal overhead for something like a struct, I would have
probably used a struct. However, since this is Python, and there is a fair overhead to making a named tuple or class,
I decided to go with an unnamed data structure. Here is a possible implementation in C++ had I needed to do it:

```cpp
struct {
    string genre;
    vector<pair<string, int>> keywords;
}
```

## Functionality

All functionality is complete. However, there is a list of improvements that I can make

### Refinements

1. **Storage of books as CSV instead of JSON:** The JSON file format is only particularly useful if the keys in the JSON are variable. However, in this case, the title / description are constant keys for each book. Hence, storing large sets of books as a csv saves considerable space. If there is an API transmission of this data, I would rather it be transmitted as a CSV file or CSV string, rather than as a JSON. _This is for this particular use case of genre classification only. I recognize that for other usecases, the JSON format is advantageous_
2. **Stricter Error Checking**: The error handling as of now is extremely basic and vague. With more time, I can make
                                sure that there are better error messages, and in some cases, maybe corrections on the fly
3. **Logging**: Logging is extremely important, which has helped me numerous times in the past identify defects with code
                during development and in production. However, due to the limited time constraints, I have not implemented
                logging in this project
4. **Extended Testing**: I will also implement extended testing, as the testing that I currently have is extremely limited, and only insures basic functionality, instead of accounting for various edge cases

## Time Taken

I took approximately 2.5 hours to code, test and, extensively document my solution.
