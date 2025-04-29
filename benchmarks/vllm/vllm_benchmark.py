import time
import concurrent.futures
from tqdm import tqdm

from request_handler import send_request
from generate_prompt import generate_prompts
from stats import calculate_statistics
from generate_report import print_report, save_results

def run_benchmark(api_url, total_requests, concurrency, output_file=None):
    prompts = generate_prompts(total_requests)
    results = []
    
    print(f"Running benchmark: {total_requests} requests with concurrency {concurrency}")
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request, prompt, api_url) for prompt in prompts]
        
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            results.append(future.result())
    
    end_time = time.time()
    total_time = end_time - start_time
    
    stats = calculate_statistics(results, total_requests, total_time)
    
    print_report(stats, total_requests, concurrency, total_time)
    save_results(stats, results, total_requests, concurrency, total_time, output_file)
