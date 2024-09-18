
# Word Finder

A simple python code to find words from given Scrambled String, such as `SGTHI` can be `SIGHT`, `SIGH`, `HIS`, `THIS` and so on

## Installation

First, ensure that you have Python 3.x installed on your system. You can check your version of Python by running:

```
python --version
```

Then, create a virtualenv, inside the project directory using this command
```
python -m venv .venv
```
If you are using pycharm, we can create it using IDE as well.

Now, Activate your venv
Windows
```
source venv/Scripts/activate
```
Then install dependencies
```
pip install -r requirements.txt
```

## Usage
Now you have to put the scrambled string inside the code but soon it will be passed as CLI argument.

### Generate Words from a scrambled string
https://github.com/dipanjal/word-finder/blob/be656ae5afeae3ce5d1fa0fe2e63dd6038c856b8/tests/test_word_finder_service.py#L9-L12

### Unmask Words from a Masked Word with scrambled string
https://github.com/dipanjal/word-finder/blob/be656ae5afeae3ce5d1fa0fe2e63dd6038c856b8/tests/test_word_finder_service.py#L28-L33
