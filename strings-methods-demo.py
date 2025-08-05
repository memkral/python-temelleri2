# text = "  Python Programlama Dili Öğreniyorum  "

# # String metodları örnekleri - Tek string üzerinden

# # 1. replace() - Belirtilen değeri başka bir değerle değiştirir
# result1 = text.replace('Python', 'Java')
# print("1. replace():", result1)

# # 2. lower() - Stringi küçük harfe çevirir
# result2 = text.lower()
# print("2. lower():", result2)

# # 3. upper() - Stringi büyük harfe çevirir
# result3 = text.upper()
# print("3. upper():", result3)

# # 4. strip() - Başındaki ve sonundaki boşlukları kaldırır
# result4 = text.strip()
# print("4. strip():", result4)

# # 5. split() - Stringi belirtilen ayırıcıya göre böler
# result5 = text.split()
# print("5. split():", result5)

# # 6. count() - Belirtilen değerin kaç kez geçtiğini sayar
# result6 = text.count('a')
# print("6. count():", result6)

# # 7. startswith() - String belirtilen değerle başlıyor mu?
# result7 = text.startswith('Python')
# print("7. startswith():", result7)

# # 8. endswith() - String belirtilen değerle bitiyor mu?
# result8 = text.endswith('m')
# print("8. endswith():", result8)

# # 9. find() - Belirtilen değerin pozisyonunu bulur
# result9 = text.find('Python')
# print("9. find():", result9)

# # 10. len() - Stringin uzunluğunu döndürür
# result10 = len(text)
# print("10. len():", result10)

# # 11. title() - Her kelimenin ilk harfini büyük yapar
# result11 = text.title()
# print("11. title():", result11)

# # 12. capitalize() - İlk harfi büyük yapar
# result12 = text.capitalize()
# print("12. capitalize():", result12)

# # 13. isalpha() - Tüm karakterler alfabetik mi?
# result13 = text.isalpha()
# print("13. isalpha():", result13)

# # 14. isdigit() - Tüm karakterler rakam mı?
# result14 = text.isdigit()
# print("14. isdigit():", result14)

# # 15. join() - Iterable elemanlarını stringe çevirir
# result15 = '-'.join(text.split())
# print("15. join():", result15)

# # 16. center() - Stringi ortalar
# result16 = text.center(50, '*')
# print("16. center():", result16)

# # 17. ljust() - Sola hizalar
# result17 = text.ljust(50, '-')
# print("17. ljust():", result17)

# # 18. rjust() - Sağa hizalar
# result18 = text.rjust(50, '-')
# print("18. rjust():", result18)

# # 19. swapcase() - Büyük/küçük harfleri değiştirir
# result19 = text.swapcase()
# print("19. swapcase():", result19)

# # 20. zfill() - Başına sıfır ekler
# result20 = "42".zfill(5)
# print("20. zfill():", result20)

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

result = ' Hello World '.strip()

result = 'www.sadikturan.com'.strip('www.').strip('.com')

result =  course.lower()

result = website.find('a')

result = website.startswith('www.')

result = website.endswith('com')

result = website.find('.com')

result = course.isalpha()

result = 'contents'.center(50,' ')
















print(result)