import glob
import os
import sys

# 拡張子.txtのファイルを取得する
path_text = './dir/*txt'
i = 1
 
# txtファイルを取得する
flist = glob.glob(path_text)

# BMP外を''に置換するマップ
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '_')

# ファイル名を一括で変更する
for file in flist:
    new_file_name=file.translate(non_bmp_map)
    os.rename(file ,new_file_name)
    i+=1
