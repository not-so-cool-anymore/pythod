# Pythod

Pythod is a lightweigh Python 3 CLI directory organization tool.

# Installation
You can install Pythod either by cloning the repository with:

```git clone https://github.com/not-so-cool-anymore/pythod.git```
and then run `pip install .` inside the repository.

Or you can install download and install it via Pip with:

```pip install pythod```

# Usage

## Configuration file

In order to properly organize a directory, the tool uses a configuration file that contains information about content types, indicators of those content types and the target folder into which they will be moved.
The format of the default configuration file is the following:

```json
{
  "contents": [
    {
      "content_class": "<content_class_x>",
      "target_directory": "<target_directory_x>",
      "content_indicators": ["<indicator>", "<indicator>", "<indicator>"]
    },
    {
      "content_class": "<content_class_y>",
      "target_directory": "<target_directory_y>",
      "content_indicators": ["<indicator>", "<indicator>", "<indicator>"]
    }
  ]
}
```
Where `content_class` indicates the type of object that would be moved and must be either `file` or `directory`.
`target_directory` is the name of the directory in which files with matching content indicators will be moved.
`content_indicators` is an array of strings which contains indicators about a specific set of files. For directories, it is part of their names, and for files - their file extensions.

There is a default configuration file in the directory of the tool.
The file contains the following:

```json
{
  "contents": [
    {
      "content_class": "file",
      "indicators": [
        "mkv",
        "mp4",
        "flv",
        "avi",
        "mov",
        "mpg",
        "amv",
        "wmv",
        "mov"
      ],
      "target_directory": "movies_and_videos"
    },
    {
      "content_class": "file",
      "indicators": [
        "jpg",
        "jpeg",
        "tiff",
        "bat",
        "gif",
        "bmp",
        "png",
        "exif",
        "svg"
      ],
      "target_directory": "images"
    },
    {
      "content_class": "file",
      "indicators": ["txt", "doc", "docx"],
      "target_directory": "text_and_documents"
    },
    {
      "content_class": "file",
      "indicators": ["pdf"],
      "target_directory": "pdfs"
    },
    {
      "content_class": "file",
      "indicators": ["zip", "rar", "tar", "gz"],
      "target_directory": "archives"
    },
    {
      "content_class": "file",
      "indicators": ["exe", "bin"],
      "target_directory": "executables"
    },
    {
      "content_class": "directory",
      "indicators": ["movie", "xvid", "brip", "dvdrip", "x264"],
      "target_directory": "movies_and_videos"
    }
  ]
}
```
