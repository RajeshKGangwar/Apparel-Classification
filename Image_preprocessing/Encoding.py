import base64

def EncodeImage(image, img_loc):

    image = base64.b64encode(image)

    with open(img_loc,'rb') as f:
        f.write(image)
        f.close()

