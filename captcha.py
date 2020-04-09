import random
import string
from PIL import Image, ImageDraw, ImageFont
# 这里面Image是PIL中的画布，ImageDraw是画笔，ImageFont是画笔的字体

class Captcha(object):
    # 生成随机验证码的位数,可以根据需要进行修改
    number = 4
    # 干扰线条的条数
    line_number = 2
    # 生成验证码图片的宽和高，可以根据需要进行修改
    size = (100,40)
    # 验证码字的大小,可以根据需要进行修改
    fontsize = 24

    # 建立验证码源文本
    # list(string.ascii_letters) ASCII码中所有的字母
    SOURCE = list(string.ascii_letters)
    # 再加入'0'到'9'
    for index in range(10):
        SOURCE.append(str(index))

    # 绘制干扰线
    @classmethod
    def __gene_line(cls,draw,width,height):
        # 干扰性的开始位置和结束位置
        begin = (random.randint(0,width),random.randint(0,height))
        end = (random.randint(0,width),random.randint(0,height))
        # 第一个参数为开始的位置和结束的位置，第二个参数的线的颜色，第三个参数为宽度
        draw.line([begin,end],fill = cls.__gene_random_color(0,255),width=2)

    # 绘制干扰点
    @classmethod
    def __gene_points(cls,draw,ponit_chance,width,height):
        # chance为界限，如果当前随机数大于他，则绘制一个干扰电
        chance = min(100,max(0,int(ponit_chance)))
        # 遍历图
        for i in range(height):
            for j in range(width):
                temp = random.randint(0,100)
                if temp > chance:
                    # 绘制干扰点，第一个参数为位置，第二个参数为颜色
                    draw.point((j,i),fill = cls.__gene_random_color(0,255))
    # 生成验证码文本
    @classmethod
    def __gene_random_captcha(cls,number):
        # number为验证码位数,返回字符串
        return ''.join(random.sample(cls.SOURCE,number))

    # 生成随机字体
    @classmethod
    def __generate_random_font(cls):
        # 这里的fonts即是我们所有字体文件的名称，这里我是只复制过来了这么多，所以他的列表的这样，大家根据自己他字体文件来写这个fonts
        fonts = [
            'Palatino.ttc',
            'PingFang.ttc',
            'STHeiti Light.ttc',
            'STHeiti Medium.ttc',
            'Thonburi.ttc',
            'Times.ttc'
        ]
        font = random.choice(fonts)
        # 这里前面的字符为我们字符文件的文件夹位置
        return '/static/font/'+font

    # 生成随机颜色
    @classmethod
    def __gene_random_color(cls,start=0,end=255):
        # start为最小值，end为最大值，这里因为是RGB格式的，我们每个颜色的值最小为0，最大为255，所以这里默认为0和255
        random.seed()
        # 返回3种颜色的值
        return (random.randint(start,end),random.randint(start,end),random.randint(start,end))

    # 生成图片验证码
    @classmethod
    def generate_graph_captcha(cls):
        # 验证码图片的宽和高,这里的size是我们上面进行设置的宽和高
        width,height = cls.size
        # 创建一个画布
        # 第一个参数为颜色的类型RGBA型，第二个参数为宽和高，第三个参数为颜色的值，这里调用__gene_random_color，这里我们参数颜色值可以自己进行修改
        image = Image.new('RGBA',(width,height),cls.__gene_random_color(0,100))

        # 设置验证码的字体
        # 第一个参数为字体的值，即我们使用什么字体，我们调用生成随机字体的函数。第二个参数为字体大小，在上面我们设置了默认值，可以进行修改
        font = ImageFont.truetype(cls.__generate_random_font(),cls.fontsize)

        # 创建画笔,并且绑定到上面创建的画布image上
        draw = ImageDraw.Draw(image)
        # 生成随机验证码文本,参数为验证码位数
        captcha_str = cls.__gene_random_captcha(cls.number)
        # 获取字体的尺寸
        font_width,font_height = font.getsize(captcha_str)
        # 设置我们绘制的位置，这里为了验证码尽量在中间，我们选择了中间点，大家可以根据需要进行修改
        position = ((width - font_width)/2, (height - font_height)/2)
        # 填充字符串
        # 第一个参数为绘制的位置，第二个参数为文本，这里使用生成的验证码文本，第三个参数为字体，第四个参数为文字的颜色
        draw.text(position, captcha_str,font = font,fill = cls.__gene_random_color(150,255))

        # 绘制干扰性
        for i in range(cls.line_number):
            cls.__gene_line(draw,width,height)

        # 绘制干扰点
        cls.__gene_points(draw,90,width,height)
        # open的第一个参数的文件名称,在这里也可以在前面加上文件夹的名，例如/static/captcha.png，第二个参数为打开方式
        with open('captcha.png','wb') as fp:
            image.save(fp)
        return (captcha_str,image)

# 返回验证码文本
print(Captcha.generate_graph_captcha()[1])
