# from torchvision.datasets import LSUN

# scene_classes = ['living_room_train',
#                  'dining_room_train',
#                  'bedroom_train',
#                  'kitchen_train',
#                  'living_room_val',
#                  'dining_room_val',
#                  'bedroom_val',
#                  'kitchen_val']

# datasets = LSUN("E:\datasets\lsun",
#                 classes=['living_room_val'])
# print(len(datasets))

# images_path = r"E:\datasets\lsun-4scene"
# data_type = r"\train"
# # scene_type = 
# image, label = datasets[0]

# index = 1;
# for image, label in datasets:
#     print(image.size)
#     image.save(images_path + data_type + "\\" + str(index) + r"_bedroom.png")
#     index += 1




# import os
# import sys
# from PIL import Image

# def remove_last_underscore(text):
#     index = text.rfind('_')
#     if index != -1:
#         return text[:index]
#     else:
#         return text
    
# def get_last_underscore(text):
#     index = text.rfind('_')
#     if index != -1:
#         return text[index + 1:]
#     else:
#         return ""
 
# def read_webps_and_write_to_png(webps_path, pngs_path, scene):
#     pngs_index = 1
#     if not os.path.exists(pngs_path):
#         os.mkdir(pngs_path)
#     for root, dirs, files in os.walk(webps_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             with Image.open(file_path) as img:
#                 # 转换图片格式保存
#                 img.convert('RGB').save(f'{pngs_path}\{str(pngs_index)}_{scene}.png', 'PNG')
#                 # 打印图片路径
#                 if pngs_index % 100 == 0:
#                     print(f'Reading file {pngs_index}: {file_path}')
#                 pngs_index += 1
 
# # 使用示例
# webps_dir = r"D:\datasets"
# pngs_dir  = r"D:\datasets\lsun_scene4"
# scene_cls = [r'\living_room_train',
#              r'\dining_room_train',
#              r'\bedroom_train',
#              r'\kitchen_train',
#              r'\living_room_val',
#              r'\dining_room_val',
#              r'\bedroom_val',
#              r'\kitchen_val']

# cls_index = 3
# scene = remove_last_underscore(scene_cls[cls_index])
# if get_last_underscore(scene_cls[cls_index]) == "train":
#     scene = scene + '_train'
#     pngs_path = fr'{pngs_dir}\train{scene_cls[cls_index]}'
# elif get_last_underscore(scene_cls[cls_index]) == "val":
#     scene = scene + '_test'
#     pngs_path = fr'{pngs_dir}\test{scene_cls[cls_index]}'
# else:
#     print('scene_cls error!')
#     sys.exit(0)
# scene = scene[1:]
# webps_path = webps_dir + scene_cls[cls_index]
# pngs_path = remove_last_underscore(pngs_path)
# print(pngs_path)

# read_webps_and_write_to_png(webps_path, pngs_path, scene)




import os
import sys
import random
import shutil

def getJpg(filename: str):
    return filename.endswith("jpg")

def getFile(fileDir, toFileDir, number):
    path = os.path.abspath(fileDir)
    if not os.path.exists(toFileDir):
        os.mkdir(toFileDir)
    # 防止转移数据时中断（如死机），可断点操作
    if len(os.listdir(toFileDir)) == number:
        return

    if os.path.isdir(fileDir):
        pathList = os.listdir(fileDir)
        jpgList = [i for i in filter(getJpg, pathList)]
        if jpgList:
            try:
                sample = random.sample(jpgList, number)
            except:
                print("The number of pictures is not enough")
            for name in sample:
                try:
                    shutil.move(fr'{path}\{name}', toFileDir)
                except:
                    print("Move pictures fail")
        dirList = set(pathList) - set(jpgList)
        if dirList:
            for dir in dirList:
                getFile(fr'{path}\{dir}', fr'{toFileDir}\{dir}', number)

if __name__ == "__main__":
    fileDir = r"D:\datasets\lsun_scene5\train\bathroom"

    toFileDir = r"D:\datasets\lsun_scene5\train\bathroom2"

    number = 4145
    if not isinstance(number, int) or int(number) <= 0:
        print("Input number error")
        sys.exit()
    getFile(fileDir, toFileDir, int(number))




# # 随机打乱文件夹中图片
# from PIL import Image
# import os
# import random

# image_path = r"D:\datasets\lsun_scene5\train\bathroom"
# output_folder = r"D:\datasets\lsun_scene5\train\bathroom2"
# if not os.path.exists(output_folder):
#     os.mkdir(output_folder)

# image_files = os.listdir(image_path)

# random.shuffle(image_files)

# for i, image_file in enumerate(image_files):
#     image_path_file = os.path.join(image_path, image_file)
#     image = Image.open(image_path_file)
#     image.save(os.path.join(output_folder, f'{i}.jpg'))
