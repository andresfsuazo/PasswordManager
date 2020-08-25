print(__name__)

try:
    # Trying to find module in the parent package
    from PM.PMServer import keys
except ImportError:
    print('Relative import failed')

try:
    # Trying to find module on sys.path
    import Keys
except ModuleNotFoundError:
    print('Absolute import failed')