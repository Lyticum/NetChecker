import urllib as url
import urllib.request as url1

def sayfa(site):
    print("Site kontrol ediciye hoş geldiniz!")
    bağlantı= url1.urlopen(site)
    print(f"Bu siteye bağlısınız; {site}")
    print(f"Bağlantı; {bağlantı.getcode()}")
    

input_site = input("Lütfen site URL'sini giriniz; ")
sayfa(input_site)
