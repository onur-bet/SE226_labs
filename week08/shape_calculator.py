import geometry_utils


def main():
    # Föyde istenen giriş mesajları
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    # String isimleri fonksiyonlara bağlayan sözlük yapısı
    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    operation_name = input("Enter the operation you want to perform: ").strip().lower()

    if operation_name not in operations:
        print("Input Error: Invalid operation.")
        return

    try:
        # Seçilen şekle göre input alma işlemleri
        if operation_name.startswith("circle"):
            radius = float(input("Enter radius: "))
            # Sözlükten fonksiyonu bul ve çalıştır
            result = operations[operation_name](radius)

        elif operation_name.startswith("rectangle"):
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations[operation_name](width, height)

        elif operation_name.startswith("triangle"):
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations[operation_name](base, height)

        # Sonucu 2 ondalık basamakla yazdır
        print(f"Result: {result:.2f}")

    except ValueError as e:
        # Eğer kullanıcı harf girerse Python'un kendi ValueError'u çalışır,
        # Negatif sayı girerse bizim 'geometry_utils' içinde yazdığımız ValueError çalışır.
        if "could not convert" in str(e):
            print("Input Error: Please enter numerical values.")
        else:
            print(f"Input Error: {e}")


if __name__ == "__main__":
    main()