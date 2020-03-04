import glob
import os
import sys

while True:
    # 指定したディレクトリのファイルを取得する
    path_text = input("BMP外の文字を除外したいディレクトリを指定してください")

    if path_text[-1] == "\\":
        print('true')
        path_text=path_text.rstrip('\\')

    flist = glob.glob(path_text+"/*")

    # BMP外を''に置換するマップ
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '_')

    # ファイル名を一括で変更する
    for file in flist:
        #print(file)
        old_file_name=file
        new_file_name=file.translate(non_bmp_map)
        os.rename(file ,new_file_name)
        if old_file_name != new_file_name:
            print('変更後:'+new_file_name)
    print("renamed")