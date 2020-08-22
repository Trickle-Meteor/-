import pandas as pd
import numpy as np

#材料の寸法表を読み込みます
hxh = pd.read_csv("hxh.csv")

#各材料ごとに処理を行います
for i in range(29):
    a = np.array(hxh.loc[i])

    xos = [0,a[3],a[0]-a[3],a[0]]
    yos = [0, (a[1]-a[2])/2, (a[1]+a[2])/2, a[1]]

    #頂点の座標を決定します
    h_pos = np.array([xos[0], xos[3], xos[0], xos[3],
                      xos[1], xos[2], xos[1], xos[2],
                      xos[1], xos[2], xos[1], xos[2],
                      yos[0], yos[0], yos[3], yos[3],
                      yos[0], yos[0], yos[3], yos[3],
                      yos[1], yos[1], yos[2], yos[2]])
    pos = h_pos
    pos = np.array([pos[0], pos[4], pos[8], pos[9],
                    pos[5], pos[1], pos[3], pos[7],
                    pos[11], pos[10], pos[6], pos[2],
                    pos[12], pos[16], pos[20], pos[21],
                    pos[17], pos[13], pos [15], pos[19],
                    pos[23], pos[22], pos[18], pos[14]])
    #Numpy表記をlist表記にします
    pos = pos.reshape(-1,12).T
    # Numpyで保存した場合↓
    #np.savetxt('h100100.txt', pp, fmt= '%.1f')

    #座標をtxtに転記します
    pos = pos.flatten()
    pos = list(pos)
    pp = [str(pos[2*i])+","+str(pos[2*i+1]) +"\n" for i in range(12)]
    f = open(str(a[0])+"X"+str(a[1])+".txt","w")
    [f.write(i) for i in pp]
    f.close()

