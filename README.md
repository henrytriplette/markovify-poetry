"# markovify-poetry"

## Install Spacy 
Based on https://spacy.io/usage

```
python -m venv venv
venv\Scripts\activate
pip install -U pip setuptools wheel
pip install -U 'spacy[cuda12x]'
python -m spacy download en_core_web_sm
python -m spacy download it_core_news_sm
```
