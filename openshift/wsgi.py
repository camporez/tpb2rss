#!/usr/bin/python2
# -*- coding: cp1252 -*-
from bs4 import BeautifulSoup
import os
import datetime
import urllib2
import tpb2rss

def feed_generator(path_info):
	try:
		xml = tpb2rss.xml_from_url(path_info, False)
		return xml
	except:
		return None

def main_body_generator(xml, path_info):
	html = "<!DOCTYPE html>"
	html += "\n<html lang=\"en\">"
	html += "\n<head>"
	html += "\n\t<meta charset=\"utf-8\" />"
	html += "\n\t<title>TPB2RSS - A RSS feed generator for ThePirateBay</title>"
	html += "\n\t<meta name=\"mobile-web-app-capable\" content=\"yes\">"
	html += "\n\t<meta name=\"HandheldFriendly\" content=\"True\" />"
	html += "\n\t<style type=\"text/css\">"
	html += "\n\t\tbody {"
	html += "\n\t\t\twidth: 100%;"
	html += "\n\t\t\theight: 100%;"
	html += "\n\t\t\tpadding: 0 0 0 0;"
	html += "\n\t\t\tmargin: 0 0 0 0;"
	html += "\n\t\t\tbackground: #4E818D; "
	html += "\n\t\t\tcolor: #fff;"
	html += "\n\t\t\tfont: 16px sans-serif; "
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t}\n"
	html += "\n\t\t.background {"
	html += "\n\t\t\theight: 100%;"
	html += "\n\t\t\twidth: 100%;"
	html += "\n\t\t\tbackground-image: -ms-radial-gradient(center, ellipse farthest-corner, #85DCF2 0%, #5B97A6 100%);"
	html += "\n\t\t\tbackground-image: -moz-radial-gradient(center, ellipse farthest-corner, #85DCF2 0%, #5B97A6 100%);"
	html += "\n\t\t\tbackground-image: -o-radial-gradient(center, ellipse farthest-corner, #85DCF2 0%, #5B97A6 100%);"
	html += "\n\t\t\tbackground-image: -webkit-gradient(radial, center center, 0, center center, 498, color-stop(0, #85DCF2), color-stop(1, #5B97A6));"
	html += "\n\t\t\tbackground-image: -webkit-radial-gradient(center, ellipse farthest-corner, #85DCF2 0%, #5B97A6 100%);"
	html += "\n\t\t\tbackground-image: radial-gradient(ellipse farthest-corner at center, #85DCF2 0%, #5B97A6 100%);"
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t}\n"
	html += "\n\t\t#container {"
	html += "\n\t\t\theight: 350px;"
	html += "\n\t\t\twidth: 500px;"
	html += "\n\t\t\ttop: 50%;"
	html += "\n\t\t\tleft: 50%;"
	html += "\n\t\t\tmargin-top: -175px;"
	html += "\n\t\t\tmargin-left: -250px;"
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t}\n"
	html += "\n\t\theader {"
	html += "\n\t\t\twidth: 100%;"
	html += "\n\t\t\tmargin: 0px auto;"
	html += "\n\t\t}\n"
	html += "\n\t\th1 {"
	html += "\n\t\t\ttext-align: center;"
	html += "\n\t\t\tcolor: #fff;"
	html += "\n\t\t\tline-height: 95px;"
	html += "\n\t\t\tfont-size: 95px;"
	html += "\n\t\t\tfont-family: \"Impact\", sans-serif;"
	html += "\n\t\t\tfont-weight: bolder;"
	html += "\n\t\t\ttext-shadow: #253e45 -1px 1px 0,"
	html += "\n\t\t\t\t#253e45 -2px 2px 0;"
	html += "\n\t\t\tmargin: 70px 0 0 0;"
	html += "\n\t\t\tdisplay: block;"
	html += "\n\t\t}\n"
	html += "\n\t\ta {"
	html += "\n\t\t\tcolor: #555;"
	html += "\n\t\t\ttext-decoration: none;"
	html += "\n\t\t}\n"
	html += "\n\t\t#search-box {;"
	html += "\n\t\t\t-webkit-border-radius: 5px;"
	html += "\n\t\t\t-moz-border-radius: 5px;"
	html += "\n\t\t\tborder-radius: 5px;"
	html += "\n\t\t\tbackground-color: #fff;"
	html += "\n\t\t\ttext-align: center;"
	html += "\n\t\t\twidth: 500px;"
	html += "\n\t\t\theight: 42px;"
	html += "\n\t\t\tline-height: 42px;"
	html += "\n\t\t\tleft: 50%;"
	html += "\n\t\t\tmargin-top: 10px;"
	html += "\n\t\t\tmargin-left: -250px;"
	html += "\n\t\t\tposition: relative;"
	html += "\n\t\t}\n"
	html += "\n\t\t#search-text {"
	html += "\n\t\t\tfont-size: 14px;"
	html += "\n\t\t\tcolor: #ddd;"
	html += "\n\t\t\tborder-width: 0;"
	html += "\n\t\t\tbackground: transparent;"
	html += "\n\t\t}\n"
	html += "\n\t\t#search-box input[type=\"text\"] {"
	html += "\n\t\t\tmargin-top: 0px;"
	html += "\n\t\t\tmargin-left: -100px;"
	html += "\n\t\t\twidth: 380px;"
	html += "\n\t\t\tpadding: 11px 0 12px 1em;"
	html += "\n\t\t\tcolor: #333;"
	html += "\n\t\t\toutline: none;"
	html += "\n\t\t}\n"
	html += "\n\t\t#search-button {"
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t\ttop: 0;"
	html += "\n\t\t\tright: 0;"
	html += "\n\t\t\theight: 42px;"
	html += "\n\t\t\tline-height: 42px;"
	html += "\n\t\t\twidth: 100px;"
	html += "\n\t\t\tfont-size: 14px;"
	html += "\n\t\t\tcolor: #fff;"
	html += "\n\t\t\ttext-transform: uppercase;"
	html += "\n\t\t\ttext-align: center;"
	html += "\n\t\t\tborder-width: 0;"
	html += "\n\t\t\tbackground-color: #243C42;"
	html += "\n\t\t\t-webkit-border-radius: 0px 5px 5px 0px;"
	html += "\n\t\t\t-moz-border-radius: 0px 5px 5px 0px;"
	html += "\n\t\t\tborder-radius: 0px 5px 5px 0px;"
	html += "\n\t\t\tcursor: pointer;"
	html += "\n\t\t}\n"
	html += "\n\t\t#message {"
	html += "\n\t\t\twidth: 120px;"
	html += "\n\t\t\tpadding: 8px 8px;"
	html += "\n\t\t\tcolor: #b94a48;"
	html += "\n\t\t\ttext-align: center;"
	html += "\n\t\t\tmargin-top: 40px;"
	html += "\n\t\t\tmargin-left: 190px;"
	html += "\n\t\t\tbackground-color: #f2dede;"
	html += "\n\t\t\ttext-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);"
	html += "\n\t\t\tborder: 1px solid #fbeed5;"
	html += "\n\t\t\t-webkit-border-radius: 4px;"
	html += "\n\t\t\t-moz-border-radius: 4px;"
	html += "\n\t\t\tborder-radius: 4px;"
	html += "\n\t\t\tposition: relative;"
	html += "\n\t\t}\n"
	html += "\n\t\t#github {"
	html += "\n\t\t\twidth: auto;"
	html += "\n\t\t\tright: 10px;"
	html += "\n\t\t\ttop: 20px;"
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t}\n"
	html += "\n\t\t#github iframe {"
	html += "\n\t\t\twidth: 90px;"
	html += "\n\t\t\theight: 30px;"
	html += "\n\t\t}\n"
	html += "\n\t\t#extensions {"
	html += "\n\t\t\twidth: auto;"
	html += "\n\t\t\ttext-align: right;"
	html += "\n\t\t\tright: 20px;"
	html += "\n\t\t\tbottom: 20px;"
	html += "\n\t\t\tposition: absolute;"
	html += "\n\t\t}\n"
	html += "\n\t\t#extensions span {"
	html += "\n\t\t\tdisplay: block;"
	html += "\n\t\t}\n"
	html += "\n\t\t@media screen and (max-width: 640px) {"
	html += "\n\t\t\th1 {"
	html += "\n\t\t\t\tfont-size: 60px;"
	html += "\n\t\t\t}\n"
	html += "\n\t\t\t#container {"
	html += "\n\t\t\t\twidth: 320px;"
	html += "\n\t\t\t\tmargin-left: -160px;"
	html += "\n\t\t\t}\n"
	html += "\n\t\t\t#search-box {"
	html += "\n\t\t\t\twidth: 310px;"
	html += "\n\t\t\t\tmargin-left: -155px;"
	html += "\n\t\t\t}\n"
	html += "\n\t\t\t#search-box input[type=\"text\"] {"
	html += "\n\t\t\t\twidth: 190px;\t\t\t"
	html += "\n\t\t\t}\n"
	html += "\n\t\t\t#message {"
	html += "\n\t\t\t\tmargin-left: 100px;"
	html += "\n\t\t\t}"
	html += "\n\t\t}"
	html += "\n\t</style>"
	html += "\n\t<!--[if IE]><script src=\"http://html5shiv.googlecode.com/svn/trunk/html5.js\"></script><![endif]-->"
	html += "\n\t<script>"
	html += "\n\tfunction changetext(){"
	html += "\n\t\tif (document.getElementById(\"search-button\").innerHTML == \"Open feed\"){"
	html += "\n\t\t\twindow.open(document.getElementById(\"search-text\").value, \"_blank\");"
	html += "\n\t\t} else {"
	html += "\n\t\t\tdocument.getElementById(\"search-button\").innerHTML = \"Open feed\";"
	html += "\n\t\t\tvar url = window.location.protocol + \"//\" + window.location.host + \"/\";"
	html += "\n\t\t\tvar input = document.getElementById(\"search-text\").value;"
	html += "\n\t\t\tvar input = input.replace(/^((http)s{0,1}:\/\/(www.){0,1}){0,1}thepiratebay\.[a-z]{1,}\//gi, \"\");"
	html += "\n\t\t\tif ((input.substring(0, 7) != \"search/\") && (input.substring(0, 7) != \"browse/\") && (input.substring(0, 5) != \"user/\")) {"
	html += "\n\t\t\t\tvar input = input.replace(/\/|\s|&|%|#|>|</g, \"%20\").replace(\"?\", \"%3F\").replace(/^(%20)(%20)*/, \"\").replace(/(%20)(%20)*$/, \"\");"
	html += "\n\t\t\t\tvar input = \"search/\" + input;"
	html += "\n\t\t\t};"
	html += "\n\t\t\tif (input.substring(7, url.length + 7) != url) {"
	html += "\n\t\t\t\tdocument.getElementById(\"search-text\").value = url + input;"
	html += "\n\t\t\t};"
	html += "\n\t\t}"
	html += "\n\t\tdocument.getElementById(\"search-text\").focus();"
	html += "\n\t\tdocument.getElementById(\"search-text\").select();"
	html += "\n\t}"
	html += "\n\tfunction checkcontent(){"
	html += "\n\t\tvar url = window.location.protocol + \"//\" + window.location.host + \"/\";"
	html += "\n\t\tvar input = document.getElementById(\"search-text\").value;"
	html += "\n\t\tif ((input.length > url.length) && (input.substring(0, url.length ) == url)) {"
	html += "\n\t\t\tdocument.getElementById(\"search-button\").innerHTML = \"Open feed\";"
	html += "\n\t\t} else {"
	html += "\n\t\t\tdocument.getElementById(\"search-button\").innerHTML = \"Generate\";"
	html += "\n\t\t};"
	html += "\n\t}"
	html += "\n\t</script>"
	html += "\n</head>"
	html += "\n<body>"
	html += "\n\t<div class=\"background\"></div>"
	html += "\n\t<div id=\"github\">"
	html += "\n\t\t<iframe src=\"http://ghbtns.com/github-btn.html?user=camporez&repo=tpb2rss&type=watch&count=true\" height=\"30\" width=\"118\" frameborder=\"0\" scrolling=\"0\" allowTransparency=\"true\"></iframe>"
	html += "\n\t\t<iframe src=\"http://ghbtns.com/github-btn.html?user=camporez&repo=tpb2rss&type=fork&count=true\" height=\"30\" width=\"118\" frameborder=\"0\" scrolling=\"0\" allowTransparency=\"true\"></iframe>"
	html += "\n\t</div>"
	html += "\n\t<div id=\"container\">"
	html += "\n\t\t<header>"
	html += "\n\t\t\t<h1>TPB2RSS</h1>"
	html += "\n\t\t</header>"
	html += "\n\t\t<div id=\"search-box\">"
	html += "\n\t\t\t<form method=\"post\" onsubmit=\"changetext(); return false;\">"
	html += "\n\t\t\t\t<input id=\"search-text\" type=\"text\" placeholder=\"Type a search term or paste a TPB link in here\" onkeyup=\"checkcontent();\" autocomplete=\"off\" autofocus required />"
	html += "\n\t\t\t\t<button type=\"submit\" id=\"search-button\">Generate</button>"
	html += "\n\t\t\t</form>"
	html += "\n\t\t</div>"
	if xml == None:
		html += "\n\t\t<div id=\"message\">Page not found</div>"
	html += "\n\t</div>"
	html += "\n\t<div id=\"extensions\">"
	html += "\n\t\t<span>Bookmarklet: <a href=\"javascript:!function(){if(/^((http)s{0,1}:\/\/(www.){0,1}){0,1}thepiratebay\.[a-z]+\/(search\/(.)+|user\/(.)+|browse\/[0-9]+|recent)+/.test(location.href)){if(/^((http)s{0,1}:\/\/(www.){0,1}){0,1}thepiratebay\.[a-z]+\/browse\/[0-9]+/.test(location.href))var%20t=%22http://rss.thepiratebay.se/%22+window.location.pathname.split(%22/%22)[2];else%20if(/^((http)s{0,1}:\/\/(www.){0,1}){0,1}thepiratebay\.[a-z]+\/user\/(.)+/.test(location.href))var%20t=document.getElementsByClassName(%22rss%22)[0].href;else%20var%20t=document.URL,t=t.replace(/^((http)s{0,1}:\/\/(www.){0,1}){0,1}thepiratebay\.[a-z]{1,}\//gi,%22http://tpb.camporez.com/%22);window.open(t,%22_blank%22)}}();\" class=\"bookmarklet\" alt=\"TPB2RSS\">TPB2RSS</a></span>"
	html += "\n\t\t<span>Chrome: <a href=\"https://github.com/camporez/tpb2rss/tree/master/chrome\">Get extension</a></span>"
	html += "\n\t\t<span>Firefox: <a href=\"https://openuserjs.org/scripts/camporez/TPB2RSS\">Greasemonkey script</a></span>"
	html += "\n\t</div>"
	html += "\n</body>"
	html += "\n</html>"
	return html

def application(environ, start_response):
	status = "200 OK"

	if (( environ['PATH_INFO'] == "") or ( environ['PATH_INFO'] == "/" )):
		xml = False
	else:
		xml = feed_generator(environ['PATH_INFO'])
	if xml:
		ctype = 'text/xml'
		response_body = xml
	else:
		ctype = 'text/html'
		status = "404 Not Found"
		response_body = main_body_generator(xml, environ['PATH_INFO'])

	response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]
