# Pythod

Pythod is a lightweigh Python 3 CLI directory organization tool.

# Usage

## Configuration file

In order to properly organize a directory, the tool uses a configuration file that contains information about content types, indicators of those content types and the target folder into which they will be moved.
The format of the default configuration file is the following:

```json
[
    {
        "content_class": <content_class_x>,
        "target_directory": <target_directory_x>,
        "content_indicators": [
            <indicator>,
            <indicator>,
            <indicator>
        ]
    },
    {
        "content_class": <content_class_y>,
        "target_directory": <target_directory_y>,
        "content_indicators": [
            <indicator>,
            <indicator>,
            <indicator>
        ]
    }
]
```

There is a default configuration file in the directory of the tool.
The file contains the following:

```json
[{
    --
}]
```
