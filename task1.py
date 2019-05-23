def copyfile_example(source, dest):
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        copyfileobj_example(src, dst)
