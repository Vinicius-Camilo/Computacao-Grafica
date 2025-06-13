def encode_image(image_path, message, output_path):
    from PIL import Image

    image = Image.open(image_path)
    encoded_image = image.copy()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110' 
    data_index = 0

    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            pixel = list(encoded_image.getpixel((x, y)))

            for i in range(3):  
                if data_index < len(binary_message):
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])  
                    data_index += 1

            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image.save(output_path)


def decode_image(image_path):
    from PIL import Image

    image = Image.open(image_path)
    binary_message = ""
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))

            for i in range(3): 
                binary_message += str(pixel[i] & 1)  

    message_bytes = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
    message = ""

    for byte in message_bytes:
        if byte == '11111111':  
            break
        message += chr(int(byte, 2))

    return message