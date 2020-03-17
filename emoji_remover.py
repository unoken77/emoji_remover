import glob
import os
import sys
import emoji

def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

while True:
    # 指定したディレクトリのファイルを取得する
    path_text = input("絵文字を除外したいディレクトリを指定してください")

    if path_text[-1] == "\\":
        path_text=path_text.rstrip('\\')

    flist = glob.glob(path_text+"/*")

    # ファイル名を一括で変更する
    file_index=1
    for file in flist:
        old_file_name=file
        new_file_name=remove_emoji(file)
        os.rename(file ,new_file_name)
        if old_file_name != new_file_name:
            new_file_name_e=new_file_name.encode('cp932', 'ignore')
            new_file_name_d=new_file_name_e.decode('cp932')
            print(str(file_index) + new_file_name+'に変更しました')
        file_index = file_index + 1
    print("完了")