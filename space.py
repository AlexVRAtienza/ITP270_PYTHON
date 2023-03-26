#!/bin/python



print("Here are the list of the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")

print("   4. Saturn  5. Uranus  6. Neptune\n")



weight = 185

planet = int(input("Enter planet number: "))



if planet == 1:

    weight = 0.91

    print("The weight on Venus would be", weight)



else:

    if planet == 2:

        weight= 0.38

        print("The weight on Mars would be", weight)



    else:

        if planet == 3:

            weight = 2.34

            print("The weight on Jupiter would be", weight)



        else:

            if planet == 4:

                weight= 1.06

                print("The weight on Saturn would be", weight)



            else:

                if planet == 5:

                    weight = 0.92

                    print("The weight on Uranus would be", weight)



                else:

                    if planet == 6:

                        weight= 1.19

                        print("The weight on Neptune would be", weight)



                    else:

                        print("Planet number is invalid. Please enter the correct number between 1 and 6.")
