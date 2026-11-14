import os
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow not installed")
    exit(1)

WIDTH = 1280
HEIGHT = 1920

# Create base canvas (dark teal)
base = Image.new('RGB', (WIDTH, HEIGHT), color='#0f2e3d')

# Open user image
try:
    user_img = Image.open('cover_raw.png')
    aspect = user_img.width / user_img.height
    new_w = WIDTH
    new_h = int(WIDTH / aspect)
    user_img = user_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_y = max(HEIGHT - new_h, 500)
    base.paste(user_img, (0, paste_y))
except Exception as e:
    print(f"Error loading cover_raw.png: {e}")
    exit(1)

draw = ImageDraw.Draw(base)

try:
    font_large = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', 110)
    font_med = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', 95)
    font_small = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf', 70)
except Exception:
    font_large = ImageFont.load_default()
    font_med = font_large
    font_small = font_large

def draw_centered_text(d, text, y, font, fill='#e1d094'):
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (WIDTH - w) / 2
    d.text((x, y), text, font=font, fill=fill)

draw_centered_text(draw, "LECTURES BY", 120, font_med)
draw_centered_text(draw, "MIGUEL ANXO BASTOS", 240, font_large)
draw_centered_text(draw, "Volume I", 400, font_small)

# Add a gold line
draw.line([(WIDTH//2 - 200, 360), (WIDTH//2 + 200, 360)], fill='#e1d094', width=4)

base.save('cover.png')
print("Successfully created cover.png")
