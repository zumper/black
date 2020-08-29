#!/usr/bin/env python3
import asyncio
import sys

from third_party import X, Y, Z

from library import some_connection, \
                    some_decorator
f'trigger 3.6 mode'
def func_no_args():
  a; b; c
  if True: raise RuntimeError
  if False: ...
  for i in range(10):
    print(i)
    continue
  exec("new-style exec", {}, {})
  return None
def function_signature_stress_test(number:int,no_annotation=None,text:str="default",* ,debug:bool=False,**kwargs) -> str:
 return text[number:-1]
def spaces(a=1, b=(), c=[], d={}, e=True, f=-1, g=1 if False else 2, h="", i=r''):
 offset = attr.ib(default=attr.Factory( lambda: _r.uniform(10000, 200000)))
 assert task._cancel_stack[:len(old_stack)] == old_stack
def spaces_types(a: int = 1, b: tuple = (), c: list = [], d: dict = {}, e: bool = True, f: int = -1, g: int = 1 if False else 2, h: str = "", i: str = r''): ...
def spaces2(result= _core.Value(None)):
 assert fut is self._read_fut, (fut, self._read_fut)
    # EMPTY LINE WITH WHITESPACE (this comment will be removed)
def example(session):
    result = session.query(models.Customer.id).filter(
        models.Customer.account_id == account_id,
        models.Customer.email == email_address,
    ).order_by(
        models.Customer.id.asc()
    ).all()
def long_lines():
    if True:
        typedargslist.extend(
            gen_annotated_params(ast_args.kwonlyargs, ast_args.kw_defaults, parameters, implicit_default=True)
        )
        typedargslist.extend(
            gen_annotated_params(
                ast_args.kwonlyargs, ast_args.kw_defaults, parameters, implicit_default=True,
                # trailing standalone comment
            )
        )
    _type_comment_re = re.compile(
        r"""
        ^
        [\t ]*
        \#[ ]type:[ ]*
        (?P<type>
            [^#\t\n]+?
        )
        (?<!ignore)     # note: this will force the non-greedy + in <type> to match
                        # a trailing space which is why we need the silliness below
        (?<!ignore[ ]{1})(?<!ignore[ ]{2})(?<!ignore[ ]{3})(?<!ignore[ ]{4})
        (?<!ignore[ ]{5})(?<!ignore[ ]{6})(?<!ignore[ ]{7})(?<!ignore[ ]{8})
        (?<!ignore[ ]{9})(?<!ignore[ ]{10})
        [\t ]*
        (?P<nl>
            (?:\#[^\n]*)?
            \n?
        )
        $
        """, re.MULTILINE | re.VERBOSE
    )
def trailing_comma():
    mapping = {
    A: 0.25 * (10.0 / 12),
    B: 0.1 * (10.0 / 12),
    C: 0.1 * (10.0 / 12),
    D: 0.1 * (10.0 / 12),
}
def f(
  a,
  **kwargs,
) -> A:
    return (
        yield from A(
            very_long_argument_name1=very_long_value_for_the_argument,
            very_long_argument_name2=very_long_value_for_the_argument,
            **kwargs,
        )
    )
def __await__(): return (yield)
def some_long_function_name_with_args_that_fit_on_one_line(argument_number1, argument_number2, argument_number3):
    return None
NAMESPACED_FIELDSETS = {
    'agents': [
        typed_fields.LongName()
    ],
}

NAMESPACED_FIELDSETS = {
    'agents': [
        typed_fields.LongName()
    ]
}


@links.links('Zapp Activity')
def _zapp_activity(self, agent):
  return links.admin_link(
    agent,
    'creditactivity',
    text=str(agent.user_id),
    params={
      'user_id': agent.user_id
    },
  )

def setUp(self):
  super(MMExcludeMonthlyRemoveTest, self).setUp()
  self.ensure_exists(
      objects.Account, account_id=1, defaults={'name': 'Account #1', 'salesforce_id': '#1'}
  )


building_high_vol = self.add_building(
  status=enums.ListingStatus.ACTIVE,
  deal_id=deal.pk,
  masked_fields=zjson.dumps({'features': [enums.PropertyFeatures.MM_EXCLUDE]}),
  features=enums.PropertyFeatures.encode_bitmask(
    [enums.PropertyFeatures.HIGH_VOLUME, enums.PropertyFeatures.MM_EXCLUDE]
  ),
)

something = [
  'abc'
]

something_else = ['abc',]

expected_ptypes = itertools.chain.from_iterable(
  x[1]
  for x in api.PROPERTY_CATEGORIES.iteritems()
  if x[0] in site_pcats
)

FORMFIELD_OVERRIDES = {
    model_utils.ArrayField: {
        'widget': admin_widgets.AdminTextInputWidget(
            attrs={'cols': 240, 'class': 'vLargeTextField',}
        )
    },
}

something = (1, )

tuple_with_stuff = (1,2,3,)

some = function('hello', 'world')

simple_tuple = ()

# output


