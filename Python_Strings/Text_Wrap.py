import textwrap

def wrap(string, max_width):
   wrapper = textwrap.TextWrapper(width=max_width)
   string1 = wrapper.fill(text=string)
   return string1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)