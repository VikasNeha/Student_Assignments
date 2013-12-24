import urllib.request
web_obj = urllib.request.urlopen("https://www.google.com/finance/converter?a=100&from=USD&to=SEK")
results_str = str(web_obj.read())
results_str = results_str[results_str.index("bld"):]
results_str = results_str[results_str.index(">")+1:results_str.index(" ")]
print(results_str)
web_obj.close()