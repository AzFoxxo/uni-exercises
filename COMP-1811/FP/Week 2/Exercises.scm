
; Takes X and Y and returns x+y, x-y, x/y, and x*y as a list
(define func
    (lambda (x y)
        (list
            (+ x y)
            (- x y)
            (/ x y)
            (* x y)
        )
    )
)

(func 1 2)

; Insert the first two elements of list one into list two
(define func1
    (lambda (lst1 lst2)
        (append (list (car lst1) (car (cdr lst1))) lst2)
    )
)

(func1 '(1 2 3) '(4 5 6))


; Return three lowest values in a list
(define func2
    (lambda (lst)
        ; On the sorted list, get the first three elements
        (let ((sorted-lst (sort lst <)))
            (list (car sorted-lst) (car (cdr sorted-lst)) (car (cdr (cdr sorted-lst))))
        )
    )
)

(func2 '(1 4 3 6 2))

; Takes a list of numbers and returns a list for negative numbers, positive numbers, and zero
(define func3
  (lambda (lst)
    (list 
      (filter negative? lst)
      (filter positive? lst)
      (filter zero? lst)
      )
    )
)

(func3 '(467 36 -3 -14 0 0 3788 -14))

; Check if a list is palindromic
(define is-palindrome
  (lambda (lst)
    (equal? lst (reverse lst))
    )
  )

(is-palindrome '(10 20 30 20 10))
(is-palindrome '(10 20 30 40 50 60 70 80 90 100))

; Swap elements around
(define swap
  (lambda (pair)
    (list (cadr pair) (car pair))
  )
)

(swap '(1 2))

; Check is a triangle can be formed
(define is_triangle
    (lambda (a b c)
        ; Check A+B>C and A+C>B and B+C>A
        (and (> (+ a b ) c) (> (+ a c) b) (> (+ b c) a))
    )
)

(is_triangle 9 3 2)
(is_triangle 3 3 3)