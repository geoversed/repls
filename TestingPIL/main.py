from PIL import Image, ImageDraw

# Create a new image
image = Image.new("RGB", (200, 200), "black")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw a red square
draw.rectangle((50, 50, 150, 150), fill="white", outline="red")

# Save the image
image.save("simple2.png")