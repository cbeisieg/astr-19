class FavoriteAnimal:
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def display_info(self):
        print("Arm length:", self.arms, "inches")
        print("Leg length:", self.legs, "inches")
        print("Number of eyes:", self.eyes)
        print("Does it have a tail:", self.tail)
        print("Is it furry:", self.furry)


def main():
    x = FavoriteAnimal(59.8, 59.8, 2, True, True)
    x.display_info()


if __name__ == "__main__":
    main()
