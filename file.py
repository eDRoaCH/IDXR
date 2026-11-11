from pathlib import Path
import hashlib
from datetime import datetime 

class File:

    def __init__(self, path, root):
        if path.is_file():
            self.path = path
            self.root = root
            self.extension = self.path.suffix
            self.compute_relative_posix()
            self.compute_hash() #this should be deferred once the database is up and likely only called if matching filename/modification time not found
            self.compute_stats()
        else:
            raise ValueError(f'Path must be file {path}')


    def __repr__(self):
        return (
            f"FILE: {self.path}\n"
            f"  RELATIVE POSIX: {self.relative_posix}, ROOT: {self.root},\n"
            f"  EXT: {self.extension}, Size(B): {self.size_bytes},\n"
            f"  MOD: {self.last_modification_time}, SHA: {self.sha256}\n"
        )

    def compute_relative_posix(self):
        relative = self.path.relative_to(self.root)
        self.relative_posix = relative.as_posix()

    def compute_hash(self):
        sha256_hash = hashlib.sha256()
        try:
            with open(self.path,"rb") as f:
                # Read and update hash string value in blocks of 1mb
                for byte_block in iter(lambda: f.read(1048576),b""):
                    sha256_hash.update(byte_block)
                self.sha256 = sha256_hash.hexdigest()
        except (PermissionError, OSError):
            self.sha256 = None  # may need to throw an error or retry
    
    def compute_stats(self):
        stat = self.path.stat()
        self.last_modification_time = datetime.fromtimestamp(stat.st_mtime)
        self.size_bytes = stat.st_size

    @staticmethod
    def human_size(size_bytes):
        # Currently unused
        size = float(size_bytes)
        units = ("B", "KiB", "MiB", "GiB", "TiB")

        for unit in units:
            if size < 1024 or unit == units[-1]:
                return f"{size:.1f} {unit}"
            size /= 1024