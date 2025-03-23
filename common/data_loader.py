import torch


# from project root
DATA_PATH = "data/cifar-10-batches-py"


class CIFARDataLoader:
    """
    Data loader for generating batches of CIFAR examples in standard format.

    We generate tensors of shape B x H x W x C, where:
      * B := batch size
      * H := height
      * W := width
      * C := number of channels
    """
