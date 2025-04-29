from lm_eval import evaluator, tasks
from lm_eval.models.huggingface import HFLM


def eval_lambda(model, tokenizer, device):
    lm = HFLM(
        pretrained=model,
        tokenizer=tokenizer,
        device=device
    )

    task_dict = tasks.get_task_dict(["lambada"])


    results = evaluator.evaluate(
        lm=lm,
        task_dict=task_dict,
    )

    return results