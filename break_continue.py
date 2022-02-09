def run():
    """ continue, we can use it within a condition within the loop,
        indicating that if the condition is met, we can continue with
        the loop, as for break, we will indicate that the loop reaches
        that point and will exit it """
    for contador in range(1001):
        if contador % 2 != 0:
            continue
        print(contador)

    for i in range(10001):
        print(i)
        if i == 5265:
            break


if __name__ == "__main__":
    run()
