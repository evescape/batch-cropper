from PIL import Image
import os

in_path = "D:\\MACHINE LEARNING\\data\\"
out_path = "D:\\MACHINE LEARNING\\new data\\"
res = 512

images = os.listdir(in_path)
total = len(images)

iteration = 0

for image in images:
    try:
        im = Image.open(in_path+image)

        width = im.size[0]
        height = im.size[1]
        if (width > height): im2 = im.crop((0,0,height,height))
        else: im2 = im.crop((0,0,width,width))

        im3 = im2.resize((res,res),resample = Image.BILINEAR)

        iteration += 1
        im3.save(f"{out_path}{iteration}.png")
        if (iteration%50 == 0): print(str(iteration/total*100)+"%")
    except:
        if (os.path.exists(f"{out_path}{iteration}.png")): 
            os.remove(f"{out_path}{iteration}.png")
            print("deleted file")
        else: print("skipping file")
    
    #os.remove(in_path+image)

print("done!")