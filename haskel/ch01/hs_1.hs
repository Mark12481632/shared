double x = x + x

qsort []     = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
               where
                   smaller = [a| a <- xs, a <= x]
                   larger = [b| b <- xs, b > x]

rqsort []     = []
rqsort (x:xs) = rqsort larger ++ [x] ++ rqsort smaller
                where
                    smaller = [a| a <- xs, a <= x]
                    larger = [b| b <- xs, b > x]

invert [] = []
invert (x:xs) = invert xs ++ [x]

times n1 n2 = n1 * n2

{-
  A multi-line comment.
  By MDR
-}

mark x y | x == 1 = y
         | y == 1 = x
         | otherwise = 100


ssum n | n == 0 = 0
       | otherwise = n + ssum (n-1)



