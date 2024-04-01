from pydantic import BaseModel

class DatasetConfig(BaseModel):
    dir_base: str = "/home/adriano/Documents/datasets/dataset_files"
    image_file: str = "images.npy"
    label_file: str = "labels.npy"
    image_size: int = 300

class HyperParameters(BaseModel):
    author: str = "Adriano A. Santos"
    file_name: str = "deeplab3plus"
    dir_base: str = "/home/adriano/Documents/tutoriais/DeepLabv3-for-self-driving-cars/weights/"
    weights_path: str = "/home/adriano/Documents/tutoriais/DeepLabv3-for-self-driving-cars/weights/deeplabv3.pt"
    n_epochs: int = 30
    max_lr: float = 3e-4
    n_classes: int = 3
    batch_size: int = 4
