#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-
#import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Récupération des URL
# document.querySelectorAll("a").forEach(a=>{console.log(a.getAttribute("href"));})
books = {"https://www.wattpad.com/story/286727820-mariposa-t-1-t-2":
[
#"https://www.wattpad.com/1315926103-mariposa-t-1-t-2-tw",
"https://www.wattpad.com/1166539735-mariposa-t-1-t-2-prologue",
"https://www.wattpad.com/1152482766-mariposa-t-1-t-2-chapitre-1-chicago-illinois",
"https://www.wattpad.com/1166942592-mariposa-t-1-t-2-chapitre-2-secret",
"https://www.wattpad.com/1166983085-mariposa-t-1-t-2-chapitre-3-fuis",
"https://www.wattpad.com/1169415043-mariposa-t-1-t-2-chapitre-4-stella",
"https://www.wattpad.com/1169816862-mariposa-t-1-t-2-chapitre-5-un-r%C3%AAve",
"https://www.wattpad.com/1170584549-mariposa-t-1-t-2-chapitre-6-rapt",
"https://www.wattpad.com/1171082034-mariposa-t-1-t-2-chapitre-7-qui-est-ce",
"https://www.wattpad.com/1171962067-mariposa-t-1-t-2-chapitre-8-le-destin",
"https://www.wattpad.com/1173026591-mariposa-t-1-t-2-chapitre-9-elle",
"https://www.wattpad.com/1174286575-mariposa-t-1-t-2-chapitre-10-petit-papillon",
"https://www.wattpad.com/1174343292-mariposa-t-1-t-2-chapitre-11-sans-r%C3%A9ponses",
"https://www.wattpad.com/1174500412-mariposa-t-1-t-2-chapitre-12-une-seule-question",
"https://www.wattpad.com/1175827264-mariposa-t-1-t-2-chapitre-13-r%C3%A9sonner",
"https://www.wattpad.com/1175892047-mariposa-t-1-t-2-chapitre-14-entre-mes-mains",
"https://www.wattpad.com/1176799730-mariposa-t-1-t-2-chapitre-15-sa-cadence",
"https://www.wattpad.com/1177976786-mariposa-t-1-t-2-chapitre-16-avec-les-crocs",
"https://www.wattpad.com/1178066605-mariposa-t-1-t-2-chapitre-17-kill-me-mariposa",
"https://www.wattpad.com/1179303236-mariposa-t-1-t-2-chapitre-18-mourir",
"https://www.wattpad.com/1180163849-mariposa-t-1-t-2-chapitre-19-ma-tombe-%C3%A0-manhattan",
"https://www.wattpad.com/1181146571-mariposa-t-1-t-2-chapitre-20-mon-reflet-dans-le",
"https://www.wattpad.com/1181723976-mariposa-t-1-t-2-chapitre-21-matin%C3%A9e-sympathique",
"https://www.wattpad.com/1181912639-mariposa-t-1-t-2-chapitre-22-famille-king",
"https://www.wattpad.com/1183918731-mariposa-t-1-t-2-chapitre-23-cauchemars-papillon",
"https://www.wattpad.com/1184435552-mariposa-t-1-t-2-chapitre-24-je-peux-g%C3%A9rer",
"https://www.wattpad.com/1185099722-mariposa-t-1-t-2-chapitre-25-ne-t%27envoles-pas",
"https://www.wattpad.com/1186331680-mariposa-t-1-t-2-chapitre-26-paralysie",
"https://www.wattpad.com/1187496511-mariposa-t-1-t-2-chapitre-27-poumons-contre-moi",
"https://www.wattpad.com/1192068260-mariposa-t-1-t-2-chapitre-28-si-l%C3%A9g%C3%A8re",
"https://www.wattpad.com/1194666645-mariposa-t-1-t-2-chapitre-29-le-silence-est-de",
"https://www.wattpad.com/1194906911-mariposa-t-1-t-2-chapitre-30-c%C3%B4me-le-psychopathe",
"https://www.wattpad.com/1197861384-mariposa-t-1-t-2-chapitre-31-je-me-souviendrais-de",
"https://www.wattpad.com/1199242314-mariposa-t-1-t-2-chapitre-32-ce-qui-te-fais-vibrer",
"https://www.wattpad.com/1200874660-mariposa-t-1-t-2-chapitre-33-dormir-sans",
"https://www.wattpad.com/1202603180-mariposa-t-1-t-2-chapitre-34-recommence-encore",
"https://www.wattpad.com/1203173926-mariposa-t-1-t-2-chapitre-35-pourquoi-elle",
"https://www.wattpad.com/1205216149-mariposa-t-1-t-2-chapitre-36-emprise",
"https://www.wattpad.com/1205737413-mariposa-t-1-t-2-chapitre-37-dangereuse-flamme",
"https://www.wattpad.com/1207223684-mariposa-t-1-t-2-chapitre-38-chaotique-mariposa",
"https://www.wattpad.com/1209233131-mariposa-t-1-t-2-chapitre-39-die-for-you",
"https://www.wattpad.com/1210118254-mariposa-t-1-t-2-chapitre-40-papillon-entre-les",
"https://www.wattpad.com/1222397504-mariposa-t-1-t-2-chapitre-41-i-can%27t-share-you",
"https://www.wattpad.com/1223393697-mariposa-t-1-t-2-chapitre-42-explose-avec-moi",
"https://www.wattpad.com/1224762263-mariposa-t-1-t-2-chapitre-43-lavande-satin",
"https://www.wattpad.com/1233927278-mariposa-t-1-t-2-chapitre-44-love",
"https://www.wattpad.com/1234970092-mariposa-t-1-t-2-interlude",
"https://www.wattpad.com/1283502610-mariposa-t-1-t-2-t-o-m-e-i-i",
"https://www.wattpad.com/1283538035-mariposa-t-1-t-2-t-2-prologue",
"https://www.wattpad.com/1284469667-mariposa-t-1-t-2-chapitre-1-seul",
"https://www.wattpad.com/1285893677-mariposa-t-1-t-2-chapitre-2-jeu-d%27%C3%A2mes",
"https://www.wattpad.com/1286371772-mariposa-t-1-t-2-chapitre-3-plus-jamais",
"https://www.wattpad.com/1290183034-mariposa-t-1-t-2-chapitre-4-la-dose-papillon",
"https://www.wattpad.com/1291930655-mariposa-t-1-t-2-chapitre-5-la-mariposa-verde",
"https://www.wattpad.com/1314566439-mariposa-t-1-t-2-chapitre-6-mabel",
"https://www.wattpad.com/1315111951-mariposa-t-1-t-2-chapitre-7-sur-mon-c%C5%93ur",
"https://www.wattpad.com/1315328347-mariposa-t-1-t-2-chapitre-8-calendula-officinalis",
"https://www.wattpad.com/1315753894-mariposa-t-1-t-2-chapitre-9-toxines",
"https://www.wattpad.com/1319853274-mariposa-t-1-t-2-chapitre-10-promise-you-a-home",
"https://www.wattpad.com/1320036576-mariposa-t-1-t-2-chapitre-11-vivre-ou-mourir",
"https://www.wattpad.com/1320645656-mariposa-t-1-t-2-chapitre-12-devant-dieu",
"https://www.wattpad.com/1321384260-mariposa-t-1-t-2-chapitre-13-stonehead",
"https://www.wattpad.com/1323000758-mariposa-t-1-t-2-chapitre-14-jamais-plus-jamais",
"https://www.wattpad.com/1324102666-mariposa-t-1-t-2-chapitre-15-c%C5%93ur-violent",
"https://www.wattpad.com/1324389403-mariposa-t-1-t-2-chapitre-16-noir-et-lumi%C3%A8re",
"https://www.wattpad.com/1324710022-mariposa-t-1-t-2-chapitre-17-larmes-de-neige",
"https://www.wattpad.com/1324963291-mariposa-t-1-t-2-chapitre-18-devant-toi",
"https://www.wattpad.com/1325543162-mariposa-t-1-t-2-chapitre-19-sad-but-optimistic",
"https://www.wattpad.com/1326102500-mariposa-t-1-t-2-chapitre-20-c%C5%93ur-de-glace",
"https://www.wattpad.com/1338333036-mariposa-t-1-t-2-chapitre-21-faux-semblant",
"https://www.wattpad.com/1353034911-mariposa-t-1-t-2-chapitre-22-bienvenue-%C3%A0-richmond",
"https://www.wattpad.com/1353703015-mariposa-t-1-t-2-chapitre-23-faire-un",
"https://www.wattpad.com/1355020014-mariposa-t-1-t-2-chapitre-24-pierogi",
"https://www.wattpad.com/1361642526-mariposa-t-1-t-2-chapitre-25-through-music",
"https://www.wattpad.com/1368321354-mariposa-t-1-t-2-chapitre-26-bleeding-love",
"https://www.wattpad.com/1370550971-mariposa-t-1-t-2-chapitre-27-effet-papillon",
"https://www.wattpad.com/1381359678-mariposa-t-1-t-2-chapitre-28-la-fin-d%27un-chapitre",
"https://www.wattpad.com/1381359899-mariposa-t-1-t-2-chapitre-29-albane",
"https://www.wattpad.com/1382231937-mariposa-t-1-t-2-chapitre-30-rolling-in-the-deep",
"https://www.wattpad.com/1383311142-mariposa-t-1-t-2-chapitre-31-haine-et-obsession",
"https://www.wattpad.com/1384458954-mariposa-t-1-t-2-chapitre-32-1000-mots",
"https://www.wattpad.com/1387728290-mariposa-t-1-t-2-chapitre-33-zostane",
"https://www.wattpad.com/1387728410-mariposa-t-1-t-2-%C3%A9pilogue"
]
}

