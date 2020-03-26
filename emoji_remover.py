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

    # BMP外を''に置換するマップ
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '')

    # ファイル名を一括で変更する
    file_index=1
    for file in flist:
        old_file_name=file
        new_file_name=remove_emoji(file)
        os.rename(file ,new_file_name)
        if old_file_name != new_file_name:
            print(str(file_index)+'番目のファイル名を変更しました')

        #bmp外文字を''に置き換える
        new_file_name2=file.translate(non_bmp_map)
        if new_file_name != new_file_name2:
            print(str(file_index)+"番目のファイルのBMP外の文字を変更しました")
        os.rename(file ,new_file_name2)
        file_index = file_index + 1
    print("完了")