
class CharTokenizer:
    def __init__(self, text: str):
        chars = sorted(set(text))

        self.stoi = {
            '<BOS>': 0,
            '<EOS>': 1
        }

        for i, ch in enumerate(chars, start=2):
            self.stoi[ch] = i

        self.itos = {i: ch for ch, i in self.stoi.items()}
        self.vocab_size = len(self.stoi)

    def encode(self, text: str) -> list:
        return (
            [self.stoi['<BOS>']]
            + [self.stoi[ch] for ch in text]
            + [self.stoi['<EOS>']]
        )

    def decode(self, indices: list) -> str:
        return ''.join(self.itos[i] for i in indices)
