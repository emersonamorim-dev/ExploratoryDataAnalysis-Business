from prefect import Flow, task
import subprocess

@task
def run_r_script(script_path: str):
    result = subprocess.run(["Rscript", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"R Script failed with error: {result.stderr}")
    return result.stdout

with Flow("User Activity Flow") as flow:
    r_output = run_r_script("path/to/your/second/r/script.R")

if __name__ == "__main__":
    flow.run()
