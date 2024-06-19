#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_and_print_lines():
    lines = []
    print("Enter lines of text (press Enter on an empty line to finish):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    read_and_print_lines()


# In[ ]:




