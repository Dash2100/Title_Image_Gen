from PIL import Image, ImageDraw, ImageFont
import os
import warnings
from tqdm import tqdm

resources_path = './resources'
out_path = './output'

def write_text(title, subtitle, out):
    title_font_size = 110 if len(title) <= 13 else 90

    title_font = ImageFont.truetype(os.path.join(resources_path, 'qfont.ttf'), title_font_size)
    sub_font = ImageFont.truetype(os.path.join(resources_path, 'qfont.ttf'), 40)

    img = Image.open(os.path.join(resources_path, 'bg.png'))
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Title
    title_text_width, title_text_height = draw.textbbox((0, 0), title, font=title_font)[2:]
    title_position = ((width - title_text_width) / 2, (height - title_text_height) / 2 - 20)  # Move text slightly downward

    # Draw the title text with a larger black border
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        draw.text((title_position[0] + dx, title_position[1] + dy), title, font=title_font, fill=(0, 0, 0))
        
    draw.text(title_position, title, font=title_font, fill=(112, 157, 255))

    # Subtitle
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
    subtitle_text_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_text_height = subtitle_bbox[3] - subtitle_bbox[1]
    subtitle_position = ((width - subtitle_text_width) / 2, (height - subtitle_text_height) / 2 + 70)  # Move text downward

    # Draw the subtitle text with a larger black border
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        draw.text((subtitle_position[0] + dx, subtitle_position[1] + dy), subtitle, font=sub_font, fill=(0, 0, 0))
        
    draw.text(subtitle_position, subtitle, font=sub_font, fill=(255, 255, 255))

    img.save(out)


if __name__ == '__main__':
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    for filename in os.listdir(out_path):
        os.remove(os.path.join(out_path, filename))

    filename = 1

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)

        with open('title.txt', encoding='UTF-8', newline='') as f:
            lines = f.readlines()

            for i in tqdm(range(0, len(lines), 2), desc="Generating Images"):
                title = lines[i].strip()
                subtitle = lines[i + 1].strip()
                write_text(title, subtitle, os.path.join(out_path, f'{filename}.png'))
                filename += 1

    # os.system(f'copy "{os.path.join(resources_path, "end.png")}" "{os.path.join(out_path, "end.png")}"')
