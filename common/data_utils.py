"""
Utils file for data related operations.
"""

import pickle
import numpy as np
import os
from typing import Dict, Tuple


def unpickle_cifar_file(file_path: str) -> Dict:
    """
    Unpickle a specific CIFAR-10 file

    :param file_path: path to a specific file
    :return: dictionary containing the data
    """

    with open(file_path, 'rb') as fo:
        return pickle.load(fo, encoding='bytes')


def load_train_images(data_dir: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load the CIFAR-10 training images

    :param data_dir: path to the CIFAR-10 data
    :return: Tuple of images and labels
    """

    # Load all training batches
    images = []
    labels = []
    file_names = [f"data_batch_{i}" for i in range(1, 6)]
    for fname in file_names:
        batch_file = os.path.join(data_dir, fname)
        batch_data = unpickle_cifar_file(batch_file)
        images.append(batch_data[b'data'])
        labels.append(batch_data[b'labels'])

    # Combine all batches
    images = np.vstack(images)
    labels = np.array(labels)

    # Reshape and transpose
    images = images.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

    return images, labels
