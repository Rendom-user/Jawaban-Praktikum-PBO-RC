class Calculator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a + other.a)
        return "Error operasi tidak valid"

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a - other.a)
        return "Error operasi tidak valid"

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a * other.a)
        return "Error operasi tidak valid"

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.a == 0:
                return "Error tidak bisa dibagi dengan nol"
            return Calculator(self.a / other.a)
        return "Error operasi tidak valid"

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a ** other.a)
        return "Error"

    def __str__(self):
        return f"Hasil {self.a}"

def get_numbers():
    while True:
        try:
            numbers = list(map(float, input("Masukkan angka (pisahkan dengan spasi, contoh : 10 12 5) ").split()))
            if len(numbers) < 2:
                print("Error masukkan minimal dua angka")
                continue
            return [Calculator(num) for num in numbers]
        except ValueError:
            print("Error masukkan angka yang valid")

def get_operator():
    operasi = {
        "1": "+ (Penjumlahan)",
        "2": "- (Pengurangan)",
        "3": "* (Perkalian)",
        "4": "/ (Pembagian)",
        "5": "** (Pangkat)"
    }

    print("\n============= PILIH OPERASI ==================")
    for key, value in operasi.items():
        print(f"{key}. {value}")

    while True:
        pilihan = input("Pilih operasi (1/2/3/4/5) : ")
        if pilihan in operasi:
            return { 
                "1": "+", "2": "-", "3": "*", "4": "/", "5": "**"
            }[pilihan]
        print("Error pilihan tidak valid, coba lagi")

def main():
    print("============= KALKULATOR SEDERHANA ================")
    operator = get_operator()
    numbers = get_numbers()
    hasil = numbers[0]

    for num in numbers[1:]:
        match operator:
            case "+":
                hasil += num
            case "-":
                hasil -= num
            case "*":
                hasil *= num
            case "/":
                hasil = hasil / num
            case "**":
                hasil = hasil ** num

    operasi_str = f" {operator} ".join(str(num.a) for num in numbers)
    print(f"Operasi : {operasi_str} = {hasil}")

if __name__ == "__main__":
    main()
