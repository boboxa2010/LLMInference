import torch
from torch import nn, Tensor
from tqdm import tqdm
from transformers import AutoTokenizer
import torch.nn.functional as F
from transformers import AutoTokenizer

def preprocess(texts: list[str], tokenizer, device) -> Tensor:
    data = tokenizer("\n\n".join(texts), return_tensors="pt")
    return data.input_ids.to(device)


def calculate_perplexity(model: nn.Module,
                         data: Tensor,
                         tokenizer: AutoTokenizer,
                         device: torch.device,
                         sequence_length: int = 512) -> float:
    nlls: list[Tensor] = []

    model.eval()
    for i in tqdm(range(0, data.shape[1] // sequence_length)):
        start = i * sequence_length
        end = min(start + sequence_length, data.shape[1])
        with torch.no_grad():
            logits = model(data[:, start:end].to(device)).logits

        shifted_logits = logits[:, :-1, :].contiguous().float()
        shifted_targets = data[:, start:end][:, 1:]

        loss = F.cross_entropy(shifted_logits.view(-1, shifted_logits.size(-1)), shifted_targets.view(-1))
        nlls.append(loss * (end - start))

    return torch.exp(torch.stack(nlls).sum() / data.shape[1]).item()