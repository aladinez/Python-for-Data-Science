import os


def ft_tqdm(lst: range) -> None:
    '''
    Display a progress bar while iterating over a range.
    '''

    total = len(lst)
    terminal_size = os.get_terminal_size().columns - 40
    coeff = (terminal_size) / total
    for i, elem in enumerate(lst):
        i += 1
        percentage = int((i) * coeff)
        progress_bar = "█" * percentage + " " * (terminal_size - percentage)
        norm_percentage = int((i) / total * 100)
        print(f"{norm_percentage}%|{progress_bar}|", f"{i}/{total}", end='\r')
        yield elem
