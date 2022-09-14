import random
import time


from BaseGames import BaseGames


def get_list_from_user():
    user_input = input("Enter the numbers, where each number is separated by a single space.")
    user_list = user_input.split()
    for i in range(0, len(user_list)):
        if user_list[i].isdigit():
            user_list[i] = int(user_list[i])
    return user_list


def is_list_equal(list1, list2):
    return list1 == list2


class MemoryGame(BaseGames):
    def play(self):
        self.load_game()
        input(f"""You will now be shown a series of {self.difficulty} numbers. Each number will be between 1 and 100.
        You will be shown this list for less than a second, after which you will be prompted to enter the list 
        in the correct order.
        When you are ready, Enter to continue...""")
        gen_list = self.generate_sequence()
        print(gen_list, end="")
        time.sleep(0.7)
        print("\r", end="")
        user_list = get_list_from_user()
        self.check_results(is_list_equal(gen_list, user_list))
        self.end_game()

    def generate_sequence(self):
        return random.sample(range(1, 100), int(self.difficulty))