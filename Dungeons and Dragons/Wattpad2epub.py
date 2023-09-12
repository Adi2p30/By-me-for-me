#! /usr/bin/python3
"""
# Python Script to Scrape Wattpad Story and convert to Epub and html file.
# By Architrixs, Created Nov 5, 2020.
# This program will create:
# 1. A html file of the entire Wattpad Book AND (You can directly Use this one to read, Images are preserved in this format.)
# 2. A Epub file of the entire Wattpad Book.(The Epub will have separate marked Chapters instead of all chapters as one whole.)

HOW TO USE :
1. Just copy the URL of any Chapter of the Wattpad Book. I repeat copy URL of any "Chapter"... you got it!
2. Either Directly Run 
	>>Wattpad2epub.py
   or	>>Wattpad2epub.py Story_url

   Yes it can take 1 Commandline Argument as the copied url of the Story.
3. You got html and epub saved in the same location.
"""
import argparse
import json
import bs4
import requests
import pyperclip
import re
import pypandoc
import os

base_apiV2_url = "https://www.wattpad.com/apiv2/"
base_apiV3_url = "https://www.wattpad.com/api/v3/"
dev_error_msg = "Please check the url again, for valid story id. Contact the developer if you think this is a bug."
"""
https://www.wattpad.com/api/v3/stories/{{story_id}}?drafts=0&mature=1&include_deleted=1&fields=id,title,createDate,modifyDate,voteCount,readCount,commentCount,description,url,firstPublishedPart,cover,language,isAdExempt,user(name,username,avatar,location,highlight_colour,backgroundUrl,numLists,numStoriesPublished,numFollowing,numFollowers,twitter),completed,isPaywalled,paidModel,numParts,lastPublishedPart,parts(id,title,length,url,deleted,draft,createDate),tags,categories,rating,rankings,tagRankings,language,storyLanguage,copyright,sourceLink,firstPartId,deleted,draft,hasBannedCover,length
"""


def get_chapter_id(url):
    """Extracts the chapter ID from the given URL."""
    search_id = re.compile(r'\d{5,}')
    id_match = search_id.search(url)
    if id_match:
        return id_match.group()
    return None


def download_webpage(url):
    """Downloads the webpage content from the given URL."""
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        return res.text
    except requests.exceptions.RequestException as exc:
        print("There was a problem: %s" % (exc))
        return None


def extract_useful_data(json_data):
    """Extracts useful data from the JSON response."""
    summary = json_data.get('description', '')
    tags = json_data.get('tags', '')
    chapters = json_data.get('parts', '')
    storyName = json_data.get('title', '')
    author = json_data.get('user', '')
    cover = json_data.get('cover', '')
    return summary, tags, chapters, storyName, author, cover

def beautifyandprint(file_name, story_name, author, cover, tags, summary, chapters):
    for i, chapter in enumerate(chapters):
        chapter_url = base_apiV2_url + f"storytext?id={chapter['id']}"
        chapter_content = download_webpage(chapter_url)
        if chapter_content:
            soup_res = bs4.BeautifulSoup(chapter_content, 'html.parser')
            print({chapter['title']} +"\n\n" + soup_res.prettify())

def save_epub_file(html_file, story_name, cover):
    """Converts the HTML file to EPUB format and saves it."""
    print("Generating EPUB...")
    story_name = story_name.replace('/', ' ')
    cover_image = f"{story_name}.jpg"
    res_img = requests.get(cover, headers={'User-Agent': 'Mozilla/5.0'})
    open(cover_image, 'wb').write(res_img.content)
    output_file = f"{story_name}.epub"

    pypandoc.convert_file(html_file, 'epub3', outputfile=output_file,
                          extra_args=['--epub-chapter-level=2', f'--epub-cover-image={cover_image}'], sandbox=False)

    os.remove(cover_image)
    print(f"Saved {output_file}")


def main(storyid):
    story_id = storyid
    if not story_id:
        print(dev_error_msg)

    # Getting JSON data from Wattpad API.
    story_info_url = base_apiV3_url + f"stories/{story_id}?drafts=0&mature=1&include_deleted=1&fields=id,title,createDate,modifyDate,description,url,firstPublishedPart,cover,language,user(name,username,avatar,location,numStoriesPublished,numFollowing,numFollowers,twitter),completed,numParts,lastPublishedPart,parts(id,title,length,url,deleted,draft,createDate),tags,storyLanguage,copyright"
    json_data = requests.get(story_info_url, headers={'User-Agent': 'Mozilla/5.0'}).json()
    usefuljsondata = extract_useful_data(json_data)
    out_file = open("quotes.json", "w")
    json.dump(usefuljsondata, out_file, indent=1)

    usefuljsondata

main("83999527")
