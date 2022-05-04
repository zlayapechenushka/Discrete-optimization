if __name__ == "__main__":
    number_of_items = int(input())
    bin_volume = int(input())
    items = [[int(input()), i] for i in range(number_of_items)]
    items = sorted(items, key=lambda x: x[0], reverse=True)
    bins = [0] * number_of_items
    answer = [0] * number_of_items

    for i in range(number_of_items):
        volume = items[i][0]
        for k in range(len(bins)):
            if bins[k] + volume <= bin_volume:
                bins[k] += volume
                answer[items[i][1]] = k + 1
                break

    print(*answer)