def downloadPageComments(url, nb, outputFile):
   driver.get(url)
   time.sleep(2)
   
   # Try to reach the end of page
   endOfPageFound = False
   driver.execute_script("window.scrollTo(0,1000000)")
   time.sleep(0.5)
   scrollY = driver.execute_script("return window.scrollY")
   
   while not(endOfPageFound):
      driver.execute_script("window.scrollTo(0,1000000)")
      time.sleep(0.5)
      newScrollY = driver.execute_script("return window.scrollY")
      print(newScrollY)
      if newScrollY == scrollY:
         endOfPageFound = True
      else:
         scrollY = newScrollY
   
   # Try to load all comments
   endOfCommentsFound = False
   try:
      zoom = driver.find_element_by_css_selector('.secondary_btn__Ae3Vl')
      zoom.click()
   except:
      print("no button")
   driver.execute_script("window.scrollTo(0,1000000)")
   time.sleep(0.5)
   scrollY = driver.execute_script("return window.scrollY")
   
   while not(endOfCommentsFound):
      try:
         zoom = driver.find_element_by_css_selector('.secondary_btn__Ae3Vl')
         zoom.click()
         time.sleep(1)
         print("Before scroll")
         print(scrollY)
         driver.execute_script("window.scrollTo(0,1000000)")
         time.sleep(0.5)
      except:
         print("no button")
      newScrollY = driver.execute_script("return window.scrollY")
      print("After scroll")
      print(newScrollY)
      if newScrollY == scrollY:
         endOfCommentsFound = True
      else:
         scrollY = newScrollY
   time.sleep(0.5)
   
   # Save all comments
   elements = driver.find_elements_by_css_selector(".comment-card-container")
   print(str(len(elements)) + " comments")
   for el in elements:
      user = el.find_element_by_css_selector("h3").get_attribute('innerText')
      comment = el.find_element_by_css_selector("pre").get_attribute('innerText')
      date = el.find_element_by_css_selector(".postedDate__xcq5D").get_attribute('innerText')
      outputFile.writelines(str(nb) + "\t" + date + "\t" + user + "\t" + comment.replace("\r\n","|`|").replace("\n","|`|").replace("\r","|`|") + "\n")


outputFile = open("comments.csv", "w", encoding="utf8")

nb = 1
for book in books:
   print(book)
   for url in books[book]:
      print("Getting comments from " + url)
      downloadPageComments(url, nb, outputFile)
      nb += 1

outputFile.close()