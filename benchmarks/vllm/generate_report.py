import json

def print_report(stats, total_requests, concurrency, total_time):
    print("\n-------- Benchmark Results --------")
    print(f"Total requests: {total_requests}")
    print(f"Concurrency: {concurrency}")
    print(f"Success rate: {stats['success_rate']:.2f}%")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Throughput: {stats['throughput']:.2f} requests/second")
    
    if stats['latency']:
        print("\nLatency (seconds):")
        print(f"  Average: {stats['latency']['average']:.4f}")
        print(f"  p50: {stats['latency']['p50']:.4f}")
        print(f"  p90: {stats['latency']['p90']:.4f}")
        print(f"  p99: {stats['latency']['p99']:.4f}")
    
    if stats['tokens']:
        print("\nTokens:")
        print(f"  Avg input tokens: {stats['tokens']['avg_input']:.2f}")
        print(f"  Avg output tokens: {stats['tokens']['avg_output']:.2f}")

def save_results(stats, results, total_requests, concurrency, total_time, output_file):
    if not output_file:
        return
        
    with open(output_file, 'w') as f:
        json.dump({
            "metadata": {
                "total_requests": total_requests,
                "concurrency": concurrency,
                "success_rate": stats['success_rate'],
                "total_time": total_time,
                "throughput": stats['throughput']
            },
            "latency": stats['latency'],
            "tokens": stats['tokens'],
            "detailed_results": results
        }, f, indent=2)
    print(f"\nDetailed results saved to {output_file}")
