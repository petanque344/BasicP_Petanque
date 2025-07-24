# # ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
# def show_movies(movie_list):
#     # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว

# # ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
# def check_age(user_age, age_restriction):
#     # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
#     # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

# # ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
# def calculate_price(base_price, genre):
#     # TODO: ถ้า genre เป็น 'Sci-Fi' บวกเพิ่ม 50 บาท
#     # ถ้าไม่ใช่ คืนราคาเดิม

# # ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
# def buy_ticket(movie_list):
#     # TODO: 
#     # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
#     # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
#     # 3. รับอายุผู้ใช้
#     # 4. ตรวจสอบอายุผ่าน check_age
#     #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
#     # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
#     # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
#     # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

# def main():
#     # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
#     movies = [
#         {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
#         {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
#         {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
#         {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
#         {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
#     ]

#     # TODO: แสดงเมนูให้ผู้ใช้เลือก
#     # 1. แสดงหนังทั้งหมด
#     # 2. ซื้อตั๋วหนัง

#     # รับค่าตัวเลือกเมนูจากผู้ใช้
#     menu = input("เลือกเมนู: ")

#     # TODO: ตรวจสอบเมนูที่เลือก
#     # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
#     # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
#     # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# # เรียก main เพื่อเริ่มโปรแกรม
# main()

# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie['movie_name']} - ราคา: {movie['ticket_price']} บาท")


# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    if age_restriction == 'G':
        return True
    return user_age >= int(age_restriction)


# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if genre == 'Sci-Fi':
        return base_price + 50
    return base_price


# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    show_movies(movie_list)
    
    try:
        choice = int(input("เลือกหนัง (1-5): "))
        if not 1 <= choice <= len(movie_list):
            print("เลือกหนังไม่ถูกต้อง")
            return
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
        return

    movie = movie_list[choice - 1]

    try:
        age = int(input("กรุณาใส่อายุของคุณ: "))
    except ValueError:
        print("กรุณาใส่อายุเป็นตัวเลข")
        return

    if not check_age(age, movie['age_restriction']):
        print("คุณอายุน้อยเกินไป ไม่สามารถดูหนังเรื่องนี้ได้")
        return

    print("เลือกเสียงพากย์:")
    print("1. พากย์ไทย")
    print("2. Soundtrack")
    dub_choice = input("เลือก (1 หรือ 2): ")

    if dub_choice == '1':
        dub = "พากย์ไทย"
    elif dub_choice == '2':
        dub = "Soundtrack"
    else:
        print("ตัวเลือกเสียงไม่ถูกต้อง")
        return

    final_price = calculate_price(movie['ticket_price'], movie['genre'])

    print("\n==== ใบเสร็จ ====")
    print(f"ชื่อหนัง: {movie['movie_name']}")
    print(f"เสียง: {dub}")
    print(f"ราคาตั๋ว: {final_price} บาท")
    print("================")


def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    print("=== เมนู ===")
    print("1. แสดงหนังทั้งหมด")
    print("2. ซื้อตั๋วหนัง")

    menu = input("เลือกเมนู (1 หรือ 2): ")

    if menu == '1':
        show_movies(movies)
    elif menu == '2':
        buy_ticket(movies)
    else:
        print("เมนูไม่ถูกต้อง")

# เรียก main เพื่อเริ่มโปรแกรม
main()
