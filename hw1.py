def get_radius(prompt):
    r = int(input(prompt))
    return r;

input_prompt=input('넓이를 구하고자 하는 원의 반지름은?')
result=get_radius(input_prompt)
print('반지름이',result,'인 원의 넓이는',3.14*result*result)

def get_circle_area(radius) :
    r=int(input(radius))
    a=r*r*3.14
    print('원의 반지름이',r,'인 원의 넓이는',a)
    return a;

input_radius=input('넓이를 구하고하 하는 원의 반지름은?')
get_circle_area(input_radius)
