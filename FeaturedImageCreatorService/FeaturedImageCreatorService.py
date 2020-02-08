from FeaturedImageCreatorToolkit.FeaturedImageCreatorToolkit import FeaturedImageCreatorToolkit

class FeaturedImageCreatorService:
    
    def __init__(self):
        pass
        
    def generate_featured_image(self, title, subtitle, imageurl):
            
            
        ### Create featured image
        featuredImage = FeaturedImageCreatorToolkit()


        #TODO add check for title and subtitle
        # if len(title) == 0:
        #     title = "a-B-c-D-e-F-g-H-i-J-k-L-m-N-o-P-r-S-t-U-w-Y-z"
        # if len(subtitle) == 0:
        #     subtitle = "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-R-s-T-u-W-y-Z-1-2-3-4-5-6-7-8"
        

        img_save_to_path = "./static/src/download/"
        selected_image_path = featuredImage.download_image(imageurl, img_save_to_path)

        # load image
        #img_input_path = './static/src/background/background (1).jpg' 
        img_input_path = selected_image_path
        featuredImage.load_base_image(img_input_path)

        # resize image
        basewidth = 1200
        featuredImage.image_resize(basewidth)

        # add logo
        #logo_image_path = './static/src/logo/logo.png'
        #use_transparency_mask = False
        #logo_location_x = 0
        #logo_location_y = 20
        #featuredImage.image_append_another_image(logo_image_path, use_transparency_mask, logo_location_x, logo_location_y)

        # add logo transparent
        logo_image_path = './static/src/logo/logo_small.png'
        use_transparency_mask = False
        logo_location_x = 450
        logo_location_y = 731
        featuredImage.image_append_another_image(logo_image_path, use_transparency_mask, logo_location_x, logo_location_y)

        # add rectangle
        rectangle_xo = 0
        rectangle_y0 = 400
        rectangle_x1 = 1200
        rectangle_y1 = 550
        rectangle_fill_color = (0,0,0)
        rectangle_transparency = 0.75
        featuredImage.image_add_rectangle_transparent(rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color, rectangle_transparency)


        # add text
        textbox_length = 1200
        font_path = '.\static\src\font\segoeuib.ttf'
        font_size = 52
        text = title
        text_location_x = 15
        text_location_y = 410
        text_color = (255,215,0)
        featuredImage.image_add_text(font_path, font_size, text, text_location_x, text_location_y, text_color, textbox_length)


        # add text
        textbox_length = 1200
        font_path = '.\static\src\font\segoeui.ttf'
        font_size = 40
        text = subtitle
        text_location_x = 15
        text_location_y = 480
        text_color = (255,215,0)
        featuredImage.image_add_text(font_path, font_size, text, text_location_x, text_location_y, text_color, textbox_length)




        ### save output image
        quality_val = 100
        output_image_folder_path = './static/output/'
        output_format = "PNG"
        output_image_file_path = featuredImage.save_image(output_image_folder_path, output_format, quality_val)
        
        
        ### return file image path
        return output_image_file_path

