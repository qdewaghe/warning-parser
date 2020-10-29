# warnings-parser

Library to transform an output from a compiler to a dict to be easily output it in a json format. \
It supports any compilers using the standard `file_path:line:column: warning: message [category]` format such as:
- gcc
- clang
- clang-tidy
- cppcheck with `--template='{file}:{line}:{column}: warning: {message} [{id}]'`

## Install

```bash
pip install warning-parser
```

## Usage

usage example to generate bitbucket annotations:
```python
from warning_parser import get_warnings

warnings = get_warnings("/path/to/gcc_output.txt", "gcc")
warnings = warnings.union(get_warnings("/path/to/clang_output.txt", "clang"))

json_data = []
for w in warnings:
    
    if warning.get_severity() == "error":
        severity = "HIGH"
    else:
        severity = "MEDIUM"


    json_data.append(
    {
        "message": f"{w.get_tool()}:{w.get_line()}:{w.get_column()}: {w.get_severity()}: {w.get_message()} [{w.get_category()}]",
        "severity": severity,
        "path": w.get_filepath(),
        "line": w.get_line(),
    })

# ... upload annotations ...

```