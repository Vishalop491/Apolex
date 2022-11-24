from discord.ext import commands
import discord.utils
import json
import os
import json
import time
import discord
import os
import aiohttp
from cogs.utils.dataIO import dataIO
from urllib.parse import quote as uriquote

try:
    from lxml import etree
except ImportError:
    from bs4 import BeautifulSoup
from urllib.parse import parse_qs, quote_plus
#from cogs.utils import common


# @common.deprecation_warn()
def load_config():
    with open('settings/config.json', 'r') as f:
        return json.load(f)


# @common.deprecation_warn()
def load_optional_config():
    with open('settings/optional_config.json', 'r') as f:
        return json.load(f)

def load_optional_config():
    with open('settings/commands.json', 'r') as f:
        return json.load(f)



def has_passed(oldtime):
    if time.time() - 20.0 < oldtime:
        return False
    return time.time()


def set_status(bot):
    if bot.default_status == 'idle':
        return discord.Status.idle
    elif bot.default_status == 'dnd':
        return discord.Status.dnd
    else:
        return discord.Status.invisible


def user_post(key_users, user):
    if time.time() - float(key_users[user][0]) < float(key_users[user][1]):
        return False, [time.time(), key_users[user][1]]
    else:
        log = dataIO.load_json("settings/log.json")
        now = time.time()
        log["keyusers"][user] = [now, key_users[user][1]]
        dataIO.save_json("settings/log.json", log)
        return True, [now, key_users[user][1]]


def gc_clear(gc_time):
    if time.time() - 3600.0 < gc_time:
        return False
    return time.time()


def game_time_check(oldtime, interval):
    if time.time() - float(interval) < oldtime:
        return False
    return time.time()


def avatar_time_check(oldtime, interval):
    if time.time() - float(interval) < oldtime:
        return False
    return time.time()


