from FeaturedImageCreatorToolkit.FeaturedImageCreatorToolkit import FeaturedImageCreatorToolkit

class FeaturedImageCreatorService:
    
    def __init__(self):
        pass
        
    def generate_featured_image(self, title, subtitle):
            
        ### Create featured image
        featuredImage = FeaturedImageCreatorToolkit()

        # load image
        img_input_path = './static/src/background/background (1).jpg' 
        featuredImage.load_base_image(img_input_path)

        # resize image
        basewidth = 1200
        featuredImage.image_resize(basewidth)

        # add logo
        logo_image_path = './static/src/logo/logo.png'
        use_transparency_mask = False
        logo_location_x = 0
        logo_location_y = 20
        featuredImage.image_append_another_image(logo_image_path, use_transparency_mask, logo_location_x, logo_location_y)

        # add logo transparent
        logo_image_path = './static/src/logo/logo_transparent_gradient.png'
        use_transparency_mask = True
        logo_location_x = 50
        logo_location_y = 600
        featuredImage.image_append_another_image(logo_image_path, use_transparency_mask, logo_location_x, logo_location_y)

        # add rectangle
        rectangle_xo = 50
        rectangle_y0 = 400
        rectangle_x1 = 1100
        rectangle_y1 = 500
        rectangle_fill_color = (9,206,42)
        featuredImage.image_add_rectangle(rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color)

        # add text
        font_path = 'C:\Windows\WinSxS\amd64_microsoft-windows-f..ype-segoeui_regular_31bf3856ad364e35_10.0.18362.1_none_46e868b51494532d\segoeui.ttf'
        font_size = 45
        text = title
        text_location_x = 60
        text_location_y = 420
        text_color = (19,11,74)
        featuredImage.image_add_text(font_path, font_size, text, text_location_x, text_location_y, text_color)



        # add transparent rectangle
        rectangle_xo = 50
        rectangle_y0 = 550
        rectangle_x1 = 1100
        rectangle_y1 = 650
        rectangle_fill_color = (0,0,0)
        rectangle_transparency = 0.75
        featuredImage.image_add_rectangle_transparent(rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color, rectangle_transparency)


        # add another text
        font_path = 'C:\Windows\WinSxS\amd64_microsoft-windows-f..i_italicssupplement_31bf3856ad364e35_10.0.18362.1_none_727f713a25a56d1b\seguibli.ttf'
        font_size = 45
        text = subtitle
        text_location_x = 60
        text_location_y = 570
        text_color = (206,75,9)
        featuredImage.image_add_text(font_path, font_size, text, text_location_x, text_location_y, text_color)




        ### save output image
        quality_val = 100
        output_image_folder_path = './static/output/'
        output_format = "PNG"
        output_image_file_path = featuredImage.save_image(output_image_folder_path, output_format, quality_val)
        
        
        ### return file image path
        return output_image_file_path

