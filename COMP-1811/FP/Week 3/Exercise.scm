; Add one to each item in the list
(define increment-list
  (lambda (lst)
    (if (null? lst)
        '()
        (cons (+ (car lst) 1)
              (increment-list (cdr lst))
        )
      )
   )
)

(increment-list '(1 2 3 4))

; Reduplicate list N times
(define list-of
    (lambda (n lst)
        (if (= n 0)
            '()
            (append lst (list-of (- n 1) lst))
            )
        )
    )

(list-of 3 '(1 2 3))
(list-of 3 '((a b)))

; Return the number X in list
(define count-x
    (lambda (x lst)
        (if (null? lst)
            0
            (+
                (if
                    (equal? x (car lst))
                    1
                    0)
                    (count-x x (cdr lst))
            )
            )
        )
    )

(count-x 1 '(1 1 1 2 1))

; Replace X in list with Y
(define replace-x
    (lambda (x y lst)
        (if (null? lst)
            '()
            (if
                (equal? x (car lst))
                (cons y (replace-x x y (cdr lst)))
                (cons (car lst) (replace-x x y (cdr lst)))
                )
        )
    )
)

(replace-x 'b 'a '(a a b b b))

; Sorted predicate which determines if a list is sorted (ascending)
(define sorted?
    (lambda (lst)
        (if (null? lst)
            #t
            (if (null? (cdr lst))
                #t
                (if
                    (< (car lst) (car (cdr lst)))
                    (sorted? (cdr lst))
                    #f
                    )
                )
            )
        )
    )

(sorted? '(68 69 60 100))
(sorted? '(1 2 3 4 5))
