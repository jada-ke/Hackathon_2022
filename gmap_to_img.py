import math
earth_radius= 6371

class ref_point:
    def __init__(self, imgx, imgy, lat, lng):
        self.imgx=imgx
        self.imgy=imgy
        self.lat=lat
        self.lng=lng

top_left_coords=ref_point(0, 0, 77.56, -143.80)
bottom_right_coords= ref_point(1151, 963, 46.12, -47.48)

def gmapscoord_to_globalxy(lat, lng):
    global_x= earth_radius*lng*math.cos((top_left_coords.lat+bottom_right_coords.lat)/2)
    global_y= earth_radius*lat
    return {"x_coord":global_x,"y_coord":global_y}


def gmapscoord_to_imgpixel(lat, lng):
    xy_proj= gmapscoord_to_globalxy(lat, lng)
    x_scale= ((xy_proj["x_coord"]-top_left_coords.xy_proj["x_coord"])/(bottom_right_coords.xy_proj["x_coord"]-top_left_coords.xy_proj["x_coord"]))
    y_scale=((xy_proj["y_coord"]-top_left_coords.xy_proj["y_coord"])/(bottom_right_coords.xy_proj["y_coord"]-top_left_coords.xy_proj["y_coord"]))
    x_pixel= top_left_coords.imgx+(bottom_right_coords.imgx-top_left_coords.imgx)*x_scale
    y_pixel= top_left_coords.imgy+(bottom_right_coords.imgy-top_left_coords.imgy)*y_scale
    return {"x_coord": x_pixel, "y_coord":y_pixel}