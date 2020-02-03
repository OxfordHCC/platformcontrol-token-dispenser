# python-token-dispenser
Stores email-password pairs, gives out Google Play Store tokens and GSFid.

This repository ports the https://github.com/yeriomin/token-dispenser to Python. This is due to problems with using the existing API.

At the moment, only one email-password pair is supported.

In the future, this behaviour will be changed to use a random couple (login, password) from the provided ones, to load balance over multiple accounts, mitigating account ban possibilities.

## Usage

`python3 token_dispenser.py`