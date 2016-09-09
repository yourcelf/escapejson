replacements = (
   # Replace forward slashes to prevent '</script>' attacks
   ('/', '\\/'),
   # Replace line separators that are invalid javascript.
   # See http://timelessrepo.com/json-isnt-a-javascript-subset/
   (u'\u2028', '\\u2028'),
   (u'\u2029', '\\u2029'),
)

def escapejson(string):
    '''
    Escape `string`, which should be syntactically valid JSON (this is not
    verified), so that it is safe for inclusion in HTML <script> environments
    and as literal javascript.
    '''
    for fro, to in replacements:
        string = string.replace(fro, to)
    return string
