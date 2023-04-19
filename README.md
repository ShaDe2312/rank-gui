
- Run the app

```sh
$ python QRCode.py
```

## Packaging the app
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.
```sh
$ python -m eel QRCode.py web --noconsole --onefile --icon=barcode.icns
```
