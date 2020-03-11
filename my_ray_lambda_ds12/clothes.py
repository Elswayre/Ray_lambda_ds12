class Clothes():
    num_of_clothes = 0
    

    def __init__(self,kind, style, size, color):
        self.style = style
        self.size = size
        self.color = color
        def pop_collar(self):
            print('popping coller')
        
        Clothes.num_of_clothes += 1




if __name__ == '__main__':
    polo = Clothes(kind = 'shirt', style='sheek', size='L',color='blue')
    print(type(polo))
    print(polo.style)
    print(polo.color)
    print(polo.size)


    polo2 = Clothes(kind = 'shirt', style='shimmer', size='s',color='yellow')
    print(type(polo2))
    print(polo2.style)
    print(polo2.color)
    print(polo2.size)

    polo3 = Clothes(kind = 'shirt', style='dapper', size='xs',color='green')
    print(type(polo3))
    print(polo3.style)
    print(polo3.color)
    print(polo3.size)

print(Clothes.num_of_clothes)