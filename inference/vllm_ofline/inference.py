from vllm import LLM, SamplingParams


def main() -> None:
    llm = LLM(model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

    sampling_params = SamplingParams(
        temperature=0.7,
        top_p=0.95,
        max_tokens=100
    )

    outputs = llm.generate("What's the capital of Russia?", sampling_params)
    print(outputs[0].outputs[0].text)

if __name__ == '__main__':
    main()