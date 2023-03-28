import html2text

def html_to_markdown(html_content):
    converter = html2text.HTML2Text()
    converter.ignore_links = True
    converter.ignore_images = True
    markdown_content = converter.handle(html_content)
    return markdown_content

# Example usage:
with open('filename.html', 'r') as html_file:
    html_content = html_file.read()

markdown_content = html_to_markdown(html_content)

with open('output.md', 'w') as md_file:
    md_file.write(markdown_content)
