
#%%
import subprocess
from pathlib import Path

path_to_script = Path(__file__).parent/"pip_list.sh"

subprocess.call(["bash", path_to_script])
# %%
