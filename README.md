# PlatformControl: Token Dispenser

*This project is part of PlatformControl: <https://github.com/OxfordHCC/PlatformControl>*

Stores email-password pairs, gives out Google Play Store tokens and GSFid. This helps the download of Android apps at scale.

This repository ports the https://github.com/yeriomin/token-dispenser to Python. This is due to problems with using the existing API.

A  random couple (login, password) from `passwords/passwords.txt` is used, to load balance over multiple accounts, mitigating account ban possibilities.

## Usage

1. Set up `passwords/passwords.txt`.
2. Run `python3 token_dispenser.py`, creating a token dispenser at `http://localhost:8080/`.
3. If required, the address, port, locale, timezone, and used device can be changed directly in the Python code.

## Troubleshooting

Often, the token generation will fail. In these cases, one has to manually visit (sometimes multiple times) the following website, after which the process can continue:

https://accounts.google.com/b/0/DisplayUnlockCaptcha

## Citation

If you use this project as part of your academic studies, please kindly cite the below article:

```
@article{kollnig2021,
      title={Are iPhones Really Better for Privacy? A Comparative Study of iOS and Android Apps}, 
      author={Konrad Kollnig and Anastasia Shuba and Reuben Binns and Max {Van Kleek} and Nigel Shadbolt},
      year={2021},
      journal={arXiv preprint arXiv:2109.13722}
}
```
