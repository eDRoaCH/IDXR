from pathlib import Path
import hashlib
from datetime import datetime 

class File:

    def __init__(self, path, root):
        ### TODO: to store: posix_path, size(b), MOD(as unix timestamp), SHA. everything else can be derived at display time (full path, name, ext, size(h))
        if path.is_file():
            self.path = path
            self.root = root
            self.relative_path = path.relative_to(root)
            self.compute_relative_posix()
            self.compute_info()
            self.compute_hash()
            self.compute_stats()
        else:
            pass

    def __repr__(self):
        return (
            f"FILE: {self.path}\n"
            f"  RELATIVE: {self.relative_path}, POSIX: {self.relative_posix},\n "
            f"  NAME: {self.filename},  EXT: {self.extension},\n"
            f"  Size(B): {self.size_bytes}, Size(H): {self.human_size},\n"
            f"  MOD: {self.last_modification_time}, SHA: {self.sha256}\n"
        )

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

    def compute_relative_posix(self):
        relative = self.path.relative_to(self.root)
        self.relative_posix = relative.as_posix()

    @staticmethod
    def human_size(size_bytes):
        # thanks boots!
        size = float(size_bytes)
        units = ("B", "KiB", "MiB", "GiB", "TiB")

        for unit in units:
            if size < 1024 or unit == units[-1]:
                return f"{size:.1f} {unit}"
            size /= 1024