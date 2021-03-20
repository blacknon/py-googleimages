# GoogleImages

`googleimages` is a free and unlimited way to find images from Google Images.

## Features

- It works!

## Installation

```bash
$ pip install git+https://github.com/Wikidepia/py-googleimages
```

## Usage

```python
>>> from googleimages import Images

>>> image = Images()
>>> image.search("python", limit=200)
# [{'url': 'https://miro.medium.com/max/4800/0*ZDMI9oMbfFIu6-zK', 'width': 2670, 'height': 4000} ...
```

## TODO

- [ ] Add image license choice
- [ ] Add proxy support
- [ ] Add random user agent, and other way to bypass google block

