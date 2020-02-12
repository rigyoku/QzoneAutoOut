import io
from urllib.request import urlopen
import cv2
import numpy

bgSrc = 'https://hy.captcha.qq.com/hycdn_1_1585311843450232320_0?aid=549000912&captype=&curenv=inner&protocol=https&clientype=2&disturblevel=&apptype=2&noheader=&color=&showtype=embed&fb=1&theme=&lang=2052&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ny4wLjM4NjUuOTAgU2FmYXJpLzUzNy4zNg==&grayscale=1&subsid=3&sess=HCSOm_0Av-7Y5gNOAJ5208QmqGzUl83iwGrt7xbza5RvWW0NZNED5RsLlOU1yvLc62ZqG2ToFkz64jnMvN_MgOWF9yirL08e1gsADbDuwyZ8X6_QFFPpx3TG8f8pNsVGsJxLMU8NP95c0NGVSwZc78t1bZlpvRVMIlDOkmpjuNVI39N8lMnXakN8b00GhofXJ74eG1bPzeQ*&fwidth=0&sid=6792115589469258588&forcestyle=undefined&wxLang=&tcScale=1&noBorder=noborder&uid=942138429&cap_cd=_ZC8iYER58Ul9lH3pyGuH0cNgHMPMUrSu2m5M0np9JfN7K1lu-gDrg**&rnd=205323&TCapIframeLoadTime=210&prehandleLoadTime=79&createIframeStart=1581412648655&rand=57618957&websig=37ba52c93bbb59cf982738b13acf321ea04ee1a1dac77bf47f841b6899fe83c5f49d0da21a78ec9ea61692097e04af4a31bcc1a89934e8682540493c711ed0ce&vsig=c01K4wOG_vnyCvdvgjv3VWFqljYqUYflQd2f6rfIijcKA9pCXil1lwkffRBaYq3oOv61kQzpLrV6ud8cRRGafgTOZN1fRzA1zZfTTd5n7zTobIVDLW7CUysatRNDG2KMmZVm84Mk12n2B4eJ-2parAwcoubUqMf3aPBwAgOIhjaBXzelWZit-jDng**&img_index=1'
blockSrc = 'https://hy.captcha.qq.com/hycdn_2_1585311843450232320_0?aid=549000912&captype=&curenv=inner&protocol=https&clientype=2&disturblevel=&apptype=2&noheader=&color=&showtype=embed&fb=1&theme=&lang=2052&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ny4wLjM4NjUuOTAgU2FmYXJpLzUzNy4zNg==&grayscale=1&subsid=4&sess=HCSOm_0Av-7Y5gNOAJ5208QmqGzUl83iwGrt7xbza5RvWW0NZNED5RsLlOU1yvLc62ZqG2ToFkz64jnMvN_MgOWF9yirL08e1gsADbDuwyZ8X6_QFFPpx3TG8f8pNsVGsJxLMU8NP95c0NGVSwZc78t1bZlpvRVMIlDOkmpjuNVI39N8lMnXakN8b00GhofXJ74eG1bPzeQ*&fwidth=0&sid=6792115589469258588&forcestyle=undefined&wxLang=&tcScale=1&noBorder=noborder&uid=942138429&cap_cd=_ZC8iYER58Ul9lH3pyGuH0cNgHMPMUrSu2m5M0np9JfN7K1lu-gDrg**&rnd=205323&TCapIframeLoadTime=210&prehandleLoadTime=79&createIframeStart=1581412648655&rand=57618957&websig=37ba52c93bbb59cf982738b13acf321ea04ee1a1dac77bf47f841b6899fe83c5f49d0da21a78ec9ea61692097e04af4a31bcc1a89934e8682540493c711ed0ce&vsig=c01K4wOG_vnyCvdvgjv3VWFqljYqUYflQd2f6rfIijcKA9pCXil1lwkffRBaYq3oOv61kQzpLrV6ud8cRRGafgTOZN1fRzA1zZfTTd5n7zTobIVDLW7CUysatRNDG2KMmZVm84Mk12n2B4eJ-2parAwcoubUqMf3aPBwAgOIhjaBXzelWZit-jDng**&img_index=2'

bgData = urlopen(bgSrc).read();
bg = cv2.imdecode(numpy.array(bytearray(bgData), dtype=numpy.uint8), -1);
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

blockData = urlopen(blockSrc).read();
block = cv2.imdecode(numpy.array(bytearray(blockData), dtype=numpy.uint8), -1);
block = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
block = block[41:95, 41:95]

diff = cv2.matchTemplate(bg, block, cv2.TM_CCOEFF_NORMED)
offset = cv2.minMaxLoc(diff)[3][0];
offset = offset - 41;
print(bg.shape[1])
print(offset * 280 / 680)