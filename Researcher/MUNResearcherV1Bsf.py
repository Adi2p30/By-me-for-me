import requests
from bs4 import BeautifulSoup
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter

def search_document(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": "YOUR_API_KEY",
        "cx": "YOUR_SEARCH_ENGINE_ID",
        "q": query,
        "num": 3,  # Number of search results to retrieve
    }
    response = requests.get(url, params=params)
    data = response.json()
    urllist = []
    if "items" in data:
        urllist.append(data["items"][0]["link"])
        urllist.append(data["items"][1]["link"])
        urllist.append(data["items"][2]["link"])
        return urllist
    return None

user_input = input("Enter your query: ")
document_url = search_document(user_input)
if document_url:
    print("Found a relevant document:", document_url)
else:
    print("No relevant document found.")

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def get_most_occurring_proper_nouns(text, top_n=5):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    proper_nouns = [word for word, pos in tagged_words if pos == 'NNP']
    most_common_proper_nouns = Counter(proper_nouns).most_common(top_n)
    return most_common_proper_nouns

def print_paragraphs_with_proper_nouns(text, proper_nouns):
    paragraphs = text.split('\n\n')  # Split text into paragraphs

    for noun, _ in proper_nouns:
        print("Paragraphs with", noun + ":")
        for paragraph in paragraphs:
            if noun in paragraph:
                print(paragraph)
                print()

def makespeech(information, portfolio):
    #non API version (Using ChatGPT)
    print("Paste this in Bard")
    print("Give me 5 detailed points on " + information)
    print("Paste this in chatGPT + the response you got from bard")
    print("Write an MUN speech as " + portfolio + " on these topics " + information + " INCORPORATE AND ADD THE FOLLOWING POINTS (paste bard output here)" )

def pdfs_and_text_extraction(topic):
    inp = ""
    version = 1
    while inp != "end":
        inp = input("What topic do you want to research about today")
        urllist = search_document(inp)
        for i in range(0,len(urllist)):
            response = requests.get(urllist[i])
            pdf_content = response.content
            pdf_file_path = 'V' + str(version) + "_pdf" + str(i) + ".pdf"
            with open(pdf_file_path, 'wb') as file:
                file.write(pdf_content)
            pdf_text = extract_text_from_pdf(pdf_file_path)
            common_proper_nouns = get_most_occurring_proper_nouns(pdf_text)
            print("Most occurring proper nouns in " + pdf_file_path + " are:")
            for noun, count in common_proper_nouns:
                print(noun, "-", count)
                print("The most prominent paragraphs maybe")
                print_paragraphs_with_proper_nouns(pdf_content, noun)
                print("-----------------(NEXT PROPER NOUN)---------------")
            print("====================================")

def main():
    portfolio = input("What is your country")
    agenda = input("What is the agenda")
    committee = input("what is your committee")
    otherportfolios = []
    while text != "end":
        text = input("What other countries are there?, put 'end' if ur done ")
        otherportfolios.append(text)

def make_POI(agenda, country):
    print("")

