

# img_arr = np.asarray(img, int)
# B, G, R = img_arr.T

# # In order to avoid division by zero
# eps = 0.0001
# # Hue
# num = 0.5 * ((R-G) + (R-B))
# den = np.sqrt(np.power((R-G),2) + np.multiply((R-B),(G-B)))
# teta = np.arccos(num/(den+eps))
# H = np.where(B > G, 2*math.pi-teta, teta)
# H = H / (2*math.pi)
# # Saturation
# num = np.minimum(np.minimum(R,G),B)
# num = np.where(num == 0, eps, num)
# den = R + G + B
# den = np.where(den == 0, eps, den)
# S = 1 - (3*num/den)
# S = np.where(S < 0, 0, S)
# H = np.where(S == 0, 0, H)
# # Intensity
# I = np.divide(R+G+B,3)


# cv2.imshow('S image', S)
# cv2.imshow('I image', I)
# cv2.imshow('H image', H)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(H)
# plt.show(block=True)
# plt.imshow(S)
# plt.show(block=True)
# plt.imshow(I)
# plt.show(block=True)
# plt.imshow(img2)

# plt.title('colors')
# plt.show()

