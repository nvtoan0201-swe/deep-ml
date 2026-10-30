
import re

def encode(text, vocab):
    # Split text using punctuation, -- and whitespace
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)

    # Remove whitespace and empty tokens
    tokens = [token.strip() for token in tokens if token.strip()]

    # Convert tokens to integer IDs
    return [vocab[token] for token in tokens]


def decode(ids, vocab):
    # Build inverse vocabulary: ID -> token
    itos = {i: token for token, i in vocab.items()}

    # Convert IDs back to tokens and join with spaces
    text = ' '.join(itos[i] for i in ids)

    # Remove spaces before punctuation
    text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)

    return text
