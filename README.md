# GitHub Issue Metrics Calculator

This Python program calculates the median and mean of the number of days taken to close GitHub issues excluding those labeled as 'enhancement' or 'new feature'.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Usage

1. Set up a GitHub personal access token with the appropriate permissions. This token will be used for authentication.
2. Save the token as an environment variable named `GITHUB_GPG_KEY`.
3. Run the script with the owner and name of the GitHub repository as the first argument.

Example:
```bash
python main.py owner/repository
```

## License
Licensed under the EUPL \
Take a look at the license file [EN](https://github.com/panos1b/Mean&Median-Bug-Fix-Time/blob/main/LICENCE_EN.txt) and [EL](https://github.com/panos1b/Mean&Median-Bug-Fix-Time/blob/main/LICENCE_EL.txt)