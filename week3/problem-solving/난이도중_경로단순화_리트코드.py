import sys
input = sys.stdin.readline

directory = [x for x in input().strip().split("/") if x]

def func(directory):
    complete_path = []

    for dir_ in directory:
        if dir_ == ".":
            continue
        elif dir_ == "..":
            if complete_path:
                complete_path.pop()
        else:
            complete_path.append(dir_)

    return "/" + "/".join(complete_path)


print(func(directory))