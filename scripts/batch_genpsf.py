import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed
from os import listdir
import numpy as np


## Running the genpsf.py code for multiple observing IDs in parallel. This code will generate PSF images for each observation and store them in
## the psf directory.

# List of observation IDs to process
# This gets the PSF for the observations in these two bands.
bands = ['J129', 'H158']
obs_ids = []
for band in bands:
    imagedir = f'../../RomanWAS_preview/images_wide/simple/{band}/'
    obs_ids.extend(listdir(imagedir ))
obs_ids = np.array(obs_ids).astype(int)


def run_genpsf(obs_id):
    try:
        print(f"Starting OBSID={obs_id}")
        subprocess.run(['python', 'genpsf.py', str(obs_id)], check=True)
        print(f"Finished OBSID={obs_id}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running genpsf.py for OBSID={obs_id}: {e}")


# Number of parallel workers (adjust based on CPU cores and memory), set to None for default
n_workers = 28

# Parallel execution
with ProcessPoolExecutor(max_workers=n_workers) as executor:
    futures = [executor.submit(run_genpsf, obs_id) for obs_id in obs_ids]
    for future in as_completed(futures):
        future.result()
