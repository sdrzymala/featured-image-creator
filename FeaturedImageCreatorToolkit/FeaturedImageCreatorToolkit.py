import os, sys
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageEnhance
import uuid
import re
import urllib.request, json
import requests

class FeaturedImageCreatorToolkit:


    

    def __init__(self):
        self.current_image = None

        # read config file
        with open('config.json') as f:
            data = json.load(f)
        self.pixabay_api_key = data["pixabay_api_key"]
    


    def download_image(self, imageurl, img_save_to_path):
        
        current_image_path = None

        image_id_candidate = str(imageurl).split("-")[-1]
        image_id = re.sub('\D', '', image_id_candidate)
        pixabay_api_call_url = "https://pixabay.com/api/" + "?key=" + self.pixabay_api_key + "&id=" + image_id
        
        try:
            with urllib.request.urlopen(pixabay_api_call_url) as url:
                response = json.loads(url.read().decode())
                image_url = response["hits"][0]["largeImageURL"]
                
                if image_url != None:
                    Picture_request = requests.get(image_url)
                    if Picture_request.status_code == 200:
                        current_image_path = img_save_to_path + str(uuid.uuid4().hex) + ".png"
                        with open(current_image_path, 'wb') as f:
                            f.write(Picture_request.content)
        except Exception as e:
            raise

        return current_image_path
    
    
    def load_base_image(self,img_input_path):
        img = Image.open(img_input_path)
        self.current_image = img.convert("RGBA")
      

    def save_image(self, img_output_folder_path, output_format, quality_val):
        img_output_path = img_output_folder_path + str(uuid.uuid4().hex) + "." + output_format
        self.current_image.save(img_output_path, output_format, quality=quality_val)
        return img_output_path

    def image_resize(self,basewidth):

        img = self.current_image
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        self.current_image = img



    def image_white_to_transparent(self):

        img = self.current_image
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        self.current_image = img

    def image_white_to_transparent_gradient(self):
        img = self.current_image
        x = np.asarray(img.convert('RGBA')).copy()
        x[:, :, 3] = (255 - x[:, :, :3].mean(axis=2)).astype(np.uint8)
        output_img = Image.fromarray(x)
        self.current_image = output_img


    def image_append_another_image(self,logo_image_path,use_transparency_mask,logo_location_x,logo_location_y):
        
        background_image = self.current_image
        logo_image = Image.open(logo_image_path)

        output_image = background_image.copy()
        if use_transparency_mask == True:
            output_image.paste(logo_image, (logo_location_x, logo_location_y), mask = logo_image)
        else:
            output_image.paste(logo_image, (logo_location_x, logo_location_y))

        self.current_image = output_image




    def image_add_text(self, font_path, font_size, text, text_location_x, text_location_y, text_color, textbox_length):

        img = self.current_image
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        w,h = font.getsize(text)
        text_start_location = ((textbox_length - (text_location_x*2)) - w)/2
        draw.text((text_start_location, text_location_y),text,font=font, fill=text_color)
        self.current_image = img




    def image_add_rectangle(self, rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color):
        
        img = self.current_image
        img.convert('RGB')
        draw = ImageDraw.Draw(img)
        draw.rectangle((rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1), fill=rectangle_fill_color)
        self.current_image = img

    def image_add_rectangle_transparent(self, rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color, rectangle_transparency):
 
        opacity = int(255 * rectangle_transparency)

        img = self.current_image
        img = img.convert("RGBA")

        overlay = Image.new('RGBA', img.size, rectangle_fill_color+(0,))
        draw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.
        draw.rectangle((rectangle_xo, rectangle_y0,rectangle_x1, rectangle_y1), fill=rectangle_fill_color+(opacity,))

        # Alpha composite these two images together to obtain the desired result.
        img = Image.alpha_composite(img, overlay)
        img = img.convert("RGB") # Remove alpha for saving in jpg format.
        self.current_image = img
        
        