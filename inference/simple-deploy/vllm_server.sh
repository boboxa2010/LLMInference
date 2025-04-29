#!/bin/bash

MODEL="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
HOST="0.0.0.0"
PORT="8000"
TENSOR_PARALLEL_SIZE="1"
MAX_MODEL_LEN="2048"

while [[ $# -gt 0 ]]; do
    case $1 in
        --model)
            MODEL="$2"
            shift 2
            ;;
        --host)
            HOST="$2"
            shift 2
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        --tensor-parallel-size)
            TENSOR_PARALLEL_SIZE="$2"
            shift 2
            ;;
        --max-model-len)
            MAX_MODEL_LEN="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  --model MODEL                  Model to use (default: $MODEL)"
            echo "  --host HOST                    Host to bind to (default: $HOST)"
            echo "  --port PORT                    Port to listen on (default: $PORT)"
            echo "  --tensor-parallel-size SIZE    Number of GPUs for tensor parallelism (default: $TENSOR_PARALLEL_SIZE)"
            echo "  --max-model-len LENGTH         Maximum sequence length (default: $MAX_MODEL_LEN)"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "Starting vLLM API server with the following configuration:"
echo "  Model: $MODEL"
echo "  Host: $HOST"
echo "  Port: $PORT"
echo "  Tensor Parallel Size: $TENSOR_PARALLEL_SIZE"
echo "  Max Model Length: $MAX_MODEL_LEN"
echo ""

if [ ! -z "$CUDA_VISIBLE_DEVICES" ]; then
    echo "Using CUDA devices: $CUDA_VISIBLE_DEVICES"
fi

echo "Launching vLLM API server..."
python -m vllm.entrypoints.api_server \
    --model "$MODEL" \
    --host "$HOST" \
    --port "$PORT" \
    --tensor-parallel-size "$TENSOR_PARALLEL_SIZE" \
    --max-model-len "$MAX_MODEL_LEN"

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    echo "vLLM API server exited with code $EXIT_CODE"
    exit $EXIT_CODE
fi
