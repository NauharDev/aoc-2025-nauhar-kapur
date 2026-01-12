import os

def compute_password():

    pos = 50
    total_zero = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'day_1.txt'), 'r') as f:
        for line in f:
            move = line.strip()
            amount = int(move[1:])
            if move[0] == 'L':
                # towards lower numbers
                pos = (pos - amount) % 100
            else:
                # towards higher numbers
                pos = (pos + amount) % 100
            if pos == 0:
                total_zero += 1
    print(total_zero)

def compute_password_p2():

    pos = 50
    total_zero = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'day_1.txt'), 'r') as f:
        for line in f:
            move = line.strip()
            amount = int(move[1:])

            num_full_circles = amount // 100
            remaining_amount = amount % 100
            total_zero += num_full_circles

            if remaining_amount > 0:
                new_pos = None
                if move[0] == 'L':
                    new_pos = pos - remaining_amount
                    if new_pos <= 0 and pos > 0:
                        total_zero += 1
                else:
                    new_pos = pos + remaining_amount
                    if new_pos >= 100:
                        total_zero += 1
                pos = new_pos % 100
    print(total_zero)


if __name__ == '__main__':
    compute_password()
    compute_password_p2()


