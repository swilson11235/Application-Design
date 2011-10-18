import Image, ImageDraw

class WaveImage:
    def __init__(self, filename, width=640, height = 480):
        self.im,self.draw =self.create_new_image(width,height)
        self.data =[]
        f = open(filename, 'r')
        for line in f:
            self.data.append(int(line))
        f.close()
        
    def fill_bkground(self):
        pass

    def create_new_image(self, width, height):
        im = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(im)
        return im,draw

    def create_wave_image(self,filename,start_sample,end_sample):
        self.fill_background("white")
        x_coord=0
        middle_y = self.im.size[1] / 2
        previous_y =middle_y-(self.data[0]/32768.)*middle_y
        for value in self.data[start_sample:end_sample]:
            y_coord=middle_y-(value/32768.)*middle_y
            self.draw.line((x_coord,previous_y,x_coord+1,y_coord), fill =128)
            x_coord+=1
            previous_y=y_coord
        self.im.save(filename,"PNG")

if __name__=="__main__":
    import sys
