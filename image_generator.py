from PIL import Image, ImageDraw, ImageFont

def load_font(font_name="arial.ttf", size=36, fallback_size=20):
    try:
        return ImageFont.truetype(font_name, size)
    except:
        return ImageFont.load_default()

def create_dice_image(dice_results, successes, probability, filename='dice_roll.png'):
    """Create a PNG image showing the dice roll results"""
    dice_per_row = 10
    num_rows = (len(dice_results) + dice_per_row - 1) // dice_per_row

    # Image dimensions
    width = 800
    height = 400 + max(0, num_rows - 1) * 80

    # Colors
    bg_color = (20, 25, 40)
    text_color = (255, 255, 255)
    success_color = (50, 255, 100)
    fail_color = (255, 80, 80)
    dice_bg = (45, 50, 65)

    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Load fonts
    title_font = load_font(size=48)
    dice_font = load_font(size=36)
    result_font = load_font(size=42)
    prob_font = load_font(size=28)

    # Draw title
    title = "CORIOLIS DICE ROLL"
    title_x = (width - draw.textbbox((0, 0), title, font=title_font)[2]) // 2
    draw.text((title_x, 20), title, fill=text_color, font=title_font)

    # Dice layout
    dice_y_start = 90
    dice_spacing = 70
    dice_size = 50
    row_spacing = 80

    for i, die_value in enumerate(dice_results):
        row, col = divmod(i, dice_per_row)
        dice_in_row = min(dice_per_row, len(dice_results) - row * dice_per_row)
        total_width = dice_in_row * dice_spacing - (dice_spacing - dice_size)
        start_x = (width - total_width) // 2

        x = start_x + col * dice_spacing
        y = dice_y_start + row * row_spacing

        # Dice color
        die_fill = success_color if die_value == 6 else dice_bg
        draw.rectangle([x, y, x + dice_size, y + dice_size], fill=die_fill, outline=text_color, width=2)

        # Die value
        value = str(die_value)
        bbox = draw.textbbox((0, 0), value, font=dice_font)
        text_x = x + (dice_size - (bbox[2] - bbox[0])) // 2
        text_y = y + (dice_size - (bbox[3] - bbox[1])) // 2 - bbox[1]
        draw.text((text_x, text_y), value, fill=(0, 0, 0) if die_value == 6 else text_color, font=dice_font)

    # Success/Failure Result
    result_y = dice_y_start + num_rows * row_spacing + 40
    if successes >= 1:
        result_text = f"{successes} SUCCESS!" if successes == 1 else f"{successes} SUCCESSES!"
        result_color = success_color
    else:
        result_text = "FAILURE!"
        result_color = fail_color

    result_x = (width - draw.textbbox((0, 0), result_text, font=result_font)[2]) // 2
    draw.text((result_x, result_y), result_text, fill=result_color, font=result_font)

    # Probability and dice count
    prob_text = f"{probability:.1f}% chance for this outcome"
    count_text = f"Rolled {len(dice_results)} dice"
    prob_y = result_y + 60
    count_y = result_y + 100

    prob_x = (width - draw.textbbox((0, 0), prob_text, font=prob_font)[2]) // 2
    count_x = (width - draw.textbbox((0, 0), count_text, font=prob_font)[2]) // 2

    draw.text((prob_x, prob_y), prob_text, fill=text_color, font=prob_font)
    draw.text((count_x, count_y), count_text, fill=(180, 180, 180), font=prob_font)

    img.save(filename)
    print(f"Image saved as '{filename}'")
