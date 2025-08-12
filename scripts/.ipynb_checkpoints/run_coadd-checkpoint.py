import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # change this if your path to pyimcom is different
from pyimcom.config import Config, Settings as Stn
from pyimcom.coadd import Block
import sys

## Run a single block

#cfg = Config(None)
cfg = Config(cfg_file = f'../configs/config_prod_{sys.argv[2]}.json')
this_sub = int(sys.argv[1])

blk = Block(cfg=cfg, this_sub=this_sub, run_coadd=True)