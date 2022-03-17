# Welcome to the CloudWalk Test QAE Repository
### [milton-castro-cloudwalk-test-qae]

---
## Project context

This project consists of a technical challenge/test for a Quality Assurance Engineer position at CloudWalk, and consists of developing a Quake Arena 3 Server game log parser, the source code developed must be able to read the log file, group the data by match, collect data (match, players, deaths), calculate scores to classify players by score (ranking), and allow this information to be consulted through a report. As a bonus, a by death mean report generator can be implemented.

This technical challenge will have as evaluation criteria:
- Accuracy and readability of the implemented code;
- Git skills, descriptive commit messages and fragmentation;
- Source code and readme.md documentation;
- Testability, test frameworks and test coverage.

The application can be developed in any programming language.

---
## How to install

### Prerequisites:
- [python](https://www.python.org/downloads/)

1. Clone the repository (HTTPS or SSH) and enter in the project folder
- Git Clone ou Download
    - HTTPS `git clone https://github.com/castromilton07/milton-castro-cloudwalk-test-qae.git`
    - SSH `git clone git@github.com:castromilton07/milton-castro-cloudwalk-test-qae.git`.
    - [Download ZIP](https://github.com/castromilton07/milton-castro-cloudwalk-test-qae/archive/refs/heads/main.zip)
- `cd milton-castro-cloudwalk-test-qae`

2. Create the virtual environment for the project
    - From the project root folder:
- `python3 -m venv .venv && source .venv/bin/activate`

3. Install dependencies
    - From the project root folder:
- `python3 -m pip install -r dev-requirements.txt`

---
## How to use

### Prerequisites:
- Command Prompt: bash, zsh, cmd, ps

1. Run with python the main.py file located in the path `quake_log_parser/main.py` from the project root folder
    - From the project root folder:
- `python3 quake_log_parser/main.py`

2. Enter one of the options between 0 and 5
```
    Select one of the options below:
    0 - Default report (total kills, players, kills ranking);
    1 - Report by death mean (kills by means);
    2 - Complete report;
    3 - Dictionary/JSON of Default Report;
    4 - Dictionary/JSON of By Death Mean Report;
    5 - Exit.
    ->
```
<p align="center">
  <img src="https://bit.ly/01-execution_menu" alt="Execution menu" width="400px">
</p>

### Outputs
    -  Option 0
        - Default report (total kills, players, kills ranking)
<p align="center">
  <img src="https://bit.ly/02-option_0" alt="Option 0" width="400px">
</p>

    -  Option 1
        - Report by death mean (kills by means)
<p align="center">
  <img src="https://bit.ly/03-option_1" alt="Option 0" width="400px">
</p>

    -  Option 2
        - Complete report
<p align="center">
  <img src="https://bit.ly/04-option_2" alt="Option 0" width="400px">
</p>

    -  Option 3
        - Dictionary/JSON of Default Report
<p align="center">
  <img src="https://bit.ly/05-option_3" alt="Option 0" width="1200px">
</p>

    -  Option 4
        - Dictionary/JSON of By Death Mean Report
<p align="center">
  <img src="https://bit.ly/06-option_4" alt="Option 0" width="1200px">
</p>

    -  Option 5
        - Exit
<p align="center">
  <img src="https://bit.ly/07-option_5" alt="Option 0" width="400px">
</p>

---
## Structure of files and directories
This repository is organized with the following directory and file structure:

```
.
├── quake_log_parser
│   ├── data
│   │   └── qgames.log
│   ├── importer
│   │   ├── importer.py
│   │   └── txt_importer.py
│   ├── reports
│   │   ├── by_death_mean_report.py
│   │   ├── complete_report.py
│   │   ├── default_report.py
│   │   └── report.py
│   └── main.py
│   └── tests
│       ├── __init__.py
│       ├── test_by_death_cause_report.py
│       ├── test_complete_report.py
│       ├── test_default_report.py
│       ├── test_importer.py
│       └── test_main.py
├── dev-requirements.txt
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
└── setup.py
```

---
##  <img src="https://bit.ly/handshake-gif" height="25px"/> Contact information
<p align="center"><a href="https://www.linkedin.com/in/milton-castro/"><img src="https://bit.ly/perfil_150px"/></a></p>
<p align="center">Milton Castro</p>
<p align="center">
  <a href="https://bit.ly/miltoncastro-cv-4"><img src="https://img.shields.io/badge/-Currículo-3423A6?style=flat&logo=Google-Chrome&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/milton-castro/"><img src="https://img.shields.io/badge/-milton--castro-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>
  <a href="mailto:castro.milton07@gmail.com"><img src="https://img.shields.io/badge/-castro.milton07@gmail.com-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
  <a href="http://be.net/milton-castro"><img src="https://img.shields.io/badge/-milton--castro-1769FF?style=flat&logo=Behance&logoColor=white"/></a>
  <a href="https://github.com/castromilton07"><img src="https://img.shields.io/badge/-castromilton07-1A1B27?style=flat&logo=Github&logoColor=white"/></a>
  <a href="https://open.spotify.com/user/castro.milton07"><img src="https://img.shields.io/badge/-castro.milton07-1DB954?style=flat&logo=Spotify&logoColor=white"/></a>
</p>
