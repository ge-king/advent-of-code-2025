import re
import click


def strip_rotate(rotation: str) -> tuple[str, int]:
    direction, num = re.match(r"([A-Za-z]+)(\d+)", rotation).groups()
    number = int(num)
    return direction, number


def rotate(current_rot: int, direction: str, number: int) -> tuple[int, int]:
    number_clicks = number // 100
    rem = number % 100
    if direction == 'L':
        if current_rot > 0 and (current_rot - rem) <= 0:
            number_clicks += 1
        current_rot = (current_rot - rem) % 100
    else:
        if (current_rot + rem) >= 100:
            number_clicks += 1
        current_rot = (current_rot + rem) % 100
    return current_rot, number_clicks


def rotate_and_check_zeros(current_rot: int, rotation_str: str, number_zeros: int) -> tuple[int, int]:
    direction, number = strip_rotate(rotation_str)
    current_rot, number_clicks = rotate(current_rot, direction, number)
    number_zeros = number_zeros + number_clicks
    return number_zeros, current_rot


@click.command()
@click.option('--input', 'input_path', required=True)
@click.option('--initial-rotation', 'initial_rot', default=50)
def main(input_path, initial_rot):
    with open(input_path) as file:
        lines = [line.rstrip() for line in file]

    number_zeros = 0
    current_rot = initial_rot

    for line in lines:
        number_zeros, current_rot = rotate_and_check_zeros(current_rot, line, number_zeros)

    print(number_zeros)


if __name__ == '__main__':
    main()
