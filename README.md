
# Word Finder

A simple python code to find words from given Scrambled String, such as `SGTHI` can be `SIGHT`, `SIGH`, `HIS`, `THIS` and so on

## Installation

First, ensure that you have Python 3.x installed on your system. You can check your version of Python by running:

```
python --version
```
## Automatic Installation

To create a virtualenv inside your project directory `.venv` and install the required dependencies.
```
make install
```
This will install the dependencies inside the virtual environment 

## Manual Installation

If you are facing problem with `make install` you can try manual installation 
First, create a virtualenv, inside the project directory using this command
```
python -m venv .venv
```

Now, Activate your venv
Windows
```
venv/Scripts/activate
```
Linux/Mac
```
source .venv/bin/activate
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
