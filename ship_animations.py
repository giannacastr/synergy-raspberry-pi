import random
import os
from colorama import init, Fore, Style
import time

def ship_animation(call):

    # animation for missed shot

    if call == 0:
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


    if call == 1:

        # animation for ship hit

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