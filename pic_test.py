import cv2
import matplotlib.pyplot as plt

content_path = "/home/sjt_758/workspace/style_trans/content/sjtu.jpg"
style_path = "/home/sjt_758/workspace/style_trans/style/starry.jpg"

print("content_path: ", content_path)
print("style_path: ", style_path)

plt.subplot(121)
figure = cv2.imread(content_path)
# plt.imshow(cv2.cvt(figure,cv2.COLOR_BGR2RG))
plt.imshow(figure)
plt.subplot(122)
figure = cv2.imread(style_path)
# plt.imshow(cv2.cvtColor(figure,cv2.COLOR_BGR2RGB))
plt.imshow(figure)