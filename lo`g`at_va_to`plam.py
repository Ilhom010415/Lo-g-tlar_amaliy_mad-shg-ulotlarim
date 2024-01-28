# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:37:16 2024

# LO`G`ATLAR

@author: User
"""
# # mening buyumlarim lo`g`ati
# my_things = {'asus':'vivobook', 'display':'oled', 'samsung':'phone'}
# print(my_things['asus'])
# print(my_things['display'])

#  # oddiy engilizchadan o`zbekchaga tarjima lo`g`at
# en_uzb = {'laptop':'noutbuk', 'book':'kitob', 'leg':'oyoq', 'TV':'telivozor'}
# print(en_uzb)
# print(en_uzb['book'])

# # bu yerda raqamlar bir tirnoq yoki qo`sh-tirnoqga olinmas ekan
# market = {'olma':10000, 'banan':18000, 'limon':13000, 'suv':3000}
# print(f"Bananning narhi {market['banan']} so'm ekan!")

# # Lo`g`atga istalgan malumot turlarini saqlashimiz mumkin ekan
# # va "\" bu belgi orqali kodimizni yangi qatordan davom ettirsak bo`lar ekan
# aboute_me = {'ism':'ilhom rahmonov', 'yosh':22, 't_year':2000}
# print(f"{aboute_me ['ism'].title()},\
#       \n{aboute_me['t_year']}-yilda tug`ilgan,\
#     \n{aboute_me['yosh']} yoshda")
# # biz "\n" belgisini har doim yangi qator boshidan boshlasak ishlaydi

# # Yangi kalit so`z va qiymat qo`shisha
# aboute_me['ism1'] = "baxodir jalolov"  # bu lo`g`atga oxiridan yana qiymat qo`shdi
# aboute_me['yosh1'] = 28 # bunda ham qiymat qo`shildi
# aboute_me['t_year'] = 1992 # bu yerda esa biz lo`g`atda borini almashtirdik

# # BO`SH LO`G`AT
# # agar biz qiymatni yangilamoqchi bo`lsak yuqoridagi usuldan foydalansak bdi
# bosh_dic = {}
# bosh_dic['day'] = 'kun'
# bosh_dic['night'] = 'tun'
# bosh_dic['green'] = 'yashil'
# bosh_dic['one'] = 1

# Lo`g`atdan qiymatni o`chirish
# my_things = {'asus':'vivobook', 'display':'oled', 'samsung':'phone'}
# # print(my_things['asus'])
# del my_things['asus'] # bitta element o`chirildi
# print(my_things)
# print(len(my_things))  # lo`g`t ichidagi elementlar ikkita bo`lib qoldi

# #   Agar bizda lo`g`t juda ham uzun bo`lsa
# davlatlar = {
#     'uzb':'O`zbekiston',
#     'kz':'Qozog`iston',
#     'rus':'Rassiya'
#     }
# # print(davlatlar)

#   .get() metodi 
# country = davlatlar['uzb']
# print(f"Bizning davlatimiz {country}")

#  # country = davlatlar['usa']
#  # print(f"Kolyaning davlati {country}")

# country = davlatlar.get('usa', 'Bunday davlat lo`g`atda mavjut emas') # agar "noma'lum" 
# # kalit so`z yo`q bo`lsa "Bunday davlat lo`g`atda mavjut emas" deb chiqar
# country = davlatlar.get('usa')
# print(country)





