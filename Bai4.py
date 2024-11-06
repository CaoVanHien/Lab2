import xml.dom.minidom as minidom

if __name__ == "__main__":
    data = open('currency.xml')
    xml_file = data.read()


    dom = minidom.parseString(xml_file)
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')
    num_code_list = []
    char_code_list = []

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1 and child.tagName == 'NumCode':
                GT = child.firstChild.data.strip()
                num_code_list.append(GT)
            if child.nodeType == 1 and child.tagName == "CharCode":
                GT = child.firstChild.data.strip()
                char_code_list.append(GT)
    

    print("NumCode List :", num_code_list,'\n \n')
    print("CharCode List :", char_code_list)
