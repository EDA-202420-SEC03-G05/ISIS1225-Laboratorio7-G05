from DataStructures.Tree import bst_node as bst

def new_map():
    x={"type":"BST",
        "root":None,
        "size":0
    }
    return x

def insert_node(root, key, value):
    """
    Ingresa una pareja llave, valor. Si la llave ya existe, se reemplaza el valor. Es usada en la función put()
    Parameters:
    - root (bst_node) - La raiz del arbol
    - key (any) - La llave asociada a la pareja
    - value (any) - El valor asociado a la pareja
    Returns: El arbol con la nueva pareja
    Return type: bst_node
    """
    if root is None:
        return bst.BSTNode(key, value)
    
    if key < root.key:
        root.left = insert_node(root.left, key, value)
    elif key > root.key:
        root.right = insert_node(root.right, key, value)
    else:
        root.value = value
    
    return root

def put(my_map, key, value):
    if my_map["type"] == "BST":
        my_map["root"] = insert_node(my_map["root"], key, value)
        my_map["size"] += 1
    return my_map

def get_node(root, key):
    if root is None:
        return None
    if key < root['key']:
        return get_node(root['left'], key)
    elif key > root['key']:
        return get_node(root['right'], key)
    else:
        return root['value']


def get(my_bst, key):
    return get_node(my_bst["root"], key)


def min_node(root):
    current = root
    while current['left'] is not None:
        current = current['left']
    return current['key']

def remove_node(root, key):
    if root is None:
        return None
    
    if key < root['key']:
        root['left'] = remove_node(root['left'], key)
    elif key > root['key']:
        root['right'] = remove_node(root['right'], key)
    else:
        if root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        
        root['key'] = min_node(root['right'])
        root['right'] = remove_node(root['right'], root['key'])
    
    root['size'] = size_tree(root)
    
    return root


def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    my_bst["size"] = size_tree(my_bst["root"])
    return my_bst

def contains(my_bst,key):
    if get(my_bst,key) is not None:
        return True
    return False


def size_tree(root):
    if root is None:
        return 0
    return size_tree(root['left']) + size_tree(root['right']) + 1


def size(my_bst):
    return size_tree(my_bst["root"])

def is_empty(my_bst):
    return my_bst['root'] is None



def key_set_tree(root, key_list):

    if root is not None:
        key_set_tree(root['left'], key_list)   # Recorremos el subárbol izquierdo
        key_list.append(root['key'])           # Añadimos la clave del nodo actual
        key_set_tree(root['right'], key_list)  # Recorremos el subárbol derecho
    return key_list

def key_set(my_bst):

    elements = key_set_tree(my_bst["root"], [])
    return {"size": len(elements),"elements": elements}

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root['left'], value_list)   # Recorremos el subárbol izquierdo
        value_list.append(root['value'])           # Añadimos el valor del nodo actual
        value_set_tree(root['right'], value_list)  # Recorremos el subárbol derecho
    return value_list

def value_set(my_bst):
    elements = value_set_tree(my_bst["root"], [])
    return {"size": len(elements),"elements": elements}


def left_key_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.key

