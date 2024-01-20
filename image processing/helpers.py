import matplotlib.pyplot as plt

def plot_images(images, rows=3,columns=3):
  fig = plt.figure(figsize=(10, 7))
  for x in range(rows):
    for y in range(columns):
      index = (x)*rows + (y+1)
      fig.add_subplot(rows, columns, index)
      plt.imshow(images[index])