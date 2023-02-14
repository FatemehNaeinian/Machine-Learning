import os
import librosa
import shutil
import audioread

path = 'C:\\Users\\asus\\Desktop\\UT\Semesters\\\Fourth Semester\\Machine learning\\Final project\\DATABASE\\Voices\\Org_not pure'

corrupted_path = 'C:\\Users\\asus\\Desktop\\UT\\Semesters\\Fourth Semester\\Machine learning\\Final project\\DATABASE' \
                 '\\Voices\\all_corrupted'

if os.path.exists(corrupted_path):
    shutil.rmtree(corrupted_path)
os.mkdir(corrupted_path)

name_list = os.listdir(path)

for i in name_list:
    path_temp = path + '\\' + i
    try:
        data, sr = librosa.load(path_temp)
    except audioread.exceptions.NoBackendError:
        corrupted_path_temp = corrupted_path + '\\' + i
        shutil.copyfile(path_temp, corrupted_path_temp)
    else:
        if (len(data) / sr) > 5.7:
            corrupted_path_temp = corrupted_path + '\\longer than 5.7 sec ' + i
            shutil.copyfile(path_temp, corrupted_path_temp)