Running IMCOM for the first time can be challenging and you may encounter errors if you don't know what data you need before running it.
There are several text files in this repo that compile some of my notes in different topics (how to get the data, how to run coaddition, etc). The filenames are fairly self-explanatory as to what they describe. Here is a quick step-by-step of things to do if you want to run coaddition. More details are in the other txt files. You should first pip install PyIMCOM:

pip install git+https://github.com/Roman-HLIS-Cosmology-PIT/pyimcom.git

I would advice to:

1. Read the general notes.

2. Download the OU24 data (either the full data or the preview data). See setup_sim_data.txt for more details.

3. Generate the input PSF from the batch_genpsf.py file. Note that to run a slurm job I also included my version as a .sh file. Change it as you wish depending on your HPC or laptop, or simply run the python file equivalent with the same name.

4. Setup the config file based on your setup preference. See config_notes.txt for info about config file. The one provided is just an example one, but it works. You will probably need to change the path to where the OU24 images live, the one included there is my path.

5. Read running_coaddition.txt and then you can proceed to run run_coadd.py or run_coadd.sh if you want to setup a slurm job.

6. To interpet the output log files, read reading_logfiles.txt

7. To understand what the output looks like and what its contents are, look at the example.ipynb notebook and play around with the outputs.
