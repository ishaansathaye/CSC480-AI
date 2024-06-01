; Define the person template with name, parent, and gender slots
(deftemplate person
    (slot name)
    (slot parent)
    (slot gender))

; Define the initial facts
(deffacts initial-facts
    (person (name john) (parent none) (gender male))
    (person (name mary) (parent john) (gender female))
    (person (name susan) (parent mary) (gender female))
    (person (name tom) (parent susan) (gender male))
    (person (name constance) (parent tom) (gender female))
    (person (name jeff) (parent tom) (gender male))
    (person (name sheldon) (parent susan) (gender male))
    (person (name linda) (parent sheldon) (gender female))
    (person (name george) (parent mary) (gender male))
    (person (name missy) (parent george) (gender female)))

; Rule to find ancestors
(defrule find-ancestor
    (person (name ?x) (parent ?y))
    (person (name ?y) (parent ?z))
    =>
    (assert (person (name ?x) (parent ?z))))

; Rule to print ancestors
(defrule print-ancestor
    (person (name ?x) (parent ?z))
    =>
    (printout t ?x " is an ancestor of " ?z crlf))

; Rule to find mothers
(defrule find-mother
    (person (name ?x) (parent ?y) (gender female))
    =>
    (assert (mother ?x ?y)))

; Rule to find fathers
(defrule find-father
    (person (name ?x) (parent ?y) (gender male))
    =>
    (assert (father ?x ?y)))

; Rule to find brothers
(defrule find-brother
    (person (name ?x) (parent ?z) (gender male))
    (person (name ?y) (parent ?z))
    (test (neq ?x ?y))
    =>
    (assert (brother ?x ?y)))

; Rule to find sisters
(defrule find-sister
    (person (name ?x) (parent ?z) (gender female))
    (person (name ?y) (parent ?z))
    (test (neq ?x ?y))
    =>
    (assert (sister ?x ?y)))

; Rule to find grandparents
(defrule find-grandparent
    (person (name ?x) (parent ?y))
    (person (name ?y) (parent ?z))
    =>
    (assert (grandparent ?z ?x)))

; Rule to find grandchildren
(defrule find-grandchild
    (person (name ?x) (parent ?y))
    (person (name ?y) (parent ?z))
    =>
    (assert (grandchild ?x ?z)))

; Rule to find cousins
(defrule find-cousin
    (person (name ?x) (parent ?p1))
    (person (name ?y) (parent ?p2))
    (sibling ?p1 ?p2)
    (test (neq ?x ?y))
    =>
    (assert (cousin ?x ?y)))

; Rule to find uncles
(defrule find-uncle
    (person (name ?x) (parent ?p))
    (brother ?u ?p)
    =>
    (assert (uncle ?u ?x)))

; Rule to find aunts
(defrule find-aunt
    (person (name ?x) (parent ?p))
    (sister ?a ?p)
    =>
    (assert (aunt ?a ?x)))

; Rule to find second cousins
(defrule find-second-cousin
    (person (name ?x) (parent ?p1))
    (person (name ?y) (parent ?p2))
    (cousin ?p1 ?p2)
    (test (neq ?x ?y))
    =>
    (assert (second-cousin ?x ?y)))

; Some examples of queries:
; (find-all-facts ((?m mother)) TRUE)
; (find-all-facts ((?b brother)) TRUE)
; (find-all-facts ((?c cousin)) TRUE)
; (find-all-facts ((?gp grandparent)) TRUE)
; (find-all-facts ((?gc grandchild)) TRUE)
; (find-all-facts ((?u uncle)) TRUE)
; (find-all-facts ((?a aunt)) TRUE)
; (find-all-facts ((?sc second-cousin)) TRUE)
