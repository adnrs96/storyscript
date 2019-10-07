# -*- coding: utf-8 -*-
import json

from .Bundle import Bundle
from .Story import Story
from .exceptions import StoryError
from .parser import Grammar


class App:
    """
    Exposes functionalities for internal use e.g the command line
    """

    @staticmethod
    def parse(path=None, ignored_path=None, story=None,
              ebnf=None, lower=False, features=None):
        """
        Parses stories found in path or a given story, returning their tree(s)
        """
        if story is not None:
            bundle = Bundle.from_string(story, features=features)
        else:
            bundle = Bundle.from_path(path, ignored_path=ignored_path,
                                      features=features)
        return bundle.bundle_trees(ebnf=ebnf, lower=lower)

    @staticmethod
    def format(path=None, story=None, ebnf=None, features=None, inplace=False):
        """
        Parses stories found in path, returning the formatted source
        """
        parser = Bundle.parser(ebnf=ebnf)
        if story is not None:
            _story = Story(story, features=features)
        else:
            _story = Story.from_file(path, features=features)
        output = _story.parse(parser=parser).format()
        if inplace and story is None:
            with open(path, 'w') as w:
                w.write(output)
            return None

        return output

    @staticmethod
    def compile(path=None, ignored_path=None, story=None, ebnf=None,
                concise=False, first=False, features=None):
        """
        Parses and compiles stories found in path, returning JSON
        """
        if story is not None:
            bundle = Bundle.from_string(story, features=features)
        else:
            bundle = Bundle.from_path(path, ignored_path=ignored_path,
                                      features=features)
        result = bundle.bundle(ebnf=ebnf)
        if concise:
            result = _clean_dict(result)
        if first:
            if len(result['stories']) != 1:
                raise StoryError.create_error('first_option_more_stories')
            result = next(iter(result['stories'].values()))
        return json.dumps(result, indent=2)

    @staticmethod
    def lex(path=None, features=None, story=None, ebnf=None):
        """
        Lex stories, producing the list of used tokens
        """
        if story is not None:
            bundle = Bundle.from_string(story, features=features)
        else:
            bundle = Bundle.from_path(path, features=features)
        return bundle.lex(ebnf=ebnf)

    @staticmethod
    def grammar():
        """
        Returns the current grammar
        """
        return Grammar().build()


def _clean_dict(d):
    """
    Removes all falsy elements from a nested dict
    """
    if not isinstance(d, dict):
        return d
    return {k: _clean_dict(v) for k, v in d.items() if v}
