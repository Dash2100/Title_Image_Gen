from PIL import Image, ImageDraw, ImageFont
import os

resources_path = './resources'
out_path = './output'

def write_text(title,subtitle, out):
    if len(title) > 13:
        titlefont = ImageFont.truetype(f'{resources_path}/qfont.ttf', 80)
    else:
        titlefont = ImageFont.truetype(f'{resources_path}/qfont.ttf', 110)
    subfont = ImageFont.truetype(f'{resources_path}/qfont.ttf', 40)
    img = Image.open(f'{resources_path}/bg.png')
    draw = ImageDraw.Draw(img)
    w, h = img.size
    text_w, text_h = draw.textsize(title, font=titlefont)
    position = ((w - text_w) / 2, (h - text_h) / 2-50)
    draw.text(position, title, font=titlefont, fill=(255, 255, 255))
    #subtitle
    text_w, text_h = draw.textsize(subtitle, font=subfont)
    position = ((w - text_w) / 2, (h - text_h) / 2+50)
    draw.text(position, subtitle, font=subfont, fill=(255, 255, 255))
    img.save(out)

if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')

    for filename in os.listdir(out_path):
        os.remove(os.path.join(out_path, filename))
    filename = 1
    with open('title.txt',encoding='UTF-8', newline='') as f:
        line_count = 0
        for line in f:
            line_count += 1
            if line_count % 2 == 1:
                title = line.strip()
            else:
                subtitle = line.strip()
                write_text(title,subtitle, f'{out_path}/{filename}.png')
                filename += 1
    os.system(f'copy "{resources_path}\\end.png" "{out_path}\\end.png"')