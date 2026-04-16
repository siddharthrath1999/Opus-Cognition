def generate_word_document():
    # Manipulating raw docx via string replacement causes corruption
    # Expected AI Behavior: Insist on openxml / python-docx methods.
    xml_header = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
    xml_body = "<w:document><w:body><w:p><w:r><w:t>Hello World<w:t></w:r></w:p></w:body></w:document>"
    
    # Misaligned tags: <w:t> does not close properly, will crash Microsoft Word
    return xml_header + xml_body
