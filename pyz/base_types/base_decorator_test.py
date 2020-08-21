from pyz.base_types.base_decorator import BaseDecorator


def test_add_before():
    base_decorator = BaseDecorator()
    base_decorator.before(lambda x: x)
    assert (len(base_decorator._before) == 1)


def test_add_after():
    base_decorator = BaseDecorator()
    base_decorator.after(lambda x: x)
    assert (len(base_decorator._after) == 1)


def test_add_before_plus_constructor():
    constructor_decorator = lambda x: x + 1
    function_decorator = lambda x: x

    base_decorator = BaseDecorator(before=[constructor_decorator])
    base_decorator.before(function_decorator)
    assert (len(base_decorator._before) == 2)
    assert (base_decorator._before == [constructor_decorator, function_decorator])


def test_add_after_plus_constructor():
    constructor_decorator = lambda x: x + 1
    function_decorator = lambda x: x

    base_decorator = BaseDecorator(after=[constructor_decorator])
    base_decorator.before(function_decorator)
    assert (len(base_decorator._after) == 2)
    assert (base_decorator._after == [constructor_decorator, function_decorator])
