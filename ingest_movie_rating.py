import os
from dotenv import load_dotenv
import gdown

# Load environment variables from .env file

load_dotenv()

# data_movie_lens.csv dataset
file_1 = os.getenv('file1_id')
url_1=f"https://drive.google.com/uc?id={file_1}"
gdown.download(url_1, "data_movie_lens.csv", quiet=False)

# item_movie_lens.csv dataset
file_2 = os.getenv('file2_id')
url_2=f"https://drive.google.com/uc?id={file_2}" 
gdown.download(url_2, "item_movie_lens.csv", quiet=False)

# user_movie_lens.csv dataset
file_3 = os.getenv('file3_id')
url_3=f"https://drive.google.com/uc?id={file_3}"
gdown.download(url_3, "user_movie_lens.csv", quiet=False)
