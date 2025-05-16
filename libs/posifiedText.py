import spacy
import json
import markovify

def posifiedTextNewlineModel(corpus, args):

    # spacy.prefer_gpu()
    nlp = spacy.load(args.spacy_language)

    class POSifiedText(markovify.NewlineText):
        """Uses spacy to parse the text into a model.

        For information on the inherited properties and functions,
        see the markovify documentation at
        [https://github.com/jsvine/markovify](https://github.com/jsvine/markovify)
        """

        def word_split(self, sentence):
            """Split the sentence into words and there respective role in the
            sentence."""
            return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

        def word_join(self, words):
            """Join words back into a sentence."""
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence
        
    text_model = POSifiedText(corpus, state_size = args.state_size)
    
    return text_model

def loadPOSifiedText(args):
    
    # spacy.prefer_gpu()
    nlp = spacy.load(args.spacy_language)

    class POSifiedText(markovify.Text):
        def word_split(self, sentence):
            """Split the sentence into words and there respective role in the
            sentence."""
            return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

        def word_join(self, words):
            """Join words back into a sentence."""
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence
    
    reconstituted_model = POSifiedText.from_json(json.load(open(args.model)))
    
    return reconstituted_model