import numpy as np

def calculate_statistics(results, total_requests, total_time):
    success_count = sum(1 for r in results if r["success"])
    success_rate = success_count / total_requests * 100
    
    latencies = [r["latency"] for r in results if r["success"]]
    
    if not latencies:
        return {
            "success_rate": 0,
            "latency": None,
            "throughput": 0,
            "tokens": None
        }
    
    latency_stats = {
        "average": np.mean(latencies),
        "p50": np.percentile(latencies, 50),
        "p90": np.percentile(latencies, 90),
        "p99": np.percentile(latencies, 99)
    }
    
    input_tokens = [r.get("input_tokens", 0) for r in results if r["success"] and "input_tokens" in r]
    output_tokens = [r.get("output_tokens", 0) for r in results if r["success"] and "output_tokens" in r]
    
    token_stats = None
    if input_tokens and output_tokens:
        token_stats = {
            "avg_input": np.mean(input_tokens),
            "avg_output": np.mean(output_tokens)
        }
    
    throughput = total_requests / total_time
    
    return {
        "success_rate": success_rate,
        "latency": latency_stats,
        "throughput": throughput,
        "tokens": token_stats
    }
