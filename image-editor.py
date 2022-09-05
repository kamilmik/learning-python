from PIL import Image, ImageDraw, ImageFont, ImageFilter

print('hello,welcome to photo editor')
file = input('input file:')
print('blur,detail,contour,edge,embossed,sharpen,smooth,bnw,negative')
action = input('choose action:')

img = Image.open(file)
width,height = img.size

def blur(img):
    blurred = img.filter(ImageFilter.BLUR)
    return blurred

def detail(img):
    detailed = img.filter(ImageFilter.DETAIL)
    return detailed

def contour(img):
    contoured = img.filter(ImageFilter.CONTOUR)
    return contoured

def edge(img):
    edgeenhanced = img.filter(ImageFilter.EDGE_ENHANCE)
    return edgeenchanced

def emboss(img):
    embossed = img.filter(ImageFilter.EMBOSS)
    return embossed

def sharpen(img):
    sharpened = img.filter(ImageFilter.SHARPEN)
    return sharpened

def smooth(img):
    smoothed = img.filter(ImageFilter.SMOOTH)
    return smooth

def bnw(img,width,height):
    result = Image.new("RGBA", (width,height))
    for w in range(width):
       for h in range(height):
           r, g, b = img.getpixel((w, h))
           gray = int(r * 0.212 + g * 0.715 + b * 0.0746)
           result.putpixel((w, h), (gray, gray, gray, 255))
    return result

def negative(img,width,height):
    result = Image.new("RGBA", (width,height))
    for w in range(width):
       for h in range(height):
           r, g, b = img.getpixel((w, h))
           result.putpixel((w, h), (255-r, 255-g, 255-b, 255))
    return result


if action == 'blur':
    img_edit = blur(img)
    
elif action == 'detail':
    img_edit = detail(img)
    
elif action == 'contour':
    img_edit = contour(img)
    
elif action == 'edge':
    img_edit = edge(img)
    
elif action == 'embossed':
    img_edit = emboss(img)
    
elif action == 'sharpen':
    img_edit = sharpen(img)
    
elif action == 'smooth':
    img_edit = smooth(img)

elif action == 'bnw':
    img_edit = bnw(img,width,height)
    
elif action == 'negative':
    img_edit = negative(img,width,height)

img_edit.show()
    
