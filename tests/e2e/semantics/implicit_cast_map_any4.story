function foo bar: Map[string, Map[any, any]]
    a = bar

bar = {} to Map[string, Map[string, Map[string, any]]]
foo(:bar)