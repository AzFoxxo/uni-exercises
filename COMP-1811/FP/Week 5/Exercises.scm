;; Running this code will show you what the data looks like.
;; There are (I hope) 21 items of data in each list.  Each
;; item refers to a person.  For example, the person called
;; A scored 0 and is in class A, the person called U scored
;; 76 and is in class C.

;; The data being used.
(define grades '(0 0 0 0 0 0 0 0 12 26 28 28 28 35 35 42 48 64 65 76 76))
(define names '("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U"))
(define class '(#\A #\B #\C #\A #\B #\C #\A #\B #\C #\A #\B #\C #\A #\B #\C #\A #\B #\C #\A #\B #\C))

;; What do the grades look like?
(define (display-student-info names grades class)
  (if (null? names)
      '()
      (begin
        (display (string-append 
                  (car names) ": Grade = " 
                  (number->string (car grades))
                  ", Class = " 
                  (string (car class))
                  "\n"))
        (display-student-info 
          (cdr names) 
          (cdr grades) 
          (cdr class)))))


;; Exercise 1
(define (coded-message x)
  (map (lambda (y) (integer->char (- (char->integer y) 1))) x))

;;Exercise 2
(define (how-many-scored-zero grades)
   (length (filter (lambda (x) (= x 0)) grades)))

;; Exercise 3
(define (average-grades grades)
  (/ (apply + grades) (length grades)))

;; Exercise 4
(define (average-non-zero grades)
  (/ (apply + (filter (lambda (x) (not (= x 0))) grades))
     (length (filter (lambda (x) (not (= x 0))) grades))))

;; Exercise 5
(define (class-averages grades names classes)
  ())

(display "The data")
(newline)
(display-student-info names grades class)
(newline)

(display "Exercise 1")
(newline)
(coded-message '(#\Z #\h #\o #\o #\# #\G #\r #\q #\h))
(newline)
(display "Exercise 2")
(newline)
(how-many-scored-zero grades)
(newline)
(display "Exercise 3")
(newline)
(average-grades grades)
(newline)
(display "Exercise 4")
(newline)
(average-non-zero grades)
(newline)
(display "Exercise 5")
(newline)
(class-averages grades names class)
