import random
from art import logo

def kartis_archeva():
  cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  #10 ით აღნიშნულია 10 , J , Q , K , ხოლო 11 ით , ტუზი
  card = random.choice(cards) # შემთხვევითობის პრინციპით ირჩევს ერთ კარტს.
  return card #აბრუნებს კარტის მნიშვლეობას

def black_jack(cards): #შემთხვევით კარტის ამოღებით კომპიუტერს ან მოთამაშეს თუ აქვს ბლეკჯექი
  if sum(cards) == 21 and len(cards) == 2: # ორი ციფრის ჯამში თუ დაჯდა ბლექჯეკი, თავიდანვე მაგ:(ტუზი,10)
    return "BlackJack" #აბრუნებს მნიშლველობას

  if 11 in cards and sum(cards) > 21: # თუ 11 არის პირველ დარიგებაზე და ჯამი ნაკლებია 21-ზე
    cards.remove(11) # მაშინ 11 წაიშლება card - ის ლისთიდან
    cards.append(1) # და ჩაჯდება მის მაგივრად 1
  return sum(cards) # ხოლო ეს მნიშვნელობა კი დააბრუნებს კარტების ჯამის მნიშვნელობას.

def shedareba(motamashis_qula, kompiuteris_qula): #ადარებს ქულებს
  if(motamashis_qula > 21 and kompiuteris_qula > 21): #თუ მოთამაშისა და კომპიუტერის ქულა აღემატება 21-ს
    return "თქვენ სამწუხაროდ წააგეთ !" # აბრუნებს მოცემულ მნიშვნელობას

  if(motamashis_qula == kompiuteris_qula): #საყაიმო შეტყობინების გამოსატანად
    return "თამაში ყაიმით დასრულდა" # აბრუნებს საყაიმო შეტყობინებას
  elif(kompiuteris_qula == "BlackJack"): #თუ კომპიუტერს ჰყავს Blackjack აბრუნდებს მე 9 ხაზის - ამ ფუნქციის შედეგს def black_jack(cards)
    return "თქვენ დამარცხდით კომპიუტერს ჰყავს Blackjack" #გამოაქვს შესაბამისი შეტყობინება
  elif(motamashis_qula == "BlackJack"): #თუ მოთამაშეს ჰყავს Blackjack აბრუნდებს მე 9 ხაზის - ამ ფუნქციის შედეგს def black_jack(cards)
    return "თქვენ გაიმარჯვეთ Blackjack-ით !" #გამოაქვს შესაბამისი შეტყობინება
  elif (motamashis_qula > 21): #თუ მოთამაშის ქულა აღემატება 21-ს
    return "თქვენი შედეგი აღემატება 21 ქულას , თქვენ დამარცხდით !" #გამოაქვს შესაბამისი შეტყობინება
  elif (kompiuteris_qula > 21): # თუ კომპიუტერის ქულა აღემატება 21 -ს
    return "კომპიუტერის ქულა აღემატება 21 ქულას, თქვენ გაიმარჯვეთ !" #გამოაქვს შესაბამისი შეტყობინება
  elif (motamashis_qula > kompiuteris_qula): #თუ კომპიუტერის ქულა აღემატება მოთამაშის ქულას
    return "გილოცავთ, თქვენ მოიგეთ!" #გამოაქვს შესაბამისი შეტყობინება
  else: #წინააღმდეგ შემთხვევაში
    return "სამწუხაროდ დამარცხდით !" #გამოაქვს შესაბამისი შეტყობინება

def tamashis_dawyeba(): #მთავარი მენიუ
  print(logo)#სვამს  from art import logo , ცვლად ლოგოს, რომელშიც დახატულია ეს ყველაფერი.
  motamashis_karti = [] #მოთამაშის კარტში ჯერ ჩასმულია შემთხვევითი ერთი ციფრი.
  kompiuteris_karti = [] #კომპიურერის კარტში ჯერ ჩასმულია შემთხვევითი ერთი ციფრი.
  tamashis_statusi = False #გამოიყენება ციკლისთვის.

  for _ in range(2): #ორჯერ ატრიალებს ციკლს და სვამს მითითებულ ცვლადებში მეორე შემთხვევით კარტს
    motamashis_karti.append(kartis_archeva()) #მოთამაშის კარტში სვამს შემთხვევით მეორე კარტს
    kompiuteris_karti.append(kartis_archeva())#კომპიუტერის კარტში სვამს შემთხვევით მეორე კარტს

  while not tamashis_statusi: # სანამ თამაშის სტატუსი ჭეშმარიტი არ გახდება მანამდე არ წვვეტს მუშაობას ციკლი (tamashis_statusi = False)
    motamashis_qula = black_jack(motamashis_karti) #სვამს მოცემულ ფუნქციაში ციფრებს, რომელი ფუნქციაც ამ ციფრებს ერთმანეთს უმატებს, ამ შემთხვევაში, მოთამაშის კარტს.
    kompiuteris_qula = black_jack(kompiuteris_karti)#სვამს მოცემულ ფუნქციაში ციფრებს, რომელი ფუნქციაც ამ ციფრებს ერთმანეთს უმატებს, ამ შემთხვევაში, კომპიუტერის კარტს.
    print("თქვენი კარტია:", motamashis_karti, "ჯამში = ", motamashis_qula) #ბეჭდავს მიღებულ შედეგებს
    print("კომპიუტერის პირველი კარტია:", kompiuteris_karti[0]) #ბეჭდავს მიღებულ შედეგებს

    if motamashis_qula == "BlackJack" or kompiuteris_qula == "BlackJack" or motamashis_qula > 21: #ასრულებს ოპერაციებს
      tamashis_statusi = True #ციკლის ასრულებს თუ ეს პირობა შესრულდა
    else: # წინააღმდეგ შემთხვევაში ასრულებს ამ პირობას 56 ლაინზე
      shetavazeba = input(str("დააჭირეთ 'y' ღილაკს თუ გსურთ კარტის აღება თუ არა დააჭირეთ 'n': "))
      if(shetavazeba == 'y'):  # თუ y დააჭირა მომხმარებელმა მაშინ 58 ლაინზე რაცაა იმას ასრულებს
        motamashis_karti.append(kartis_archeva()) #სვამს მესამე კარტს
      else:
        tamashis_statusi = True #წინააღმდეგ შემთხვევაში ასრულებს ციკლს.

                    #კომპიუტერის ალგორითმი
  while kompiuteris_qula != 0 and kompiuteris_qula < 17: #სანამ 0-ს არ უდრის და სანამ 17 ზე ნაკლებია
    kompiuteris_karti.append(kartis_archeva()) #ამატებს კარტს
    kompiuteris_qula = black_jack(kompiuteris_karti) # ითვლის რაოდენობას
  print("მოთამაშის საბოლოო კარტია:", motamashis_karti, "საბოლოო შედეგია: ", motamashis_qula) # გამოაქვს შედეგები
  print("კომპიუტერის საბოლოო კარტია:", kompiuteris_karti, "საბოლოო შედეგია: ", kompiuteris_qula) # გამოაქვს შედეგები
  print(shedareba(motamashis_qula,kompiuteris_qula)) #ადარებს მე 18 ხაზზე განთავსებული ფუნქიციის წინაპირობებს

while input("დავიწყოთ Black-Jack - ის თამაში? აკრიფეთ 'y' ან 'n'") == 'y': #გვეკითხება თუ გვინდა თამაშის დაწყება
  tamashis_dawyeba() # იძახებს თამაშის მთავარ ფუნქციას სადაც გაერთიანებულია ყველა ფუნქცია!

