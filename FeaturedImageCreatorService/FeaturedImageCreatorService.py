from FeaturedImageCreatorToolkit.FeaturedImageCreatorToolkit import FeaturedImageCreatorToolkit




class FeaturedImageCreatorService:
    



    def __init__(self):
        pass




    def generate_featured_image(self, title, subtitle, imageurl):
            
        try:

            ### Create featured image
            featuredImage = FeaturedImageCreatorToolkit()

            #check for title and subtitle
            featuredImage.handle_text(title, subtitle)
            selected_image_path = featuredImage.download_image(imageurl)

            # load image
            featuredImage.load_base_image(selected_image_path)

            # resize image
            basewidth = 1200
            x,y = featuredImage.image_resize(basewidth)

            # add logo transparent
            use_transparency_mask = False
            logo_location_x = 0
            logo_location_y = 0
            featuredImage.image_append_another_image(use_transparency_mask, logo_location_x, logo_location_y)

            # add rectangle
            rectangle_xo = 0
            rectangle_y0 = 570
            rectangle_x1 = 1200
            rectangle_y1 = rectangle_y0 + 150
            rectangle_fill_color = (0,0,0)
            rectangle_transparency = 0.75
            featuredImage.image_add_rectangle_transparent(rectangle_xo, rectangle_y0, rectangle_x1, rectangle_y1, rectangle_fill_color, rectangle_transparency)

            # add text
            text_type = "TITLE"
            textbox_length = 1200
            font_size = 52
            text = title
            text_location_x = 15
            text_location_y = rectangle_y0 + 10
            text_color = (255,219,0,255)
            featuredImage.image_add_text(text_type, font_size, text, text_location_x, text_location_y, text_color, textbox_length)

            # add text
            text_type = "SUBTITLE"
            textbox_length = 1200
            font_size = 40
            text = subtitle
            text_location_x = 15
            text_location_y = rectangle_y0 + 80
            text_color = (255,219,0,255)
            featuredImage.image_add_text(text_type, font_size, text, text_location_x, text_location_y, text_color, textbox_length)

            ### save output image
            quality_val = 100
            output_format = "PNG"
            output_image_file_path = featuredImage.save_image(output_format, quality_val)

            # finalize
            return_msg = completed_succesfully = True
            return_msg = "Completed succesfully"

            ### return file image path
            return output_image_file_path, completed_succesfully, return_msg

        except Exception as e:
            output_image_file_path = None 
            completed_succesfully = False
            return_msg = e
            return output_image_file_path, completed_succesfully, return_msg