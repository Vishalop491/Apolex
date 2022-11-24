from __future__ import annotations
from discord.ext import commands
import discord
from discord.ext import commands, tasks
from discord.commands import ( 
    slash_command,
)
import json
import requests
from discord.ui import Button, View
import humanize
from discord.ext import commands
import discord
import json
import requests
#import logging
import asyncio

import datetime
from datetime import datetime
from itertools import cycle
import contextlib
from core import Context 
from contextlib import suppress
from discord.ext.commands import Context
from discord.channel import DMChannel
import os
os.system("pip install urbandictionary")
#os.system("pip install utilities")
import aiohttp
import utilities as tragedy
#from utils.language import Language
import psutil
from urllib.parse import urlparse
#from utils import checks
from psutil import Process, virtual_memory
from typing import Union, Optional
from ext.paginator import PaginatorSession
import random
#from cogs.utils.checks import embed_perms
import asyncio
import time
#from utils.language import Language
import aiohttp
import urbandictionary as ud
import datetime
from .utils.config import *
import math
from afks import afks
from discord.utils import get
import numpy as np
import re

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}


class ButtonView(discord.ui.View):
  def __init__(self):
    super().__init__()
  
    button = discord.ui.Button(label='Claim', style=discord.enums.ButtonStyle.green)
  
    self.add_item(button)

