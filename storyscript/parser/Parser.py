# -*- coding: utf-8 -*-
import io

from lark import Lark

from .Grammar import Grammar
from .Indenter import CustomIndenter
from .Transformer import Transformer
from .Tree import Tree


class Parser:
    """
    Wraps up the parser submodule and exposes parsing and lexing
    functionalities.
    """
    def __init__(self, algo='lalr', ebnf=None):
        self.algo = algo
        self.ebnf = ebnf
        self.lark = self._lark()

    @staticmethod
    def indenter():
        """
        Initialize the indenter
        """
        return CustomIndenter()

    @staticmethod
    def transformer():
        """
        Initialize the transformer
        """
        return Transformer()

    def grammar(self):
        if self.ebnf:
            with io.open(self.ebnf, 'r') as f:
                return f.read()
        return Grammar().build()

    def _lark(self):
        """
        Get the grammar and initialize Lark.
        """
        return Lark(self.grammar(), parser=self.algo, postlex=self.indenter())

    def parse(self, source):
        """
        Parses the source string.
        """
        if source == '':
            return Tree('empty', [])
        source = '{}\n'.format(source)
        lark = self.lark
        tree = lark.parse(source)
        result = self.transformer().transform(tree)
        result.parser = self
        return result

    def lex(self, source):
        """
        Lexes the source string
        """
        return self.lark.lex(source)
