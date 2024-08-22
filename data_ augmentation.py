import os
import random
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

# 翻转图像
def flip_image(image, mode='horizontal'):
    if mode == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Mode should be 'horizontal' or 'vertical'")

# 旋转图像
def rotate_image(image, angle):
    return image.rotate(angle)

# 缩放图像
def scale_image(image, scale_factor):
    width, height = image.size
    return image.resize((int(width * scale_factor), int(height * scale_factor)))

# 平移图像
def translate_image(image, x, y):
    return ImageOps.offset(image, x, y)

# 裁剪图像
def crop_image(image, crop_box):
    return image.crop(crop_box)

# 调整亮度、对比度、饱和度、色调
def adjust_color(image, brightness=1, contrast=1, saturation=1, hue=1):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation)
    # hue adjustment not directly available in PIL, skipped
    return image

# 添加噪声
def add_noise(image, noise_type='gaussian', mean=0, std=1):
    # This function is a placeholder; PIL doesn't support direct noise addition
    return image

# 模糊图像
def blur_image(image, blur_type='gaussian', radius=2):
    if blur_type == 'gaussian':
        return image.filter(ImageFilter.GaussianBlur(radius))
    elif blur_type == 'motion':
        return image.filter(ImageFilter.MotionBlur(radius))  # Pillow doesn't have MotionBlur, custom implementation needed
    else:
        raise ValueError("Blur type should be 'gaussian' or 'motion'")

# 仿射变换
def affine_transform(image, matrix):
    return image.transform(image.size, Image.AFFINE, matrix)

def main():
    image_path = r"D:\datasets\lsun_scene5\train\bathroom"
    output_folder = r"D:\datasets\lsun_scene5\train\bathroom2"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    pngs_index = 1
    for root, dirs, files in os.walk(image_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with Image.open(file_path) as img:

                # 设置增强方法及其参数
                methods = [
                    ('unchanged', "unchanged"),
                    ('flip', {'mode': 'horizontal'}),
                    ('rotate', {'angle': 10}),
                    ('rotate', {'angle': -10}),
                    ('blur', {'blur_type': 'gaussian', 'radius': 1}),
                ]

                # 应用选择的增强方法
                for method_name, params in methods:
                    if method_name =='unchanged':
                        result_image = img
                    elif method_name == 'flip':
                        result_image = flip_image(img, **params)
                    elif method_name == 'rotate':
                        result_image = rotate_image(img, **params)
                    elif method_name == 'blur':
                        result_image = blur_image(img, **params)
                    else:
                        continue

                    result_image.save(f'{output_folder}\{str(pngs_index)}.jpg')

                    # 打印图片路径
                    if pngs_index % 1000 == 0:
                        print(f'Reading file {pngs_index}: {file_path}')
                    pngs_index += 1

if __name__ == '__main__':
    main()

