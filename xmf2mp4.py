from os import listdir, system
videoFilesNames = [f for f in listdir('./v') if f[0] != '.']
audioFilesNames = [f for f in listdir('./a') if f[0] != '.']
names = []
for videoFileName in videoFilesNames:
    audiofilename = ""
    for audioName in audioFilesNames:
        if audioName[:6] == videoFileName[:6] and audioName[6:] == "00.MXF":
            names.append([videoFileName, audioName])
            break
[print(i) for i in names]

for name in names:
    system(f'ffmpeg -i v/{name[0]} -i a/{name[1]} -vcodec libx264 -s 1920x1080 -vf yadif {name[1][:6]}.mp4')
