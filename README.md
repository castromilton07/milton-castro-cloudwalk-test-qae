# Boas Vindas ao Repositório CloudWalk Test QAE
### [milton-castro-cloudwalk-test-qae]

---
## Contexto do Projeto

Este projeto consiste em desafio técnico/teste para uma vaga de Engenheiro de Garantia de Qualidade na empresa CloudWalk, e consiste em elaborar um analizador de log do jogo Quake Arena 3 Server, o código-fonte desenvolvido deverá ser capaz de ler o arquivo de log, agrupar os dados por partida, coletar dodos (partida, jogadores, mortes), calcular pontuação para classificar jogadores por pontuação, e permitir que essas informações sejam consultadas através de relatório. Como forma de bônus, poderá ser implementado um gerador de relatório por causa de morte ("by death mean").

Esse desafio técnico terá como critérios de avaliação:
- Precisão e legibilidade do código implementado;
- Habilidades com o Git, mensagens de commit bem descritivas e fragmentação;
- Documentação do código-fonte e do Leia-me;
- Testabilidade, ferramentas de teste utilizadase e cobertura de testes.

A aplicação pode ser desenvolvida em qualquer linguagem de programação.

---
## Como instalar

### Pre-requisitos:
- [python](https://www.python.org/downloads/)

1. Clone o repositório (HTTPS ou SSH) e entrar na pasta do projeto
- Git Clone ou Download
    - HTTPS `git clone https://github.com/castromilton07/milton-castro-cloudwalk-test-qae.git`
    - SSH `git clone git@github.com:castromilton07/milton-castro-cloudwalk-test-qae.git`.
    - [Download ZIP](https://github.com/castromilton07/milton-castro-cloudwalk-test-qae/archive/refs/heads/main.zip)
- `cd milton-castro-cloudwalk-test-qae`

2. Crie o ambiente virtual para o projeto
    - A partir da raiz do projeto:
- `python3 -m venv .venv && source .venv/bin/activate`

3. Instalar dependências e iniciar o Front-end
    - A partir da raiz do projeto:
- `python3 -m pip install -r dev-requirements.txt`

---
## Estrutura de arquivos e diretórios
Este repositório está organizado com a seguinte estrutura de diretórios e arquivos:

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
##  <img src="https://bit.ly/handshake-gif" height="25px"/> Informações de contato
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