def right_key_node(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.key

def delete_left_tree(root):
    if root.left is None:
        return root.right
    root.left = delete_left_tree(root.left)
    return root

def delete_right_tree(root):
    if root.right is None:
        return root.left
    root.right = delete_right_tree(root.right)
    return root



def left_key(my_bst,key):
    return left_key_node(my_bst["root"])

def right_key(my_bst,key):
    return right_key_node(my_bst["root"])

def delete_left(my_bst):
    my_bst["root"] = delete_left_tree(my_bst["root"])
    my_bst["size"] -= 1
    return my_bst

def delete_right(my_bst):
    my_bst["root"] = delete_right_tree(my_bst["root"])
    my_bst["size"] -= 1
    return my_bst


def floor_key(root, key):
    if root is None:
        return None
    
    if key == root['key']:
        return key
    
    if key < root['key']:
        return floor_key(root['left'], key)
    
    t = floor_key(root['right'], key)
    
    if t is not None:
        return t
    
    return root['key']


def ceiling_key(root, key):
    if root is None:
        return None
    
    if key == root['key']:
        return key
    
    if key > root['key']:
        return ceiling_key(root['right'], key)
    
    t = ceiling_key(root['left'], key)
    
    if t is not None:
        return t
    
    return root['key']


def select_key(root, key):

    if root is None:
        return None

    t = size_tree(root['left'])  # Obtenemos el tamaño del subárbol izquierdo

    if t > key:
        return select_key(root['left'], key)
    elif t < key:
        return select_key(root['right'], key - t - 1)
    else:
        return root['key']
    
def rank_keys(root, key):
    if root is None:
        return 0
    
    if key < root['key']:
        return rank_keys(root['left'], key)
    elif key > root['key']:
        return 1 + size_tree(root['left']) + rank_keys(root['right'], key)
    else:
        return size_tree(root['left'])
    
    
def height_tree(root):
    if root is None:
        return -1
    return 1 + max(height_tree(root.left), height_tree(root.right))



def default_compare(key, element):
    if key == element:
        return 0
    if key < element:
        return -1
    return 1

def floor(my_bst, key):

    return floor_key(my_bst["root"], key)

def ceiling(my_bst, key):

    return ceiling_key(my_bst["root"], key)


def select(my_bst, key):
    return select_key(my_bst["root"], key)

def rank(my_bst, key):
    return rank_keys(my_bst["root"], key)

def height(my_bst):
    return height_tree(my_bst["root"])

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    if key_initial < root['key']:  
        keys_range(root['left'], key_initial, key_final, list_key)  
    if key_initial <= root['key'] and key_final >= root['key']:  
        list_key.append(root['key'])  
    if key_final > root['key']: 
        keys_range(root['right'], key_initial, key_final, list_key)
    return list_key


def keys(my_bst, key_initial, key_final):
    if my_bst["root"] is None:
        return {"size": 0,"elements": []}
    
    elements = keys_range(my_bst["root"], key_initial, key_final, [])
    
    return {"size": len(elements),"elements": elements}


def values_range(root, key_lo, key_hi, list_values):
    if root is None:
        return
    if key_lo < root['key']:  
        values_range(root['left'], key_lo, key_hi, list_values)  
    if key_lo <= root['key'] and key_hi >= root['key']:  
        list_values.append(root['value'])  
    if key_hi > root['key']:  
        values_range(root['right'], key_lo, key_hi, list_values)
    return list_values

def values(my_bst, key_initial, key_final):
    if my_bst["root"] is None:
        return {"size": 0,"elements": []}
    
    elements = values_range(my_bst["root"], key_initial, key_final, [])
    
    return {"size": len(elements),"elements": elements }


def min_key(my_bst):
    if my_bst is None or my_bst['root'] is None:
        return None
    
    current = my_bst['root']
    while current['left'] is not None:
        current = current['left']
    return current['key']

def max_key(my_bst):
    if my_bst is None or my_bst['root'] is None:
        return None
    
    current = my_bst['root']
    while current['right'] is not None:
        current = current['right']
    return current['key']

def delete_max(my_bst):
    if my_bst is None or ('root' in my_bst and my_bst['root'] is None):
        return None
    if 'root' in my_bst:
        if my_bst['root']['right'] is None:
            my_bst['root'] = my_bst['root']['left']
        else:
            my_bst['root']['right'] = delete_max(my_bst['root']['right'])
        
        my_bst['root']['size'] = 1 + (my_bst['root']['left']['size'] if my_bst['root']['left'] else 0) + (my_bst['root']['right']['size'] if my_bst['root']['right'] else 0)

    else:
        if my_bst['right'] is None:
            return my_bst['left']
        my_bst['right'] = delete_max(my_bst['right'])
        my_bst['size'] = 1 + (my_bst['left']['size'] if my_bst['left'] else 0) + (my_bst['right']['size'] if my_bst['right'] else 0)

    return my_bst

def delete_min(my_bst):
    if my_bst is None or ('root' in my_bst and my_bst['root'] is None):
        return None

    if 'root' in my_bst:
        if my_bst['root']['left'] is None:
            my_bst['root'] = my_bst['root']['right']
        else:
            my_bst['root']['left'] = delete_min(my_bst['root']['left'])

        my_bst['root']['size'] = 1 + (my_bst['root']['left']['size'] if my_bst['root']['left'] else 0) + (my_bst['root']['right']['size'] if my_bst['root']['right'] else 0)

    else:
        if my_bst['left'] is None:
            return my_bst['right']
        my_bst['left'] = delete_min(my_bst['left'])
        my_bst['size'] = 1 + (my_bst['left']['size'] if my_bst['left'] else 0) + (my_bst['right']['size'] if my_bst['right'] else 0)

    return my_bst

    
