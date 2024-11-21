import inspect

def introspection_info(obj):
    attributes_list, methods_list = [], []
    for element in dir(obj):
        if '__' in element:
            methods_list.append(element)
        else:
            attributes_list.append(element)
    info_dict = {'type': type(obj).__name__, 'attributes': attributes_list, 'methods': methods_list, 'module': inspect.getmodule(introspection_info).__name__}
    return info_dict

print(introspection_info(42))