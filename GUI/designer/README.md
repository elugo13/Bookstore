# How to convert the designer files to python fiiles

Make sure to install pyuic5-tool and pyqt5designer on your main Python installation (not on venv)

On your terminal:

```bash
pip install pyuic5-tool pyqt5designer
```

To conver the UI files to python, execute this on a termial:

```bash
pyuic5 your_file.ui -o your_file.py
```
