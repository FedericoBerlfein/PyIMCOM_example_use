#!/bin/bash
###SBATCH -p HENON
#SBATCH --nodes 1
#SBATCH --cpus-per-task 28
#SBATCH --time 48:00:00
#SBATCH --job-name genpsf
#SBATCH -o ../psf/logs/out.txt
#SBATCH -e ../psf/logs/out.txt

cd $SLURM_SUBMIT_DIR
python batch_genpsf.py 