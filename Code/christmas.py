def christmas_tree(height):

  for i in range(1, height + 1):
    print(' ' * (height - i), end='')
    print('*' * (2 * i - 1))
#(height-2) just to make the branch look almost like it's in the middle    
  print(' ' * (height-2), '**')
  print(' ' * (height-2), '**')

inputHeight = int(input("Height of the tree: "))
christmas_tree(inputHeight)