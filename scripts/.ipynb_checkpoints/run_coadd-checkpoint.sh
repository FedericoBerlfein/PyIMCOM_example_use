#!/bin/bash
##SBATCH -p HENON
#SBATCH --array=0-3           # this should be the number of blocks squared - 1 (2x2 mosaic here)
#SBATCH --nodes=1
#SBATCH --cpus-per-task=28     # Give each task 2 CPUs
#SBATCH --time=48:00:00
#SBATCH -o ../output/J129/logs/out_%a.txt # change logs if changing band
#SBATCH -e ../output/J129/logs/out_%a.txt

cd $SLURM_SUBMIT_DIR
python run_coadd.py $SLURM_ARRAY_TASK_ID 'J'