#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                element1 = my_list_1[i]
                element2 = my_list_2[i]

                if not (isinstance(element1, (int, float))
                        and isinstance(element2, (int, float))):
                    raise ValueError("wrong type")

                if element2 == 0:
                    raise ZeroDivisionError("division by 0")

                result.append(element1 / element2)
            else:
                raise IndexError("out of range")
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except ValueError as e:
            print(e)
            result.append(0)
        except IndexError as e:
            print(e)
            result.append(0)
        finally:
            pass  # The finally block

    return result
