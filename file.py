from pathlib import Path
import hashlib
from datetime import datetime 

class File:

    def __init__(self, path):
        #TODO: block out directories, error handling
        self.path = path
        self.compute_info()
        self.compute_hash()
        self.compute_stats()

    def __repr__(self):
        return f'FILE: {self.path}, NAME: {self.filename}, EXT: {self.extension}, Size(B): {self.size_bytes}, Size(H): {self.human_size}, MOD: {self.last_modification_time}, SHA: {self.sha256}'

    def compute_info(self):
        self.filename = self.path.name
        self.extension = self.path.suffix

    def compute_hash(self):
        # copied from the internet, because I know it needs to be split into chunks but never remember exactaly how. 
        sha256_hash = hashlib.sha256()
        with open(self.path,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            self.sha256 = sha256_hash.hexdigest()
    
    def compute_stats(self):
        stat = self.path.stat()
        self.last_modification_time = datetime.fromtimestamp(stat.st_mtime)
        self.size_bytes = stat.st_size
        self.human_size = self.human_size(stat.st_size)

    @staticmethod
    def human_size(size_bytes):
        # thanks boots!
        size = float(size_bytes)
        units = ("B", "KiB", "MiB", "GiB", "TiB")

        for unit in units:
            if size < 1024 or unit == units[-1]:
                return f"{size:.1f} {unit}"
            size /= 1024