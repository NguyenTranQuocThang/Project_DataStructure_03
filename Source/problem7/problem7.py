# The Router class will wrap the Trie and handle
from os import curdir


class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
        # Initialize the node with children as before, plus a handler

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, list_path):
        current = self.root
        for element in list_path:
            if element not in current.children:
                current.insert(element)
            current = current.children[element]
        current.handler = True

        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, list_path):

        current = self.root

        for element in list_path:
            if element not in current.children:
                return None
            current = current.children[element]
        return current.handler

        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class Router:
    def __init__(self):
        self.router = RouteTrie()
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, link):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        list_path = self.split_path(link)
        self.router.insert(list_path)

    def lookup(self, link):
        list_path = self.split_path(link)
        if len(list_path) == 0:
            return "root handler"
        if self.router.find(list_path):
            return "about handler"
        else:
            return "not found handler"
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

    def split_path(self, link):
        list_path = link.split('/')
        list_path = list(filter(None, list_path))
        return list_path
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        # A RouteTrie will store our routes and their associated handlers

        # Here are some test cases and expected outputs you can use to test your implementation

        # create the router and add a route
        # remove the 'not found handler' if you did not implement this
router = Router()
router.add_handler("/home/about")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))


router = Router()
router.add_handler("/home")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'about handler'
print(router.lookup("/home/"))  # should print 'about handler'
print(router.lookup("/home/about"))  # should print 'not about handler'
print(router.lookup("/home/about/"))  # should print 'not about handler'


router = Router()
router.add_handler("/")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not about handler'
print(router.lookup("/home/"))  # should print 'not about handler'
print(router.lookup("/home/about"))  # should print 'not about handler'
print(router.lookup("/home/about/"))  # should print 'not about handler'


router = Router()
router.add_handler("")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not about handler'
print(router.lookup("/home/"))  # should print 'not about handler'
print(router.lookup("/home/about"))  # should print 'not about handler'
print(router.lookup("/home/about/"))  # should print 'not about handler'