def update_bot(message):
    g = git.cmd.Git(working_dir=os.getcwd())
    branch = g.execute(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    g.execute(["git", "fetch", "origin", branch])
    update = g.execute(["git", "remote", "show", "origin"])
    if ('up to date' in update or 'fast-forward' in update) and message:
        return False
    else:
        if message is False:
            version = 4
        else:
            version = g.execute(["git", "rev-list", "--right-only", "--count", "{0}...origin/{0}".format(branch)])
        version = description = str(int(version))
        if int(version) > 4:
            version = "4"
        commits = g.execute(["git", "rev-list", "--max-count={0}".format(version), "origin/{0}".format(branch)])
        commits = commits.split('\n')
        em = discord.Embed(color=0x24292E, title='Latest changes for the selfbot:', description='{0} release(s) behind.'.format(description))
        for i in range(int(version)):
            i = i - 1  # Change i to i -1 to let the formatters below work
            title = g.execute(["git", "log", "--format=%ar", "-n", "1", commits[i]])
            field = g.execute(["git", "log", "--pretty=oneline", "--abbrev-commit", "--shortstat", commits[i], "^{0}".format(commits[i + 1])])
            field = field[8:].strip()
            link = 'https://github.com/appu1232/Discord-Selfbot/commit/%s' % commits[i]
            em.add_field(name=title, value='{0}\n[Code changes]({1})'.format(field, link), inline=False)
        em.set_thumbnail(url='https://image.flaticon.com/icons/png/512/25/25231.png')
        em.set_footer(text='Full project: https://github.com/appu1232/Discord-Selfbot')
        return em


def cmd_prefix_len():
    config = load_config()
    return len(config['cmd_prefix'])


def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

    return check


def get_user(message, user):
    try:
        member = message.mentions[0]
    except:
        member = message.guild.get_member_named(user)
    if not member:
        try:
            member = message.guild.get_member(int(user))
        except ValueError:
            pass
    if not member:
        return None
    return member


def find_channel(channel_list, text):
    if text.isdigit():
        found_channel = discord.utils.get(channel_list, id=int(text))
    elif text.startswith("<#") and text.endswith(">"):
        found_channel = discord.utils.get(channel_list,
                                          id=text.replace("<", "").replace(">", "").replace("#", ""))
    else:
        found_channel = discord.utils.get(channel_list, name=text)
    return found_channel


async def get_google_entries(query, session=None):
    if not session:
        session = aiohttp.ClientSession()
    url = 'https://www.google.com/search?q={}'.format(uriquote(query))
    params = {
        'safe': 'off',
        'lr': 'lang_en',
        'h1': 'en'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
    }
    entries = []
    async with session.get(url, params=params, headers=headers) as resp:
        if resp.status != 200:
            config = load_optional_config()
            async with session.get("https://www.googleapis.com/customsearch/v1?q=" + quote_plus(query) + "&start=" + '1' + "&key=" + config['google_api_key'] + "&cx=" + config['custom_search_engine']) as resp:
                result = json.loads(await resp.text())
            return None, result['items'][0]['link']

        try:
            root = etree.fromstring(await resp.text(), etree.HTMLParser())
            search_nodes = root.findall(".//div[@class='g']")
            for node in search_nodes:
                url_node = node.find('.//h3/a')
                if url_node is None:
                    continue
                url = url_node.attrib['href']
                if not url.startswith('/url?'):
                    continue
                url = parse_qs(url[5:])['q'][0]
                entries.append(url)
        except NameError:
            root = BeautifulSoup(await resp.text(), 'html.parser')
            for result in root.find_all("div", class_='g'):
                url_node = result.find('h3')
                if url_node:
                    for link in url_node.find_all('a', href=True):
                        url = link['href']
                        if not url.startswith('/url?'):
                            continue
                        url = parse_qs(url[5:])['q'][0]
                        entries.append(url)
    return entries, root


def attach_perms(message):
    return message.author.permissions_in(message.channel).attach_files


def parse_prefix(bot, text):
    prefix = bot.cmd_prefix
    if type(prefix) is list:
        prefix = prefix[0]
    return text.replace("[c]", prefix).replace("[b]", bot.bot_prefix)


async def hastebin(content, session=None):
    if not session:
        session = aiohttp.ClientSession()
    async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
        if resp.status == 200:
            result = await resp.json()
            return "https://hastebin.com/" + result["key"]
        else:
            return "Error with creating Hastebin. Status: %s" % resp.status

class No_Owner(commands.CommandError): pass
class No_Perms(commands.CommandError): pass
class No_Role(commands.CommandError): pass
class No_Admin(commands.CommandError): pass
class No_Mod(commands.CommandError): pass
class No_Sup(commands.CommandError): pass
class No_ServerandPerm(commands.CommandError): pass
class Nsfw(commands.CommandError): pass

owner_id = '130070621034905600'

def is_owner_check(message):
	if message.author.id == owner_id:
		return True
	raise No_Owner()

def is_owner():
	return commands.check(lambda ctx: is_owner_check(ctx.message))

def check_permissions(ctx, perms):
	msg = ctx.message
	if msg.author.id == owner_id:
		return True
	ch = msg.channel
	author = msg.author
	resolved = ch.permissions_for(author)
	if all(getattr(resolved, name, None) == value for name, value in perms.items()):
		return True
	return False

def role_or_perm(t, ctx, check, **perms):
	if check_permissions(ctx, perms):
		return True
	ch = ctx.message.channel
	author = ctx.message.author
	if ch.is_private:
		return False
	role = discord.utils.find(check, author.roles)
	if role is not None:
		return True
	if t:
		return False
	else:
		raise No_Role()

# def role_or_perm(t, ctx, check, **perms):
#   if check_permissions(ctx, perms):
#     return True
#   ch = ctx.message.channel
#   author = ctx.message.author
#   if ch.is_private:
#     return False
#   role = discord.utils.find(check, author.roles)
#   if role is not None:
#     return True
#   if t == 0:
#     raise No_Mod()
#   elif t == 1:
#     raise No_Admin()
#   else:
#     raise No_Role()

admin_perms = ['administrator', 'manage_server']
mod_perms = ['manage_messages', 'ban_members', 'kick_members']

mod_roles = ('mod', 'moderator')
def mod_or_perm(**perms):
	def predicate(ctx):
		if ctx.message.channel.is_private:
			return True
		if role_or_perm(True, ctx, lambda r: r.name.lower() in mod_roles, **perms):
			return True
		for role in ctx.message.author.roles:
			role_perms = []
			for s in role.permissions:
				role_perms.append(s)
			for s in role_perms:
				for x in mod_perms:
					if s[0] == x and s[1] == True:
						return True
				for x in admin_perms:
					if s[0] == x and s[1] == True:
						return True
		raise No_Mod()
	return commands.check(predicate)

admin_roles = ('admin', 'administrator', 'mod', 'moderator', 'owner', 'god', 'manager', 'boss')
def admin_or_perm(**perms):
	def predicate(ctx):
		if ctx.message.channel.is_private:
			return True
		if role_or_perm(True, ctx, lambda r: r.name.lower() in admin_roles, **perms):
			return True
		for role in ctx.message.author.roles:
			role_perms = []
			for s in role.permissions:
				role_perms.append(s)
			for s in role_perms:
				for x in admin_perms:
					if s[0] == x and s[1] == True:
						return True
		raise No_Admin()
	return commands.check(predicate)

def is_in_servers(*server_ids):
	def predicate(ctx):
		server = ctx.message.server
		if server is None:
			return False
		return server.id in server_ids
	return commands.check(predicate)

def server_and_perm(ctx, *server_ids, **perms):
	if ctx.message.channel.is_private:
		return False
	server = ctx.message.server
	if server is None:
		return False
	if server.id in server_ids:
		if check_permissions(ctx, perms):
			return True
		return False
	raise No_ServerandPerm()

def sup(ctx):
	server = ctx.message.server
	if server.id == "197938366530977793":
		return True
	raise No_Sup()

def nsfw():
	def predicate(ctx):
		channel = ctx.message.channel
		if channel.is_private:
			return True
		name = channel.name.lower()
		if name == 'nsfw' or name == '[nsfw]':
			return True
		elif name == 'no-nsfw' or name == 'sfw':
			raise Nsfw()
		split = name.split()
		if 'nsfw' in name:
			try:
				i = split.index('nsfw')
			except:
				i = None
			if len(split) > 1 and i != None and split[i-1] != 'no':
				return True
			elif i is None:
				split = name.split('-')
				try:
					i = split.index('nsfw')
				except:
					i = None
				if len(split) > 1 and i != None and split[i-1] != 'no':
					return True
		if channel.topic != None:
			topic = channel.topic.lower()
			split = topic.split()
			if '{nsfw}' in topic or '[nsfw]' in topic or topic == 'nsfw':
				return True
			elif 'nsfw' in topic and 'sfw' not in split:
				try:
					i = split.index('nsfw')
				except:
					i = None
				if len(split) > 1 and i != None and split[i-1] != 'no':
					return True
				elif i is None:
					split = topic.split('-')
					try:
						i = split.index('nsfw')
					except:
						i = None
					if len(split) > 1 and i != None and split[i-1] != 'no':
						return True
		raise Nsfw()
	return commands.check(predicate)
