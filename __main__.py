import os
import glob
from itertools import islice

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIRECTORY = '/home/dio/Projects/*/'
RECENT = 10
BOOKMARKS_FILE = os.path.join(BASE_DIR, 'bookmarks')
TARGET_BOOKMARKS_FILE = '/home/dio/.config/gtk-3.0/bookmarks'

if __name__ == '__main__':
    with open(BOOKMARKS_FILE, 'r') as bookmarks:
        output = bookmarks.readlines()
        for path in islice(sorted(glob.glob(DIRECTORY), key=lambda d: os.stat(d).st_mtime, reverse=True), RECENT):
            name = [i for i in path.split('/') if i][-1]
            name = name.replace('-', ' ').replace('_', ' ').title()
            output.append('file://{} {}\n'.format(path, name))


        with open(TARGET_BOOKMARKS_FILE, 'w') as output_bookmarks:
            output_bookmarks.writelines(output)
