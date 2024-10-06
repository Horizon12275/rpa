api https://api.github.com/repos/kelaberetiv/TagUI/releases
echo `api_result`
author = api_json[0].author.login