; Grades and weights
(define grades (list 78 10 0 0))
(define weights (list 0.4 0.15 0.3 0.15))

; Multiplication function
(define (times a b)
  (* a b))

; Overall function
(define (overall grades weights)
  (if (null? grades) 
      0  
      (+ (times (car grades) (car weights))
         (overall (cdr grades) (cdr weights)))))

; Overall function (lambda)
(define (overall-lambda grades weights)
  (if (null? grades) 
      0  
      (+ ((lambda (a b) (* a b)) (car grades) (car weights))
         (overall (cdr grades) (cdr weights)))))

; Calculate amount needed to pass
(define (pass-amount grades weights)
  (- 40 (overall grades weights)))

; Calculate amount needed (lambda)
(define (pass-amount-lambda grades weights)
  (- 40 (overall-lambda grades weights)))


; Insert (overall grades weights) after pass
(display (format "Additional marks to pass: ~a." (pass-amount grades weights))) 
(newline)
(display (format "Additional marks to pass (lambda): ~a." (pass-amount-lambda grades weights)))