"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story('example', ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""

        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


def get_story(title):
    for story in stories:
        if story.title == title:
            return story

stories = []

stories.append(Story(
    "goobers'n'goblins",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
))

stories.append(Story(
    "all's well that ends well",
    ["plural_noun", "adjective", "adverb", "person", "verb", "pronoun"],
    """The {plural_noun} ate their deviled eggs as would a {adjective} beast! But it made them {adverb} grow tired.
     {person} would not approve! To {verb} is to do the lord's work, {pronoun} would say."""))

stories.append(Story(
    'time to put the baby to bed!',
    ['plural_noun', 'color', 'noun', 'adjective', 'place'],
    """Travel warning!!! Down in the {plural_noun}, nothing is what it seems.Rivers run red, flowers bloom {color},
     the {noun} is even {adjective}! I think I'll stick to vacationing in {place}!"""))