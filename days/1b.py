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
    for number in list_left:
        count = list_right.count(number)
        if count > 0:
            results.append(int(number) * count)
    print(results)
    print(sum(results))
