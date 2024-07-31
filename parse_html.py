from bs4 import BeautifulSoup

def parse_html(html_file):
    soup = BeautifulSoup(html_file, 'html.parser')
    target_element = soup.select_one('div.prewrap')
    with open('html_output.html', 'w') as html_output_file:
        html_output_file.write(target_element.prettify())
    macronized_text = target_element.get_text()
    return macronized_text

