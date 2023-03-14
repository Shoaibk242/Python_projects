'''19.Write a Python program to convert the two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
def list_dict(l1,l2):
    dict={}
    for key in keys:
        for value in values:
            dict[key] = value
            values.remove(value)
            break  
    return dict
print(list_dict(keys,values))
'''another method is to use zip()
dict1 = dict(zip(keys,values))'''