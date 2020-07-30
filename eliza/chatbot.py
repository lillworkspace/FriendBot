import random
from textblob import TextBlob
from responses import *

## Look for sentence patterns

def look_for_bad_words(sentence):
    for word in BAD_WORDS:
        if word in sentence:
            return random.choice(CRISIS_RESPONSES)

def look_for_greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)

def look_for_farewell(sentence):
    for word in sentence.split():
        if word.lower() in FAREWELL_KEYWORDS:
            return random.choice(FAREWELL_RESPONSES)

def look_for_comment_about_bot(pronoun, noun, adjective, p):
    resp = None
    if pronoun == 'I' and (noun or adjective):
        if noun:
            if random.choice((True, False)):
                resp = random.choice(BOT_VERBS_PNOUN).format(**{'noun': noun.pluralize()})
            else:
                a_ = "an" if starts_with_vowel(noun) else "a"
                noun = a_ + " " + noun
                resp = random.choice(BOT_VERBS_SNOUN).format(**{'noun': noun})
        else:
            resp = random.choice(BOT_VERBS_ADJECTIVE).format(**{'adjective': adjective})
            if p == 1:
                resp = "Thank you. " + resp
    return resp

def look_for_comment_about_self(pronoun, noun, adjective, verb, p):
    resp = None
    if pronoun == 'You' and (noun or adjective):
        if noun:
            if verb[0] in ('be', 'am', 'is', "'m"):
                a_ = "an" if starts_with_vowel(noun) else "a"
                noun = a_ + " " + noun
                if p == 0:
                    resp = random.choice(NEUTRAL_YOU_ARE_NOUN).format(**{'noun': noun})
                if p < 0:
                    resp = random.choice(NEGATIVE_YOU_ARE_NOUN).format(**{'noun': noun})
                if p > 0:
                    resp = random.choice(POSTIVE_YOU_ARE_NOUN).format(**{'noun': noun})
            else:
                if p == 0:
                    resp = random.choice(NEUTRAL_YOU_VERB_NOUN).format(**{'noun': noun}, **{'verb': verb[0]})
                if p < 0:
                    resp = random.choice(NEGATIVE_YOU_VERB_NOUN).format(**{'noun': noun}, **{'verb': verb[0]})
                if p > 0:
                    resp = random.choice(POSTIVE_YOU_VERB_NOUN).format(**{'noun': noun}, **{'verb': verb[0]})

        if adjective:
            if verb[0] in ('be', 'am', 'is', "'m"):
                if p == 0:
                    resp = random.choice(NEUTRAL_YOU_ARE_ADJ).format(**{'adjective': adjective})
                if p < 0:
                    resp = random.choice(NEGATIVE_YOU_ARE_ADJ).format(**{'adjective': adjective})
                if p > 0:
                    resp = random.choice(POSITIVE_YOU_ARE_ADJ).format(**{'adjective': adjective})

    return resp

def choose_random_none_choice(p):
    if p == 0:
        resp = random.choice(NEUTRAL_NONE_RESPONSES)
    elif p == -1:
        resp = random.choice(NEGATIVE_NONE_RESPONSES)
    elif p == 1:
        resp = random.choice(POSITIVE_NONE_RESPONSES)
    return resp


## Find parts of speech

def find_pronoun(sent):
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            pronoun = 'You'
    return pronoun

def find_verb(sent):
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos

def find_noun(sent):
    noun = None
    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # noun
                noun = w
                break
    return noun

def find_adjective(sent):
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # adjective
            adj = w
            break
    return adj

## Preprocessing

def preprocess_text(sentence):
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I'm"
        cleaned.append(w)
    return ' '.join(cleaned)

def find_candidate_parts_of_speech(parsed):
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sent in parsed.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    return pronoun, noun, adjective, verb

def starts_with_vowel(word):
    return True if word[0] in 'aeiou' else False

def determine_polarity(parsed):
    sentiment = parsed.sentiment
    if sentiment.polarity == 0.0:
        return 0
    elif sentiment.polarity < 0.0:
        return -1
    elif sentiment.polarity > 0.0:
        return 1


## Make a response

def respond(sentence):

    if sentence == '':
        resp = random.choice(START_RESPONSES)
        return resp

    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)

    p = determine_polarity(parsed)

    pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)

    resp = look_for_bad_words(parsed)

    if not resp:
        resp = look_for_greeting(parsed)
    if not resp:
        resp = look_for_farewell(parsed)
    if not resp:
        resp = look_for_comment_about_self(pronoun, noun, adjective, verb, p)
    if not resp:
        resp = look_for_comment_about_bot(pronoun, noun, adjective, p)
    if not resp:
        resp = choose_random_none_choice(p)
    return resp
