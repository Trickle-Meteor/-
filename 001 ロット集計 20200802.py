#import numpy as np
import pandas as pd
import os
path_c=[];dfs=[]

#path = ディレクトリパス
path = ""
file_format = ".csv" ; file_len = (-1)*len(file_format)
#file_format = ".xlsx" ; file_len = (-1)*len(file_format)

def pathread():
    #フォルダディレクトリ内のファイル一覧表示する
    path_a =os.listdir(path)
    path_b = [path_a[i] for i in range(len(path_a)) if path_a[i][file_len:] == file_format]
    #ファイル読み込み
    name = [path +"/" + path_b[i] for i in range(len(path_b))]
    Dataframe_s = [pd.read_csv(name[i],
                               header=0, index_col =0) for i in range(len(path_b))]
    """
    #read_file エクセルの場合は　csv → xlsx
    Dataframe_s = [pd.read_xlsx(name[i],
                               header=0, index_col =0) for i in range(len(path_b))]
    """
    return path_b,Dataframe_s

path_c,dfs = pathread()
lot = sum(dfs)
lot.to_csv(path+'/all-lot-pipe'+file_format)
