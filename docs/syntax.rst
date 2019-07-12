Syntax
=======
Reference for the current syntax

Strings
-------

Strings can be declared with single or double quotes::

    color = 'blue'
    color = "blue"

Escaping is done with backslashes::

    funky = ".\"."

Templating
##########

Strings can reference existing variables with templating.
In curly brace blocks, variables can be referenced::

    where = "Amsterdam"
    message = "Hello, {where}!"

Numbers
-------

Storyscript support integer and floating point numbers::

    n = 1
    pie = 3.14

Boolean
-------

Boolean types have two states (`true` and `false`)::

    happy = true
    sad = false

Lists
-----

Lists are a set of elements with guaranteed order::

    colours = ["blue", "red"]

A list can be defined over more lines::

    colours = [
        "blue",
        "red",
    ]

Elements are accessed by index::

    blue = colours[0]


Objects
-------

An unordered collection of elements, accessable by key::

    colours = {'red': '#f00', 'blue': '#00f'}


Keys can be variables::

    colour = 'red'
    colours = {colour: '#f00'} # equal to {'red': '#f00'}


Objects can be access with dot notation or by key index::

    colours.red
    colours['red']


Regular expressions
-------------------
Regular expressions are defined with slashes::

    pattern = /^foo/


Flags are supported::

    pattern = /^foo/i


Arithmetical expressions
------------------------

An arithmetical operation between values.
Addition (`+`), subtraction (`-`), multiplication (`*`), divison (`/`),
power (`^`), modulus (`%`) are supported::

    a = 1 + 2
    a = 1 - 2
    a = 1 * 2
    a = 1 / 2
    a = 1 % 2


Logical expressions
-------------------

A logical operation between values.
The logical `and`, `or` and the unary negation (`!`) are supported::

    c = a and b
    c = a or b
    c = !a

Comparison expressions
----------------------

A comparison between values.
The equal (`==`), not equal (`!=`), greater (`>`), greater or equal (`>=`),
less (`<`) and less or equal (`<=`) relation are supported::

    foo == bar
    foo != bar
    foo > bar
    foo >= bar
    foo < bar
    foo <= bar

Control flow
------------

Program flow can be controlled with `if` conditional blocks::

    if foo
        bar = foo
    else if foo > bar
        bar = foo
    else
        bar = foo

Iterating
---------

Iteration over lists can be done with `foreach`::

    foreach items as item
        # ..


And over objects::

    foreach object as key, value
        # ...

Loops
-----

For more flexible looping, a `while` block can be used::

    while cond


Functions
---------

Functions allow to write repeatable sub procedures::

    function sum a:int b:int returns int
        x = a + b
        return x

The output declaration is optional::

    function sum a:int b:int
        # ...

Calling a function requires parentheses::

    sum (a:1 b:2)

Services
--------

Services can be called with a `<service-name> <command-name> <arguments>*` expression::

    result = service command key:value foo:bar

Arguments with the value equal to the argument name can be shortened::

    # instead of: service command argument:argument
    service command :argument

Streams
-------
When a service provides a stream, the service+when syntax can be used. This
could be an http stream, a stream of events or a generator-like result::

    service command key:value as client
        when client event name:'some_name' as data
            # ...


Exceptions
-----------
Exceptions can be handled with try::

    try
        x = 0 / 0

Exceptions can be caught::

    try
        x = 0 / 0
    catch as error
        alpine echo message:"caught!"

Finally can be used to specify instructions that are always executed,
regardless of the try's outcomet::

    try
        x = 0 / 0
    finally
        a = 1

Inline expressions
------------------
Inline expressions are a shorthand to have on the same line something that
would normally be on its own line::

    service command argument:(service2 command)

Mutations
---------
::

    1 isOdd

Mutations can have arguments::

    ['a', 'b', 'c'] join by:':'


Comments
--------
::

    # inline


::

    ###
    multi
    line
    ###

Importing
---------
To import another story and have access to its functions:

::

    import 'colours.story' as Colours
