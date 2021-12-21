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

If you use this project as part of your academic studies, please kindly cite the below articles:

```
@article{kollnig2022_iphone_android,
      title={Are iPhones Really Better for Privacy? A Comparative Study of iOS and Android Apps}, 
      author={Konrad Kollnig and Anastasia Shuba and Reuben Binns and Max {Van Kleek} and Nigel Shadbolt},
      year={2022},
      journal={Proceedings on Privacy Enhancing Technologies}
}

@article{kollnig_before_2021,
      title = {Before and after {{GDPR}}: Tracking in Mobile Apps},
      shorttitle = {Before and after {{GDPR}}},
      author = {Kollnig, Konrad and Binns, Reuben and {Van Kleek}, Max and Lyngs, Ulrik and Zhao, Jun and Tinsman, Claudine and Shadbolt, Nigel},
      year = {2021},
      journaltitle = {Internet Policy Review},
      volume = {10},
      number = {4},
      issn = {2197-6775},
      doi = {10.14763/2021.4.1611}
}

@inproceedings {kollnig2021_consent,
      author = {Konrad Kollnig and Reuben Binns and Pierre Dewitte and Max Van Kleek and Ge Wang and Daniel Omeiza and Helena Webb and Nigel Shadbolt},
      title = {A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps},
      booktitle = {Seventeenth Symposium on Usable Privacy and Security ({SOUPS} 2021)},
      year = {2021},
      isbn = {978-1-939133-25-0},
      pages = {181--196},
      url = {https://www.usenix.org/conference/soups2021/presentation/kollnig},
      publisher = {{USENIX} Association},
      month = aug,
}
```
