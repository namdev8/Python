color=input("ENTER COLOURS SEPARATED BY COMMAS: ")
color_list1=color.split(',')
print(color_list1)
print("FIRST COLOUR:",color_list1[0])
print("LAST COLOUR:",color_list1[-1])
color_list2=["Red","Orange","Black","White"]
print("COLOUR LIST 1 NOT CONTAINED IN COLOUR LIST 2 ARE: ")
diff=list(set(color_list1)-set(color_list2))
print(diff)
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))
print(f"List of integers corresponding to each colour: {color_int_list}")
