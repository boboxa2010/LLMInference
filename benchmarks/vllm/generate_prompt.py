import random

def generate_prompts(count, min_length=10, max_length=200):
    prompts = []
    topics = [
        "Explain quantum computing in simple terms",
        "Write a short story about a robot learning to feel emotions",
        "What are the main challenges of space exploration?",
        "Describe the process of photosynthesis",
        "Explain how machine learning works",
        "Summarize the history of artificial intelligence",
        "Write a poem about the changing seasons",
        "Provide a recipe for chocolate chip cookies",
        "Explain the theory of relativity",
        "Describe the water cycle"
    ]
    
    for _ in range(count):
        topic = random.choice(topics)
        prompt_length = random.randint(min_length, max_length)
        # Adjust length with random additional text
        prompt = f"{topic} in about {prompt_length} words. Be concise and clear."
        prompts.append(prompt)
    
    return prompts
