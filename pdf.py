# coding:utf8
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from PIL import Image
from os import listdir
from os.path import isfile, join

# 获取img文件夹下的所有文件
my_path = './img'
only_files = ['{my_path}/{f}'.format(my_path=my_path, f=f) for f in listdir(my_path) if isfile(join('./img', f))]

def conver_to_pdf(file_list):
    # 获取A4纸的高度,宽度
    (w, h) = landscape(A4)
    # 获取原图片大小设置pdf
    #(h, w) = Image.open(file_list[0]).size
    new_name = 'example1.pdf'
    # 设置画板,即pdf的大小
    c = canvas.Canvas(new_name , pagesize=(h,w))
    # 遍历文件
    for filename in file_list:
        # 写入图片,0,0 为坐标轴开始位置,h,w为写入图像大小
        c.drawImage(filename,0,0,h,w)
        # 分页
        c.showPage()
    # 写入图片完毕,保存pdf
    c.save()

conver_to_pdf(only_files)

#  参考 http://www.cnblogs.com/wei-li/archive/2012/04/19/2456725.html
#  https://zhuanlan.zhihu.com/p/20709824
#  http://www.jinglingshu.org/?p=3695
#  https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/39/README.html
