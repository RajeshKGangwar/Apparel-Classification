import base64


def DecodeImage(image,img_loc):

    img_decoded = base64.b64decode(image)

    with open(img_loc,'wb') as f:
        f.write(img_decoded)
        f.close()

