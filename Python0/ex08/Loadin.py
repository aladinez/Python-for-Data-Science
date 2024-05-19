
def ft_tqdm(lst: range) -> None:
    total = len(lst)
    coeff = 100 / total
    for i, elem in enumerate(lst):
        eq = int((i + 1) * coeff)
        progress_bar = "=" * eq + " " * (100 - eq)
        print(f"{eq}%|[{progress_bar}]|", end='\r')
        print(f"{i+1}/{total}", end='\r')
        yield elem

