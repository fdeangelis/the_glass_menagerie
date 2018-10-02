print("The Glass Menagerie is an ace act play of 7 scenes: The narrator is Tom Wingfield."
      "The name of the act play is inspired at the glass menagerie of Laura."
      "Tom lives with his family:Laura , her older sister,and the mother, Amanda.")


while True:
  value = input("Which person (Jim, Tom, Amanda, Laura): ")

  if (value.lower() == "jim"):
      print(" An old acquaintance of Tom and Laura. Jim was a popular athlete in high school"
            " and is now a shipping clerk at the shoe warehouse in which Tom works.")
           

  if (value.lower() ==  "tom"):
      print("Amanda's son and Laura's younger brother. An aspiring poet, "
            "Tom works at a shoe warehouse to support the family. He is frustrated"
            " by the numbing routine of his job and escapes from it through movies, literature, and alcohol.")

  if (value.lower() ==  "amanda"):
      print("Laura and Tom's mother. A proud, vivacious woman, Amanda clings fervently"
            " to memories of a vanished, genteel past. She is simultaneously admirable, charming, pitiable, and laughable.")

  if (value.lower() == "laura"):
    print("Amanda's daughter and Tom's older sister. Laura has a bad leg, on which she has to wear a brace, and walks with a limp."
          " Twenty-three years old and painfully shy, "
          "she has largely withdrawn from the outside world and devotes herself to old records and her collection of glass figurines")

  if (value.lower() != "jim") and(value.lower() != "tom") and(value.lower() != "amanda") and(value.lower() != "laura"):
    print("Wrong value, possible values: Jim, Tom, Amanda and Laura")
      
  