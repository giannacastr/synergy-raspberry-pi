import random
import os
from colorama import init, Fore, Style
import time

def ship_animation(call):

    # animation for missed shot

    if call == 0:
        fiftychance = random.randint(0,1)

        if fiftychance == 1:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("""     
            -}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""     
            ---}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""     
            -----}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""      
                            /     |
            -------}===>   __/       |
                        /           |
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
                            /     |
            ---------}===> __/       |
                        /           |
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""           
                            (        )
            --------------(   BOOM!   )
                            (        )
            """)

            print("\nThe missile struck an innocent island...")

        else:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""     
            -}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""     
            ---}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""     
            -----}===>
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""      
                            
            -------}===>  
                    
            """)

            time.sleep(.3)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("""           
                            (~~~~~~~~~)
            ------------}===>(~~~~~~~~~~~~)
                            (~~ >(^) ~~)
            """)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nTHE POOR FISHIES")  


    if call == 1:

        # animation for ship hit
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""     
         -}===>
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""     
            ---}===>
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""     
              -----}===>
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
                                  ___|___
                -------}===>      |     |
                                  |_____/""")
        
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
                                  ___|___
                  ---------}===>  |     |
                                  |_____/""")
        
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
                                  ___|___
                  ---------BOOOMM )     |
                                  |_____/""") 