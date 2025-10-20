class FavoriteAnimal:
    def __init__(animal, arms, legs, eyes, tail, furry):
        animal.arms = arms
        animal.legs = legs
        animal.eyes = eyes
        animal.tail = tail
        animal.furry = furry

    def display_info(animal):
        print("Arm length:", animal.arms, "inches")
        print("Leg length:", animal.legs, "inches")
        print("Number of eyes:", animal.eyes)
        print("Does it have a tail:", animal.tail)
        print("Is it furry:", animal.furry)

x = FavoriteAnimal(59.8, 59.8, 2, True, True)
x.display_info()