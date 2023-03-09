import os
import threading

root = 'C:\\'
search = input('digite o nome do arquivo: ')

def whatisthefile(packet):
    try:
        for files in os.listdir(packet):
            actual_dir = os.path.join(packet, files)
            if os.path.isdir(actual_dir):
                whatisthefile(actual_dir)

            if os.path.isfile(actual_dir):
                filename, extension = os.path.splitext(files)

                if filename == search or files == search or search in filename:
                    print('o caminho do arquivo é:', actual_dir)

    except PermissionError:
        pass

thread = threading.Thread(target=whatisthefile(root))
thread.start()
