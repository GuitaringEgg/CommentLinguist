import sys
from os.path import abspath, join, dirname
# Some path fiddling to make sure we can access the module
sys.path.append(abspath(join(abspath(dirname(__file__)), "../CommentLinguist")))

from translate import translate

bing = translate(raw_input("Enter the client id: "), raw_input("Enter the secret key"))

#bing.translate_batch_py(raw_input("Enter Python file to translate the comments of: "), raw_input("Input language = "), raw_input("Output language = "))
print "Translating retry.py..."
bing.translate_batch_py("retry.py", "en", "es")
