from PIL import Image

root_path = './data/'
def umap():
    umap_image=[]
    for number in range(2,15):
        umap_image.append(Image.open(f'{root_path}umap/umap_{number}.png'))
    print(len(umap_image))
    return umap_image
umap_image = umap()