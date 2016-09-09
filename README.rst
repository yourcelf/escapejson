==============================================
escapejson function and django template filter
==============================================

`JSON is not javascript <http://timelessrepo.com/json-isnt-a-javascript-subset/>`_.
Many developers erroneously think that they can just place the output of
``json.dumps(obj)`` inside ``<script>`` tags and be good to go -- but this is
dangerously vulnerable to cross-site scripting attacks from 2 important edge
cases for how JSON differs from javscript: (1) the handling of a literal
``</script>`` within script blocks, and (2) the behavior of two pesky unicode
whitespace characters.

This very simple library provides a function ``escapejson``, and a Django
template filter of the same name.  The output of ``escapejson`` should be safe
for inclusion in HTML ``<script>`` tags, and interpretation directly as
javascript.

NOTE: this escaping is only "safe" if the input is a syntactically valid JSON
string.  The output is NOT safe if you pass it untrusted input or if your JSON
formatter produces invalid syntax.  This library does not validate the
correctness of the JSON it is fed.

Usage
=====

Example API usage (with or without Django)::

    import json
    from escapejson import escapejson

    my_obj = {'message': '</script><script>alert("oh no!")</script>'}
    my_str = json.dumps(myobj)
    my_safe_str = escapejson(my_str)

Example Django templates usage::

    {# First, add "escapejson" to INSTALLED_APPS #}
    {% load escapejson %}

    <script>
        var my_obj = {{obj_or_str|escapejson}};
    </script>

What it protects against
========================

</script> attacks
-----------------

Any string containing a literal ``</script>`` inside javascript within HTML
script tags will be interpreted by modern browsers as closing the script tag,
resulting at best in broken scripts and syntax errors, and at worst in
full-blown XSS.  By escaping all ``/`` characters as ``\/`` (a valid optional
escape in the JSON spec), this is mitigated.

U+2028 and U+2029
-----------------

Two funky unicode whitespace characters count as valid JSON, but cause syntax
errors in javascript.  This is mitigated by replacing the literal characters
with the strings ``\u2028`` and ``\u2029``.
[`reference <http://timelessrepo.com/json-isnt-a-javascript-subset/>`_]
