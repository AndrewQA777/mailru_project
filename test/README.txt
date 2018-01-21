- Tests are designed to be executed with standart built-in 'unittest' module.

- Recommended command to run tests: Win   : 'python -m unittest discover %cd% *_test.py -f'
                                    Linux : 'python -m unittest discover $(pwd) *_test.py -f'

- Dependencies are listed in 'requirements.txt'. Please install them if you need
  (execute 'pip install -r requirements.txt' in this directory).

- Python 3 should be installed (not Python 2 - there are differencies in syntax).

- It's considered that target browser is chrome - so chromedriver should be added to PATH or placed into the directory with tests
  (\mailru_project\test\test_cases). You can download it here: https://sites.google.com/a/chromium.org/chromedriver/downloads
  By default chromedriver 2.35 is provided in \test_cases folder. You can also install chromedriver using pip but note,
  that it doesn't offer latest versions.

- Test run demonstration: https://drive.google.com/open?id=1pKavmMZGFSJuyzzK1Im-JLnbq5rdNq2P