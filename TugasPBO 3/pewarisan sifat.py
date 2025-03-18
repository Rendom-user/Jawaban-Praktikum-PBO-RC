import random

class Parent:
    def __init__(self, name, gol_darah):
        self.name = name
        self.gol_darah = gol_darah
        self.alel1, self.alel2 = self.penentuan_alel()

    def penentuan_alel(self):
        gol_darah_ke_alel = {
            "A": [("A", "A"), ("A", "O")],
            "B": [("B", "B"), ("B", "O")],
            "O": [("O", "O")],
            "AB": [("A", "B")]
        }
        return random.choice(gol_darah_ke_alel[self.gol_darah])

    def get_random_alel(self):
        return random.choice([self.alel1, self.alel2])

class Father(Parent):
    def __init__(self, gol_darah):
        super().__init__("Father", gol_darah)

class Mother(Parent):
    def __init__(self, gol_darah):
        super().__init__("Mother", gol_darah)

class Child:
    def __init__(self, father, mother):
        self.alel1 = father.get_random_alel()
        self.alel2 = mother.get_random_alel()
        self.gol_darah = self.penentuan_gol_darah()

    def penentuan_gol_darah(self):
        alel = {self.alel1, self.alel2}

        if alel == {"A", "B"}:
            return "AB"
        elif "A" in alel:
            return "A"
        elif "B" in alel:
            return "B"
        else:
            return "O"

    def __str__(self):
        return f"Golongan Darah Anak : {self.gol_darah}"

def input_gol_darah(parent_name):
    while True:
        gol_darah = input(f"Masukkan golongan darah {parent_name} (A, B, O, AB) : ").upper()
        if gol_darah in {"A", "B", "O", "AB"}:
            return gol_darah
        else:
            print("Golongan darah tidak valid! Silakan coba lagi.")

def main():
    print("----- Simulasi Pewarisan Golongan Darah -----")

    gol_darah_father = input_gol_darah("Father")
    gol_darah_mother = input_gol_darah("Mother")

    father = Father(gol_darah_father)
    mother = Mother(gol_darah_mother)
    child = Child(father, mother)

    print("\nHasil Pewarisan : ")
    print(f"Golongan Darah Ayah : {gol_darah_father}")
    print(f"Golongan Darah Ibu : {gol_darah_mother}")
    print(child)

if __name__ == "__main__":
    main()
