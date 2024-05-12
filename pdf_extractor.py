import fitz
import PIL.Image
import io

pdf = fitz.open("")

counter =1
for i in range(len(pdf)):
    page= pdf[i]