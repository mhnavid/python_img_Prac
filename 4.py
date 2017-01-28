import matplotlib.pyplot as plt

img=plt.imread('bn.jpg')
print(img.shape)
img_frame=img[130:3550,:]
# img1=img_frame[0:800,0:750]
x=0
y=0
c1=0
c2=750
fn=1

while x<2251:
    img1 = img_frame[0:800, c1:c2]
    x=c2
    c1=c2
    c2+=750
    if (img1.shape[1]>500):
        plt.imsave('numb/img%d.jpg'%fn, img1 )
        fn+=1

