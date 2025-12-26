import os 
from dotenv import load_dotenv 

# load ENV-variables from .env 
load_dotenv() 

class SWConfig: 
    """Configuration class containing arguments for the SDK client. 
    Contains configuration for the base URL and progressive backoff."""

    swc_base_url: str 
    sws_backoff: bool 
    swc_backoff_max_time: int 
    swc_bulk_file_format: str 

    def __init__(
            self,
            swc_base_url: str = None, # base_url to access the API 
            backoff: bool = True,     # determines if SDK should retry the call using backoff when error occurs 
            backoff_max_time: int = 30, # the number of seconds the SDK should keep trying an API call before stopping 
            bulk_file_format: str = "csv", # set format for bulk files 
    ):
        """Constructor for configuration class.
        Executed once when the class is created. Sets the class variables from the parameters the user passes in. 
        Default values are set in this method. 

        Args:
        swc_base_url (optional): 
            The base URL to use for all the API calls. Pass this in or set in evironment variable. 
        swc_backoff:
            A boolean that determines if the SDK should keep trying an API call before stopping. 
        swc_bulk_file_format:
            If bulk files should be in csv or parquet format. 
        """

        self.swc_base_url = swc_base_url or os.getenv("SVC_API_BASE_URL")
        print(f"SVC_API_BASE_URL in SWCConfig init: {self.swc_base_url}")

        if not self.swc_base_url:
            raise ValueError("Base URL is required. Set SWC_API_BASE_URL environment variable.")
        
        self.swc_backoff = backoff 
        self.swc_backoff_max_time = backoff_max_time
        self.swc_bulk_file_format = bulk_file_format 

    def __str__(self):
        """Stringify funtion to return contents of config object for logging"""
        return f"{self.swc_base_url} {self.swc_backoff} {self.swc_backoff_max_time} {self.swc_bulk_file_format}"

