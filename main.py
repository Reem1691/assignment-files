__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil


def clean_cache():
    if not os.path.exists('cache'):
        os.makedirs('cache')
    if os.path.exists('cache'):
        #for i in os.listdir('cache'):
        #for filename in os.listdir('cache'):
        #    print(i)
            #print(filename)
        contents = [os.path.join('cache', i) for i in os.listdir('cache')]
        [os.remove(i) if os.path.isfile(i) or os.path.islink(i) else shutil.rmtree(i) for i in contents]
        for k in os.listdir('cache'):
            print(k)

clean_cache()


def cache_zip(zip_path, cache_path):
    clean_cache()
    shutil.unpack_archive(zip_path, cache_path)

filename = 'data.zip'
zip_file_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename 
cache_dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'cache'
cache_zip(zip_file_path, cache_dir_path)


def cached_files():
    from os import listdir
    from os.path import isfile, join
    file_path = os.path.abspath('cache')
    files_only_list = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    files_only_list_abspath = []
    for i in files_only_list:
        files_only_list_abspath.append(file_path + '\\' + i)
    #for j in files_only_list_abspath:
    #    print(j)
    return files_only_list_abspath
    
cached_files()


def find_password(search_list):
    for i in search_list:
        with open(i) as f:
            if 'password' in f.read():
                with open(i) as f:
                    file_content = f.read()
                    password_start = file_content[(file_content.find(': '))+2:]
                    password_end_pos = password_start.find('\n')
                    password = password_start[:password_end_pos]
                    return password
            
find_password(cached_files())
    