import yaml, xml.dom.minidom, sys

def expand(node, parent):
    if isinstance(node, dict):
        for (key, value) in node.iteritems():
            if key != '':
                child=dom.createElement(key)
                parent.appendChild(child)
                expand(value, child)

    elif isinstance(node, list):
        child=dom.createElement('list')
        parent.appendChild(child)
        parent=child
        for value in node:
            child=dom.createElement('member')
            parent.appendChild(child)
            expand(value, child)

    else:
        node=(node, str(node))[isinstance(node, int)]
        text=dom.createTextNode(node)
        parent.appendChild(text)

if __name__ == '__main__':
    if 2 < len(sys.argv):
        impl=xml.dom.minidom.getDOMImplementation()
        dom=impl.createDocument(None, 'top', None)
        yaml_loaded=yaml.load(file(sys.argv[1]).read())
        top=dom.documentElement

        expand(yaml_loaded, top)
        f=file(sys.argv[2], 'w')
        dom.writexml(f, '', '    ', '\n')
        f.close()
    else:
        print('Usage: python %s source.yaml target.yaml'%__file__)
