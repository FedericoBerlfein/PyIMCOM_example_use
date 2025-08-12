# code for creating symlinks between preview images, which contain observations for the deep
# and wide survey. This essentially creates symlinks in a different catalog to only
# use onservations in the wide survey.

import numpy as np
import os
from os import listdir

def create_symlinks(src_base, dest_base, directories, files, band):
    """
    Creates symlinks for the specified directories and files in the 'images2' directory.
    
    Parameters:
    src_base (str): Path to the source directory (e.g., "images").
    dest_base (str): Path to the destination directory (e.g., "images2").
    directories (list): List of directory names to include.
    files (list): List of file numbers to include for each directory.
    """
    # Check that both arrays have the same length
    if len(directories) != len(files):
        print("Error: directories and files lists must have the same length.")
        return
    
    # Loop through the list of directories and files to include
    for i in range(len(directories)):
        directory = directories[i]
        file_number = files[i]
        
        # Define the source and destination directories and files
        src_dir = os.path.join(src_base, str(directory))
        dest_dir = os.path.join(dest_base, str(directory))

        # Create the destination directory if it does not exist
        os.makedirs(dest_dir, exist_ok=True)

        # Create the source and destination file paths (absolute paths)
        src_file = os.path.abspath(os.path.join(src_dir, f"Roman_WAS_simple_model_{band}_{directory}_{file_number}.fits.gz"))
        dest_file = os.path.abspath(os.path.join(dest_dir, f"Roman_WAS_simple_model_{band}_{directory}_{file_number}.fits.gz"))
        
        # Check if the source file exists, and create a symlink if it does
        if os.path.exists(src_file):
            # If the symlink already exists, remove it first
            if os.path.exists(dest_file):
                print(f"Symlink exists, overwriting: {dest_file}")
                os.remove(dest_file)  # Remove the existing symlink or file
            
            # Create the new symlink
            os.symlink(src_file, dest_file)
            print(f"Created symlink: {dest_file} -> {src_file}")


dtype = [('col1', 'U5'), ('col2', 'i4'), ('col3', 'i4')]
# read list of observations from preview area of OU24 that are observed by the wide survey
data = np.genfromtxt('../wide-survey-list.txt', dtype=dtype)
column1 = data['col1']
column2 = data['col2']
column3 = data['col3']

# read list of observing IDs for a specific band in the preview data. Images must be downloaded
# if you want to run this script, since we are creating symlinks for the images
band = 'J129'
imagedir = '../../RomanWAS_preview/images/simple/' + band
obsid_list = np.array(listdir(imagedir )).astype(int)

obslist_cut = np.in1d(column2, obsid_list)
filter_cut = column1 == band
directories = column2[obslist_cut & filter_cut]
files = column3[obslist_cut & filter_cut]


# Paths to the source and destination directories
src_base = '../RomanWAS_preview/images/simple/' + band  # Source base directory
dest_base = '../RomanWAS_preview/images_wide/simple/' + band  # Destination base directory

# Create symlinks
create_symlinks(src_base, dest_base, directories, files, band)