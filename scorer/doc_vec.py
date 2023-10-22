from transformers import AutoTokenizer, AutoModel
import torch

def convert_vec(input):
    # Load pre-trained BERT model and tokenizer
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Input string
    # input_text = "Your input text goes here."

    # Tokenize and convert to tensor
    inputs = tokenizer(input, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)

    return embeddings