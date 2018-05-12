grammar NameList;

list_: '[' elements ']';
elements: element ( ',' element)*;
element: NAME | list_;
NAME: [a-zA-Z];