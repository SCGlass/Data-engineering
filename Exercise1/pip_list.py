
#%%
import subprocess
from pathlib import Path
import sys

path_to_script = Path(__file__).parent/"pip_list.sh"

subprocess.call(["bash", path_to_script.as_posix()])

print(f"Python version: {sys.version}")
# %%