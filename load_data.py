import tensorflow_datasets as tfds
# run python -m tensorflow_datasets.scripts.download_and_prepare --register_checksums=True --datasets='flores'
tfds.load('mnist', split=['train','test'], data_dir="data/")