# -*- coding: utf-8 -*-
from lark.lexer import Token

from pytest import fixture

from storyscript.compiler import FakeTree
from storyscript.parser import Tree


@fixture
def fake_tree(block):
    return FakeTree(block)


def test_faketree_init(block, fake_tree):
    assert fake_tree.block == block
    assert fake_tree.original_line == str(block.line())
    assert fake_tree.new_lines == {}


def test_faketree_line(patch, fake_tree):
    """
    Ensures FakeTree.line can create a fake line number
    """
    fake_tree.original_line = '1'
    result = fake_tree.line()
    assert fake_tree.new_lines == {'1.1': None}
    assert result == '1.1'


def test_faketree_line_successive(patch, fake_tree):
    """
    Ensures FakeTree.line takes into account FakeTree.new_lines
    """
    fake_tree.original_line = '1.1'
    fake_tree.new_lines = {'1.1': None}
    assert fake_tree.line() == '1.2'


def test_faketree_get_line(patch, tree, fake_tree):
    """
    Ensures FakeTree.get_line can get a new line
    """
    patch.object(FakeTree, 'line')
    result = fake_tree.get_line(tree)
    assert result == FakeTree.line()


def test_faketree_get_line_existing(tree, fake_tree):
    """
    Ensures FakeTree.get_line gets the existing line when appropriate.
    """
    fake_tree.new_lines = {'0.1': None}
    tree.line.return_value = '0.1'
    assert fake_tree.get_line(tree) == tree.line()


def test_faketree_path(patch, fake_tree):
    patch.object(FakeTree, 'line')
    FakeTree.line.return_value = 'fake.line'
    result = fake_tree.path()
    name = 'p-fake.line'
    assert result == Tree('path', [Token('NAME', name, line=FakeTree.line())])


def test_faketree_path_name(patch, fake_tree):
    patch.object(FakeTree, 'line')
    FakeTree.line.return_value = 'fake.line'
    result = fake_tree.path(name='x')
    assert result.child(0).value == 'x'


def test_faketree_path_line(fake_tree):
    assert fake_tree.path(line=1).child(0).line == 1


def test_faketree_assignment(patch, tree, fake_tree):
    patch.many(FakeTree, ['path', 'get_line'])
    result = fake_tree.assignment(tree)
    FakeTree.get_line.assert_called_with(tree)
    line = FakeTree.get_line()
    FakeTree.path.assert_called_with(line=line)
    tree.find_first_token.assert_called()
    assert tree.find_first_token().line == line
    assert result.children[0] == FakeTree.path()
    subtree = [Token('EQUALS', '=', line=line), tree]
    expected = Tree('assignment_fragment', subtree)
    assert result.children[1] == expected


def test_faketree_add_assignment(patch, fake_tree, block):
    patch.object(FakeTree, 'assignment')
    block.child.return_value = None
    result = fake_tree.add_assignment('value', original_line=10)
    FakeTree.assignment.assert_called_with('value')
    assert block.children == [FakeTree.assignment(), block.child()]
    name = Token('NAME', FakeTree.assignment().path.child(0), line=10)
    assert result.data == 'path'
    assert result.children == [name]


def test_faketree_add_assignment_more_children(patch, fake_tree, block):
    patch.object(FakeTree, 'assignment')
    fake_tree.add_assignment('value', original_line=42)
    expected = [block.child(), FakeTree.assignment(), block.child()]
    assert block.children == expected
