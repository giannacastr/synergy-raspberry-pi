import random
import os
from colorama import init, Fore, Style
import time

def ship_animation(call):
    if call == missileLaunchMiss:
        fiftychance = random.randint(0,1)

        if fiftychance == 1:

            print("""     
            -}===>
            """)

            time.sleep(.3)

            print("""     
            ---}===>
            """)

            time.sleep(.3)

            print("""     
            -----}===>
            """)

            time.sleep(.3)

            print("""      
                            /     |
            -------}===>   __/       |
                        /           |
            """)

            time.sleep(.3)

            print("""
                            /     |
            ---------}===> __/       |
                        /           |
            """)

            time.sleep(.3)

            print("""           
                            (        )
            --------------(   BOOM!   )
                            (        )
            """)

            print("\nThe missile struck an innocent island...")

        else:

            print("""     
            -}===>
            """)

            time.sleep(.3)

            print("""     
            ---}===>
            """)

            time.sleep(.3)

            print("""     
            -----}===>
            """)

            time.sleep(.3)

            print("""      
                            
            -------}===>  
                    
            """)

            time.sleep(.3)

            print("""           
                            (~~~~~~~~~)
            ------------}===>(~~~~~~~~~~~~)
                            (~~ >(^) ~~)
            """)

            print("\nTHE POOR FISHIES")  


    if call == missileLaunchStrike:
        print("""     
         -}===>
        """)

        time.sleep(.3)

        print("""     
            ---}===>
        """)

        time.sleep(.3)

        print("""     
              -----}===>
        """)

        time.sleep(.3)

        print("""
                                  ___|___
                -------}===>      |     |
                                  |_____/""")
        
        time.sleep(.3)

        print("""
                                  ___|___
                  ---------}===>  |     |
                                  |_____/""")
        
        time.sleep(.3)

        print("""
                                  ___|___
                  ---------BOOOMM )     |
                                  |_____/""") 