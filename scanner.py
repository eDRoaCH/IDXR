from pathlib import Path
import uuid
from file import File

class Scanner:

    def __init__(self, path):
        if path.is_dir():
            self.path = path
        else:
            raise NotADirectoryError(f'Directory required. Got: {self.path}')
        self.uuid = self.path / 'uuid.idxr'
        if not self.uuid.exists():
            self.id = uuid.uuid4()
            self.uuid.write_text(str(self.id), encoding="utf-8")
            self.first_scan = True
        else:
            self.id = uuid.UUID(self.uuid.read_text(encoding="utf-8").strip())
            self.first_scan = False

    def __repr__(self):
        result = f'SCANNER - path: {self.path}, id: {self.id}, first_scan: {self.first_scan}'
        if self.files:
            for file in self.files:
                result += file.__repr__()
        return result

    def scan(self, path=None, root=None):
        if path is None:
            path = self.path
        if root is None:
            root = self.path
        self.files = []
        if self.first_scan:
            for item in path.iterdir():
                if item.is_dir():
                    self.scan(item, root=self.path)
                if item.is_file():
                    self.files.append(File(item, root))

    def add_file(self, path):
        relative_path = path.relative_to(self.root)
        self.files.append(File(relative_path))    