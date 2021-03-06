
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '0210C5CB8BB3AD32A112CA1972240C56'
    
_lr_action_items = {'ACTION':([0,],[1,]),'KIND':([7,],[8,]),'NUMBER':([0,],[3,]),'SIZE':([3,],[6,]),'$end':([1,2,4,5,8,],[-4,0,-1,-2,-3,]),'COLOR':([6,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'mainRule':([0,],[5,]),'expression':([0,],[2,]),'actionRule':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> actionRule','expression',1,'p_expression','main.py',45),
  ('expression -> mainRule','expression',1,'p_expression','main.py',46),
  ('mainRule -> NUMBER SIZE COLOR KIND','mainRule',4,'p_mainRule','main.py',49),
  ('actionRule -> ACTION','actionRule',1,'p_actionRule','main.py',54),
]
