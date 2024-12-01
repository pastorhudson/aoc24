from aocd import data


def split_list(data):
    list_left = []
    list_right = []

    for row in data.splitlines():
        left, right = row.split("   ")
        list_left.append(left)
        list_right.append(right)
    return list_left, list_right


if __name__ == '__main__':
    list_left, list_right = split_list(data)
    list_left.sort()
    list_right.sort()
    results = []
    for i in range(len(list_left)):
        print(list_left[i], list_right[i])
        results.append(abs(int(list_left[i]) - int(list_right[i])))
    print(results)
    print(sum(results))
