"""
This program takes the value "a" and calculates all dimensions for a vortex ring parachute gore and line components

"""
def annular():
    from math import pi

    try:
        a = float(input('Enter length of "a": '))
        

    except ValueError:
        print('Invalid Number')

    Base = float(a*0.83) #base of triangle above 10 degree point
    PBL = float(a*0.83)
    SL = float(a*1.25)
    AIL = float(a*1.66)
    ShortPBL = float(a*0.415)
    LongeSL = float(a*1.655)
  
    
    print('______________________________________')
    print('The triangle baseline length at 90 degrees to base of a is', Base)
    print('The Periphery Bridge Line length is', PBL)
    print('The Suspension Line length is',SL)
    print('The Apex Inversion Line length is',AIL)
    print('The short version PBL is', ShortPBL)
    print('The long version SL is',LongeSL)
    print('The Bridle Length is greater than or equal to',a)
    
   
    print ('All dimensions do not include seam allowances')

if __name__ == '__main__':
    while True:
        annular()
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
