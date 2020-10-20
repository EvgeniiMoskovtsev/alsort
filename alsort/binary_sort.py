from loguru import logger


@logger.catch
def binary_sort(array, number):
    while True:
        index = len(array) // 2
        mid = array[index]
        if mid > number:
            return binary_sort(array[:len(array) // 2], number) + len(array) // 2
        elif mid < number:
            return binary_sort(array[len(array) // 2:], number) + len(array) // 2
        elif mid == number:
            return index


if __name__ == "__main__":
    target_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_index = binary_sort(target_array, 9)
    logger.info("Target index: {}".format(target_index))
