import ntpath
ntpath.basename("a/b/c")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

filename='file:///C:/Users/Vani/Downloads/CSS20Experiment%20-20220details-20220201/CSS20Expt202.pdf'
file=path_leaf(filename)
print(file)