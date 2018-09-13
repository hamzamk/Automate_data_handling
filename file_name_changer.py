import os
import sys
import fnmatch


def main():
    folder_name = 'xml'
    path = '{}/{}'.format(os.getcwd(), folder_name)
    search_exp, replace_exp = 'vv', 'vh'

    list_of_files = []
    for filename in os.listdir(path):

        if search_exp in filename:
            list_of_files.append(filename)
            os.rename('{}/{}'.format(path, filename), '{}/{}'.format(path, filename).replace(search_exp, replace_exp))
    print('{} files found'.format(len(list_of_files)))

if __name__ == '__main__':
    main()
