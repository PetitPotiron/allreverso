# allreverso
[<img src="docs/python_allreverso.png" width="50" alt="logo de allreverso">](https://petitpotiron.github.io/allreverso/fr/)


[![widget du serveur discord](https://discord.com/api/guilds/800032961525317693/embed.png)](https://discord.gg/t2dxrXMKya)
[![version de allreverso](https://img.shields.io/pypi/v/allreverso.svg)](https://pypi.org/project/allreverso/)
[![versions de python supportées](https://img.shields.io/pypi/pyversions/allreverso.svg)](https://pypi.org/project/allreverso/)


A simple package to handle reverso.net services (translation, voice, dictionary etc.)

Run `pip install allreverso` to install the package.

[Click here to see the documentation](https://petitpotiron.github.io/allreverso)

[PyPI](https://pypi.org/project/allreverso/)

Example of usage :
```python
import allreverso

client = reverso.ReversoClient()
print(client.translate("en", "fr",
                       "Hello, this text has been translated by the reverso package in python."))  # a simple translation example
print(client.define("en", "boat"))  # a simple definition example
print(client.synonymize("en", "boat"))  # a simple synonym example
client.speak_to_mp3("en", "Hello !")  # a simple voice example

```
Having troubles ? Check our [discord ![discord widget](https://discord.com/api/guilds/831480772455038996/widget.png)](https://discord.gg/v4yfnjWKvy)
