; Exercise one
(display "Exercise 1")(newline)
(define abc-list '(a b c))
(append abc-list '((d e)))

; Base list
(define base-list '(b c))
; Add (a) to start
(define list-a (cons '(a) base-list))
; Add (d e) to end
(append list-a '((d e)))

; Base list
(define base-list2 '(a b c))
(define base-list3 '((d (e))))
(append base-list2 base-list3)

; Exercise two
(display "Exercise 2")(newline)
(define modules empty)
(append (list "COMP1811" "Level 4"))
(append (list "COMP1821" "Level 4"))
(append (list "COMP1802" "Level 5"))
(append (list "COMP1815" "Level 6"))

; Exercise three
(display "Exercise 3")(newline)
(define list-a '(a (b c) d x e))
(define list-b '(a (b c d) (x)))

; Get the fourth element
(define element4 (car (cdr (cdr (cdr list-a)))))
element4

(define element3 (car (car (cdr (cdr list-b)))))
element3

; Exercise four
(display "Exercise 4")(newline)
(define list-a2 '(a (b (c d)) e (f g y)))
(define list-b2 '(a b c d e f (y)))

; Get the 1st:1st (reverse both lists)
(car (reverse (car (reverse list-a2))))

; Get the 1st:1st element (reverse first list)
(car (car (reverse list-b2)))

; Exercise five
(display "Exercise 5")(newline)
(define list-5 '(a b c d))
(reverse (cons 'x (reverse list-5)))