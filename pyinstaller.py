if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['main.py','-w','-F','--hidden-import=queue','--icon=./asset/myicon.ico']
    run(opts)