from PIL import Image, ImageDraw, ImageFont

def create_dice_image(dice_results, successes, probability, filename='dice_roll.png'):
    """Create a PNG image showing the dice roll results"""
    # Calculate image height based on number of dice rows
    dice_per_row = 10
    num_rows = (len(dice_results) + dice_per_row - 1) // dice_per_row  # Ceiling division
    
    # Image dimensions 
    width = 800
    base_height = 400
    extra_height_per_row = 80 if num_rows > 1 else 0
    height = base_height + (num_rows - 1) * extra_height_per_row
    
    # Colors
    bg_color = (20, 25, 40)  # Dark blue background
    text_color = (255, 255, 255)  # White text
    success_color = (50, 255, 100)  # Bright green for successes
    fail_color = (255, 80, 80)  # Red for failures
    dice_bg = (45, 50, 65)  # Dark gray for dice background
    
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a better font if available
        title_font = ImageFont.truetype("arial.ttf", 48)
        dice_font = ImageFont.truetype("arial.ttf", 36)
        result_font = ImageFont.truetype("arial.ttf", 42)
        prob_font = ImageFont.truetype("arial.ttf", 28)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default(48)
        dice_font = ImageFont.load_default(36)
        result_font = ImageFont.load_default(42)
        prob_font = ImageFont.load_default(28)
    
    # Title
    title = "CORIOLIS DICE ROLL"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_x = (width - (title_bbox[2] - title_bbox[0])) // 2
    draw.text((title_x, 20), title, fill=text_color, font=title_font)
    
    # Draw dice results
    dice_y_start = 90
    dice_spacing = 70
    dice_size = 50
    row_spacing = 80
    
    for i, die_value in enumerate(dice_results):
        # Calculate row and column
        row = i // dice_per_row
        col = i % dice_per_row
        dice_in_current_row = min(dice_per_row, len(dice_results) - row * dice_per_row)
        
        # Calculate starting position to center dice in current row
        total_width = dice_in_current_row * dice_spacing - (dice_spacing - dice_size)
        start_x = (width - total_width) // 2
        
        # Calculate position
        x = start_x + col * dice_spacing
        y = dice_y_start + row * row_spacing
        
        # Dice background (highlight successes)
        dice_color = success_color if die_value == 6 else dice_bg
        draw.rectangle([x, y, x + dice_size, y + dice_size], fill=dice_color, outline=text_color, width=2)
        
        # Dice value - properly centered
        value_text = str(die_value)
        value_bbox = draw.textbbox((0, 0), value_text, font=dice_font)
        text_width = value_bbox[2] - value_bbox[0]
        text_height = value_bbox[3] - value_bbox[1]
        
        # Center the text in the dice square
        value_x = x + (dice_size - text_width) // 2
        value_y = y + (dice_size - text_height) // 2 - value_bbox[1]  # Subtract top offset
        
        text_fill = (0, 0, 0) if die_value == 6 else text_color
        draw.text((value_x, value_y), value_text, fill=text_fill, font=dice_font)
    
    # Adjust text positions based on number of rows
    result_y = dice_y_start + num_rows * row_spacing + 40
    
    # Result text
    if successes >= 1:
        if successes == 1:
            result_text = "1 SUCCESS!"
        else:
            result_text = f"{successes} SUCCESSES!"
        result_color = success_color
    else:
        result_text = "FAILURE!"
        result_color = fail_color
    
    result_bbox = draw.textbbox((0, 0), result_text, font=result_font)
    result_x = (width - (result_bbox[2] - result_bbox[0])) // 2
    draw.text((result_x, result_y), result_text, fill=result_color, font=result_font)
    
    # Probability text
    prob_text = f"{probability:.1f}% chance for this outcome"
    prob_bbox = draw.textbbox((0, 0), prob_text, font=prob_font)
    prob_x = (width - (prob_bbox[2] - prob_bbox[0])) // 2
    draw.text((prob_x, result_y + 60), prob_text, fill=text_color, font=prob_font)
    
    # Dice count
    count_text = f"Rolled {len(dice_results)} dice"
    count_bbox = draw.textbbox((0, 0), count_text, font=prob_font)
    count_x = (width - (count_bbox[2] - count_bbox[0])) // 2
    draw.text((count_x, result_y + 100), count_text, fill=(180, 180, 180), font=prob_font)
    
    # Save the image
    img.save(filename)
    print(f"Image saved as '{filename}'")