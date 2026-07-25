import os
import sys

# Add project directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import get_dynamic_sentences

sentences = get_dynamic_sentences()
print("Sentences loaded:")
for idx, s in enumerate(sentences):
    print(f"{idx + 1}. {s}")
