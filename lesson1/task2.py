import os

def print_directory_contents(path, sm = 1):
    
    if os.path.isfile(path) == True:
        print(" "*sm, end="")
        print(path)
    else:
        print(path)
        dirs = os.listdir(path)
        for i in range(len(dirs)):
            print_directory_contents(f"{path}\\{dirs[i]}", sm=sm+1)
    #return print_directory_contents()




if __name__ == "__main__":
    path = "C:\\Dev\\gb_cv"
    print_directory_contents(path)