
washing_times = {
    "jacket": 40,
    "underwear": 70,
    "shoes": 20
}


rinse = True
spin = False


washing_product = "shoes"


total_washing_time = washing_times.get(washing_product, 0)


if rinse:
    total_washing_time += 15


if spin:
    total_washing_time += 9


print(f"Total washing time: {total_washing_time} minutes")
