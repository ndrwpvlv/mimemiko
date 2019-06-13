import os
from mimemiko.library import BASIC_MIMETYPES, MIMETYPES


def mime_by_extension(extension: str) -> str:
    return BASIC_MIMETYPES.get(extension) or MIMETYPES.get(extension) or None


def mime_by_extensions(extensions: list) -> list:
    return [BASIC_MIMETYPES.get(extension) or MIMETYPES.get(extension) or None for extension in extensions]


def mime_by_path(path: str) -> str:
    return mime_by_extension(os.path.splitext(path)[1])
