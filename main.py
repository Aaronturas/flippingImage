#Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
def flip_image(image):
    # Write your code here
    l = len(image)
    
    for i in range(l):
        first = 0
        last = len(image[0]) - 1
        
        while first < last:
            image[i][first], image[i][last] = image[i][last], image[i][first]
            first += 1
            last -= 1
        
    for i in range(l):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                image[i][j] = 1
            else:
                image[i][j] = 0
    return image

#TestCases
image = [[1,1,0],[1,0,1],[0,0,0]]
print('Initial Image:', image)
print('Flipped Image:', flip_image(image), '\n')

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print('Initial Image:', image)
print('Flipped Image:', flip_image(image), '\n')