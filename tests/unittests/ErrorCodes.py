# -*- coding: utf-8 -*-
from pytest import mark

from storyscript.ErrorCodes import ErrorCodes


@mark.parametrize('name, definition', [
    ('unidentified_error', ('E0001', '')),
    ('service_name', ('E0002', "A service name can't contain `.`")),
    ('arguments_noservice', (
        'E0003', 'You have defined an argument, but not a service'
    )),
    ('return_outside', ('E0004', '`return` is allowed only inside functions')),
    ('variables_backslash', ('E0005', "A variable name can't contain `/`")),
    ('variables_dash', ('E0006', "A variable name can't contain `-`")),
    ('assignment_incomplete', ('E0007', 'Missing value after `=`')),
    ('function_misspell', ('E0008', 'You have misspelt `function`')),
    ('import_misspell', ('E0009', 'You have misspelt `import`')),
    ('import_misspell_as', ('E0010',
                            'You have misspelt `as` in an import statement')),
    ('import_unquoted_file', ('E0011',
                              'The imported filename must be in quotes')),
    ('string_opening_quote', ('E0012', 'Missing opening quote for string')),
    ('string_closing_quote', ('E0013', 'Missing closing quote for string')),
    ('list_trailing_comma', ('E0014', 'Trailing comma in list')),
    ('list_opening_bracket', ('E0015', 'Missing opening bracket for list')),
    ('list_closing_bracket', ('E0016', 'Missing closing bracket for list')),
    ('object_opening_bracket',  (
        'E0017', 'Missing opening bracket for object'
    )),
    ('object_closing_bracket', ('E0018',
                                'Missing closing bracket for object')),
    ('service_argument_colon', ('E0019', 'Missing colon in service argument')),
    ('reserved_keyword_function', ('E0020',
                                   '`function` is a reserved keyword')),
    ('reserved_keyword_if', ('E0021', '`if` is a reserved keyword')),
    ('reserved_keyword_else', ('E0022', '`else` is a reserved keyword')),
    ('reserved_keyword_foreach', ('E0023', '`foreach` is a reserved keyword')),
    ('reserved_keyword_return', ('E0024', '`return` is a reserved keyword')),
    ('reserved_keyword_returns', ('E0025', '`returns` is a reserved keyword')),
    ('reserved_keyword_try', ('E0026', '`try` is a reserved keyword')),
    ('reserved_keyword_catch', ('E0027', '`catch` is a reserved keyword')),
    ('reserved_keyword_finally', ('E0028', '`finally` is a reserved keyword')),
    ('reserved_keyword_when', ('E0029', '`when` is a reserved keyword')),
    ('reserved_keyword_as', ('E0030', '`as` is a reserved keyword')),
    ('reserved_keyword_import', ('E0031', '`import` is a reserved keyword')),
    ('reserved_keyword_while', ('E0032', '`while` is a reserved keyword')),
    ('reserved_keyword_throw', ('E0033', '`throw` is a reserved keyword')),
    ('future_reserved_keyword_async', (
        'E0034',
        '`async` is reserved for future use')),
    ('future_reserved_keyword_story', (
        'E0035',
        '`story` is reserved for future use')),
    ('future_reserved_keyword_assert', (
        'E0036',
        '`assert` is reserved for future use')),
    ('future_reserved_keyword_called', (
        'E0037',
        '`called` is reserved for future use')),
    ('future_reserved_keyword_mock', (
        'E0038',
        '`mock` is reserved for future use')),
    ('arguments_nomutation', (
        'E0039',
        'You have defined a chained mutation, but not a mutation')),
    ('compiler_error_no_operator', ('E0040', 'No operator provided')),
    ('invalid_character', (('E0041', '`{}` is not allowed here'))),
    ('function_already_declared',
        ('E0042', '`{}` has already been declared at line {}')),
    ('unexpected_token', ('E0043', '`{}` is not allowed here. Allowed: {}')),
    ('break_outside', ('E0044', '`break` is allowed only inside loops')),
    ('unnecessary_colon', (
        'E0045',
        'There is an unnecessary colon at the end of the line'))
])
def test_errorcodes_errors(name, definition):
    assert getattr(ErrorCodes, name) == definition


def test_errorcodes_is_error():
    """
    Ensures that is_errror can find out whether an error name is valid.
    """
    assert ErrorCodes.is_error('service_name') is True


def test_errorcodes_is_error_none():
    assert ErrorCodes.is_error(None) is None


def test_errorcodes_is_error_string():
    assert ErrorCodes.is_error('foo') is None


def test_errorcodes_get_error():
    ErrorCodes.mock = 'value'
    assert ErrorCodes.get_error('mock') == 'value'
