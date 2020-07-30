import random

## Greetings
''' The bot greets the user back '''

GREETING_KEYWORDS = ["hello", "hi", "hey", "heyo", "what's up", "whats up"]

GREETING_RESPONSES = ["Hi there.", "How do you feel?", "Is something troubling you?", "Good to hear from you today.", "How are you doing?", "Want to talk about something?", "Are you here for your appointment?"]

## Farewells
''' The bot says a farewell when the user quits '''

FAREWELL_KEYWORDS = ["bye", "goodbye", "quit", "end", "good night", "adios"]

FAREWELL_RESPONSES = ["Take care.", "Nice talking with you.", "All the best.", "Thanks for stopping by."]

## Generic
''' The bot encourages the user to continue talking '''

NEUTRAL_NONE_RESPONSES = ["Tell me more.", "I'm listening.", "Please go on."]

NEGATIVE_NONE_RESPONSES = ["I'm sorry to hear.", "I'm here to listen.", "I'm here for you."]

POSITIVE_NONE_RESPONSES = ["That's good to hear.", "Glad to hear it.", "That's nice."]


## Bot is Noun or Adjective
''' The bot deflects comments about itself '''

BOT_VERBS_PNOUN = [
    "I don't know much about {noun}.",
    "Do you know a lot about {noun}?",
    "I'm not an expert on {noun}, tell me more.",
]

BOT_VERBS_SNOUN= [
    "Do I seem like {noun}?",
    "What makes you think that?"
]

BOT_VERBS_ADJECTIVE = [
    "Do you think so?",
    "This isn't about me, though.",
    "This is about you, not me.",
    "What about you?",
    "If you think so, I'll take note of that."
]


## I am Noun or Adjective
''' The bot inquires further about user's view of themselves '''

NEUTRAL_YOU_ARE_NOUN = [
    "Oh, {noun}? Tell me more."
]
NEGATIVE_YOU_ARE_NOUN = [
    "Hmm. Why do you consider yourself so?",
    "You aren't though. Why do you feel this way?"
]
POSTIVE_YOU_ARE_NOUN = [
    "That's cool. Can you tell me more about being {noun}?",
    "How'd you become a {noun}? I'd like to hear."
]

NEUTRAL_YOU_ARE_ADJ= [
    "How long have you been {adjective}?"
]
NEGATIVE_YOU_ARE_ADJ= [
    "How long have you been feeling {adjective}?",
    "Can you further explain what made you feel {adjective}?"
]
POSITIVE_YOU_ARE_ADJ= [
    "Yes, you seem very {adjective}.",
    "When'd you notice you are {adjective}?",
    "What makes you feel {adjective}?"
]

## I verb Noun
''' The bot inquired further about user's opinion of something '''

NEUTRAL_YOU_VERB_NOUN = [
    "Tell me about why you {verb} {noun}.",
    "How does {noun} make you feel?"
]
NEGATIVE_YOU_VERB_NOUN = [
    "Why do you {verb} {noun}?"
]
POSTIVE_YOU_VERB_NOUN = [
    "Tell me more about {noun}."
]

## Crisis

''' These hard-coded phrases will immediately direct user to human help '''

BAD_WORDS = ["kill myself", "killing myself", "hurt myself", "hurting myself", "harm myself", "harming myself", "cut myself", "cutting myself", "kms"]

CRISIS_RESPONSES = [
    "I'm sorry, have you considered getting human help? An online chat for suicide prevention can be found at 'https://suicidepreventionlifeline.org/chat/'",
    "Are you in crisis? Please consider getting human help. An online chat for suicide prevention can be found at 'https://suicidepreventionlifeline.org/chat/'"
]