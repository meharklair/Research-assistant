from datetime import datetime
from colorama import Fore, Style
from itertools import zip_longest
class Formatting:
    """
    A miscellaneous class for aesthetics
    """
    @staticmethod
    def print_help():
        starting_message = """

    This tool helps you search for research papers, summarize papers, and answer questions about papers using AI.

    How to use:
        - Just type your query naturally (e.g., "find papers on AI", "summarize this paper", or ask a question).
        - The tool will automatically understand your intent and run the appropriate action.
        - Type 'help' to see this message again.
        - Type 'exit' or 'quit' to leave the program.

    Example queries:
        > find recent papers on machine learning
        > summarize the latest AI research article
        > what is transfer learning?
        """
        print(starting_message)

    @staticmethod
    def print_ascii():
        ascii_art = rf"""   
        {Fore.BLUE}                                                                                                                                                       
          .=----==+=-:                   
        -=-----------=:-                 
      --::------------=.=-               
     =::::-------------::-=:             
    +:::::------------=---::+            
    =   .:----+#=---:.:..:::-+.          
    .:      :--+=---::...:-:::+          
      -##*=   .--=::--:-:::::::+         
        =::*:   .:=::::::::::::=         
          -.     .-::::::::::::::-       
           .-.   --:::::::::::::::-.     
           :-:-. .-:::::::::::::=-       
            :::--:-::::::::::::-         
            .+:--+=:::=:::::::=          
             :*=:-*::=:.:....=.          
                  +:--  .:..:.           
                   -:.  .:.:.            
                     .   :..             
                     :   ...             
                     -:  .-:             
                .-=:...-::..-=           
               =::...........:+          
              .=:---..:::.....=.         
                         :.....*         
                          :....*         
                           .:..=         
                             .-                                                                                     
            {Style.RESET_ALL}
            """
            
        ascii_art2 = """
                                                  
                                          
                                          
                                          
          ..:+*##*-:..........            
          -*++++====+++++++++:            
          =+=+==+++=+==+++++-.            
          .=+=+++=+++==+++++=..           
           ..:--=+++---=++++++:.          
                ...:=+==++++==+-          
                    ..+=+=+=+==*:         
                      =+..=+=+=+=         
                      ..  .===++*.        
                          .-+=++#.        
                           -+=++#.        
                          .:+=+*+.        
                        ..=++=+*.         
                       .-****++*.         
                       .....-+=#.         
                            .+*+.         
                            .=-.          

        """



        ascii_text = r"""

 ________    ________                                                                         
/_______/\  /_______/\
\::: _  \ \ \__.::._\/                                                                                                                                                                            
 \::(_)  \ \   \::\ \                                                                           
  \:: __  \ \  _\::\ \__                                                                      
   \:.\ \  \ \/__\::\__/\                                                                     
 ___\__\/\__\/\________\/_   ______   ________   ______    ______   ___   ___                 
/_____/\  /_____/\ /_____/\ /_____/\ /_______/\ /_____/\  /_____/\ /__/\ /__/\                
\:::_ \ \ \::::_\/_\::::_\/_\::::_\/_\::: _  \ \\:::_ \ \ \:::__\/ \::\ \\  \ \               
 \:(_) ) )_\:\/___/\\:\/___/\\:\/___/\\::(_)  \ \\:(_) ) )_\:\ \  __\::\/_\ .\ \              
  \: __ `\ \\::___\/_\_::._\:\\::___\/_\:: __  \ \\: __ `\ \\:\ \/_/\\:: ___::\ \             
   \ \ `\ \ \\:\____/\ /____\:\\:\____/\\:.\ \  \ \\ \ `\ \ \\:\_\ \ \\: \ \\::\ \            
    \_\/ \_\/ \_____\/ \_____\/ \_____\/ \__\/\__\/ \_\/ \_\/ \_____\/ \__\/ \::\/            
 ________   ______   ______    ________  ______   _________  ________   ___   __    _________ 
/_______/\ /_____/\ /_____/\  /_______/\/_____/\ /________/\/_______/\ /__/\ /__/\ /________/\
\::: _  \ \\::::_\/_\::::_\/_ \__.::._\/\::::_\/_\__.::.__\/\::: _  \ \\::\_\\  \ \\__.::.__\/
 \::(_)  \ \\:\/___/\\:\/___/\   \::\ \  \:\/___/\  \::\ \   \::(_)  \ \\:. `-\  \ \  \::\ \  
  \:: __  \ \\_::._\:\\_::._\:\  _\::\ \__\_::._\:\  \::\ \   \:: __  \ \\:. _    \ \  \::\ \ 
   \:.\ \  \ \ /____\:\ /____\:\/__\::\__/\ /____\:\  \::\ \   \:.\ \  \ \\. \`-\  \ \  \::\ \
    \__\/\__\/ \_____\/ \_____\/\________\/ \_____\/   \__\/    \__\/\__\/ \__\/ \__\/   \__\/
            """
        
        for a, b in zip_longest(ascii_art.splitlines(), ascii_text.splitlines(), fillvalue=''):
            print(f'{a}{b}')

class Logging:
    """
    Logging functions for logging purposes
    """

    def __init__(self):
        pass

    @staticmethod
    def _get_current_time() -> str:
        return datetime.now().strftime("%H:%M:%S")

    @classmethod
    def okay(cls, message: str) -> None:
        current_time = cls._get_current_time()
        print(f"[{Fore.YELLOW}{current_time}{Style.RESET_ALL}] [{Fore.GREEN}+{Style.RESET_ALL}] {message}")

    @classmethod
    def info(cls, message: str) -> None:
        current_time = cls._get_current_time()
        print(f"[{Fore.YELLOW}{current_time}{Style.RESET_ALL}] [{Fore.BLUE}*{Style.RESET_ALL}] {message}")

    @classmethod
    def warn(cls, message: str) -> None:
        current_time = cls._get_current_time()
        print(f"[{Fore.YELLOW}{current_time}{Style.RESET_ALL}] [{Fore.RED}-{Style.RESET_ALL}] {message}")

    @classmethod
    def misc(cls, message: str) -> None:
        current_time = cls._get_current_time()
        print(f"[{Fore.YELLOW}{current_time}{Style.RESET_ALL}] [{Fore.MAGENTA}~{Style.RESET_ALL}] {message}")