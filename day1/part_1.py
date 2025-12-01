import click


def strip_rotate(rotation: str) -> tuple[str, int]:
    direction = rotation[0]
    number = int(rotation[1:])
    return direction, number


def rotate(current_rot: int, direction: str, number: int) -> int:
    if direction == 'L':
        current_rot = current_rot - number
        if current_rot < 0:
            current_rot = current_rot % 100
    else:
        current_rot = current_rot + number
        if current_rot > 99:
            current_rot = current_rot % 100
    return current_rot


def rotate_and_check_zeros(current_rot: int, rotation_str: str, number_zeros: int) -> tuple[int, int]:
    direction, number = strip_rotate(rotation_str)
    current_rot = rotate(current_rot, direction, number)
    if current_rot == 0:
        number_zeros = number_zeros + 1
    return number_zeros, current_rot


@click.command()
@click.option('--input', 'input_path', required=True)
@click.option('--initial-rotation', 'initial_rot', default=50)
def main(input_path, initial_rot):
    with open(input_path) as file:
        lines = [line.strip() for line in file]

    number_zeros = 0
    current_rot = initial_rot

    for line in lines:
        number_zeros, current_rot = rotate_and_check_zeros(current_rot, line, number_zeros)

    print(number_zeros)


if __name__ == '__main__':
    main()
