score = int(input( "Ball kriting: "))

def ged_grade(score):
    if score > 90:
        print( "A" )
    elif 90 >score> 75:
        print( "B" )
    elif 75 >score> 60:
        print( "C" )
    elif score < 60:
        print( "F" )
ged_grade(score)
