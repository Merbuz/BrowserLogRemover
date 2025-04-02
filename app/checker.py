from pathlib import Path
from typing import List
import os


class LogsChecker:
    def __init__(self, path: str):
        if Path(path).is_dir():
            self.path = Path(path)

        else:
            raise Exception("Incorrect path selected")

    def _read_text(self, path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8", errors="ignore")

        except Exception:
            return ''

    def _contains(self, string: str, contents: List[str]) -> bool:
        return any(content in string for content in contents)

    def scan_files(self, extensions: List[str]) -> List[Path]:
        """Returns files with the specified extension"""

        return [f for ext in extensions for f in self.path.glob(f"**/*{ext}")]

    def read_files(self, paths: List[Path], contents: List[str]) -> List[Path]:
        """Searches for matches in the contents of files"""

        return [path for path in paths if self._contains(self._read_text(path), contents)]  # noqa: E501

    def remove_files(self, paths: List[Path]) -> None:
        """Deletes files from specified paths"""

        for path in paths:
            try:
                os.remove(path)

            except Exception:
                pass
