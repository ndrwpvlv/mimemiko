# Mimemiko
Mimemiko — simple mime type recognition library. 

## Basics
Package contains:

* Mime type recognition by extension
```
import from mimemiko.mime mime_by_extension

mime_by_extension(extension: str) -> str
``` 
* Mime type recognition by list of extensions
```
import from mimemiko.mime mime_by_extensions

mime_by_extensions(extensions: list) -> list
``` 
* Mime type recognition by path
```
import from mimemiko.mime mime_by_path

mime_by_path(path: str) -> str
``` 

## Contributors
Andrei S. Pavlov (https://github.com/ndrwpvlv/)