def getROP():
    print("Committee proceedings")
    print("In the conference the rules of procedure are as follows:\n")

    print("1. Roll call:-")
    print(
        "The roll call is something that will take place every day or every session of the MUN. You have 2 options when the Executive Board calls out your portfolio")
    print(
        "- Present - This means that you are present in committee and when it comes time to vote on documentation towards the end of the committee you will have the option to abstain from the document meaning you either agree or disagree with the points put forward by the document.")
    print(
        "- Present and Voting - Means that you are present in committee and you have decided that you will be voting yes or no in the documentation put forward and you won't have the right to abstain. There’s a lot more pressure to present and voting, and in the heat of the moment, you could go with the general consensus, but be sure to form your own opinion and go against the grain if you think it’s the right choice.\n")

    print("2. GSL:-")
    print(
        "The General speakers list is an inexhaustible list that consists of delegates giving speeches with a default time of 90 seconds. These speeches are generally based on the agenda and not on specific topics, but the delegate may choose to do so. One feature about the general speakers list is that you have the option to yield time, something you cannot do in other speeches.")
    print(
        "The GSL is typically used during committee sessions, and it allows delegates to sign up to speak on a particular issue or to address the committee more generally.")
    print(
        "To sign up for the GSL, a delegate typically raises their placard or hand and requests the floor from the chair. The chair will then add the delegate's name to the GSL, and the delegate will be given a set amount of time to speak when their turn comes. The GSL is typically organized in the order in which delegates signed up, and the chair will call on each delegate in turn.")
    print(
        "The GSL is an important part of the MUN process, as it allows all delegates to have an opportunity to speak and to contribute to the discussions of the committee. Delegates should be aware of the GSL and be prepared to speak when their turn comes.")
    print(
        "Yielding - refers to the process of giving up the floor to another delegate during a committee session. Yielding may be done for a variety of reasons, such as to allow another delegate to speak, to ask a question, or to make a point of order.")
    print("You have 4 options to yield:")
    print(
        "- Yield to the chair - This means that you wish to give the remaining time to the chair, and the chair may have questions or comments to make, but usually, the chair will skip the time and move on.")
    print(
        "- Yield to another delegate - This means that you wish to give time in your speech to another delegate. This may be done to show alliance and teamwork in speeches. Prior notice is usually given to the delegate.")
    print(
        "- Yield to Comments - This means that you wish to give your time to comments that delegates might have on the speech you just gave.")
    print(
        "- Yield to Questions - This means that you wish to give your time to questions that delegates might have to ask on the speech you just gave.\n")

    print("MOTIONS:-")
    print("These are usually asked for between every 3-4 GSL speeches")
    print("The types of Motions are:\n")

    print("3. Moderated Caucus:-")
    print(
        "A moderated caucus is a type of discussion in which the chair of the committee moderates and maintains order. During a moderated caucus, each delegate is given a set amount of time to speak, and the chair ensures that all delegates have an opportunity to contribute to the discussion.")
    print(
        "Moderated caucuses are typically used when the committee needs to discuss a specific issue in depth or when delegates need to reach an agreement on a resolution. It is also used to discuss specific subtopics in the vaguer agenda. They allow for a more structured and controlled discussion than an unmoderated caucus, in which delegates are free to speak at any time, and the conversation may be less focused.")
    print(
        "The verbatim to ask for a moderated caucus when the chair asks for a motion is: The delegate of ___ would like to move into a moderated caucus with topic ___ total time ___ and per speaker time ___")
    print(
        "the total time should be divisible by the per speaker time such that the number of speakers is in whole numbers.\n")

    print("4. Unmoderated Caucus:-")
    print(
        "An unmoderated caucus is a type of discussion in which the delegates are free to speak and discuss issues without the chair moderating the conversation. During an unmoderated caucus, each delegate is free to speak at any time, and there is no set time limit for each delegate's remarks.")
    print(
        "Unmoderated caucuses are typically used when the committee needs to have a general discussion on a particular issue or when delegates need to informally discuss a resolution before it is formally introduced. They allow for a more informal and less structured discussion than a moderated caucus, in which the chair moderates the conversation and maintains order.")
    print(
        "Unmoderated caucuses can be useful for allowing delegates to get a sense of the opinions and positions of other countries on an issue, but they may not be as productive as moderated caucuses in terms of coming to a consensus or making progress on a specific resolution.")
    print("Yet this does not mean that this doesn't affect the chair's mentality about participation in the committee.")
    print(
        "This time is usually used to lobby delegates, but towards the end of the MUN, unmoderated caucuses can also be used to discuss and create documentation.")
    print(
        "The verbatim to ask for an unmoderated caucus is: The delegate of __ would like to move into an unmoderated caucus with total time __\n")

    print("Extension motions:-")
    print(
        "Usually used to extend moderated caucuses or unmoderated caucuses, they must be less or equal to half of the time of the original motion.")
    print(
        "The verbatim to ask for an extension caucus is: (the delegate of ___ would like to extend the (moderated/unmoderated) caucus with time\n")

    print("Discretion of Motions:")
    print(
        "When the chair asks for motions, there are multiple delegates that will raise moderated or unmoderated caucuses, and if a delegate changes the per speaker time and the total time, the moderated caucus that accommodates the most speakers will be voted upon first.")
    print("If there is an unmoderated caucus raised, then it will always be voted upon first.")
    print("Though this is not always followed, and chairs usually decide the order upon their discretion.\n")

    print("5. Points:-")
    print("a. Point of Parliamentary inquiry:-")
    print("Asking a question on ROP or the chair during a committee session")
    print("b. Point of personal privilege:")
    print(
        "Used for personal problems (go slower, faster and speak louder, etc. my net was lagging, could you please repeat?)")
    print("c. Points of Order:")
    print("i. Mistake in the ROP")
    print("ii. It also may be used to state out a Factual Inaccuracy, which could lead to a lot of marks.")
    print("d. Right to reply:-")
    print("A right to reply may be used when")
    print("ii. When a delegate personally attacks you as a delegate")
    print("iii. When the sovereignty of your country is affected\n")

    print("6. Documentation:-")
    print(
        "Documentation is the final result of the committee, all that is discussed in the form of solutions to the main agenda consists of documentation. The 4 main types of documentation are:")
    print("a. Draft Resolution: a formal document with all your solutions")
    print("b. Working Papers: informal document with all your solutions")
    print("c. Press Release: An informal document sent to the press")
    print("d. Communique: a formal document which needs to be agreed unanimously\n")

    print("7. Mandate:- The expected result and discussion method of a particular committee\n")

    print("8. Chits:- Used for communication informally to other delegates in a written format")

def makeDR(solutions):
    