kisses = ['https://cdn.nekos.life/kiss/kiss_138.gif', 'https://cdn.nekos.life/kiss/kiss_106.gif', 'https://cdn.nekos.life/kiss/kiss_128.gif', 'https://cdn.nekos.life/kiss/kiss_139.gif', 'https://cdn.nekos.life/kiss/kiss_061.gif']
loves = ['']
cuteim = ['https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218764136337469/868354099043794944.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218760332083200/856799753815326760.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://i.redd.it/o1g3su199hp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/g09y1v5iugp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/hai3526j6hp71.jpg', 'https://i.redd.it/91p1yme33ip71.jpg', 'https://i.redd.it/6lvfdsdp6hp71.jpg', 'https://i.redd.it/5arz0zh57hp71.jpg', 'https://i.redd.it/nxukbymljjp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/w544woii9gp71.jpg', 'https://i.redd.it/6bqrmkzpjgp71.jpg']
pfps = ['https://cdn.discordapp.com/attachments/608711473652563968/1018307916710817842/22EE8237-C6D8-4BDC-8366-596C4D6ED487.gif', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121440714817596/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018051616756219916/5dc823c5bb21cdc63dac7dd86ec93d2f.jpg', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191077506396170/a_fe6fbe3cec2fccbff3c71ccb6d0c9f9a.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019186587180990514/a_4fbe6403d85f03bcd428ac52a04b1731.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018152608860475462/image5.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018152606893346816/Gif6.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151757743923341/a_af347fce39d2a0640e672ffbad797a7a.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151756221394944/a_62550197c4ec87e91770a22dd4f45edb-1.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151755273474110/a_67d61390265cb7294137ab700b327755.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151433671032892/a_44dcbf79100c201d91390c78e23fe39e.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151432437899264/a_9e465caa99b2c136ecc6c98a8185c86f.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151431276081202/a_6ea343b4bf2373d38adbc855877754de.gif', 'https://cdn.discordapp.com/attachments/608711474952798221/1018984869424013333/ugur_askimin_ppsi.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018949984843997214/e1240bba6622954599804b94eeea22b0.jpg', 'https://cdn.discordapp.com/attachments/608711473652563968/1019152927220301875/ba90d567d37ae57d41c10ece156e2111.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018636127814570064/9de66e99de86f66cbe3d479ef6756e9b.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018309211983192184/147367F7-B146-4623-89D7-5E7FD3E633DA.gif', 'https://cdn.discordapp.com/attachments/768864495522283560/1018984139946459196/IMG_20220912_233247.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1018983026589450270/2.png', 'https://cdn.discordapp.com/attachments/768864495522283560/1018970085173497946/750f5e44205acea8ed30397cae020fa9.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1018955729496969317/a_85480d503d1c0bbe448742f4a2cd83a9.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019337978679668786/a_90a2caf6bd7be576a9ba3b4e4ba81810.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019336375293706392/menace-santana-menace-santana-gif.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019336312739856464/menace-santana-booskap.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019336014503874630/menace-santana.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019331930384248863/96ebadd862d6eeb5817c28b3472e2dc4.png', 'https://cdn.discordapp.com/attachments/768864495522283560/1019357643141292042/b.gif', 'https://cdn.discordapp.com/attachments/768864495522283560/1019341567066128435/013c579c700043c96583f99a0775ad6b.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1019328501154844733/pp_13.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1019311556800020500/a0133a1991742ed8e142af3f0c072563.png', 'https://cdn.discordapp.com/attachments/768864495522283560/1019258155298992148/a_5eca60140eccaeec69f2662cbc600400.gif', 'https://cdn.discordapp.com/attachments/768864495522283560/1019726853386272869/edfd38527129a09a90767ae23205ea73.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1019686929572315166/c62590c1756680060e7c38011cd704b5.jpg', 'https://cdn.discordapp.com/attachments/768864495522283560/1019686282747719750/a_c2178733158e5e80a0ba80b10d53501a.gif']
boyspng = ['https://cdn.discordapp.com/attachments/608711478496854019/1018153780786774097/images_24.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1018153202975244379/98f0d329ea4452cbc51d45cde2601da2.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1018122035316150342/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121781036466226/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121729211629688/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121698165395566/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121684768788542/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121647074586654/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121647074586654/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121638778241084/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121620247814144/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121602254245908/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121572017508402/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121552568516652/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121536525324288/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121463422787625/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018121448700772382/unknown.png', 'https://cdn.discordapp.com/attachments/608711478496854019/1018051616756219916/5dc823c5bb21cdc63dac7dd86ec93d2f.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1018051616550703124/55f724042e6c9a8cffdf896a75835adf.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1018051616328396810/55981e6682c262aea523fcdada48e07d.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1019502062255484938/fc35beb42bd3d58546765fcbb37e9675.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1019502061802504192/aa623fb85df127a7d0788adb7afad424.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1019501988410572821/9879d6ae061333c7c3345ef01925a610.jpg', 'https://cdn.discordapp.com/attachments/608711478496854019/1019501987877896232/15aeb18b8eb8c568ae465fc79d193de7.jpg']
boysgif = ['https://cdn.discordapp.com/attachments/608711476219478045/1018151755273474110/a_67d61390265cb7294137ab700b327755.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1018151757743923341/a_af347fce39d2a0640e672ffbad797a7a.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019186587180990514/a_4fbe6403d85f03bcd428ac52a04b1731.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019190886602641438/a_440717d1a0682299b382721985e3ab44.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019190951064907847/a_580331609d1dbae6f8a924a5ccd1bc1a.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191001824366592/a_9216e2285cf4662ec0278926521258e9.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191048423100456/a_5629581e37281c6098d325673f40a75d.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191077506396170/a_fe6fbe3cec2fccbff3c71ccb6d0c9f9a.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191111085998110/a_81aa4b9a7bacd5d3937b7273be9ffbcd.gif', 'https://cdn.discordapp.com/attachments/608711476219478045/1019191143545704528/a_5bc7210b892a6534e8a7c6a5b9a0a0d8.gif']
girlspng = ['https://cdn.discordapp.com/attachments/608711474952798221/1018949918427201628/9345e3b76b5b94b721b76139761717fd.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018949978225397870/3e2efb2a9b7eb1d50acc80c68e64ae5c.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018949984843997214/e1240bba6622954599804b94eeea22b0.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018950006180425888/eac2545c5b7ca1bbad397dbcac43d028.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018950018184519751/9ebe939f3206417bbb4fe213d562df76.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1018956823283367957/59a2920daca0e3ae08177c04dbebfa55.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019006065653858404/e517461d37748604040875e98ce01672.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019006067201556640/1a9c10217ec2dc1dbeb181990b48feaa.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019006227210059789/7bad07723979d27368b992ff26454e4f.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019006227210059789/7bad07723979d27368b992ff26454e4f.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019025824785113180/bbdca2a3f44cf08cf6b861e5110ddece.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019124254865887293/69a74536ca13732c665ca30be1d52c34.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019124287711498290/6283ad38d48567fdead26f0f9ee196f6.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019129050956042290/112e7c6c55f07c8f9b00d57827814bbd.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019171107259023400/FWfy12hWYAIvYvr.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019183142785007688/f146217a5975656d318f55a048c3d5be.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019411261127135332/48456c2b6d46704eac62b74664f6adc3.webp', 'https://cdn.discordapp.com/attachments/608711474952798221/1019411260628021248/f33b9743d7a51227a163b7d9f9761c2b.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019398015330558012/817d8631e104efe01fc065ab287f7f23.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019342233096433736/89ffa9f53a6ed48a47656c8024fe0ae6.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019342220433817760/907b261b7e4a723fc205556c1e6feafe.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019853188532289546/IMG_20220831_151223.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019853120697815096/IMG_9719.png', 'https://cdn.discordapp.com/attachments/608711474952798221/1019853073620930580/c1a45258e1af98f6677f7b53b7687f5e.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852824110182420/bdaffd216677d77faa74998bb96cb7ab.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852773803696159/unknown-9.png', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852761241755698/unknown-6_1.png', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852730916937788/4177d4499bd998d10a2b65c5acfec0a1.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852715184107540/3f1a8f1db321e3c5aa95d59ffe4a6942.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852686012715058/b436ab48c401575c1ee12e301eadae61.jpg', 'https://cdn.discordapp.com/attachments/608711474952798221/1019852675237543946/8bae29fd38826f8045986a902de54add.jpg']
girlsgif = ['https://cdn.discordapp.com/attachments/608711473652563968/1018307916710817842/22EE8237-C6D8-4BDC-8366-596C4D6ED487.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018547736884293762/o.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018637183978053672/a_b9d30a968ff1829b0dc347b5c9231c3e.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018637429634257027/mavi_gif_25.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1018637548886691850/IMG_6542.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019152978474717194/3667bfc33f7f271a59b4ae8ddba5ad61.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019153096804421632/0ba601f55a0bb68a17b5e3ad024b4d1f.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019153145319931944/7c68f7e7ccf6239e3f7aa9c9b9522499.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019153228740427796/2a407ae5981aa0f9a94da00045db00c0.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181736204193802/1DFBB8CC-9783-42DB-BE8B-8C35027748A7.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181736678133800/a_f07baf7e3c051e0af90bba08d6c0f574.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019182016568234034/hit_gif_14.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019182016220114944/gif_3_1-1.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181740473974856/rererr.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181740473974856/rererr.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181739651899392/Man_PP_Gif_9.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019181738871754872/image0_17.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019324790747705395/a_5cf769c363a107c4f376484c0323a29b.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019299528668626954/a_f84900a162b4f54fc9bb6756251c80ea.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019299494321475594/a_c7fe0ca9b65247fc7ea4c6a5217a2393.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019299438184910948/a_70e031ccba3e1a91cb3da03c2183e497.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019603950049165343/edc6cbe81fd98982098de93a9253f42d.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019598841407885343/6.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019598840149594313/Rylie.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019598837926613032/2.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019581044804026388/a_cc0d2ae8230ee576c6e330e7f84ef3bb.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019603952561553448/9cc273b9196784a1b2d50eefd21c02c3.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019603951911456848/bbc721e2c8e48d79cd59da6824b1f861.gif', 'https://cdn.discordapp.com/attachments/608711473652563968/1019603951559127111/7502e1ed0b08ff07e6c393e45575e51c.gif']
couplespng = ['https://cdn.discordapp.com/attachments/608711481969868811/1019199430353764412/20220913_125743.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018526535881326633/unknown.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1018414869881557032/c46790afdfa2d8fc21c22368a0261307.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018414869583773776/adcbdda4b721271e9dc01465415bd160.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018414868598112369/7ffbac1b3919b476524f349820e90a39.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018414868262572072/ac2721a2fddb53766bfd3fa0d363a1cc.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018414867910230016/a52d5c65ad6640b0cd15e668d0d4af3c.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291162374737971/f3b6a974fcd6ea684b7ff85ec69a3707.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291162156630036/0771d7b1728c11414e3b940bb7d3d792.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291161904984124/af53f31728b2a2647714fac478bf3a70.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291161162592286/36f4e7410423a909befba4541acf7f5c.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291160881569802/4a7b22f5797eb44ada5dc5141e6622f6.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018291160151756800/52e07587c6e4d27fe5ababff7bedca54.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018211053580062820/unknown.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1018211052867043408/unknown.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1018211052443406366/unknown.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1018137854972538991/1662813354402.gif', 'https://cdn.discordapp.com/attachments/608711481969868811/1018137854569889833/1662813354388.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018137854272086056/1662813354381.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1018137854028808212/1662813354372.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1018052114972409957/89b41f16ebf70bf548c8031b476fb191.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019330043454951554/c441a6db77aa8bb4969285b28e505ee6.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019330041009684601/0565c8ce1ff527cd13fc377d0a258bbc.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739424046727268/d69a75f10c2c99b9be391882eda4b97b.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739423820230738/e04e4136c895fb11d9bd06efd2be767d.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739423576948867/e2c15399ae880a8150470f80753f86b3.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739423346278501/b4848f597885c8d51f0a0477df681844.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739423044284546/7f5414eb69d0aa08efdbe6469a3461f2.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019739422520000573/a709ba6f4b0049f7e1d6f9f9013e8753.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676743713435648/SmartSelect_-.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676743449182259/SmartSelect_-_Discord.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676743205933066/SmartSelect_-_Discord.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676742920704020/SmartSelect_-_Discord.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676742622912572/SmartSelect_-_Discord.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019676742379655178/SmartSelect_-_Discord.png', 'https://cdn.discordapp.com/attachments/608711481969868811/1019675515688325191/c3edeaa85140a5ac21469563d0d4afd1.jpg', 'https://cdn.discordapp.com/attachments/608711481969868811/1019675515487014952/bff7bc9e26fa1122c4234bdbd0499415.jpg',  ]
couplesgif = ['https://cdn.discordapp.com/attachments/608711480346542102/1017580583469207663/hit_gif_6.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1018571269093990410/Couple_PP_Gif_68.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1017822994090950706/a_30ff8b1ad24c4d340061293721bd39e7.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1017822775446097960/a_6d874dde08bb02e8b14156c0e71595bf.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1017822458285396048/7380DF2C-CF6F-476A-A757-434CA48A3868.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1019294573970870303/4a2da082cf8d7339c5d28efea3bf0ae0.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1019582919003607100/739e167748e257144756217cf930bad1.gif', 'https://cdn.discordapp.com/attachments/608711480346542102/1019655115457704016/a_30ff8b1ad24c4d340061293721bd39e7.gif']
animepng = ['https://cdn.discordapp.com/attachments/608711487325995008/1018650218113286195/IMG_1813.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018289296047870062/ab85225a3657fd369d1dee20d036e019.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018289294189805648/00dc090b2e90aea174f5fad47d90648f.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018159501930659860/6b23aaa52d04bc4805ea1eb9b5b5ee9d.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018159112174960722/IMG-20211219-WA0018.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158867374419968/fae0bc26b3c5e337a5152eefe172b04c.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158866602676305/IMG_4036.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158866019667988/fedf2e14a5e85cc10a31b6115f1f6dec.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158865579253861/images_4.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158795844755476/ece2f63fe78b11075e1c846efaa1f661.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158795572133969/crop.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158722490568714/c5ccfb47b7378e295a4d763dca99b844.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158721697845399/Avatar_24.png', 'https://cdn.discordapp.com/attachments/608711487325995008/1018158721442001017/Avatar_26.png', 'https://cdn.discordapp.com/attachments/608711487325995008/1019328930345394196/Screenshot_20220820_223448.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1019328053618409602/912bb4e363bce997239acb16241a8cbc.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1019326263552385024/1a08260fec87bbf580594edba7ff5f90.jpg', 'https://cdn.discordapp.com/attachments/608711487325995008/1019612827562029087/3590e741680dfc2430828aa1b3e1b9ad.jpg', 'https://cdn.discordapp.com/attachments/608711485849337856/1019662778497236992/unknown.png', ]
animegif = ['https://cdn.discordapp.com/attachments/608711485849337856/1018263019224051722/a_874eeb773b56296044cbd2ca06312925.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018263021358948417/a_6d0b6cfa566d67b5e386cd9effd9bbf0.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018263027105153054/a_bc8397a09527ebce4029151d0bf212a0.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018263031655972864/a_c87b37c697db3b6ea68021cff251d6f8.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018263041781014599/a_cfb53c1d169b0565e912a4167b78ecf5.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018309682848354404/d4b22bf78ff3c0783b7cd27da14247a7.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018476312245043220/a_50cdf5f3f6bd6470c90edbbc8ff44983.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018855756956717127/1464199626-f0f25477aefb1699b983a5a460c2b12a.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018513399036002314/68809b2508330d3eb74c354fde075270.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018513397131784202/3d6eeea19b1ca264de148652480d8cd6.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1018491398158307438/yoriichi.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1019369714692149288/0e5465cb74798e4c9105d3b954e6c23f.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1019340426563559444/6a2330e2ed77ec9df2075b222e5aa87f.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1019268454219534416/unknown.png', 'https://cdn.discordapp.com/attachments/608711485849337856/1019589246757117982/OldDiratex.gif', 'https://cdn.discordapp.com/attachments/608711485849337856/1019458139025850478/69d4941f7fcc091c66b596e336e7b39e.gif']
banners = ['https://cdn.discordapp.com/attachments/857714045251878972/1018592538124353548/cd0a0d4d16c35195cf26ace01a851102.gif', 'https://cdn.discordapp.com/attachments/857714065710776320/1019245541374308412/images_6.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1018919376424030429/bb0402088285fbf46d0b83c67b258f11.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1018919376143003678/e3d279fe5494844260e4e2fdf072c14d.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1018748387878785094/f853e9172f088d5ffa135ebab82db238.png', 'https://cdn.discordapp.com/attachments/857714065710776320/1018748387404808222/16453dbb8705d1c8bbf8318f8aa22d73.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019331744350076928/18b66c364182a6e2f31165658013a483.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019309957398667325/376415e614690f84e92b6c1709ddfcea.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019306462478078022/66b1ac8d481fd2f0ca6d8a13cc719dd9.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019305603392356443/65ab7531f98ab43cfdb69d7a0f0ff7bb.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019302199584632873/326821a3ff9fe82dc04f7a2fb40ac34f.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019302188494884924/0bf4e7de34095cc058de8c1557d1d6e2.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301900052615268/5753814cceed2b09315b75920df7125f.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301880037392494/7ed5f4c66f8e64e55ea5ecba83ec1a25.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301874391863316/6ccbfa66ea4a8a186345df6deebd99b5.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301868834398319/d0a456f5cb808b972d1bc4369f1e5daa.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301864187121714/c4a716a12a0e77da8c6d53b3d6e9f403.jpg', 'https://cdn.discordapp.com/attachments/857714065710776320/1019301842439643256/b231ee360c213b76286362eb83ff410c.jpg', 'https://cdn.discordapp.com/attachments/857714045251878972/1019312310474510358/Anka_Code_Girl_Banner_2.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019302079405232218/7c750b26d3d563f1b1affba930c91d4b.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019302076859289659/6cca2105bc742f38dfaa713a3f4276bf.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019302003123441744/950b2c0d071d0ebddac74b1c56cd9913.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019301995418484796/c6242842fe5ee3d67d3b1839dfb0c31e.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019729036190167090/d80eb3916a578456d5d8114a58c84e7b.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019685305990795398/a_efa044c29baf083b2fd19c6c79b36850.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019660928272310283/unknown.png', 'https://cdn.discordapp.com/attachments/857714045251878972/1019518362285506611/original.gif', 'https://cdn.discordapp.com/attachments/857714045251878972/1019503558078500874/d7d95c534c9fa8cb16a5b1270cf6ad33.gif', 'https://cdn.discordapp.com/attachments/768864615676903466/1019727499845959761/a_2386c681f1aea4c4ce5b506c90073613.gif', 'https://cdn.discordapp.com/attachments/768864495522283560/1019712202418171914/cachedImage.png', 'https://cdn.discordapp.com/attachments/768864495522283560/1019699791908839445/unknown.png', 'https://cdn.discordapp.com/attachments/768864495522283560/1019697848842993815/488b7266a37efcc9aebea279f3496dde.png']
slaps = ['https://cdn.weeb.sh/images/B1fnQyKDW.gif', 'https://cdn.weeb.sh/images/ByTR7kFwW.gif', 'https://cdn.weeb.sh/images/HyV5mJtDb.gif', 'https://cdn.weeb.sh/images/SkNimyKvZ.gif', 'https://cdn.weeb.sh/images/HkK2mkYPZ.gif', 'https://cdn.weeb.sh/images/SkSCyl5yz.gif', 'https://cdn.weeb.sh/images/SJx7M0Ft-.gif']
pats = ['https://cdn.nekos.life/pat/pat_035.gif', 'https://cdn.nekos.life/pat/pat_074.gif', 'https://cdn.nekos.life/pat/pat_028.gif', 'https://cdn.nekos.life/pat/pat_022.gif']
jokes = ['']
cats = ['']
password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
advices = ['Respect your elders', 'Speak always truth', 'be honest', 'Think About your future.', 'Think positive.', 'Work hard not going for smart work.', 'Always remember your culture.', 'Trust on god.', 'Never give up.', 'be cool be calm', 'Listen carefully.', 'Remember Your responseblity.', 'Never forget your past.']
margya = ['']
boreds = ['']
gayr = ['1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '68%', '69%', '70%', '71%', '72%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%','100%']
quacks = ['']
carry = ['I\'d slap you, but that will be animal abuse.', 'You must have born on a highway cos\' that\'s where most accidents happen.', 'I would roast you but momma says i\'m ain\'t allowed to burn trash.', 'English maybe I don\'t speak idiot.', 'If I wanted a bitch i would buy a dog.', 'Boys only bully girls If they fancy them.', 'Oh sorry was i supposed to be offnded?', 'Maybe if you ate some of your makeup , You would on pretty the inside.', 'I could argue back but i would be in the wrong too.', 'Go make a hate page if you don\'t like me.', 'If your name is not google stop , acting like you know everything.', 'If you ran like your mouth , you would be in good shape.']
battles = ['']
typeracer = ['Happiness is the reward we get for living to the highest right we know.', 'Babur was the first Mughal emperor in india.', 'Nobody followed up on that email.', 'Gopal pays no attention on his health.', 'Mikesh is unable to follow instructions.', 'Shall we go on a Goa trip?']
dances = ['']
cuddles = ['']
koalas = ['']
pandas = ['']
tickles = ['']
ages = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
truths = ["Are you a hard-working student?",
"Are you into any sports?",
"Are you scared of any animals?",
"Are you scared of dying? Why?",
"Are you scared of ghosts?",
"Are you still a virgin?",
"Can you lick your elbow?",
"Can you see yourself being married to the creepiest kid a your school someday?",
"Can you speak a different language?",
"Can you touch your tongue to your nose?",
"Can you use a pogo stick?",
"Could you go a week without junk food?",
"Could you go two months without talking to your friends?",
"Describe the weirdest dream you've ever had?",
"Describe the weirdest dream you’ve ever had?",
"Describe your most recent dream that you recall.",
"Describe your most recent romantic encounter.",
"Describe your worst kiss ever.",
"Do you believe in love at all?",
"Do you believe in love at first sight?",
"Do you ever talk to yourself in the mirror?",
"Do you have a hidden talent? What is it?",
"Do you have a job? If so, what is your favourite thing about it?",
"Do you have an imaginary friend?",
"Do you have any phobias?",
"Do you have any unusual talents?",
"Do you know how to cook?",
"Do you know how to dance?",
"Do you like doing chores?",
"Do you like to exercise?",
"Do you message people during your classes?",
"Do you prefer apple or android?",
"Do you sing in the shower? What song did you sing the last time?",
"Do you think you will marry your bf/gf? If not, why not?",
"Explain to the person you like least in this group why you like them the least.",
"Have you been in any fights while in school?",
"Have you ever been kissed yet? If so, who was your best kiss?",
"Have you ever bitten a toenail?",
"Have you ever blamed a fart on an animal?",
"Have you ever blamed something that you have done on one of your siblings?",
"Have you ever cheated on a test?",
"Have you ever cheated or been cheated on?",
"Have you ever climbed a tree?",
"Have you ever crapped your pants since you were a child?",
"Have you ever eaten food that you've dropped on the ground? If so, how long was it on the ground?",
"Have you ever fallen asleep during a class?",
"Have you ever had a crush on a teacher?",
"Have you ever had a crush on someone that your best friend has dated?",
"Have you ever had someone write an assignment or a work for you?",
"Have you ever kissed an animal?",
"Have you ever let someone take the blame for something you did?",
"Have you ever lied to your best friend?",
"Have you ever lied to your parents about if you were in classes or not?",
"Have you ever lied to your parents about what you were doing after school?",
"Have you ever peed in a pool?",
"Have you ever picked your nose in public?",
"Have you ever posted something on the internet/social media that you regret?",
"Have you ever pulled a prank on one of your teachers?",
"Have you ever received a love letter?",
"Have you ever ridden the bus without paying the fare?",
"Have you ever stolen something of value worth more than $10?",
"Have you ever stolen something?",
"Have you ever taken money from your roommate?",
"Have you ever taken money that didn't belong to you?",
"Have you ever thrown a party at your house?",
"Have you ever told a lie during a game of Truth or Dare? What was it and why?",
"Have you ever told one of your best friend's secrets, even if you said you wouldn't?",
"Have you ever used someone else's password?",
"Have you ever watched an adult film without your parents knowing?",
"Have you ever worn the same clothes for more than three days?",
"How do you feel about end pieces of a loaf of bread?",
"How do you feel about social media?",
"How far would you go to land the guy or girl of your dreams?",
"How many boyfriends (or girlfriends) have you had?",
"How many days could you go without your partner?",
"How many kids would you like to have?",
"How many siblings do you have?",
"How many times have you skipped class for no reason?",
"How old were you when your parents sat you down for 'the talk' and what did they say (or not say) about 'the birds and the bees'?",
"How soon did you realize that you were in love with your partner?",
"How soon did/do you want start a family?",
"How was your first kiss?",
"If there was no such thing as money, what would you do with your life?",
"If you could be a superhero; what would your power be?",
"If you could be any animal, which one would you be?",
"If you could be any dinosaur; which would it be?",
"If you could be any super villain; who would you be?",
"If you could change one thing on your body, what would it be?",
"If you could dye your hair any colour, what colour would you pick?",
"If you could erase one past experience, what would it be?",
"If you could go anywhere in the world, where would you go?",
"If you could make one wish right this second, what would it be?",
"If you could only hear one song for the rest of your life, what would it be?",
"If you could own your own business one day, what would it be?",
"If you could own your own business one day; what would it be?",
"If you could switch lives with any celebrity for a day, who would it be?",
"If you could take away one bad thing in the world, what would it be?",
"If you could, what would you change about your life?",
"If you had never met your partner, where do you think you would be?",
"If you had the choice to live on your own right now, would you do it?",
"If you have ever cheated, why did you do it?",
"If you suddenly had a million dollars; what would you do with all of your money?",
"If you were a billionaire, what would you spend your time doing?",
"If you were rescuing everyone here from a burning building, but you had to leave one behind, who would it be?",
"If you were to be stuck on a deserted island, which friend would you want with you?",
"If you were to be trapped on an island for 3 days, what would you take with you?"]
dares = ["Act like a monkey and record a video of it.",
"Act like you do not understand human language until your next turn (come up with your own language).",
"Act like your favourite Disney character for the rest of the game.",
"Close your eyes and send a blind text to a random person.",
"Compose a poem on the spot based on something the group comes up with.",
"Everything you say for the next 5 minutes has to rhyme.",
"Everything you say for the next 5 minutes must not contain the words: 'but', 'a', 'the', 'or'",
"Make a freestyle rap song about each person in the group",
"Make a poem using the words 'orange' and 'moose'.",
"Make a poem using the words 'pineapple' and 'apple'.",
"Make a poem using the words 'goose' and 'peanuts'.",
"Make up a poem about the colour blue.",
"Make up a story about a random person in the group.",
"Post 'I love English!' on a social media.",
"Record a video of you dancing, but without music.",
"Record a video of you playing the air drums to a song of your choice.",
"Record a video of you playing the air guitar to a song of your choice.",
"Record an impression of your favourite celebrity.",
"Record an impression of your favourite animal.",
"Record your best evil laugh; as loud as you can.",
"Record your best president impression.",
"Record yourself saying the alphabet backwards.",
"Record yourself singing 'Twinkle Twinkle, Little Star' while beat boxing.",
"Record yourself singing the alphabet without moving your mouth.",
"Record yourself talking about your favourite food in a russian accent.",
"Say 'ya heard meh' after everything you say for the next 5 minutes.",
"Say 'you know what am sayin' after everything you say for the next 5 minutes.",
"Text someone asking them if they believe in aliens, send a screenshot of the conversation.",
"Send an email to one of your teachers, telling them about how your day is going and take a screenshot.",
"Send an unsolicited text message to one of your friends, telling them about how your day is going and take a screenshot.",
"Send the last photo you took with your phone camera.",
"Send the last screenshot you took on your phone.",
"Send the most embarrassing photo on your phone.",
"Send the oldest selfie on your phone.",
"Send a screenshot of your most recent google search history.",
"Send a selfie of you making a funny face.",
"Set your phone language to Chinese for the next 10 minutes.",
"Show the last three people you texted and what the messages said.",
"Text your crush and tell them how much you like them.",
"Use the letters of the name of another player to describe them (ex. SAM : S = Silly ; A = Attractive ; M = Merry)",
"Yell out the first word that comes to your mind, and record it."]
shaadi = ['']
cries = ['']
feeds = ['']
khush = ['']
sharam = ['']
chases = ['']
confuse = ['']
laughes = ['']
cheers = ['']
hugs = ['']
EIGHT_BALL_ANSWERS = [
            "Yeah", "Yes", "Ofcourse", "Ofc", "Ah Yes", "I see in the Prophecy: TRUE!"
            "Nah", "No", 'Nope', 'Never', "I don't think so",
            "idk", "Maybe", "ig", "I'm bored", "You're annoying"
        ]
birthdayfile = './data/databases/bdays.txt'

def sub(self, x: float, y: float):
  return x - y

def add(self, x: float, y: float):
  return x + y

def div(self, x: float, y: float):
  return x / y


def sqrt(self, x: float):
  return math.sqrt(x)

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

def advantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    highRoll = max(a)
    ind = np.argmax(a)
    highRollMath = b[ind]
    return str(highRoll), highRollMath

def disadvantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    lowRoll = min(a)
    ind = np.argmin(a)
    lowRollMath = b[ind]
    return str(lowRoll), lowRollMath


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title="Here is a meme for you!", color = 0x2f3136, timestamp=ctx.message.created_at)
        embed.set_footer(text="Requested by {}".format(ctx.author.name))

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=h ot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
              

  #@commands.has_permissions(ban_members=True)


   #@commands.has_permissions(ban_members=True)
    @commands.command(aliases=["ub", "massunban"], description="unbanall")
    @commands.has_permissions(ban_members=True)

    async def unbanall(self, ctx):
      button = Button(label="Confirm", style=discord.ButtonStyle.green)
      #button1 = Button(label="Quite", style=discord.ButtonStyle.red)
      async def button_callback(interaction: discord.Interaction):
        a = 0
        if interaction.user == ctx.author:
          if interaction.guild.me.guild_permissions.ban_members:
            await interaction.response.edit_message(content=f"Unbanning all banned members... it will take sometime", embed=None, view=None)
            async for idk in interaction.guild.bans(limit=None):
              await interaction.guild.unban(user=idk.user, reason="With Reason UNBANALL By {}".format(ctx.author))
              a += 1

            
            await interaction.channel.send(content=f"Successfully unbanned all banned members, Total {a} banned members before")
          else:
            await interaction.response.edit_message(content="I dont have ban members permission", embed=None, view=None)
        else:
          await interaction.response.send_message("Dumb ?", embed=None, view=None, ephemeral=True)
      async def button1_callback(interaction: discord.Interaction):
        if interaction.user == ctx.author:
          await interaction.response.edit_message(content="Command cancelled", embed=None, view=None)
        else:
          await interaction.response.send_message("Dumb ?", embed=None, view=None, ephemeral=True)
   # if ctx.guild.me.guild_permissions.ban_members:
      embed = discord.Embed(title='Apolex',
                          color=0x2f3136,
                          description=f'**So, you want me to unbanall all banned members?**\n\n`Note - All credits have been already given you can check it by using !credits`')
      view = View()
      button.callback = button_callback
      #button1.callback = button1_callback
      view.add_item(button)
     # view.add_item(button1)
      await ctx.reply(embed=embed, view=view, mention_author=False)

    



    @commands.command()
    async def sync(self, ctx: Context):
      await ctx.reply("Syncing...", mention_author=False)
      with open('config.json', 'r') as f:
        data = json.load(f)
        for op in data["guilds"]:
          g = self.bot.get_guild(int(op))
          if not g:
            data["guilds"].pop(str(op))
            with open('config.json', 'w') as f:
              json.dump(data, f, indent=4)
          

    @commands.command()
    async def reverse(self, ctx, *, text):
        reversed = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send("🔄 %s" % (reversed))


        
    @commands.command()
    async def github(self, ctx, *, search_query):
        json = requests.get(
            f"https://api.github.com/search/repositories?q={search_query}"
        ).json()

        if json["total_count"] == 0:
            await ctx.send("No matching repositories found")
        else:
            await ctx.send(
                f"First result for '{search_query}':\n{json['items'][0]['html_url']}")
          
  #  @commands.command(name="badges", help="Check what premium badges a user have.", aliases=["badge"])
