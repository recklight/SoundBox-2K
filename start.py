import zipfile
from main import *
from pathlib import Path

for f in ["models", "testfile", "data"]:
    if not Path(f).is_dir():
        with zipfile.ZipFile(f"{f}.zip", 'r') as zip_ref:
            zip_ref.extractall()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SoundBox-2K")
    parser.add_argument("--full", action='store_true')
    args = parser.parse_args()
    app = QApplication(sys.argv)
    _main_ = SoundBox()
    if args.full:
        _main_.showFullScreen()
    else:
        _main_.show()
    sys.exit(app.exec_())
