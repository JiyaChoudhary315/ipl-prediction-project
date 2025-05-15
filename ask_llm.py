import subprocess

def ask_llm(prompt):
    result = subprocess.run(['ollama', 'run', 'llama3'], input=prompt.encode(), capture_output=True)
    return result.stdout.decode()

response = ask_llm("Explain why team A is likely to win based on recent form.")
print(response)