#  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
#@commands.guild_only()
 # async def _badges2(self, ctx: Context, user: Optional[discord.User] = None):
  #  mem = user or ctx.author
  #  badges = getbadges(mem.id)
#if badges == []:
    #  msg = f"<:error_ok:946729104126922802> | {mem} Have No Bot Badges For Now"
     # await ctx.reply(msg, mention_author=False)
  #  else:
    #  embed = discord.Embed(title="Badges", description="Badge(s) of {}\n\n".format(mem), color=discord.Colour(0x2f3136))
     # embed.set_author(name=mem, icon_url = mem.avatar.url if mem.avatar else mem.default_avatar.url)
     # embed.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
     # embed.timestamp = discord.utils.utcnow()
   #   for badge in badges:
     #   embed.description += f"**{badge}**\n"
     # await ctx.reply(embed=embed, mention_author=False)
      
    # Embed command
    @commands.command(aliases=["makeembed", "createembed"], description="Create an embed")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def newembed(self, ctx):
        msg1 = await ctx.send(
            "I'll now ask you to send some messages to use for the embed!\n___"
        )

        msg2 = await ctx.channel.send(
            "Now send the **title you want to use for the embed** within 60 seconds."
        )

        try:
            title_msg = await self.bot.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=60,
            )
            title = title_msg.content

            if len(title) > 256:
                await ctx.send(
                    "❌ Title is too long. Run the command again but use a shorter title!"
                )
                return

            await msg2.delete()
            await title_msg.delete()

            msg3 = await ctx.channel.send(
                f"Title of the embed will be set to '{title}'.\n"
                + "Now send the text to use for the **content of the embed** within 60 seconds."
            )
            desc_msg = await self.bot.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=60,
            )

            description = desc_msg.content
            await msg3.delete()
            await desc_msg.delete()

            msg4 = await ctx.channel.send(
                "Please send the text to use as a **footer**.\n"
                + "The footer text will be small and light and will be at the bottom of the embed.\n\n"
                + "**If you don't want a footer, say 'empty'.**"
            )
            footer_msg = await self.bot.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=60,
            )

            footer = footer_msg.content
            await msg4.delete()
            await footer_msg.delete()

            msg5 = await ctx.channel.send(
                "Do you want me to display you as the author of the embed?\n"
                + "Please answer with **yes** or **no** within 60 seconds.\n\n"
                + "__Send anything *other than* yes or no to cancel__ - the embed will not be sent if you cancel."
            )
            author_msg = await self.bot.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=60,
            )

            author = author_msg.content
            await msg5.delete()
            await author_msg.delete()

            embed = discord.Embed(title=title, description=description)

            if author.lower() == "yes":
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            elif author.lower() != "no":
                await ctx.send(
                    "❗ Cancelled - you will have to run the command again if you want to make an embed."
                )
                return

            if footer.lower() != "empty":
                embed.set_footer(text=footer)

            await msg1.delete()
            with suppress(AttributeError):
                await ctx.message.delete()

            await ctx.channel.send(embed=embed)

        except asyncio.TimeoutError:
            await ctx.channel.send("❌ Command has timed out. Exiting embed creator.")


          
    @commands.command()
    async def aw(self, ctx):
        embedaw = discord.Embed(title=f"awww", color =  0x2f3136)

        random_link = random.choice(cuteim)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)
      
    @commands.command(aliases=["Nick"])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, name: str = None):
        """ Nicknames a user from the current server. """
        
        try:
            await member.edit(nick=name)
            embed = discord.Embed(description=f"<:sowlbz:989006711920668703> | Changed **{member.name}'s** nickname to **{name}**", color=0x2f3136)
            if name is None:
                embed = discord.Embed(description=f"<:sowlbz:989006711920668703> | Reset **{member.name}'s** nickname to **DEAFULT**", color=discord.Colour(0x2f3136))
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)

    @commands.group()
    @commands.guild_only()
    @commands.max_concurrency(1, per=commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx):
        """ Removes messages from the current server. """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            return await ctx.send(f"Too many messages to search given ({limit}/2000)")

        if not before:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden:
            return await ctx.send("I do not have permissions to delete messages.")
        except discord.HTTPException as e:
            return await ctx.send(f"Error: {e} (try a smaller search?)")

        deleted = len(deleted)
        if message is True:
            await ctx.send(f"🚮 Successfully removed {deleted} message{'' if deleted == 1 else 's'}.")

    @clean.command()
    async def embeds(self, ctx, search=100):
        """Removes messages that have embeds in them."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @clean.command()
    async def files(self, ctx, search=100):
        """Removes messages that have attachments in them."""
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @clean.command()
    async def mentions(self, ctx, search=100):
        """Removes messages that have mentions in them."""
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @clean.command()
    async def images(self, ctx, search=100):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @clean.command(name="all")
    async def _remove_all(self, ctx, search=100):
        """Removes all messages."""
        await self.do_removal(ctx, search, lambda e: True)



    @clean.command(name="bots")
    async def _bots(self, ctx, search=100, prefix=None):
        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = "!"

        def predicate(m):
            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)


    @clean.command(name="emojis")
    async def _emojis(self, ctx, search=100):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r"<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]")

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)

    @clean.command(name="reactions")
    async def _reactions(self, ctx, search=100):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await ctx.send(f"Too many messages to search for ({search}/2000)")

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()

        await ctx.send(f"Successfully removed {total_reactions} reactions.")


    @commands.command()
    async def pbot(self, ctx, max_messages:int=50):
      if max_messages > 5000:
        await ctx.send("2 many messages (<= 5000)")
        return
        deleted = await self.bot.purge_from(ctx.message.channel, limit=max_messages, before=ctx.message, check=lambda m: m.author.bot)
        users = set([str(u.author) for u in deleted])
        if len(deleted) == 0:
          x = await ctx.send(ctx.message.channel, ":warning: No messages found by bots within `{0}` searched messages!".format(max_messages))
        else:
          self.bot.pruned_messages.append(deleted)
          x = await ctx.send(ctx.message.channel, 'ok, removed `{0}` messages by bot{2} `{1}`.'.format(len(deleted), ', '.join(users), 's' if len(users) > 1 else ''))
          await asyncio.sleep(10)
          try:
            self.bot.pruned_messages.append(ctx.message)
            await self.bot.delete_message(ctx.message)
          except:
            pass
            try:
              await self.bot.delete_message(x)
            except:
              pass

	
    @commands.command()
    async def vcinfo(self, ctx: Context, vc: discord.VoiceChannel):
      e = discord.Embed(title='VC Information', color=self.bot.color)
      e.add_field(name='VC name', value=vc.name, inline=False)
      e.add_field(name='VC ID', value=vc.id, inline=False)
      e.add_field(name='VC bitrate', value=vc.bitrate, inline=False)
      e.add_field(name='Mention', value=vc.mention, inline=False)
      e.add_field(name='Category name', value=vc.category.name, inline=False)
      e.add_field(name='VC Created', value=format_date(vc.created_at), inline=False)
      await ctx.send(embed=e)

    


    @commands.command(
        name='avatar',
        aliases=['av', 'avt', 'ac', 'aux', 'pfp', 'avi', 'ico', 'icon'],
        help='get any discord user profile picture'
    )
    async def avatar(self, ctx, user: discord.Member = None):
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        avemb = discord.Embed(
            color=0x2f3136,
            title=f"{user}'s Avatar",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not user.avatar.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({user.avatar.replace(format='gif')})"
        )
        avemb.set_image(url=user.avatar.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)



      
        if (user.premium_since):
            Booster = '✔️'
        else:
            Booster = '❌'
  
    @commands.command()
    async def userinfo6999(self, ctx: commands.Context,
                      member: discord.Member = None):
      button = discord.ui.Button(label=f'Badges', style=discord.ButtonStyle.grey)
      if member == None:
        member = ctx.author
      async def button_callback(interaction: discord.Interaction):
        permissions = ", ".join(
          [perm[0] for perm in member.guild_permissions if perm[1]])
        permissions = permissions.replace("_", " ")
        permissions = permissions.split(",")
        permissions_formatted = []
        word = ""
        for p in permissions:
            for p in p.split():
                word += " "+p[0].upper()+p[1:]
            permissions_formatted.append(word)
            word = ""
        permissions_formatted = ",  ".join(
            [permissions for permissions in permissions_formatted])
        badges = ""
        if ctx.author.public_flags.hypesquad:
          badges = "Hypesquad"
        elif ctx.author.public_flags.hypesquad_balance:
          badges = "Hypesquad Balance"
        elif ctx.author.public_flags.hypesquad_bravery:
          badges = "Hypesquad Bravery"
        elif ctx.author.public_flags.hypesquad_brilliance:
          badges = "Hypesquad Brilliance"
        elif ctx.author.public_flags.early_supporter:
          badges = "Early Supporter"
        elif ctx.author.public_flags.verified_bot_developer:
          badges = "Verified Bot Developer"
        elif ctx.author.public_flags.partner:
          badges = "Partner"
        elif ctx.author.public_flags.bug_hunter:
          badges = "Bug Hunter"
        for i in badges:
          embed1 = discord.Embed(title='Badges', color = 0x2f3136)
          embed1.set_author(name=f'{member}', icon_url=f'{member.avatar}')
          await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(color = 0x2f3136)
      bannerUser = await self.bot.fetch_user(member.id)
      embed.add_field(name=f"__**General Information**__", value=f"**Name:** {member.name}#{member.discriminator}\n **ID**: {member.id}\n **Account Created:** <t:{int(member.created_at.timestamp())}:D>\n **Joined Server On:** <t:{int(member.joined_at.timestamp())}:D>\n **Highest Role:** {member.top_role.mention}\n **Roles:** {len(ctx.message.author.roles)}\n**Status**: {member.status}\n**Bot?**: {member.bot}\n**Booster?**: {member.premium_since}\n**User Permissions:** {permissions_formatted}")
      embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embed.set_thumbnail(url=member.avatar)
      if not bannerUser.banner:
        pass
      else:
        embed.set_image(url=bannerUser.banner) 
      await ctx.send(embed=embed)


    @commands.command(pass_context=True, description="Shows useful information about a user")
    @commands.guild_only()
    async def userinfo(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        roles = roles[1:]
        if len(roles) != 0:
            user_roles = ", ".join([role.mention for role in roles])
        else:
            user_roles = "User has no roles"

        hoisted_role = None
        for role in roles:
            if role.hoist == True:
                hoisted_role = role.mention

        embed = discord.Embed(colour=0x2f3136, timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        #embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        permissions = ", ".join(
            [perm[0] for perm in member.guild_permissions if perm[1]])
        permissions = permissions.replace("_", " ")
        permissions = permissions.split(",")
        permissions_formatted = []
        word = ""
        for p in permissions:
            for p in p.split():
                word += " "+p[0].upper()+p[1:]
            permissions_formatted.append(word)
            word = ""
        permissions_formatted = ",  ".join(
            [permissions for permissions in permissions_formatted])
        is_user_bot = "Yes" if member.bot == True else "No"
        user_created = int(member.created_at.timestamp())
        user_joined = int(member.joined_at.timestamp())
        user_boosting = None
        user_boosting_days = None
        if member.premium_since != None:
            user_boosting = f"<t:{int(member.premium_since.timestamp())}:F>"
            user_boosting_days = f"<t:{int(member.premium_since.timestamp())}:R>"

        user_highest_role = member.top_role.mention
        embed.add_field(name="User identity:", value=f"**Status**: **{member.status}**\n**User id:** **{member.id}**\n**Bot user?** **{is_user_bot}**\n\n**Boosting since:** **{user_boosting}**\n**Boosting days:** **{user_boosting_days}**", inline=False)
        embed.add_field(
                name="Dates:", value=f"Account created at: **<t:{user_created}:F>**\nUser account was created: **<t:{user_created}:R> **\n\nJoined server at: **<t:{user_joined}:F>**\nUser joined the server: **<t:{user_joined}:R> **", inline=False)
        embed.add_field(name="User Permissions: ",
                        value=f"\n{permissions_formatted}", inline=False)

        if not (len(member.roles)-1 >= 25):
            embed.add_field(
                name=f"Roles[{len(member.roles)-1}]:", value=user_roles, inline=False)
        else:
            embed.add_field(name=f"Roles[{len(member.roles)-1}]:",
                            value=f'{member.mention} has too many roles, hence they wont be printed.')
        embed.add_field(name="Highest Role:",
                        value=user_highest_role, inline=False)
        embed.add_field(name="Hoisted Role:", value=hoisted_role, inline=False)
        embed.set_author(name=self.bot.user.name)
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def getemotes(self, ctx):
        """Gets a list of the server's emotes"""
        emotes = ctx.guild.emojis
        if len(emotes) == 0:
            await ctx.send(("information.no_server_emotes", ctx))
            return
        emotes = ["`:{}:` = {}".format(emote.name, emote) for emote in emotes]
        await ctx.send("\n".join(emotes))

    @commands.command(aliases=['trump', 'trumpquote'])
    async def asktrump(self, ctx, *, question):
        '''Ask Donald Trump a question!'''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}') as resp:
                file = await resp.json()
        quote = file['message']
        em = discord.Embed(color = 0x2f3136)
        em.title = "What does Trump say?"
        em.description = quote
        em.set_footer(text="Trump Fam")
        await ctx.send(embed=em)
      
    


    @commands.Cog.listener()
    async def on_message_delete(self, message):
      if message.author.bot is False and isinstance(message.channel, DMChannel) is not True:
        self.sniped.get[message.channel.id] = message

    @commands.command(aliases=["addemoji"], description="Adds an emoji to the server.", usage="addemoji <emoji|image-url> <name>")
    async def steal(self, ctx, emote, *, name=None):
        if '<' in emote and '>' in emote and ':' in emote:
            name = name if name else emote.split(':')[2]
            print(emote.split(':'))
            id = emote.split(':')[2].replace('>', '').replace('<', '')
            if '<a' in emote:
                url = f"https://cdn.discordapp.com/emojis/{id}.gif"
            else:
                url = f"https://cdn.discordapp.com/emojis/{id}.png"
            r = requests.get(url)
            if r.status_code == 200 or str(r.status_code).startswith('2'):
                #create emoji
                emoji = await ctx.guild.create_custom_emoji(name=name, image=r.content)
                await ctx.send(f'Emote Created with the name "**{name}**" : {emoji}')
            else:
                await ctx.send(ctx, f'**An error occured**', color=0x2f3136)
        elif str(emote).startswith('http://') or str(emote).startswith('https://'):
            r = requests.get(emote)
            if r.status_code == 200:
                #create emoji
                if name == None:
                    return await ctx.send(f'Please provide a name for the emoji.')
                emoji = await ctx.guild.create_custom_emoji(name=name, image=r.content)
                await ctx.send(f'Emote Created with the name "**{name}**" : {emoji}')
            else:
                await ctx.send(f'**An error occured**')
        else:
            await ctx.send(f'**An error occured**')


          
    @commands.command(aliases=['urban23'])
    async def snipe2(self, ctx):
      if not ctx.channel.id in self.sniped.get:
        return await ctx.send('Nothing to snipe.')
        data: discord.Message = self.sniped.get[ctx.channel.id]
        time = data.created_at
        embed = discord.Embed(color=0x2f3136, timestamp=time)
        embed.set_author(name=data.author.name,
						 icon_url=data.author.avatar.url)
        if data.content:
          embed.description = data.content
          if data.attachments:
            if str(data.attachments[0].filename).lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
              embed.set_image(
					url="attachment://{}".format(data.attachments[0].filename))
              embed.set_footer(text='Sniped message sent at {}'.format(
					time.strftime("%I:%M %p")))
              del self.sniped.get[ctx.channel.id]
              return await ctx.send(embed=embed, file=await data.attachments[0].to_file())
              del self.sniped.get[ctx.channel.id]
              await ctx.send(embed=embed)
    
    @commands.command(aliases=['urban2'])
    async def ud2(self, ctx, *, query):
        '''Search terms with urbandictionary.com'''
        em = discord.Embed(title=f'{query}', color=discord.Color.green())
      #  em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        em.set_footer(text='Powered by urbandictionary.com')
        defs = f'https://udict-api.glique.repl.co/{query}'
        try:
            res = defs[0]
        except IndexError:
            em.description = 'No results.'
            return await ctx.send(embed=em)
        em.description = f'**Definition:** {res.defs}\n**Usage:** {res.example}\n**Votes:** {res.upvotes}:thumbsup:{res.downvotes}:thumbsdown:'
        await ctx.send(embed=em)
      
    @commands.command()
    async def servericon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=0x2f3136,
            title=f"{server}'s Icon",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not server.icon.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)



    @commands.command(aliases=['inv'])
    async def invite(self, ctx: commands.Context):
        embed = discord.Embed(title=f"", description = f">>> • [Click here to get me](https://discord.com/api/oauth2/authorize?client_id=992797622094016622&permissions=8&scope=bot)\n• [Support server](https://discord.gg/apolex)\n• [Vote me](https://top.gg/bot/992797622094016622/vote)", color =  0x2f3136, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Made with 💖")
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)

    @commands.command()
    async def banners(self, ctx):
        embedaw = discord.Embed(title=f"Banners!", color =  0x2f3136)

        random_link = random.choice(banners)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw) 

    @commands.command()
    async def animepng(self, ctx):
        embedaw = discord.Embed(title=f"Anime png!", color =  0x2f3136)

        random_link = random.choice(animepng)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)      

    @commands.command()
    async def animegif(self, ctx):
        embedaw = discord.Embed(title=f"Anime gif!", color =  0x2f3136)

        random_link = random.choice(animegif)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw) 
  
    @commands.command()
    async def couplespng(self, ctx):
        embedaw = discord.Embed(title=f"Couples png!", color =  0x2f3136)

        random_link = random.choice(couplespng)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command()
    async def couplesgif(self, ctx):
        embedaw = discord.Embed(title=f"Couples gif!", color =  0x2f3136)

        random_link = random.choice(couplesgif)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)
  
    @commands.command()
    async def boysgif(self, ctx):
        embedaw = discord.Embed(title=f"Boys gif!", color =  0x2f3136)

        random_link = random.choice(boysgif)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command()
    async def girlsgif(self, ctx):
        embedaw = discord.Embed(title=f"Girls gif!", color =  0x2f3136)

        random_link = random.choice(girlsgif)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)
      
    @commands.command()
    async def girlspng(self, ctx):
        embedaw = discord.Embed(title=f"Girls png!", color =  0x2f3136)

        random_link = random.choice(girlspng)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)
      
    @commands.command()
    async def boyspng(self, ctx):
        embedaw = discord.Embed(title=f"Boys png!", color =  0x2f3136)

        random_link = random.choice(boyspng)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command()
    async def pfps(self, ctx):
        embedaw = discord.Embed(title=f"Random Pfps!", color =  0x2f3136)

        random_link = random.choice(pfps)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)
      
    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        embedaw = discord.Embed(title=f"{ctx.author.name} slaps {member.display_name}!", color =  0x2f3136)

        random_link = random.choice(slaps)
        embedaw.set_image(url = random_link)

        await ctx.send(embed=embedaw)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
      embedpat = discord.Embed(title=f"{ctx.author.name} pats {member.display_name}!", color = 0x2f3136)

      random_link = random.choice(pats)
      embedpat.set_image(url=random_link)
      
      await ctx.send(embed=embedpat)



    @commands.command()
    async def inspire(self, ctx):
        quote = get_quote()
        embedin = discord.Embed(title=f"Get Inspired!", description=f"{quote}", color =  0x2f3136)
        await ctx.send(embed=embedin)

  
    @commands.command()
    async def poll(self, ctx,*,message):
      emp = discord.Embed(title=f"**Poll!**", description=f"{message}", color =  000000)
      msg = await ctx.send(embed=emp)
      await msg.add_reaction("👍")
      await msg.add_reaction("👎")

    @commands.command()
    async def hack(self, ctx, member: discord.Member):
      random_pass = random.choice(password)
      embed = discord.Embed(title=f"**Hacked!**", description=f"Username - {member.display_name}\n E-Mail - {member.display_name}@gmail.com\n Password - {member.display_name}@{random_pass}", color =  0x2f3136)
      await ctx.send(embed=embed)



    @commands.command()
    async def gay(self, ctx, user: discord.Member):
      random_msg = random.choice(gayr)
      embed = discord.Embed(title=f"{user.display_name}'s gay rate:", description=F"{random_msg}", color =  0x2f3136)

      await ctx.send(embed=embed)



    @commands.command()
    async def token(self, ctx, user: discord.Member = None):
        list = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
            '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        token = random.choices(list, k=59)
        if user is None:
            user = ctx.author
            await ctx.send(user.mention + "'s token is " + ''.join(token))
        else:
            await ctx.send(user.mention + "'s token is " + "".join(token))





    @commands.command()
    async def typerace(self, ctx):
        starttime = time.time()
        answer = random.choice(typeracer)
        timer = 17.0
        await ctx.send(f"You have {timer} seconds to type: {answer}")

        def is_correct(msg):
            return msg.author==ctx.author

        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=timer)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long :(")

        if guess.content == answer:
            await ctx.send("You got it!")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")

        else:
            await ctx.send("Nope, that wasn't really right")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")
   


    @commands.command(aliases=['invitei', 'ii'], pass_context=True)
    async def inviteinfo(self, ctx, *, invite: str = None):
        """Shows invite information."""
        if invite:
            for url in re.findall(r'(https?://\S+)', invite):
                try:
                    invite = await self.bot.get_invite(urlparse(url).path.replace('/', '').replace('<', '').replace('>', ''))
                except discord.NotFound:
                    return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                break
        else:
            async for msg in ctx.message.channel.history():
                if any(x in msg.content for x in self.invites):
                    for url in re.findall(r'(https?://\S+)', msg.content):
                        url = urlparse(url)
                        if any(x in url for x in self.invite_domains):
                            print(url)
                            url = url.path.replace('/', '').replace('<', '').replace('>', '').replace('\'', '').replace(')', '')
                            print(url)
                            try:
                                invite = await self.bot.get.invite(url)
                            except discord.NotFound:
                                return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                            break
                
        if not invite:
            return await ctx.send(self.bot.bot_prefix + "Couldn't find an invite in the last 100 messages. Please specify an invite.")
        
        data = discord.Embed()
        content = None
        if invite.id is not None:
            content = self.bot.bot_prefix + "**Information about Invite:** %s" % invite.id
        if invite.revoked is not None:
            data.colour = discord.Colour.red() if invite.revoked else discord.Colour.green()
        if invite.created_at is not None:
            data.set_footer(text="Created on {} ({} days ago)".format(invite.created_at.strftime("%d %b %Y %H:%M"), (invite.created_at - invite.created_at).days))
        if invite.max_age is not None:
            if invite.max_age > 0:
                expires = '%s s' % invite.max_age
            else:
                expires = "Never"
            data.add_field(name="Expires in", value=expires)
        if invite.temporary is not None:
            data.add_field(name="Temp membership", value="Yes" if invite.temporary else "No")
        if invite.uses is not None:
            data.add_field(name="Uses", value="%s / %s" % (invite.uses, invite.max_uses))
        if invite.inviter.name is not None:
            data.set_author(name=invite.inviter.name + '#' + invite.inviter.discriminator + " (%s)" % invite.inviter.id, icon_url=invite.inviter.avatar.url)

        if invite.guild.name is not None:
            data.add_field(name="Guild", value="Name: " + invite.guild.name + "\nID: %s" % invite.guild.id, inline=False)
        if invite.guild.icon.url is not None:
            data.set_thumbnail(url=invite.guild.icon.url)

        if invite.channel.name is not None:
            channel = "%s\n#%s" % (invite.channel.mention, invite.channel.name) if isinstance(invite.channel, discord.TextChannel) else invite.channel.name
            data.add_field(name="Channel", value="Name: " + channel + "\nID: %s" % invite.channel.id, inline=False)

        try:
            await ctx.send(content=content, embed=data)
        except:
            await ctx.send(content="I need the `Embed links` permission to send this")

    # Embeds the message

          
    @commands.command(aliases=['serverinfo'])
    async def info(self, ctx: commands.Context):
      vanity = "VANITY_URL" in str(ctx.guild.features)
      splash = "INVITE_SPLASH" in str(ctx.guild.features)
      animicon = "ANIMATED_ICON" in str(ctx.guild.features)
      discoverable = "DISCOVERY" in str(ctx.guild.features)
      banner = "BANNER" in str(ctx.guild.features)
      vanityFeature = "{} - Vanity URL".format(tragedy.EmojiBool(vanity)) if not vanity else "{} - Vanity URL ({})".format(tragedy.EmojiBool(vanity), str(await ctx.guild.vanity_invite())[15:])
      nsfw_level = ''
     # button = discord.ui.Button(label=f'Server icon', style=discord.ButtonStyle.url, url=f'{ctx.guild.icon}')
      button = discord.ui.Button(label=f'Roles', style=discord.ButtonStyle.grey)
      view = discord.ui.View()
      view.add_item(button)
     # view.add_item(button2)
      if ctx.guild.nsfw_level.name == 'default':
        nsfw_level = '**Default**'
      if ctx.guild.nsfw_level.name == 'explicit':
        nsfw_level = '**Explicit**'
      if ctx.guild.nsfw_level.name == 'safe':
        nsfw_level = '**Safe**'
      if ctx.guild.nsfw_level.name == 'age_restricted':
        nsfw_level = '**Age Restricted**'
      async def button_callback(interaction: discord.Interaction):
        roles = ""
        for i in ctx.guild.roles:
          roles += "• " + str(i.mention) + "\n"
        embed1 = discord.Embed(title=f'{ctx.guild.name}', description=f'{roles}', color=0x2f3136)
        await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(title=f'{ctx.guild.name} | {ctx.guild.id}', color = 0x2f3136)
      embed.add_field(name=f'**__ Server General Information__**', value=f"""
**Owner:** {ctx.guild.owner.mention} 
**Owner Id:** {ctx.guild.owner.id}
**Member count:** {ctx.guild.member_count}
**Created**: <t:{int(ctx.guild.created_at.timestamp())}:D>

__**Server Roles & Channels Info**__
**Server Channels**: {len(ctx.guild.channels)}
**Server Voice Channels:** {len(ctx.guild.voice_channels)}
**Server Roles**: {len(ctx.guild.roles)}
**NSFW level:** {nsfw_level}

__**Server Verification & Emojis Info**__
**Verification level:** {ctx.guild.verification_level.name}
**Explicit Content Filter:** {ctx.guild.explicit_content_filter.name}
**Max Talk Bitrate:** {int(ctx.guild.bitrate_limit)}kbps
**Emojis:** {len(ctx.guild.emojis)}
**Stickers:** {len(ctx.guild.stickers)}""")
      embed.add_field(name="__**Server Features**__", value="{} - Banner\n{}\n{} - Splash Invite\n{} - Animated Icon\n{} - Server Discoverable".format(tragedy.EmojiBool(banner), vanityFeature, tragedy.EmojiBool(splash), tragedy.EmojiBool(animicon), tragedy.EmojiBool(discoverable)))
      embed.add_field(name="__**Server Boost Info**__", value="Number of Boosts - **{}**\nBooster Role - **{}**\nBoost Level/Tier - **{}**".format( str(ctx.guild.premium_subscription_count), ctx.guild.premium_subscriber_role.mention if ctx.guild.premium_subscriber_role != None else ctx.guild.premium_subscriber_role, ctx.guild.premium_tier), inline=False)
      embed.add_field(name="__**Server Afk Info**__", value="AFK Channel: **{}**\nAFK Timeout: **{} minute(s)**\nFilesize Limit - **{}**".format( ctx.guild.afk_channel, str(ctx.guild.afk_timeout / 60), len(ctx.guild.emojis), len(ctx.guild.roles), humanize.naturalsize(ctx.guild.filesize_limit)), inline=False)
      embed.set_footer(text=f"Requested by {ctx.author} | Made with 💖 by Team Apolex")
	#await ctx.reply(embed=embed, mention_author=True)
#      embed.add_field(name=f'**__Additional__**', value=f"""\n""")
      button.callback = button_callback
      await ctx.send(embed=embed, view=view)


    
    @commands.command(aliases=['channeli', 'cinfo', 'ci'], pass_context=True, no_pm=True)
    async def channelinfo(self, ctx, *, channel: int = None):
        """Shows channel information"""
        if not channel:
            channel = ctx.message.channel
        else:
            channel = self.bot.get_channel(channel)
        data = discord.Embed()
        if hasattr(channel, 'mention'):
            data.description = "**Information about Channel:** " + channel.mention
        if hasattr(channel, 'changed_roles'):
            if len(channel.changed_roles) > 0:
                data.color = 0x2f3136 if channel.changed_roles[0].permissions.read_messages else 0x2f3136
        if isinstance(channel, discord.TextChannel): 
            _type = "Text"
        elif isinstance(channel, discord.VoiceChannel): 
            _type = "Voice"
        else: 
            _type = "Unknown"
        data.add_field(name="Type", value=_type)
        data.add_field(name="ID", value=channel.id, inline=False)
        if hasattr(channel, 'position'):
            data.add_field(name="Position", value=channel.position)
        if isinstance(channel, discord.VoiceChannel):
            if channel.user_limit != 0:
                data.add_field(name="User Number", value="{}/{}".format(len(channel.voice_members), channel.user_limit))
            else:
                data.add_field(name="User Number", value="{}".format(len(channel.voice_members)))
            userlist = [r.display_name for r in channel.members]
            if not userlist:
                userlist = "None"
            else:
                userlist = "\n".join(userlist)
            data.add_field(name="Users", value=userlist)
            data.add_field(name="Bitrate", value=channel.bitrate)
        elif isinstance(channel, discord.TextChannel):
            try:
                pins = await channel.pins()
                data.add_field(name="Pins", value=len(pins), inline=True)
            except discord.Forbidden:
                pass
            data.add_field(name="Members", value="%s"%len(channel.members))
            if channel.topic:
                data.add_field(name="Topic", value=channel.topic, inline=False)
            hidden = []
            allowed = []
            for role in channel.changed_roles:
                if role.permissions.read_messages is True:
                    if role.name != "@everyone":
                        allowed.append(role.mention)
                elif role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        hidden.append(role.mention)
            if len(allowed) > 0: 
                data.add_field(name='Allowed Roles ({})'.format(len(allowed)), value=', '.join(allowed), inline=False)
            if len(hidden) > 0:
                data.add_field(name='Restricted Roles ({})'.format(len(hidden)), value=', '.join(hidden), inline=False)
        if channel.created_at:
            data.set_footer(text=("Created on {} ({} days ago)".format(channel.created_at.strftime("%d %b %Y %H:%M"), (ctx.message.created_at - channel.created_at).days)))
        await ctx.send(embed=data)
#from utils import checks

    @commands.command()
    async def wizz(self, ctx):
      message6 = await ctx.send(f"`Wizzing {ctx.guild.name}, will take 22 seconds to complete`")
      message5 = await ctx.send(f"`Deleting {len(ctx.guild.roles)} Roles...`")
      message4 = await ctx.send(f"`Deleting {len(ctx.guild.channels)} Channels...`")
      message3 = await ctx.send(f"`Deleting Webhooks...`")
      message2 = await ctx.send(f"`Deleting emojis`")
      message1 = await ctx.send(f"`Installing Ban Wave..`")
      await message6.delete()
      await message5.delete()
      await message4.delete()
      await message3.delete()
      await message2.delete()
      await message1.delete()

    @commands.command()
    async def truth(self, ctx):
      random_msg = random.choice(truths)
      await ctx.send(f"{random_msg}")

    @commands.command()
    async def dare(self, ctx):
      random_msg = random.choice(dares)
      await ctx.send(f"{random_msg}")


    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! {}'.format(round(self.bot.latency * 600)))
    
    @commands.command()
    async def botinfo26(self, ctx):
      proc = Process()
      with proc.oneshot():
        mem_total =virtual_memory().total / (1024**2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
        embed = discord.Embed(color = 0x2f3136  )
        embed.add_field(name=f"**__{self.bot.user.name} Info__**", value=f"""```asciidoc\n Servers : {len(self.bot.guilds)}\nUsers : {len(set(self.bot.get_all_members()))}\n Commands : {len(self.bot.commands)}\nMemory Usage : {mem_usage}\nTotal Storage : `{mem_usage:,.3f} MB\nDevelopers : Archduke, Vivox, Ghost, Godking```""")
        await ctx.send(embed=embed)






    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question) -> None:
        embed = discord.Embed(title=f"8Ball", description=f"Question - {question}\nAnswer - {random.choice(EIGHT_BALL_ANSWERS)}", color = 0x2f3136);
        await ctx.send(embed=embed)

    @commands.command()
    async def afk(self, ctx, *, reason="I am afk."):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick = f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        await ctx.send(f"{member.name} Added Afk.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            await message.channel.send(f"{message.author.name}, I removed your AFK.")

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                await message.reply(f"{member.name} is AFK For: I am afk.")

    @commands.command()#for times loop, random(1, sides). multiplier
    async def roll(self, ctx, times=0, sides=0, *, args=None):
        member = ctx.author
        times = int(times)
        sides = int(sides)
        try:
            num = re.sub('[^\d.,]' , '', str(args))
            add = int(num)
            if "-" in args:
                add = "-"+ str(add)
                add = int(add)
        except:
            add = 0
        if not args:
            args = "normal"
        if times == 0 or  sides == 0:
            await ctx.send("Yo bro/sis you need to specify the parts I use\n `roll (how many times) (how many sided dice) (modifier)`")
        else:
            try:
                if 'disadv' in str(args.lower()) or 'disadvantage' in str(args.lower()):
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Disadvantage', colour=discord.Colour.default())
                    result = disadvantageRoll(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
                elif 'adv' in str(args.lower()) or 'advantage' in str(args.lower()):
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Advantage', colour=discord.Colour.default())
                    result = advantageRoll(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
                else:
                    embed = discord.Embed(title='Roll:', description=f'Rolled: {times}d{sides}\n Roll Type: Normal', colour=discord.Colour.default())
                    result = fun(times, sides, add)
                    embed.add_field(name=f'The total is: **{result[0]}**', value=f'{result[1]}')
            except:
                embed = discord.Embed(title='Roll:', description='Roll Type: **ERROR**', colour=discord.Colour.default())
                embed.add_field(name='**ERROR**', value='\uFEFF')
            embed.set_author(icon_url=member.avatar, name=str(member))
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def pokemon(self,ctx,*,pokemon):
      async with aiohttp.ClientSession() as session:
        message0 = await ctx.send("I am looking for that Pokemon. Please be patient.")
        await ctx.channel.trigger_typing()
        response = await session.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon}') # Again, I use the same API. They are really good and I consider using them
        await ctx.channel.trigger_typing()
        if str(response.status) == "404":
            await ctx.send("I couldn't find that pokemon. Please try again.")
        else:
                        rj = await response.json()
                        name = (rj['name']).capitalize()
                        pid = (rj['id'])
                        ptype = (rj['type'])
                        desc = (rj['description'])
                        species = (rj['species'])
                        stats = (rj['stats'])
                        evolfam = (rj['family'])
                        evs = (evolfam['evolutionLine'])
                        evs=str(evs)
                        evs=evs.replace("'","")
                        evs=evs.replace("]","")
                        evs=evs.replace("[","")
                        hp = (stats['hp'])
                        attack = (stats['attack'])
                        defense = (stats['defense'])
                        speed = (stats['speed'])
                        spattack = (stats['sp_atk'])
                        spdef = (stats['sp_def'])
                        abilities = (rj['abilities'])
                        abilities = str(abilities)
                        abilities=abilities.replace("'","")
                        abilities=abilities.replace("[","")
                        abilities=abilities.replace("]","")
                        weight = (rj['weight'])
                        height = (rj['height'])
                        weight = weight.replace(u'\xa0', u' ')
                        height = height.replace(u'\xa0', u' ')
                        species = str(species)
                        species=species.replace("'","")
                        species=species.replace("[","")
                        species=species.replace("]","")
                        species=species.replace(",","")
                        ptype = str(ptype)
                        ptype=ptype.replace("'","")
                        ptype=ptype.replace("[","")
                        ptype=ptype.replace("]","")
                        imgs=(rj['sprites'])
                        if int(rj['generation']) < 6:
                            img=(imgs['animated'])
                        else:
                            img=(imgs['normal'])
                        url = (imgs['normal'])
                        try:
                            idx = await session.get(url)
                            idx = await idx.read()
                            #await url.save(f'{pokemon}av.png',seek_begin = True)
                            embed=discord.Embed(title=name,description=desc,color=random.randint(0, 0xFFFFFF))
                        except:
                            embed=discord.Embed(title=name,description=desc)
                        embed.set_thumbnail(url=img)
                        embed.add_field(name="Information",value=f"Pokedex Entry: {pid}\nFirst introduced in generation {(rj['generation'])}\nType(s): {ptype}\nAbilities: {abilities}",inline=True)
                        embed.add_field(name="Base Stats",value=f"HP: {hp}\nDefense: {defense}\nSpeed: {speed}\nAttack: {attack}\nSpecial Attack: {spattack}\nSpecial Defense: {spdef}",inline=True)
                        if len(evs) != 0:
                            embed.add_field(name="Evolution Line",value=evs,inline=True)
                        await ctx.channel.trigger_typing()
                        await message0.delete()
                        await ctx.send(embed=embed)

    @commands.command()
    async def pikachu(self, ctx):
      response = requests.get('https://some-random-api.ml/img/pikachu')
      data = response.json()
      embed = discord.Embed(
        title = 'Pikachu',
        description = 'Here is a gif of Pikachu.',
        color = 0xfff900
      )
      embed.set_image(url=data['link'])
      embed.set_footer(text="")
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

    @commands.group()
    async def banner(self, ctx: commands.Context):
      ...

    @banner.command()
    async def userinfooanza(self, ctx: commands.Context, *, member: discord.Member = None):
      if member == None:
        member = ctx.author
      embed = discord.Embed(title=f'{member.name} + {member.discriminator}\'s Banner', color = 0x2f3136)
      embed.set_image(url=member.banner.url)
      await ctx.send(embed=embed)
      
    @banner.command()
    async def server(self, ctx: commands.Context):
      if not ctx.guild.banner:
        await ctx.send('This server does not have any banner!')
      embed = discord.Embed(title=f'{ctx.guild.name}\'s Banner', color = 0x2f3136)
      embed.set_image(url=ctx.guild.banner)
      await ctx.send(embed=embed)

    @commands.command(aliases=['match'])
    async def ship(self, ctx: commands.Context, *, user: discord.Member):
      love_count = range(0, 100)
      love_emoji = ""
      if love_count <= 50:
        love_emoji.replace('', '💔')
        embed = discord.Embed(title=f'{ctx.author.name}#{ctx.author.discriminator} {love_emoji} {user.name}#{user.discriminator}', color = 0x2f3136)
        await ctx.send(content=f'{ctx.author.name}#{ctx.author.discriminator} ships {user.name}#{user.discriminator}',embed=embed)
      else:
        love_emoji.replace('', '💖')
        embed = discord.Embed(title=f'{ctx.author.name}#{ctx.author.discriminator} {love_emoji} {user.name}#{user.discriminator}', color = 0x2f3136)
        await ctx.send(content=f'{ctx.author.name}#{ctx.author.discriminator} ships {user.name}#{user.discriminator}',embed=embed)



def setup(bot):
    bot.add_cog(fun(bot))
