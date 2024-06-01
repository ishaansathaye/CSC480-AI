% Facts
parent(john, mary).
parent(mary, susan).
parent(susan, tom).
parent(tom, missy).
parent(tom, jeff).
parent(susan, sheldon).
parent(sheldon, constance).
parent(mary, george).

male(john).
female(mary).
female(susan).
male(tom).
female(missy).
male(jeff).
male(sheldon).
female(constance).
male(george).

% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \== Y.
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \== Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandchild(X, Y) :- grandparent(Y, X).
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \== Y.

% Additional Rules
grandmother(X, Y) :- grandparent(X, Y), female(X).
grandfather(X, Y) :- grandparent(X, Y), male(X).
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
second_cousin(X, Y) :- parent(A, X), parent(B, Y), cousin(A, B).

% Sample Queries
% ?- brother(tom, missy).
% ?- cousin(susan, missy).
% ?- grandchild(tom, john).
% ?- grandmother(mary, tom).
% ?- grandfather(john, jeff).
% ?- uncle(sheldon, missy).
% ?- aunt(susan, george).
% ?- second_cousin(missy, constance).
