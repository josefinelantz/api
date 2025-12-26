# swcvpy software development kit (SDK)

This is a python SDK to interact with the SportsWorldCentral Football API. 

## Installing swcpy 

```
pip install swcpy@git+https://github.com/josefinelantz/api#subdirectory=sdk
```

## Example usage 

This SDK implements all the endpoints in the SWC API, in addition to providing bulk downloads of the SWC fantasy data in CSV format. 

### Setting base URL for the API 

The SDK looks for a value of "SWC_API_BASE_URL" in the environment. 