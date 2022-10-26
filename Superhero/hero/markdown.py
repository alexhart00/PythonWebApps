from markdown import markdown

def document_card(document):
    markdown_text = open(f'Documents/{document}.md').read()
    link = dict(href='Index', text='Doc Index')
    return dict(body=markdown(markdown_text), file=document, color='bg-primary text-light p-5', width='', link=link)


def document_data(document):
    return dict(documents=[document_card(document)])