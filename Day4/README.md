# Url-shortener
## Shorten Link using cutt.ly API

This is a Python function to shorten a URL using the [cutt.ly API](https://cutt.ly/cuttly-api).

### Requirements

The following libraries are required:

- `sys`
- `requests`

You can install them using the following command:
```pip install requests```

### Parameters 
- full_link (str): the full URL to be shortened.
- link_name (str): an optional name to customize the short link. If not provided, a random name will be generated.

### Return Value
This function does not return any value. It writes the shortened link and its title to a file named shorten_link_output.txt and prints the link and title to the console.

### Example

`shorten_link("https://www.example.com", "example-link")`
- This will generate a short link with the name example-link for the URL https://www.example.com and print the link and its title to the console.
- The output will also be written to the shorten_link_output.txt file.
