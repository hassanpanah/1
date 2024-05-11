import highlighter

# Get the URL of the page you want to retrieve highlighted terms from
url = input("Enter the URL of the page you read before: ")

# Create a Highlighter object
highlighter = highlighter.Highlighter()

# Retrieve the highlighted terms from the page
highlighted_terms = highlighter.get_highlighted_terms(url)

# Print the list of highlighted terms
print("Highlighted terms:")
for term in highlighted_terms:
    print(term)
