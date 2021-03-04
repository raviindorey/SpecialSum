# Code challenge

## Task 1

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as command line arguments and output is to be printed on screen

### Examples

| Input                | Output                         |
| -------------------- | ------------------------------ |
| python app.py 1 2 3  | 6                              |
| python app.py 2 13 1 | 3                              |
| python app.py 2 1 14 | 3                              |
| python app.py 2 1 15 | 18                             |
| python app.py 1 2    | Exactly 3 numbers are required |
| python app.py 1 2 a  | All inputs must be numeric     |

### Deliverables

Solution must contain the following files and be pushed to a GitHub repository.

- A well-documented python script for the above task
- README.md
- Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
- requirements.txt

## Task 2

Convert the script from task 1 to a REST API that accepts json input and returns json output with appropriate error handling

### Examples

Replace {INPUT} in the curl command below with inputs in the table
curl -H 'Content-Type: application/json' -X PUT -d '{INPUT}’ http://localhost:5000/sum

| Input     | Output                                                     |
| --------- | ---------------------------------------------------------- |
| [1,2,3]   | {“status”: 200, “result”: 6}                               |
| [2,13,1]  | {“status”: 200, “result”: 3}                               |
| [2,1,14]  | {“status”: 200, “result”: 3}                               |
| [2,1,15]  | {“status”: 200, “result”: 18}                              |
| [1,2]     | {“status”: 400, “error”: “Exactly 3 numbers are required”} |
| [1,2,”a”] | {“status”: 400, “error”: “All inputs must be numeric”}     |

### Deliverables

Solution must contain the following files and be pushed to a GitHub repository.

- A well-documented python script for the above task
- README.md
- Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
- requirements.txt

## Task 3

Dockerize the above application

### Deliverables

Solution must contain the following files and be pushed to a GitHub repository.

- A well-documented python script for the above task
- README.md
- Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
- requirements.txt
- Dockerfile

## Solution

All tasks are on different branch. The master branch will contain the resultant project.
Navigate through tasks by `$ git checkout <branch-name>`.

Follow examples to understand command and input.

## Setup

### Dependencies

For `pipenv` use:

```powershell
$ pipenv install
```

For `pip` use `requirements.txt`

```powershell
$ pip install -r requirements.txt
```

### Solution: Task 1

Covers all criteria for task. To run tests: `python tests.py`