#!/usr/bin/env python3
import asyncio
import sys

from third_party import X, Y, Z

from library import some_connection, some_decorator

f'trigger 3.6 mode'


def func_no_args():
  a
  b
  c
  if True:
    raise RuntimeError
  if False:
    ...
  for i in range(10):
    print(i)
    continue
  exec ('new-style exec', {}, {})
  return None


def function_signature_stress_test(
    number: int,
    no_annotation=None,
    text: str = 'default',
    *,
    debug: bool = False,
    **kwargs
) -> str:
  return text[number:-1]


def spaces(a=1, b=(), c=[], d={}, e=True, f=-1, g=1 if False else 2, h='', i=r''):
  offset = attr.ib(default=attr.Factory(lambda: _r.uniform(10000, 200000)))
  assert task._cancel_stack[: len(old_stack)] == old_stack


def spaces_types(
    a: int = 1,
    b: tuple = (),
    c: list = [],
    d: dict = {},
    e: bool = True,
    f: int = -1,
    g: int = 1 if False else 2,
    h: str = '',
    i: str = r'',
):
  ...


def spaces2(result=_core.Value(None)):
  assert fut is self._read_fut, (fut, self._read_fut)


def example(session):
  result = (
      session.query(models.Customer.id)
      .filter(
          models.Customer.account_id == account_id,
          models.Customer.email == email_address,
      )
      .order_by(models.Customer.id.asc())
      .all()
  )


def long_lines():
  if True:
    typedargslist.extend(
        gen_annotated_params(
            ast_args.kwonlyargs,
            ast_args.kw_defaults,
            parameters,
            implicit_default=True,
        )
    )
    typedargslist.extend(
        gen_annotated_params(
            ast_args.kwonlyargs,
            ast_args.kw_defaults,
            parameters,
            implicit_default=True,
            # trailing standalone comment
        )
    )
  _type_comment_re = re.compile(
      r"""
        ^
        [\t ]*
        \#[ ]type:[ ]*
        (?P<type>
            [^#\t\n]+?
        )
        (?<!ignore)     # note: this will force the non-greedy + in <type> to match
                        # a trailing space which is why we need the silliness below
        (?<!ignore[ ]{1})(?<!ignore[ ]{2})(?<!ignore[ ]{3})(?<!ignore[ ]{4})
        (?<!ignore[ ]{5})(?<!ignore[ ]{6})(?<!ignore[ ]{7})(?<!ignore[ ]{8})
        (?<!ignore[ ]{9})(?<!ignore[ ]{10})
        [\t ]*
        (?P<nl>
            (?:\#[^\n]*)?
            \n?
        )
        $
        """,
      re.MULTILINE | re.VERBOSE,
  )


def trailing_comma():
  mapping = {
      A: 0.25 * (10.0 / 12),
      B: 0.1 * (10.0 / 12),
      C: 0.1 * (10.0 / 12),
      D: 0.1 * (10.0 / 12),
  }


def f(
    a,
    **kwargs,
) -> A:
  return (
      yield from A(
          very_long_argument_name1=very_long_value_for_the_argument,
          very_long_argument_name2=very_long_value_for_the_argument,
          **kwargs,
      )
  )


def __await__():
  return (yield)


def some_long_function_name_with_args_that_fit_on_one_line(
    argument_number1,
    argument_number2,
    argument_number3,
):
  return None


NAMESPACED_FIELDSETS = {
    'agents': [typed_fields.LongName()],
}

NAMESPACED_FIELDSETS = {'agents': [typed_fields.LongName()]}


@links.links('Zapp Activity')
def _zapp_activity(self, agent):
  return links.admin_link(
      agent,
      'creditactivity',
      text=str(agent.user_id),
      params={'user_id': agent.user_id},
  )


def setUp(self):
  super(MMExcludeMonthlyRemoveTest, self).setUp()
  self.ensure_exists(
      objects.Account,
      account_id=1,
      defaults={'name': 'Account #1', 'salesforce_id': '#1'},
  )


building_high_vol = self.add_building(
    status=enums.ListingStatus.ACTIVE,
    deal_id=deal.pk,
    masked_fields=zjson.dumps({'features': [enums.PropertyFeatures.MM_EXCLUDE]}),
    features=enums.PropertyFeatures.encode_bitmask(
        [enums.PropertyFeatures.HIGH_VOLUME, enums.PropertyFeatures.MM_EXCLUDE]
    ),
)

something = ['abc']

something_else = [
    'abc',
]

expected_ptypes = itertools.chain.from_iterable(
    x[1] for x in api.PROPERTY_CATEGORIES.iteritems() if x[0] in site_pcats
)

FORMFIELD_OVERRIDES = {
    model_utils.ArrayField: {
        'widget': admin_widgets.AdminTextInputWidget(
            attrs={
                'cols': 240,
                'class': 'vLargeTextField',
            }
        )
    },
}

something = (1,)

tuple_with_stuff = (
    1,
    2,
    3,
)

some = function('hello', 'world')

simple_tuple = ()
