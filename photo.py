from PIL import Image, ImageDraw, ImageFont
import csv

def write_text(title,subtitle, out):
    if len(title) > 13:
        titlefont = ImageFont.truetype('qfont.ttf', 80)
    else:
        titlefont = ImageFont.truetype('qfont.ttf', 110)
    subfont = ImageFont.truetype('qfont.ttf', 40)
    img = Image.open("bg.png")
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
    a = 1
    # write_text('國一國文文抽背','The Chinese recitation for the 7th grade students in vocational high.', 'out.png')
    with open('title.csv',encoding='UTF-8', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            write_text(row[0],row[1], str(a)+'.png')
            a = a + 1