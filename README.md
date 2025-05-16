# markovify-poetry

A poetry/text generator using Markov chains, spaCy, and Ollama for AI-assisted correction or lyric adaptation.

---

## Setup Instructions

### 1. Create and Activate a Virtual Environment

```sh
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```sh
pip install -U pip setuptools wheel
pip install -U "spacy[cuda12x]"
```

### 3. Download spaCy Language Models

```sh
python -m spacy download en_core_web_sm
python -m spacy download it_core_news_sm
```

---

## Ollama Requirement

This project requires [Ollama](https://ollama.com/download) to be installed and running for AI-powered text correction or lyric adaptation.

---

## Usage

First generate the model by feeding it some text:

```sh
python generateModel.py -f "some-text.txt"
```

Then generate some new text based on the model style:

```sh
python generateText.py -m "some-model.json" -n 10
```

- `-m` / `--model`: Path to your Markovify JSON model.
- `-n` / `--length`: Number of lines to generate (default: 10).

Use `-h` to print the help text

---

## Configuration

Edit `config.ini` to enable/disable AI, select the Ollama model, and set the AI mode (`song` or `poem`):

```ini
[AI]
ai_enable = true
ai_model = qwen3:32b
ai_mode = song
```
