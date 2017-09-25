# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment: Unit1-04
# This program calculates the circumference of a circle in cm with the radius given by the user

import ui

def calculate_button_touch_up_inside(sender): 
    #This calculates the circumference of the circle in cm
    
    # constants
    PI = 3.14
    
    #input
    radius = float(view['input_radius_textbox'].text)
    
    #process
    circumference = 2.0 * PI * radius
    
    #output
    view['circumference_answer_label'].text = "Circumference = "+str(circumference)+" cm"
    
view = ui.load_view() 
view.present('full_screen')
