FLAVORS = [
"Banana",
"Chocolate",
"Lemon",
"Pistachio",
"Raspberry",
"Strawberry",
"Vanilla",]

already_tried = []

for i in FLAVORS:
    if len(FLAVORS) >= 1:
        for g in FLAVORS:
            if g==i or g in already_tried:
                continue
            else:
                print(f"{i}, {g}")
        already_tried.append(i)