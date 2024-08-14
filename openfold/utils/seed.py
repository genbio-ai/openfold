import os
import logging
import random
import numpy as np
import torch
from openfold.utils.suppress_output import SuppressLogging


# from pytorch_lightning.utilities.seed import seed_everything
def seed_everything(seed=None):
    print("Warning: seed_everything is reimpl by ourselves because this function is deprecated by lightning.")
    if seed is None:
        return
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    return seed


def seed_globally(seed=None):
    if "PL_GLOBAL_SEED" not in os.environ:
        if seed is None:
            seed = random.randint(0, np.iinfo(np.uint32).max)
        os.environ["PL_GLOBAL_SEED"] = str(seed)
        logging.info(f'os.environ["PL_GLOBAL_SEED"] set to {seed}')

    # seed_everything is a bit log-happy
    with SuppressLogging(logging.INFO):
        seed_everything(seed=None)
