< d i v   s t y l e = " m a r g i n - t o p :   3 0 p x ; f o n t - s i z e :   0 . 8 e m ; 
                         b o r d e r - t o p :   1 p x   s o l i d   # e e e ; p a d d i n g - t o p :   8 p x ; " > 
         < i m g   s r c = " h t t p s : / / m a r k d o w n m o n s t e r . w e s t - w i n d . c o m / f a v i c o n . p n g " 
                   s t y l e = " h e i g h t :   2 0 p x ; f l o a t :   l e f t ;   m a r g i n - r i g h t :   1 0 p x ; " / > 
         t h i s   p o s t   c r e a t e d   a n d   p u b l i s h e d   w i t h   
         < a   h r e f = " h t t p s : / / m a r k d o w n m o n s t e r . w e s t - w i n d . c o m "   
               t a r g e t = " t o p " > M a r k d o w n   M o n s t e r < / a >   
 < / d i v > F o r   t h i s   r e q u e s t ,   I ' l l   c r e a t e   a   b a s i c   c h e c k i n g   d e p o s i t   s y s t e m   t h a t   s i m u l a t e s   d e p o s i t i n g   c h e c k s   i n t o   a n   a c c o u n t   a n d   t h e   a b i l i t y   t o   p r o c e s s   a n d   t r a n s f e r   f u n d s   b e t w e e n   d i f f e r e n t   a c c o u n t s .   H e r e ' s   a   d e t a i l e d   a p p r o a c h   f o r   h o w   I   w i l l   s t r u c t u r e   t h e   s y s t e m : 
 T h o u g h t   P r o c e s s : 
 
         A c c o u n t s   R e p r e s e n t a t i o n : 
                 U s e   a   c l a s s   t o   r e p r e s e n t   b a n k   a c c o u n t s .   E a c h   a c c o u n t   h a s   a n   i d e n t i f i e r ,   b a l a n c e ,   a n d   o w n e r   i n f o r m a t i o n . 
 
         C h e c k   R e p r e s e n t a t i o n : 
                 R e p r e s e n t   a   c h e c k   w i t h   a t t r i b u t e s   l i k e   c h e c k   I D ,   a m o u n t ,   t h e   i s s u e r  s   a c c o u n t ,   a n d   t h e   p a y e e  s   a c c o u n t . 
 
         D e p o s i t   a n d   C a s h i n g   F u n c t i o n a l i t y : 
                 T h e   s y s t e m   s h o u l d   i n c l u d e   m e t h o d s   t o   p r o c e s s   a   c h e c k   a n d   d e p o s i t   i t   t o   t h e   a p p r o p r i a t e   a c c o u n t .   T h i s   m e a n s   c h e c k i n g   i f   f u n d s   a r e   a v a i l a b l e   i n   t h e   i s s u e r  s   a c c o u n t   a n d ,   i f   s o ,   t r a n s f e r r i n g   t h e   m o n e y   t o   t h e   p a y e e  s   a c c o u n t . 
 
         A s s u m p t i o n s : 
                 A   c h e c k   i s   o n l y   v a l i d   i f   t h e r e   a r e   e n o u g h   f u n d s   i n   t h e   i s s u e r ' s   a c c o u n t . 
                 W e ' l l   a s s u m e   a   s i m p l e   s y s t e m   w i t h o u t   r e a l - t i m e   b a n k i n g   i n t e g r a t i o n  j u s t   c l a s s e s   s i m u l a t i n g   b e h a v i o r . 
 
         S y s t e m   R e q u i r e m e n t s : 
                 A c c o u n t   c l a s s   t o   h o l d   b a l a n c e   a n d   m a n a g e   d e p o s i t s / w i t h d r a w a l s . 
                 C h e c k   c l a s s   t o   r e p r e s e n t   a   c h e c k . 
                 F u n c t i o n s   t o   p r o c e s s   a n d   v a l i d a t e   t h e   c h e c k . 
 
 H e r e ' s   t h e   i n i t i a l   i m p l e m e n t a t i o n   o f   t h i s   s y s t e m : 
 P y t h o n   C o d e : 
 
 p y t h o n 
 
 c l a s s   A c c o u n t : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   b a l a n c e = 0 . 0 ) : 
                 s e l f . a c c o u n t _ i d   =   a c c o u n t _ i d 
                 s e l f . o w n e r   =   o w n e r 
                 s e l f . b a l a n c e   =   b a l a n c e 
 
         d e f   d e p o s i t ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   0 : 
                         s e l f . b a l a n c e   + =   a m o u n t 
                         p r i n t ( f " D e p o s i t e d   { a m o u n t }   t o   { s e l f . a c c o u n t _ i d } .   N e w   B a l a n c e :   { s e l f . b a l a n c e } " ) 
                 e l s e : 
                         p r i n t ( " D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
 
         d e f   w i t h d r a w ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   s e l f . b a l a n c e : 
                         p r i n t ( f " I n s u f f i c i e n t   f u n d s   i n   a c c o u n t   { s e l f . a c c o u n t _ i d } . " ) 
                         r e t u r n   F a l s e 
                 e l i f   a m o u n t   < =   0 : 
                         p r i n t ( " W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                         r e t u r n   F a l s e 
                 e l s e : 
                         s e l f . b a l a n c e   - =   a m o u n t 
                         p r i n t ( f " W i t h d r e w   { a m o u n t }   f r o m   { s e l f . a c c o u n t _ i d } .   N e w   B a l a n c e :   { s e l f . b a l a n c e } " ) 
                         r e t u r n   T r u e 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ) " 
 
 
 c l a s s   C h e c k : 
         d e f   _ _ i n i t _ _ ( s e l f ,   c h e c k _ i d ,   a m o u n t ,   i s s u e r _ a c c o u n t ,   p a y e e _ a c c o u n t ) : 
                 s e l f . c h e c k _ i d   =   c h e c k _ i d 
                 s e l f . a m o u n t   =   a m o u n t 
                 s e l f . i s s u e r _ a c c o u n t   =   i s s u e r _ a c c o u n t 
                 s e l f . p a y e e _ a c c o u n t   =   p a y e e _ a c c o u n t 
 
         d e f   p r o c e s s _ c h e c k ( s e l f ) : 
                 #   T r y   t o   w i t h d r a w   t h e   c h e c k   a m o u n t   f r o m   t h e   i s s u e r ' s   a c c o u n t 
                 i f   s e l f . i s s u e r _ a c c o u n t . w i t h d r a w ( s e l f . a m o u n t ) : 
                         #   I f   s u c c e s s f u l ,   d e p o s i t   t h e   a m o u n t   t o   t h e   p a y e e ' s   a c c o u n t 
                         s e l f . p a y e e _ a c c o u n t . d e p o s i t ( s e l f . a m o u n t ) 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   p r o c e s s e d   s u c c e s s f u l l y . " ) 
                 e l s e : 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   f a i l e d   d u e   t o   i n s u f f i c i e n t   f u n d s . " ) 
 
 
 #   E x a m p l e   U s a g e : 
 
 #   C r e a t e   t w o   a c c o u n t s 
 a c c o u n t _ 1   =   A c c o u n t ( " A C C 0 0 1 " ,   " A l i c e " ,   1 0 0 0 . 0 ) 
 a c c o u n t _ 2   =   A c c o u n t ( " A C C 0 0 2 " ,   " B o b " ,   5 0 0 . 0 ) 
 
 #   C r e a t e   a   c h e c k   f r o m   A l i c e ' s   a c c o u n t   t o   B o b ' s   a c c o u n t   f o r   2 0 0 
 c h e c k _ 1   =   C h e c k ( " C H K 0 0 1 " ,   2 0 0 . 0 ,   a c c o u n t _ 1 ,   a c c o u n t _ 2 ) 
 
 #   P r o c e s s   t h e   c h e c k 
 #   c h e c k _ 1 . p r o c e s s _ c h e c k ( ) 
 
 #   D i s p l a y   a c c o u n t   d e t a i l s 
 #   p r i n t ( a c c o u n t _ 1 ) 
 #   p r i n t ( a c c o u n t _ 2 ) 
 
 #   C r e a t e   a n o t h e r   c h e c k   t h a t   e x c e e d s   t h e   b a l a n c e 
 c h e c k _ 2   =   C h e c k ( " C H K 0 0 2 " ,   1 2 0 0 . 0 ,   a c c o u n t _ 1 ,   a c c o u n t _ 2 ) 
 
 #   P r o c e s s   t h e   c h e c k 
 #   c h e c k _ 2 . p r o c e s s _ c h e c k ( ) 
 
 #   D i s p l a y   a c c o u n t   d e t a i l s   a g a i n 
 #   p r i n t ( a c c o u n t _ 1 ) 
 #   p r i n t ( a c c o u n t _ 2 ) 
 
 C o d e   R e v i e w   &   A n a l y s i s : 
 
         C l a s s e s   U s e d : 
                 A c c o u n t :   H a n d l e s   t h e   b a l a n c e   a n d   b a s i c   o p e r a t i o n s   l i k e   d e p o s i t   a n d   w i t h d r a w a l . 
                 C h e c k :   R e p r e s e n t s   a   f i n a n c i a l   i n s t r u m e n t   t h a t   t r a n s f e r s   f u n d s   b e t w e e n   a c c o u n t s . 
 
         C o r e   F u n c t i o n a l i t y : 
                 T h e   A c c o u n t   c l a s s   p r o v i d e s   d e p o s i t   a n d   w i t h d r a w   m e t h o d s ,   a l l o w i n g   f u n d s   t o   b e   m a n a g e d   e a s i l y . 
                 T h e   C h e c k   c l a s s   p r o c e s s e s   a   c h e c k   b y   a t t e m p t i n g   a   w i t h d r a w a l   f r o m   t h e   i s s u e r ' s   a c c o u n t   a n d ,   i f   s u c c e s s f u l ,   d e p o s i t i n g   i t   i n t o   t h e   p a y e e  s   a c c o u n t . 
 
         I m p r o v e m e n t s   &   S u g g e s t i o n s : 
                 V a l i d a t i o n :   A d d   b e t t e r   v a l i d a t i o n   t o   e n s u r e   t h a t   t h e   c h e c k   a m o u n t   i s   p o s i t i v e . 
                 T r a n s a c t i o n   L o g g i n g :   A d d i n g   a   l o g g i n g   s y s t e m   c o u l d   b e   u s e f u l   t o   k e e p   t r a c k   o f   a l l   t r a n s a c t i o n s   f o r   a u d i t i n g   p u r p o s e s . 
                 E r r o r   H a n d l i n g :   F o r   a   r e a l   a p p l i c a t i o n ,   m o r e   s o p h i s t i c a t e d   e r r o r   h a n d l i n g   w o u l d   b e   n e e d e d   f o r   n e t w o r k   i s s u e s ,   i n c o r r e c t   a c c o u n t   d e t a i l s ,   e t c . 
 
 N e x t   S t e p s : 
 
         I f   y o u  d   l i k e   t o   s e e   i m p r o v e m e n t s ,   s u c h   a s   a d d i n g   m o r e   c o m p l e x   f e a t u r e s   l i k e   t r a n s a c t i o n   h i s t o r y ,   m o r e   r o b u s t   e r r o r   h a n d l i n g ,   o r   a   m o c k   t e s t i n g   e n v i r o n m e n t ,   l e t   m e   k n o w ! 
         A d d i t i o n a l l y ,   I   c a n   a d d   a   u s e r   a u t h e n t i c a t i o n   s y s t e m   t o   e n h a n c e   s e c u r i t y   i f   d e s i r e d . 
 
 W o u l d   y o u   l i k e   m e   t o   a d d   a n y   s p e c i f i c   f e a t u r e s   o r   c r e a t e   u n i t   t e s t s   f o r   t h i s   s y s t e m ? 
 Y o u   s a i d : 
 a d d   a l l   o f   i t   u p g r a d e 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 T o   u p g r a d e   t h e   s y s t e m   w i t h   e n h a n c e d   f e a t u r e s ,   I ' l l   i n c o r p o r a t e   t h e   f o l l o w i n g   i m p r o v e m e n t s : 
 
         T r a n s a c t i o n   H i s t o r y : 
                 E a c h   a c c o u n t   w i l l   k e e p   a   l o g   o f   i t s   t r a n s a c t i o n s   ( d e p o s i t s ,   w i t h d r a w a l s ) . 
                 T h i s   w i l l   b e   h e l p f u l   f o r   t r a c k i n g   f i n a n c i a l   a c t i v i t y   i n   e a c h   a c c o u n t . 
 
         L o g g i n g   S y s t e m : 
                 A d d   a   l o g g i n g   m e c h a n i s m   t o   t r a c k   o p e r a t i o n s   f o r   b o t h   a c c o u n t s   a n d   c h e c k s .   T h i s   w i l l   i n c l u d e   a   s i m p l e   i n - m e m o r y   t r a n s a c t i o n   h i s t o r y . 
 
         B e t t e r   V a l i d a t i o n : 
                 V a l i d a t i o n   t o   e n s u r e   t h a t   c h e c k s   h a v e   v a l i d   a m o u n t s . 
                 E n s u r e   a c c o u n t s   i n v o l v e d   i n   t r a n s a c t i o n s   e x i s t   a n d   h a v e   p o s i t i v e   b a l a n c e s . 
 
         E r r o r   H a n d l i n g : 
                 I m p r o v e   e r r o r   h a n d l i n g   t o   d e a l   w i t h   n e g a t i v e   d e p o s i t s ,   i n c o r r e c t   a c c o u n t   d e t a i l s ,   e t c . 
 
         A u t h e n t i c a t i o n   S y s t e m : 
                 A d d   a   b a s i c   u s e r n a m e   a n d   p a s s w o r d - b a s e d   a u t h e n t i c a t i o n   f o r   a c c o u n t s   t o   e n h a n c e   s e c u r i t y . 
 
 U p g r a d e d   P y t h o n   C o d e : 
 
 p y t h o n 
 
 i m p o r t   h a s h l i b 
 
 c l a s s   A c c o u n t : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ) : 
                 s e l f . a c c o u n t _ i d   =   a c c o u n t _ i d 
                 s e l f . o w n e r   =   o w n e r 
                 s e l f . p a s s w o r d _ h a s h   =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
                 s e l f . b a l a n c e   =   b a l a n c e 
                 s e l f . t r a n s a c t i o n _ h i s t o r y   =   [ ] 
 
         d e f   a u t h e n t i c a t e ( s e l f ,   p a s s w o r d ) : 
                 r e t u r n   s e l f . p a s s w o r d _ h a s h   = =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
 
         d e f   d e p o s i t ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   + =   a m o u n t 
                 s e l f . t r a n s a c t i o n _ h i s t o r y . a p p e n d ( f " D e p o s i t e d   { a m o u n t } .   N e w   B a l a n c e :   { s e l f . b a l a n c e } " ) 
 
         d e f   w i t h d r a w ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   s e l f . b a l a n c e : 
                         r a i s e   V a l u e E r r o r ( f " I n s u f f i c i e n t   f u n d s   i n   a c c o u n t   { s e l f . a c c o u n t _ i d } . " ) 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   - =   a m o u n t 
                 s e l f . t r a n s a c t i o n _ h i s t o r y . a p p e n d ( f " W i t h d r e w   { a m o u n t } .   N e w   B a l a n c e :   { s e l f . b a l a n c e } " ) 
 
         d e f   g e t _ t r a n s a c t i o n _ h i s t o r y ( s e l f ) : 
                 r e t u r n   s e l f . t r a n s a c t i o n _ h i s t o r y 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ) " 
 
 
 c l a s s   C h e c k : 
         d e f   _ _ i n i t _ _ ( s e l f ,   c h e c k _ i d ,   a m o u n t ,   i s s u e r _ a c c o u n t ,   p a y e e _ a c c o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " C h e c k   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . c h e c k _ i d   =   c h e c k _ i d 
                 s e l f . a m o u n t   =   a m o u n t 
                 s e l f . i s s u e r _ a c c o u n t   =   i s s u e r _ a c c o u n t 
                 s e l f . p a y e e _ a c c o u n t   =   p a y e e _ a c c o u n t 
 
         d e f   p r o c e s s _ c h e c k ( s e l f ,   i s s u e r _ p a s s w o r d ) : 
                 #   A u t h e n t i c a t e   t h e   i s s u e r ' s   a c c o u n t 
                 i f   n o t   s e l f . i s s u e r _ a c c o u n t . a u t h e n t i c a t e ( i s s u e r _ p a s s w o r d ) : 
                         r a i s e   P e r m i s s i o n E r r o r ( " A u t h e n t i c a t i o n   f a i l e d .   I n c o r r e c t   p a s s w o r d . " ) 
                 
                 #   T r y   t o   w i t h d r a w   t h e   c h e c k   a m o u n t   f r o m   t h e   i s s u e r ' s   a c c o u n t 
                 t r y : 
                         s e l f . i s s u e r _ a c c o u n t . w i t h d r a w ( s e l f . a m o u n t ) 
                         s e l f . p a y e e _ a c c o u n t . d e p o s i t ( s e l f . a m o u n t ) 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   p r o c e s s e d   s u c c e s s f u l l y . " ) 
                 e x c e p t   V a l u e E r r o r   a s   e : 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   f a i l e d :   { e } " ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " C h e c k ( I D :   { s e l f . c h e c k _ i d } ,   A m o u n t :   { s e l f . a m o u n t } ,   I s s u e r :   { s e l f . i s s u e r _ a c c o u n t . a c c o u n t _ i d } ,   P a y e e :   { s e l f . p a y e e _ a c c o u n t . a c c o u n t _ i d } ) " 
 
 
 #   E x a m p l e   U s a g e : 
 
 #   C r e a t e   a c c o u n t s 
 a c c o u n t _ 1   =   A c c o u n t ( " A C C 0 0 1 " ,   " A l i c e " ,   " a l i c e _ p a s s w o r d " ,   1 0 0 0 . 0 ) 
 a c c o u n t _ 2   =   A c c o u n t ( " A C C 0 0 2 " ,   " B o b " ,   " b o b _ p a s s w o r d " ,   5 0 0 . 0 ) 
 
 #   P r i n t   i n i t i a l   a c c o u n t   d e t a i l s 
 p r i n t ( a c c o u n t _ 1 ) 
 p r i n t ( a c c o u n t _ 2 ) 
 
 #   C r e a t e   a   c h e c k   f r o m   A l i c e ' s   a c c o u n t   t o   B o b ' s   a c c o u n t   f o r   2 0 0 
 c h e c k _ 1   =   C h e c k ( " C H K 0 0 1 " ,   2 0 0 . 0 ,   a c c o u n t _ 1 ,   a c c o u n t _ 2 ) 
 
 #   P r o c e s s   t h e   c h e c k   w i t h   a u t h e n t i c a t i o n 
 t r y : 
         #   A s s u m i n g   A l i c e   p r o v i d e s   h e r   p a s s w o r d 
         c h e c k _ 1 . p r o c e s s _ c h e c k ( " a l i c e _ p a s s w o r d " ) 
 e x c e p t   P e r m i s s i o n E r r o r   a s   e : 
         p r i n t ( e ) 
 
 #   D i s p l a y   a c c o u n t   d e t a i l s   a f t e r   p r o c e s s i n g   t h e   c h e c k 
 p r i n t ( a c c o u n t _ 1 ) 
 p r i n t ( a c c o u n t _ 2 ) 
 
 #   P r i n t   t r a n s a c t i o n   h i s t o r i e s 
 p r i n t ( " \ n T r a n s a c t i o n   H i s t o r y   f o r   A l i c e ' s   A c c o u n t : " ) 
 f o r   t r a n s a c t i o n   i n   a c c o u n t _ 1 . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) : 
         p r i n t ( t r a n s a c t i o n ) 
 
 p r i n t ( " \ n T r a n s a c t i o n   H i s t o r y   f o r   B o b ' s   A c c o u n t : " ) 
 f o r   t r a n s a c t i o n   i n   a c c o u n t _ 2 . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) : 
         p r i n t ( t r a n s a c t i o n ) 
 
 #   A t t e m p t   t o   p r o c e s s   a   c h e c k   w i t h   a n   i n v a l i d   p a s s w o r d 
 c h e c k _ 2   =   C h e c k ( " C H K 0 0 2 " ,   3 0 0 . 0 ,   a c c o u n t _ 1 ,   a c c o u n t _ 2 ) 
 
 t r y : 
         #   W r o n g   p a s s w o r d   s c e n a r i o 
         c h e c k _ 2 . p r o c e s s _ c h e c k ( " w r o n g _ p a s s w o r d " ) 
 e x c e p t   P e r m i s s i o n E r r o r   a s   e : 
         p r i n t ( e ) 
 
 #   A t t e m p t   t o   p r o c e s s   a   c h e c k   w i t h   a n   a m o u n t   e x c e e d i n g   t h e   i s s u e r ' s   b a l a n c e 
 c h e c k _ 3   =   C h e c k ( " C H K 0 0 3 " ,   2 0 0 0 . 0 ,   a c c o u n t _ 1 ,   a c c o u n t _ 2 ) 
 
 t r y : 
         c h e c k _ 3 . p r o c e s s _ c h e c k ( " a l i c e _ p a s s w o r d " ) 
 e x c e p t   V a l u e E r r o r   a s   e : 
         p r i n t ( e ) 
 
 #   D i s p l a y   a c c o u n t   d e t a i l s   a g a i n 
 p r i n t ( a c c o u n t _ 1 ) 
 p r i n t ( a c c o u n t _ 2 ) 
 
 #   P r i n t   t r a n s a c t i o n   h i s t o r i e s   a g a i n 
 p r i n t ( " \ n T r a n s a c t i o n   H i s t o r y   f o r   A l i c e ' s   A c c o u n t : " ) 
 f o r   t r a n s a c t i o n   i n   a c c o u n t _ 1 . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) : 
         p r i n t ( t r a n s a c t i o n ) 
 
 p r i n t ( " \ n T r a n s a c t i o n   H i s t o r y   f o r   B o b ' s   A c c o u n t : " ) 
 f o r   t r a n s a c t i o n   i n   a c c o u n t _ 2 . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) : 
         p r i n t ( t r a n s a c t i o n ) 
 
 C o d e   R e v i e w   &   A d v a n c e d   A n a l y s i s : 
 
         A u t h e n t i c a t i o n : 
                 P a s s w o r d - b a s e d   A u t h e n t i c a t i o n :   A d d e d   a   s i m p l e   p a s s w o r d - b a s e d   a u t h e n t i c a t i o n   m e c h a n i s m   u s i n g   S H A - 2 5 6   h a s h i n g   f o r   s t o r i n g   p a s s w o r d s   s e c u r e l y . 
                 T h e   a u t h e n t i c a t e   m e t h o d   c h e c k s   t h e   h a s h   o f   t h e   p a s s w o r d   p r o v i d e d   a g a i n s t   t h e   s t o r e d   h a s h . 
 
         T r a n s a c t i o n   L o g g i n g : 
                 E a c h   a c c o u n t   h a s   a   t r a n s a c t i o n _ h i s t o r y   l i s t   t h a t   l o g s   a l l   d e p o s i t s   a n d   w i t h d r a w a l s . 
                 T h e   m e t h o d   g e t _ t r a n s a c t i o n _ h i s t o r y   r e t r i e v e s   t h e   t r a n s a c t i o n   l o g . 
 
         E r r o r   H a n d l i n g : 
                 E n h a n c e d   e r r o r   h a n d l i n g   u s i n g   e x c e p t i o n s   ( V a l u e E r r o r ,   P e r m i s s i o n E r r o r ) . 
                 T h e   c o d e   g r a c e f u l l y   h a n d l e s   c a s e s   l i k e   i n c o r r e c t   p a s s w o r d s ,   w i t h d r a w a l   e x c e e d i n g   t h e   a v a i l a b l e   b a l a n c e ,   a n d   i n v a l i d   c h e c k   a m o u n t s . 
 
         B e t t e r   V a l i d a t i o n : 
                 V a l i d a t i o n   t o   e n s u r e   t h e   c h e c k   a m o u n t   i s   a l w a y s   p o s i t i v e . 
                 A u t h e n t i c a t i o n   r e q u i r e d   b e f o r e   i s s u i n g   c h e c k s ,   m a k i n g   i t   m o r e   s e c u r e . 
 
 S u g g e s t e d   N e x t   S t e p s : 
 
         U n i t   T e s t i n g :   I t  s   c r u c i a l   t o   v a l i d a t e   t h e   c o r r e c t n e s s   o f   t h e s e   n e w   f u n c t i o n a l i t i e s   t h r o u g h   u n i t   t e s t i n g . 
                 I   c a n   i m p l e m e n t   a   t e s t   s u i t e   u s i n g   t h e   u n i t t e s t   o r   p y t e s t   f r a m e w o r k   t o   v e r i f y   e a c h   f u n c t i o n ' s   b e h a v i o r . 
 
         D a t a b a s e   I n t e g r a t i o n :   R e p l a c e   t h e   i n - m e m o r y   r e p r e s e n t a t i o n   w i t h   a   d a t a b a s e   f o r   p e r s i s t e n t   s t o r a g e   o f   a c c o u n t   a n d   t r a n s a c t i o n   d a t a . 
 
         E n h a n c e d   S e c u r i t y   F e a t u r e s : 
                 I m p l e m e n t   r a t e   l i m i t i n g   o r   o t h e r   p r o t e c t i v e   m e a s u r e s   f o r   a u t h e n t i c a t i o n   a t t e m p t s . 
                 U t i l i z e   m o r e   a d v a n c e d   c r y p t o g r a p h i c   m e t h o d s   f o r   s e n s i t i v e   i n f o r m a t i o n . 
 
 W o u l d   y o u   l i k e   m e   t o   a d d   u n i t   t e s t s   f o r   t h e   c u r r e n t   i m p l e m e n t a t i o n ,   o r   e x p l o r e   d a t a b a s e   i n t e g r a t i o n   o p t i o n s ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 I ' l l   p r o c e e d   w i t h   a d d i n g   u n i t   t e s t s   f o r   t h e   c u r r e n t   i m p l e m e n t a t i o n   t o   e n s u r e   c o r r e c t n e s s   a n d   r e l i a b i l i t y .   I ' l l   u s e   P y t h o n ' s   b u i l t - i n   u n i t t e s t   m o d u l e   f o r   t e s t i n g   v a r i o u s   c o m p o n e n t s   o f   t h e   c h e c k i n g   d e p o s i t   s y s t e m . 
 
 T h e   t e s t s   w i l l   c o v e r   t h e   f o l l o w i n g   s c e n a r i o s : 
 
         A c c o u n t   C l a s s : 
                 C r e a t i n g   a c c o u n t s   w i t h   i n i t i a l   b a l a n c e s . 
                 T e s t i n g   t h e   d e p o s i t   m e t h o d   f o r   v a l i d   a n d   i n v a l i d   i n p u t s . 
                 T e s t i n g   t h e   w i t h d r a w a l   m e t h o d ,   i n c l u d i n g   o v e r d r a f t s   a n d   v a l i d   w i t h d r a w a l s . 
                 T e s t i n g   t r a n s a c t i o n   h i s t o r y   l o g g i n g . 
 
         C h e c k   C l a s s : 
                 P r o c e s s i n g   c h e c k s   s u c c e s s f u l l y . 
                 H a n d l i n g   i n v a l i d   c h e c k   a m o u n t s   ( n e g a t i v e   o r   z e r o ) . 
                 T e s t i n g   f a i l e d   c h e c k s   d u e   t o   i n s u f f i c i e n t   f u n d s . 
                 A u t h e n t i c a t i n g   c h e c k s   w i t h   i n c o r r e c t   p a s s w o r d s . 
 
 H e r e ' s   t h e   c o d e   w i t h   a   u n i t t e s t   s u i t e : 
 U n i t   T e s t   C o d e 
 
 p y t h o n 
 
 i m p o r t   u n i t t e s t 
 
 c l a s s   T e s t B a n k i n g S y s t e m ( u n i t t e s t . T e s t C a s e ) : 
 
         d e f   s e t U p ( s e l f ) : 
                 #   S e t   u p   t w o   a c c o u n t s   f o r   t e s t i n g 
                 s e l f . a c c o u n t _ 1   =   A c c o u n t ( " A C C 0 0 1 " ,   " A l i c e " ,   " a l i c e _ p a s s w o r d " ,   1 0 0 0 . 0 ) 
                 s e l f . a c c o u n t _ 2   =   A c c o u n t ( " A C C 0 0 2 " ,   " B o b " ,   " b o b _ p a s s w o r d " ,   5 0 0 . 0 ) 
 
         #   A c c o u n t   C l a s s   T e s t s 
         d e f   t e s t _ a c c o u n t _ c r e a t i o n ( s e l f ) : 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 1 . b a l a n c e ,   1 0 0 0 . 0 ) 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 2 . o w n e r ,   " B o b " ) 
 
         d e f   t e s t _ d e p o s i t _ p o s i t i v e ( s e l f ) : 
                 s e l f . a c c o u n t _ 1 . d e p o s i t ( 2 0 0 ) 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 1 . b a l a n c e ,   1 2 0 0 . 0 ) 
 
         d e f   t e s t _ d e p o s i t _ n e g a t i v e ( s e l f ) : 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         s e l f . a c c o u n t _ 1 . d e p o s i t ( - 1 0 0 ) 
 
         d e f   t e s t _ w i t h d r a w _ s u c c e s s f u l ( s e l f ) : 
                 s e l f . a c c o u n t _ 1 . w i t h d r a w ( 5 0 0 ) 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 1 . b a l a n c e ,   5 0 0 . 0 ) 
 
         d e f   t e s t _ w i t h d r a w _ i n s u f f i c i e n t _ f u n d s ( s e l f ) : 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         s e l f . a c c o u n t _ 1 . w i t h d r a w ( 2 0 0 0 ) 
 
         d e f   t e s t _ w i t h d r a w _ n e g a t i v e _ a m o u n t ( s e l f ) : 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         s e l f . a c c o u n t _ 1 . w i t h d r a w ( - 5 0 ) 
 
         d e f   t e s t _ t r a n s a c t i o n _ h i s t o r y ( s e l f ) : 
                 s e l f . a c c o u n t _ 1 . d e p o s i t ( 3 0 0 ) 
                 s e l f . a c c o u n t _ 1 . w i t h d r a w ( 2 0 0 ) 
                 h i s t o r y   =   s e l f . a c c o u n t _ 1 . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) 
                 s e l f . a s s e r t I n ( " D e p o s i t e d   3 0 0 . 0 " ,   h i s t o r y [ 0 ] ) 
                 s e l f . a s s e r t I n ( " W i t h d r e w   2 0 0 . 0 " ,   h i s t o r y [ 1 ] ) 
 
         #   C h e c k   C l a s s   T e s t s 
         d e f   t e s t _ c h e c k _ p r o c e s s i n g _ s u c c e s s f u l ( s e l f ) : 
                 c h e c k   =   C h e c k ( " C H K 0 0 1 " ,   2 0 0 . 0 ,   s e l f . a c c o u n t _ 1 ,   s e l f . a c c o u n t _ 2 ) 
                 c h e c k . p r o c e s s _ c h e c k ( " a l i c e _ p a s s w o r d " ) 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 1 . b a l a n c e ,   8 0 0 . 0 ) 
                 s e l f . a s s e r t E q u a l ( s e l f . a c c o u n t _ 2 . b a l a n c e ,   7 0 0 . 0 ) 
 
         d e f   t e s t _ c h e c k _ p r o c e s s i n g _ f a i l e d _ a u t h e n t i c a t i o n ( s e l f ) : 
                 c h e c k   =   C h e c k ( " C H K 0 0 2 " ,   2 0 0 . 0 ,   s e l f . a c c o u n t _ 1 ,   s e l f . a c c o u n t _ 2 ) 
                 w i t h   s e l f . a s s e r t R a i s e s ( P e r m i s s i o n E r r o r ) : 
                         c h e c k . p r o c e s s _ c h e c k ( " w r o n g _ p a s s w o r d " ) 
 
         d e f   t e s t _ c h e c k _ i n s u f f i c i e n t _ f u n d s ( s e l f ) : 
                 c h e c k   =   C h e c k ( " C H K 0 0 3 " ,   2 0 0 0 . 0 ,   s e l f . a c c o u n t _ 1 ,   s e l f . a c c o u n t _ 2 ) 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         c h e c k . p r o c e s s _ c h e c k ( " a l i c e _ p a s s w o r d " ) 
 
         d e f   t e s t _ c h e c k _ n e g a t i v e _ a m o u n t ( s e l f ) : 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         C h e c k ( " C H K 0 0 4 " ,   - 5 0 0 . 0 ,   s e l f . a c c o u n t _ 1 ,   s e l f . a c c o u n t _ 2 ) 
 
         d e f   t e s t _ c h e c k _ z e r o _ a m o u n t ( s e l f ) : 
                 w i t h   s e l f . a s s e r t R a i s e s ( V a l u e E r r o r ) : 
                         C h e c k ( " C H K 0 0 5 " ,   0 . 0 ,   s e l f . a c c o u n t _ 1 ,   s e l f . a c c o u n t _ 2 ) 
 
 #   R u n   t h e   t e s t s 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
         u n i t t e s t . m a i n ( a r g v = [ ' ' ] ,   e x i t = F a l s e ) 
 
 E x p l a n a t i o n : 
 
         s e t U p   M e t h o d : 
                 T h i s   m e t h o d   i s   c a l l e d   b e f o r e   e a c h   t e s t   t o   c r e a t e   t h e   n e c e s s a r y   a c c o u n t s   ( a c c o u n t _ 1   a n d   a c c o u n t _ 2 )   w i t h   i n i t i a l   b a l a n c e s . 
                 U s i n g   s e t U p   e n s u r e s   a   c o n s i s t e n t   s t a r t i n g   s t a t e   f o r   e a c h   t e s t . 
 
         A c c o u n t   C l a s s   T e s t s : 
                 t e s t _ a c c o u n t _ c r e a t i o n :   V e r i f i e s   t h a t   a c c o u n t s   a r e   c r e a t e d   w i t h   t h e   c o r r e c t   o w n e r   a n d   b a l a n c e . 
                 t e s t _ d e p o s i t _ p o s i t i v e   &   t e s t _ d e p o s i t _ n e g a t i v e :   T e s t   d e p o s i t s ,   i n c l u d i n g   p o s i t i v e   v a l u e s   a n d   v a l i d a t i o n   f o r   n e g a t i v e   d e p o s i t s . 
                 t e s t _ w i t h d r a w _ s u c c e s s f u l :   E n s u r e s   s u c c e s s f u l   w i t h d r a w a l   r e d u c e s   t h e   b a l a n c e   c o r r e c t l y . 
                 t e s t _ w i t h d r a w _ i n s u f f i c i e n t _ f u n d s :   T e s t s   i f   w i t h d r a w a l   f a i l s   w h e n   t h e   b a l a n c e   i s   i n s u f f i c i e n t . 
                 t e s t _ w i t h d r a w _ n e g a t i v e _ a m o u n t :   V e r i f i e s   t h a t   n e g a t i v e   w i t h d r a w a l s   a r e   n o t   a l l o w e d . 
                 t e s t _ t r a n s a c t i o n _ h i s t o r y :   C h e c k s   w h e t h e r   d e p o s i t s   a n d   w i t h d r a w a l s   a r e   l o g g e d   i n   t h e   t r a n s a c t i o n   h i s t o r y   p r o p e r l y . 
 
         C h e c k   C l a s s   T e s t s : 
                 t e s t _ c h e c k _ p r o c e s s i n g _ s u c c e s s f u l :   V e r i f i e s   t h a t   a   c h e c k   c a n   b e   p r o c e s s e d   s u c c e s s f u l l y   w h e n   t h e   i s s u e r   h a s   s u f f i c i e n t   f u n d s   a n d   p r o v i d e s   t h e   c o r r e c t   p a s s w o r d . 
                 t e s t _ c h e c k _ p r o c e s s i n g _ f a i l e d _ a u t h e n t i c a t i o n :   T e s t s   t h a t   c h e c k   p r o c e s s i n g   f a i l s   i f   t h e   i s s u e r   p r o v i d e s   a n   i n c o r r e c t   p a s s w o r d . 
                 t e s t _ c h e c k _ i n s u f f i c i e n t _ f u n d s :   T e s t s   i f   a   c h e c k   f a i l s   w h e n   t h e   i s s u e r   h a s   i n s u f f i c i e n t   f u n d s . 
                 t e s t _ c h e c k _ n e g a t i v e _ a m o u n t   &   t e s t _ c h e c k _ z e r o _ a m o u n t :   V e r i f i e s   t h a t   c r e a t i n g   a   c h e c k   w i t h   a   n e g a t i v e   o r   z e r o   a m o u n t   r a i s e s   a   V a l u e E r r o r . 
 
 C o d e   R e v i e w   a n d   I m p r o v e m e n t s : 
 
         T e s t   C o v e r a g e :   T h e   t e s t   s u i t e   c o v e r s   a   w i d e   r a n g e   o f   c a s e s ,   i n c l u d i n g : 
                 V a l i d   a n d   i n v a l i d   i n p u t s   f o r   d e p o s i t   a n d   w i t h d r a w a l . 
                 S u c c e s s f u l   a n d   f a i l e d   c h e c k   p r o c e s s i n g   d u e   t o   a u t h e n t i c a t i o n   a n d   i n s u f f i c i e n t   f u n d s . 
                 A c c o u n t   t r a n s a c t i o n   h i s t o r y . 
 
         E r r o r   H a n d l i n g   V a l i d a t i o n :   E a c h   t e s t   c a s e   i n v o l v i n g   i n v a l i d   o p e r a t i o n s   ( l i k e   a   n e g a t i v e   d e p o s i t   o r   f a i l e d   a u t h e n t i c a t i o n )   c o r r e c t l y   u s e s   a s s e r t i o n s   f o r   e x c e p t i o n   h a n d l i n g   t o   v a l i d a t e   e r r o r   s c e n a r i o s . 
 
         E x t e n s i b i l i t y :   T h i s   s u i t e   i s   d e s i g n e d   t o   b e   e x t e n d a b l e  a d d i t i o n a l   t e s t   c a s e s   c a n   b e   e a s i l y   a d d e d   f o r   m o r e   a d v a n c e d   f e a t u r e s ,   l i k e   n e w   c h e c k   t y p e s   o r   m u l t i - c u r r e n c y   s u p p o r t . 
 
 R u n n i n g   t h e   T e s t s : 
 
 T h e   u n i t t e s t . m a i n ( )   c o m m a n d   i s   u s e d   t o   r u n   t h e   t e s t s .   T h e   a r g u m e n t   a r g v = [ ' ' ]   i s   p r o v i d e d   t o   p r e v e n t   J u p y t e r   N o t e b o o k   f r o m   p a s s i n g   i t s   c o m m a n d - l i n e   a r g u m e n t s   t o   t h e   u n i t t e s t   f r a m e w o r k .   Y o u   c a n   e x e c u t e   t h i s   c o d e   t o   v e r i f y   t h a t   t h e   e n t i r e   s y s t e m   b e h a v e s   a s   e x p e c t e d . 
 
 W o u l d   y o u   l i k e   m e   t o   p r o c e e d   w i t h   f u r t h e r   e n h a n c e m e n t s ,   s u c h   a s   d a t a b a s e   i n t e g r a t i o n   o r   e x p a n d i n g   t h e   s y s t e m   w i t h   n e w   f e a t u r e s   l i k e   m u l t i - u s e r   s u p p o r t   o r   i n t e r e s t   r a t e   c a l c u l a t i o n s ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 F o r   t h e   n e x t   s t e p ,   I ' l l   e x t e n d   t h e   s y s t e m   t o   i n c l u d e   d a t a b a s e   i n t e g r a t i o n   a n d   m u l t i - u s e r   s u p p o r t .   T h i s   i n v o l v e s   s e v e r a l   e n h a n c e m e n t s : 
 
         D a t a b a s e   I n t e g r a t i o n : 
                 I m p l e m e n t   a   s i m p l e   S Q L i t e   d a t a b a s e   t o   p e r s i s t   d a t a   f o r   a c c o u n t s   a n d   t r a n s a c t i o n s . 
                 S t o r e   a c c o u n t   d e t a i l s ,   i n c l u d i n g   c r e d e n t i a l s   a n d   b a l a n c e s ,   t o   e n s u r e   d a t a   p e r s i s t e n c e   a c r o s s   s e s s i o n s . 
 
         M u l t i - U s e r   S u p p o r t : 
                 A l l o w   m u l t i p l e   u s e r s   t o   a c c e s s   t h e i r   a c c o u n t s ,   a u t h e n t i c a t e   s e c u r e l y ,   a n d   p e r f o r m   o p e r a t i o n s   s u c h   a s   d e p o s i t s ,   w i t h d r a w a l s ,   a n d   c h e c k   p r o c e s s i n g . 
                 I m p l e m e n t   a   b a s i c   C L I   ( C o m m a n d   L i n e   I n t e r f a c e )   f o r   i n t e r a c t i n g   w i t h   t h e   b a n k   a c c o u n t s   t o   d e m o n s t r a t e   u s e r   o p e r a t i o n s . 
 
         I n t e r e s t   R a t e   C a l c u l a t i o n   ( O p t i o n a l   F e a t u r e ) : 
                 I m p l e m e n t   a n   i n t e r e s t   m e c h a n i s m   f o r   s a v i n g s   a c c o u n t s   t o   i l l u s t r a t e   a n   e x t e n d e d   b a n k i n g   c a p a b i l i t y . 
 
 T h o u g h t   P r o c e s s   f o r   I m p l e m e n t a t i o n : 
 
         D a t a b a s e   S e t u p : 
                 U s e   S Q L i t e   a s   a   l i g h t w e i g h t   d a t a b a s e   f o r   p r o t o t y p i n g   p u r p o s e s . 
                 C r e a t e   t a b l e s   f o r   s t o r i n g   a c c o u n t s   ( a c c o u n t s )   a n d   t r a n s a c t i o n   l o g s   ( t r a n s a c t i o n s ) . 
 
         M o d i f i c a t i o n s   t o   A c c o u n t   C l a s s : 
                 E x t e n d   t h e   A c c o u n t   c l a s s   t o   i n t e r a c t   w i t h   t h e   d a t a b a s e . 
                 I m p l e m e n t   m e t h o d s   f o r   s a v i n g   t o   a n d   l o a d i n g   f r o m   t h e   d a t a b a s e . 
 
         M u l t i - U s e r   C L I : 
                 C r e a t e   a   b a s i c   c o m m a n d - l i n e   i n t e r f a c e   t o   i n t e r a c t   w i t h   t h e   u s e r . 
                 A l l o w   u s e r s   t o   c r e a t e   a c c o u n t s ,   l o g i n ,   d e p o s i t   m o n e y ,   w i t h d r a w ,   p r o c e s s   c h e c k s ,   e t c . 
 
 B e l o w   i s   t h e   e x t e n d e d   v e r s i o n   o f   t h e   c o d e : 
 P y t h o n   C o d e   w i t h   D a t a b a s e   I n t e g r a t i o n   a n d   M u l t i - U s e r   S u p p o r t 
 
 p y t h o n 
 
 i m p o r t   s q l i t e 3 
 i m p o r t   h a s h l i b 
 
 #   S e t t i n g   u p   t h e   d a t a b a s e   c o n n e c t i o n 
 c o n n   =   s q l i t e 3 . c o n n e c t ( " : m e m o r y : " )     #   U s i n g   i n - m e m o r y   d a t a b a s e   f o r   s i m p l i c i t y 
 c u r s o r   =   c o n n . c u r s o r ( ) 
 
 #   C r e a t i n g   a c c o u n t s   t a b l e 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   a c c o u n t s   ( 
                 a c c o u n t _ i d   T E X T   P R I M A R Y   K E Y , 
                 o w n e r   T E X T , 
                 p a s s w o r d _ h a s h   T E X T , 
                 b a l a n c e   R E A L 
         ) 
 " " " ) 
 
 #   C r e a t i n g   t r a n s a c t i o n s   t a b l e 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   t r a n s a c t i o n s   ( 
                 t r a n s a c t i o n _ i d   I N T E G E R   P R I M A R Y   K E Y   A U T O I N C R E M E N T , 
                 a c c o u n t _ i d   T E X T , 
                 t r a n s a c t i o n _ t y p e   T E X T , 
                 a m o u n t   R E A L , 
                 t i m e s t a m p   D A T E T I M E   D E F A U L T   C U R R E N T _ T I M E S T A M P , 
                 F O R E I G N   K E Y ( a c c o u n t _ i d )   R E F E R E N C E S   a c c o u n t s ( a c c o u n t _ i d ) 
         ) 
 " " " ) 
 
 c o n n . c o m m i t ( ) 
 
 c l a s s   A c c o u n t : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ) : 
                 s e l f . a c c o u n t _ i d   =   a c c o u n t _ i d 
                 s e l f . o w n e r   =   o w n e r 
                 s e l f . p a s s w o r d _ h a s h   =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
                 s e l f . b a l a n c e   =   b a l a n c e 
 
         d e f   s a v e _ t o _ d b ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   O R   R E P L A C E   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ) 
                         V A L U E S   ( ? ,   ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   s e l f . o w n e r ,   s e l f . p a s s w o r d _ h a s h ,   s e l f . b a l a n c e ) ) 
                 c o n n . c o m m i t ( ) 
 
         @ s t a t i c m e t h o d 
         d e f   l o a d _ f r o m _ d b ( a c c o u n t _ i d ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( a c c o u n t _ i d , ) ) 
                 r o w   =   c u r s o r . f e t c h o n e ( ) 
                 i f   r o w : 
                         r e t u r n   A c c o u n t ( a c c o u n t _ i d = r o w [ 0 ] ,   o w n e r = r o w [ 1 ] ,   p a s s w o r d = " " ,   b a l a n c e = r o w [ 3 ] ) 
                 r e t u r n   N o n e 
 
         d e f   a u t h e n t i c a t e ( s e l f ,   p a s s w o r d ) : 
                 r e t u r n   s e l f . p a s s w o r d _ h a s h   = =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
 
         d e f   d e p o s i t ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   + =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " D e p o s i t " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   w i t h d r a w ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   s e l f . b a l a n c e : 
                         r a i s e   V a l u e E r r o r ( f " I n s u f f i c i e n t   f u n d s   i n   a c c o u n t   { s e l f . a c c o u n t _ i d } . " ) 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   - =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " W i t h d r a w a l " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   g e t _ t r a n s a c t i o n _ h i s t o r y ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   t r a n s a c t i o n _ t y p e ,   a m o u n t ,   t i m e s t a m p   F R O M   t r a n s a c t i o n s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( s e l f . a c c o u n t _ i d , ) ) 
                 r e t u r n   c u r s o r . f e t c h a l l ( ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ) " 
 
 
 c l a s s   C h e c k : 
         d e f   _ _ i n i t _ _ ( s e l f ,   c h e c k _ i d ,   a m o u n t ,   i s s u e r _ a c c o u n t ,   p a y e e _ a c c o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " C h e c k   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . c h e c k _ i d   =   c h e c k _ i d 
                 s e l f . a m o u n t   =   a m o u n t 
                 s e l f . i s s u e r _ a c c o u n t   =   i s s u e r _ a c c o u n t 
                 s e l f . p a y e e _ a c c o u n t   =   p a y e e _ a c c o u n t 
 
         d e f   p r o c e s s _ c h e c k ( s e l f ,   i s s u e r _ p a s s w o r d ) : 
                 #   A u t h e n t i c a t e   t h e   i s s u e r ' s   a c c o u n t 
                 i f   n o t   s e l f . i s s u e r _ a c c o u n t . a u t h e n t i c a t e ( i s s u e r _ p a s s w o r d ) : 
                         r a i s e   P e r m i s s i o n E r r o r ( " A u t h e n t i c a t i o n   f a i l e d .   I n c o r r e c t   p a s s w o r d . " ) 
                 
                 #   T r y   t o   w i t h d r a w   t h e   c h e c k   a m o u n t   f r o m   t h e   i s s u e r ' s   a c c o u n t 
                 t r y : 
                         s e l f . i s s u e r _ a c c o u n t . w i t h d r a w ( s e l f . a m o u n t ) 
                         s e l f . p a y e e _ a c c o u n t . d e p o s i t ( s e l f . a m o u n t ) 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   p r o c e s s e d   s u c c e s s f u l l y . " ) 
                 e x c e p t   V a l u e E r r o r   a s   e : 
                         p r i n t ( f " C h e c k   { s e l f . c h e c k _ i d }   f a i l e d :   { e } " ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " C h e c k ( I D :   { s e l f . c h e c k _ i d } ,   A m o u n t :   { s e l f . a m o u n t } ,   I s s u e r :   { s e l f . i s s u e r _ a c c o u n t . a c c o u n t _ i d } ,   P a y e e :   { s e l f . p a y e e _ a c c o u n t . a c c o u n t _ i d } ) " 
 
 
 #   B a s i c   C L I   f o r   M u l t i - U s e r   I n t e r a c t i o n 
 d e f   m a i n ( ) : 
         w h i l e   T r u e : 
                 p r i n t ( " \ n - - -   B a n k i n g   S y s t e m   - - - " ) 
                 p r i n t ( " 1 .   C r e a t e   A c c o u n t " ) 
                 p r i n t ( " 2 .   L o g i n   t o   A c c o u n t " ) 
                 p r i n t ( " 3 .   E x i t " ) 
                 c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                 i f   c h o i c e   = =   " 1 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         o w n e r   =   i n p u t ( " E n t e r   O w n e r   N a m e :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
                         b a l a n c e   =   f l o a t ( i n p u t ( " E n t e r   I n i t i a l   B a l a n c e :   " ) ) 
 
                         n e w _ a c c o u n t   =   A c c o u n t ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ) 
                         n e w _ a c c o u n t . s a v e _ t o _ d b ( ) 
                         p r i n t ( f " A c c o u n t   { a c c o u n t _ i d }   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 e l i f   c h o i c e   = =   " 2 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
 
                         a c c o u n t   =   A c c o u n t . l o a d _ f r o m _ d b ( a c c o u n t _ i d ) 
                         i f   a c c o u n t   a n d   a c c o u n t . a u t h e n t i c a t e ( p a s s w o r d ) : 
                                 p r i n t ( f " W e l c o m e   { a c c o u n t . o w n e r } ! " ) 
                                 w h i l e   T r u e : 
                                         p r i n t ( " \ n - - -   A c c o u n t   M e n u   - - - " ) 
                                         p r i n t ( " 1 .   D e p o s i t " ) 
                                         p r i n t ( " 2 .   W i t h d r a w " ) 
                                         p r i n t ( " 3 .   C h e c k   B a l a n c e " ) 
                                         p r i n t ( " 4 .   V i e w   T r a n s a c t i o n   H i s t o r y " ) 
                                         p r i n t ( " 5 .   L o g o u t " ) 
                                         s u b _ c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                                         i f   s u b _ c h o i c e   = =   " 1 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   d e p o s i t :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . d e p o s i t ( a m o u n t ) 
                                                         p r i n t ( " D e p o s i t   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 2 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   w i t h d r a w :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . w i t h d r a w ( a m o u n t ) 
                                                         p r i n t ( " W i t h d r a w a l   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 3 " : 
                                                 p r i n t ( a c c o u n t ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 4 " : 
                                                 h i s t o r y   =   a c c o u n t . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) 
                                                 f o r   t r a n s   i n   h i s t o r y : 
                                                         p r i n t ( f " { t r a n s [ 0 ] } :   { t r a n s [ 1 ] }   a t   { t r a n s [ 2 ] } " ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 5 " : 
                                                 p r i n t ( " L o g g i n g   o u t . . . " ) 
                                                 b r e a k 
 
                                         e l s e : 
                                                 p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
                         e l s e : 
                                 p r i n t ( " I n v a l i d   A c c o u n t   I D   o r   P a s s w o r d . " ) 
 
                 e l i f   c h o i c e   = =   " 3 " : 
                         p r i n t ( " G o o d b y e ! " ) 
                         b r e a k 
 
                 e l s e : 
                         p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
 
 #   R u n   t h e   C L I   f o r   u s e r   i n t e r a c t i o n 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
         m a i n ( ) 
 
 E x p l a n a t i o n : 
 
         D a t a b a s e   S e t u p : 
                 S Q L i t e   I n - M e m o r y   D a t a b a s e :   U s e d   s q l i t e 3   t o   c r e a t e   a n   i n - m e m o r y   d a t a b a s e   ( " : m e m o r y : " )   f o r   s i m p l i c i t y . 
                 C r e a t e d   t a b l e s :   a c c o u n t s   f o r   s t o r i n g   a c c o u n t   d e t a i l s   a n d   t r a n s a c t i o n s   f o r   r e c o r d i n g   f i n a n c i a l   a c t i v i t i e s . 
 
         A c c o u n t   C l a s s   E n h a n c e m e n t s : 
                 D a t a b a s e   M e t h o d s : 
                         s a v e _ t o _ d b ( ) :   I n s e r t s   o r   r e p l a c e s   a n   a c c o u n t   i n   t h e   d a t a b a s e . 
                         l o a d _ f r o m _ d b ( ) :   S t a t i c   m e t h o d   t o   r e t r i e v e   a n   a c c o u n t   b y   a c c o u n t _ i d . 
                 T r a n s a c t i o n   R e c o r d i n g :   E v e r y   d e p o s i t   o r   w i t h d r a w a l   i s   r e c o r d e d   i n   t h e   t r a n s a c t i o n s   t a b l e . 
 
         C h e c k   C l a s s : 
                 R e t a i n e d   t h e   e x i s t i n g   f e a t u r e s   b u t   n o w   w o r k s   s e a m l e s s l y   w i t h   a c c o u n t s   t h a t   i n t e r a c t   w i t h   t h e   d a t a b a s e . 
 
         M u l t i - U s e r   C L I : 
                 T h e   C L I   a l l o w s   u s e r s   t o : 
                         C r e a t e   a c c o u n t s . 
                         L o g i n   w i t h   c r e d e n t i a l s . 
                         P e r f o r m   t r a n s a c t i o n s   l i k e   d e p o s i t s ,   w i t h d r a w a l s ,   v i e w   b a l a n c e s ,   a n d   t r a n s a c t i o n   h i s t o r y . 
                 T h e   s y s t e m   i s   i n t e r a c t i v e   a n d   s u p p o r t s   m u l t i p l e   u s e r s ,   e n s u r i n g   s e c u r e   a c c e s s   t h r o u g h   p a s s w o r d   a u t h e n t i c a t i o n . 
 
 I m p r o v e m e n t s   a n d   F u t u r e   E n h a n c e m e n t s : 
 
         D a t a b a s e   P e r s i s t e n c e :   C u r r e n t l y ,   u s i n g   a n   i n - m e m o r y   d a t a b a s e   m e a n s   a l l   d a t a   i s   l o s t   w h e n   t h e   a p p l i c a t i o n   e n d s .   F o r   a   p r o d u c t i o n   s y s t e m ,   u s i n g   a   f i l e - b a s e d   S Q L i t e   d a t a b a s e   o r   a n   R D B M S   l i k e   M y S Q L / P o s t g r e S Q L   i s   r e c o m m e n d e d . 
         I n t e r e s t   C a l c u l a t i o n :   F o r   s a v i n g s   a c c o u n t s ,   a n   i n t e r e s t   c a l c u l a t i o n   c o u l d   b e   a d d e d   b a s e d   o n   a   s p e c i f i c   i n t e r e s t   r a t e   a n d   t i m e   d u r a t i o n . 
         S e c u r i t y :   P a s s w o r d s   a r e   h a s h e d ,   b u t   f u r t h e r   i m p r o v e m e n t s   c o u l d   b e   a d d e d   l i k e   s a l t i n g   h a s h e s   o r   u s i n g   a   d e d i c a t e d   l i b r a r y   f o r   s e c u r i t y   ( e . g . ,   b c r y p t ) . 
         C o n c u r r e n c y :   T o   h a n d l e   m u l t i p l e   u s e r s   a c c e s s i n g   t h e   s y s t e m   c o n c u r r e n t l y ,   i m p l e m e n t i n g   p r o p e r   l o c k i n g   m e c h a n i s m s   o r   u s i n g   a n   A C I D - c o m p l i a n t   d a t a b a s e   i s   c r u c i a l . 
 
 W o u l d   y o u   l i k e   m e   t o   p r o c e e d   w i t h   i m p l e m e n t i n g   i n t e r e s t   r a t e   c a l c u l a t i o n s   o r   p e r h a p s   i m p r o v e   t h e   d a t a b a s e   i n t e g r a t i o n   t o   p e r s i s t   d a t a   b e t w e e n   r u n s ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 L e t ' s   p r o c e e d   w i t h   i n t e r e s t   r a t e   c a l c u l a t i o n s   f o r   s a v i n g s   a c c o u n t s   a n d   i m p r o v i n g   t h e   d a t a b a s e   i n t e g r a t i o n   t o   e n s u r e   p e r s i s t e n c e   a c r o s s   r u n s . 
 P l a n n e d   I m p r o v e m e n t s : 
 
         I n t e r e s t   R a t e   C a l c u l a t i o n : 
                 A d d   s u p p o r t   f o r   i n t e r e s t   c a l c u l a t i o n   f o r   s a v i n g s   a c c o u n t s . 
                 I m p l e m e n t   a   n e w   S a v i n g s A c c o u n t   c l a s s   d e r i v e d   f r o m   A c c o u n t   t h a t   s u p p o r t s   i n t e r e s t   a c c r u a l   b a s e d   o n   a   s p e c i f i e d   i n t e r e s t   r a t e . 
                 C a l c u l a t e   i n t e r e s t   m o n t h l y   o r   a n n u a l l y ,   a n d   a l l o w   u s e r s   t o   a p p l y   i n t e r e s t   t o   t h e i r   b a l a n c e . 
 
         D a t a b a s e   P e r s i s t e n c e : 
                 M o d i f y   t h e   d a t a b a s e   t o   b e   s t o r e d   o n   d i s k   r a t h e r   t h a n   i n   m e m o r y ,   e n s u r i n g   d a t a   p e r s i s t e n c e   a c r o s s   a p p l i c a t i o n   r e s t a r t s . 
                 C h a n g e   t h e   S Q L i t e   c o n n e c t i o n   t o   a   f i l e - b a s e d   d a t a b a s e   ( b a n k . d b )   i n s t e a d   o f   a n   i n - m e m o r y   o n e . 
 
 E n h a n c e d   P y t h o n   C o d e 
 
 B e l o w ,   I ' l l   e n h a n c e   t h e   s y s t e m   w i t h   t h e   a f o r e m e n t i o n e d   f e a t u r e s : 
 
 p y t h o n 
 
 i m p o r t   s q l i t e 3 
 i m p o r t   h a s h l i b 
 i m p o r t   d a t e t i m e 
 
 #   S e t t i n g   u p   t h e   d a t a b a s e   c o n n e c t i o n   w i t h   a   p e r s i s t e n t   f i l e - b a s e d   d a t a b a s e 
 c o n n   =   s q l i t e 3 . c o n n e c t ( " b a n k . d b " )     #   U s i n g   a   p e r s i s t e n t   f i l e   f o r   d a t a b a s e 
 c u r s o r   =   c o n n . c u r s o r ( ) 
 
 #   C r e a t i n g   a c c o u n t s   t a b l e   i f   n o t   e x i s t s 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   I F   N O T   E X I S T S   a c c o u n t s   ( 
                 a c c o u n t _ i d   T E X T   P R I M A R Y   K E Y , 
                 o w n e r   T E X T , 
                 p a s s w o r d _ h a s h   T E X T , 
                 b a l a n c e   R E A L , 
                 a c c o u n t _ t y p e   T E X T , 
                 i n t e r e s t _ r a t e   R E A L   D E F A U L T   0 
         ) 
 " " " ) 
 
 #   C r e a t i n g   t r a n s a c t i o n s   t a b l e   i f   n o t   e x i s t s 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   I F   N O T   E X I S T S   t r a n s a c t i o n s   ( 
                 t r a n s a c t i o n _ i d   I N T E G E R   P R I M A R Y   K E Y   A U T O I N C R E M E N T , 
                 a c c o u n t _ i d   T E X T , 
                 t r a n s a c t i o n _ t y p e   T E X T , 
                 a m o u n t   R E A L , 
                 t i m e s t a m p   D A T E T I M E   D E F A U L T   C U R R E N T _ T I M E S T A M P , 
                 F O R E I G N   K E Y ( a c c o u n t _ i d )   R E F E R E N C E S   a c c o u n t s ( a c c o u n t _ i d ) 
         ) 
 " " " ) 
 
 c o n n . c o m m i t ( ) 
 
 
 c l a s s   A c c o u n t : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ) : 
                 s e l f . a c c o u n t _ i d   =   a c c o u n t _ i d 
                 s e l f . o w n e r   =   o w n e r 
                 s e l f . p a s s w o r d _ h a s h   =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
                 s e l f . b a l a n c e   =   b a l a n c e 
 
         d e f   s a v e _ t o _ d b ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   O R   R E P L A C E   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ) 
                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ' S t a n d a r d ' ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   s e l f . o w n e r ,   s e l f . p a s s w o r d _ h a s h ,   s e l f . b a l a n c e ) ) 
                 c o n n . c o m m i t ( ) 
 
         @ s t a t i c m e t h o d 
         d e f   l o a d _ f r o m _ d b ( a c c o u n t _ i d ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( a c c o u n t _ i d , ) ) 
                 r o w   =   c u r s o r . f e t c h o n e ( ) 
                 i f   r o w : 
                         i f   r o w [ 4 ]   = =   " S a v i n g s " : 
                                 r e t u r n   S a v i n g s A c c o u n t ( a c c o u n t _ i d = r o w [ 0 ] ,   o w n e r = r o w [ 1 ] ,   p a s s w o r d = " " ,   b a l a n c e = r o w [ 3 ] ,   i n t e r e s t _ r a t e = r o w [ 5 ] ) 
                         r e t u r n   A c c o u n t ( a c c o u n t _ i d = r o w [ 0 ] ,   o w n e r = r o w [ 1 ] ,   p a s s w o r d = " " ,   b a l a n c e = r o w [ 3 ] ) 
                 r e t u r n   N o n e 
 
         d e f   a u t h e n t i c a t e ( s e l f ,   p a s s w o r d ) : 
                 r e t u r n   s e l f . p a s s w o r d _ h a s h   = =   h a s h l i b . s h a 2 5 6 ( p a s s w o r d . e n c o d e ( ) ) . h e x d i g e s t ( ) 
 
         d e f   d e p o s i t ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   + =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " D e p o s i t " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   w i t h d r a w ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   s e l f . b a l a n c e : 
                         r a i s e   V a l u e E r r o r ( f " I n s u f f i c i e n t   f u n d s   i n   a c c o u n t   { s e l f . a c c o u n t _ i d } . " ) 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   - =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " W i t h d r a w a l " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   g e t _ t r a n s a c t i o n _ h i s t o r y ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   t r a n s a c t i o n _ t y p e ,   a m o u n t ,   t i m e s t a m p   F R O M   t r a n s a c t i o n s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( s e l f . a c c o u n t _ i d , ) ) 
                 r e t u r n   c u r s o r . f e t c h a l l ( ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ) " 
 
 
 c l a s s   S a v i n g s A c c o u n t ( A c c o u n t ) : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ,   i n t e r e s t _ r a t e = 0 . 0 1 ) : 
                 s u p e r ( ) . _ _ i n i t _ _ ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ) 
                 s e l f . i n t e r e s t _ r a t e   =   i n t e r e s t _ r a t e 
 
         d e f   s a v e _ t o _ d b ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   O R   R E P L A C E   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ,   i n t e r e s t _ r a t e ) 
                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ' S a v i n g s ' ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   s e l f . o w n e r ,   s e l f . p a s s w o r d _ h a s h ,   s e l f . b a l a n c e ,   s e l f . i n t e r e s t _ r a t e ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   a p p l y _ i n t e r e s t ( s e l f ) : 
                 #   A s s u m i n g   a   s i m p l e   i n t e r e s t   f o r m u l a   a p p l i e d   a n n u a l l y 
                 i n t e r e s t   =   s e l f . b a l a n c e   *   s e l f . i n t e r e s t _ r a t e 
                 s e l f . b a l a n c e   + =   i n t e r e s t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " I n t e r e s t " ,   i n t e r e s t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " S a v i n g s A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ,   I n t e r e s t   R a t e :   { s e l f . i n t e r e s t _ r a t e } ) " 
 
 
 #   B a s i c   C L I   f o r   M u l t i - U s e r   I n t e r a c t i o n   w i t h   I n t e r e s t   C a l c u l a t i o n   F e a t u r e 
 d e f   m a i n ( ) : 
         w h i l e   T r u e : 
                 p r i n t ( " \ n - - -   B a n k i n g   S y s t e m   - - - " ) 
                 p r i n t ( " 1 .   C r e a t e   S t a n d a r d   A c c o u n t " ) 
                 p r i n t ( " 2 .   C r e a t e   S a v i n g s   A c c o u n t " ) 
                 p r i n t ( " 3 .   L o g i n   t o   A c c o u n t " ) 
                 p r i n t ( " 4 .   E x i t " ) 
                 c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                 i f   c h o i c e   = =   " 1 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         o w n e r   =   i n p u t ( " E n t e r   O w n e r   N a m e :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
                         b a l a n c e   =   f l o a t ( i n p u t ( " E n t e r   I n i t i a l   B a l a n c e :   " ) ) 
 
                         n e w _ a c c o u n t   =   A c c o u n t ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ) 
                         n e w _ a c c o u n t . s a v e _ t o _ d b ( ) 
                         p r i n t ( f " A c c o u n t   { a c c o u n t _ i d }   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 e l i f   c h o i c e   = =   " 2 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         o w n e r   =   i n p u t ( " E n t e r   O w n e r   N a m e :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
                         b a l a n c e   =   f l o a t ( i n p u t ( " E n t e r   I n i t i a l   B a l a n c e :   " ) ) 
                         i n t e r e s t _ r a t e   =   f l o a t ( i n p u t ( " E n t e r   I n t e r e s t   R a t e   ( a s   a   d e c i m a l ,   e . g . ,   0 . 0 2   f o r   2 % ) :   " ) ) 
 
                         n e w _ a c c o u n t   =   S a v i n g s A c c o u n t ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ,   i n t e r e s t _ r a t e ) 
                         n e w _ a c c o u n t . s a v e _ t o _ d b ( ) 
                         p r i n t ( f " S a v i n g s   A c c o u n t   { a c c o u n t _ i d }   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 e l i f   c h o i c e   = =   " 3 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
 
                         a c c o u n t   =   A c c o u n t . l o a d _ f r o m _ d b ( a c c o u n t _ i d ) 
                         i f   a c c o u n t   a n d   a c c o u n t . a u t h e n t i c a t e ( p a s s w o r d ) : 
                                 p r i n t ( f " W e l c o m e   { a c c o u n t . o w n e r } ! " ) 
                                 w h i l e   T r u e : 
                                         p r i n t ( " \ n - - -   A c c o u n t   M e n u   - - - " ) 
                                         p r i n t ( " 1 .   D e p o s i t " ) 
                                         p r i n t ( " 2 .   W i t h d r a w " ) 
                                         p r i n t ( " 3 .   C h e c k   B a l a n c e " ) 
                                         p r i n t ( " 4 .   V i e w   T r a n s a c t i o n   H i s t o r y " ) 
                                         i f   i s i n s t a n c e ( a c c o u n t ,   S a v i n g s A c c o u n t ) : 
                                                 p r i n t ( " 5 .   A p p l y   I n t e r e s t " ) 
                                         p r i n t ( " 6 .   L o g o u t " ) 
                                         s u b _ c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                                         i f   s u b _ c h o i c e   = =   " 1 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   d e p o s i t :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . d e p o s i t ( a m o u n t ) 
                                                         p r i n t ( " D e p o s i t   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 2 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   w i t h d r a w :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . w i t h d r a w ( a m o u n t ) 
                                                         p r i n t ( " W i t h d r a w a l   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 3 " : 
                                                 p r i n t ( a c c o u n t ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 4 " : 
                                                 h i s t o r y   =   a c c o u n t . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) 
                                                 f o r   t r a n s   i n   h i s t o r y : 
                                                         p r i n t ( f " { t r a n s [ 0 ] } :   { t r a n s [ 1 ] }   a t   { t r a n s [ 2 ] } " ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 5 "   a n d   i s i n s t a n c e ( a c c o u n t ,   S a v i n g s A c c o u n t ) : 
                                                 a c c o u n t . a p p l y _ i n t e r e s t ( ) 
                                                 p r i n t ( " I n t e r e s t   a p p l i e d   s u c c e s s f u l l y . " ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 6 " : 
                                                 p r i n t ( " L o g g i n g   o u t . . . " ) 
                                                 b r e a k 
 
                                         e l s e : 
                                                 p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
                         e l s e : 
                                 p r i n t ( " I n v a l i d   A c c o u n t   I D   o r   P a s s w o r d . " ) 
 
                 e l i f   c h o i c e   = =   " 4 " : 
                         p r i n t ( " G o o d b y e ! " ) 
                         b r e a k 
 
                 e l s e : 
                         p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
 
 #   R u n   t h e   C L I   f o r   u s e r   i n t e r a c t i o n 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
         m a i n ( ) 
 
 E x p l a n a t i o n   o f   E n h a n c e m e n t s : 
 
         P e r s i s t e n t   D a t a b a s e : 
                 D a t a b a s e   F i l e :   T h e   s y s t e m   n o w   u s e s   a   S Q L i t e   f i l e - b a s e d   d a t a b a s e   ( b a n k . d b )   t h a t   s a v e s   d a t a   t o   d i s k ,   a l l o w i n g   p e r s i s t e n c e   a c r o s s   r u n s . 
                 T a b l e   C r e a t i o n   i f   N o t   E x i s t s :   U s e d   C R E A T E   T A B L E   I F   N O T   E X I S T S   t o   e n s u r e   t a b l e s   a r e   o n l y   c r e a t e d   i f   t h e y   d o   n o t   a l r e a d y   e x i s t . 
 
         S a v i n g s   A c c o u n t   w i t h   I n t e r e s t : 
                 S a v i n g s A c c o u n t   C l a s s :   I n h e r i t s   f r o m   A c c o u n t   a n d   a d d s   a n   i n t e r e s t _ r a t e   a t t r i b u t e . 
                 I n t e r e s t   C a l c u l a t i o n : 
                         T h e   a p p l y _ i n t e r e s t ( )   m e t h o d   c a l c u l a t e s   a n d   a p p l i e s   i n t e r e s t   t o   t h e   c u r r e n t   b a l a n c e . 
                         I n t e r e s t   i s   r e c o r d e d   a s   a   t r a n s a c t i o n   f o r   t r a n s p a r e n c y . 
                 I n t e r e s t   R a t e   F l e x i b i l i t y :   U s e r s   c a n   s p e c i f y   a n   i n t e r e s t   r a t e   a t   t h e   t i m e   o f   a c c o u n t   c r e a t i o n . 
 
         M u l t i - U s e r   C L I   E n h a n c e m e n t s : 
                 A c c o u n t   T y p e s :   U s e r s   c a n   n o w   c r e a t e   e i t h e r   a   s t a n d a r d   a c c o u n t   o r   a   s a v i n g s   a c c o u n t   w i t h   i n t e r e s t . 
                 A p p l y   I n t e r e s t   O p t i o n :   T h e   a c c o u n t   m e n u   i n c l u d e s   a n   o p t i o n   t o   a p p l y   i n t e r e s t   i f   t h e   l o g g e d - i n   u s e r   h a s   a   s a v i n g s   a c c o u n t . 
 
 F u t u r e   E n h a n c e m e n t s : 
 
         I n t e r e s t   C a l c u l a t i o n   S c h e d u l i n g : 
                 A u t o m a t e   i n t e r e s t   c a l c u l a t i o n s   b a s e d   o n   a   t i m e   i n t e r v a l   ( e . g . ,   m o n t h l y   o r   a n n u a l l y )   u s i n g   a   b a c k g r o u n d   p r o c e s s   o r   s c h e d u l e r . 
 
         S e c u r i t y   I m p r o v e m e n t s : 
                 U s e   b c r y p t   f o r   s t r o n g e r   p a s s w o r d   h a s h i n g . 
                 A d d   a   l o c k o u t   m e c h a n i s m   a f t e r   a   n u m b e r   o f   f a i l e d   l o g i n   a t t e m p t s . 
 
         S c a l a b l e   D a t a b a s e : 
 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 T o   f u r t h e r   e n h a n c e   t h e   s y s t e m ,   I   w i l l   o u t l i n e   a n d   i m p l e m e n t   t h e   f o l l o w i n g   f e a t u r e s : 
 
         A u t o m a t e d   I n t e r e s t   C a l c u l a t i o n : 
                 S e t   u p   a   m e c h a n i s m   t o   a u t o m a t e   i n t e r e s t   c a l c u l a t i o n   o n   a   m o n t h l y   b a s i s . 
                 W e   w i l l   s i m u l a t e   m o n t h l y   i n t e r e s t   a c c r u a l   f o r   d e m o n s t r a t i o n   p u r p o s e s . 
 
         E n h a n c e d   S e c u r i t y   f o r   P a s s w o r d   H a s h i n g : 
                 U s e   t h e   b c r y p t   l i b r a r y   f o r   s e c u r e   p a s s w o r d   h a s h i n g   i n s t e a d   o f   S H A - 2 5 6 ,   a d d i n g   i n c r e a s e d   r e s i s t a n c e   a g a i n s t   b r u t e   f o r c e   a t t a c k s . 
                 I n c l u d e   r a t e   l i m i t i n g   f o r   l o g i n   a t t e m p t s   t o   p r e v e n t   b r u t e   f o r c e   a t t a c k s . 
 
         S c a l a b l e   D a t a b a s e   E n h a n c e m e n t s : 
                 R e f a c t o r   t h e   d a t a b a s e   t o   b e   m o r e   s c a l a b l e ,   c o n s i d e r i n g   l a r g e r   d a t a s e t s   a n d   c o n c u r r e n t   a c c e s s . 
                 I n t r o d u c e   i n d e x i n g   a n d   a p p r o p r i a t e   r e l a t i o n s h i p s   b e t w e e n   t a b l e s   f o r   e f f i c i e n t   q u e r i e s . 
 
 I ' l l   i n c o r p o r a t e   t h e s e   f e a t u r e s   o n e   b y   o n e . 
 1 .   A u t o m a t e d   I n t e r e s t   C a l c u l a t i o n 
 
 A p p r o a c h : 
 
         I n t r o d u c e   a n   a u t o m a t e d   p r o c e s s   t h a t   r u n s   p e r i o d i c a l l y   a n d   a p p l i e s   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s . 
         F o r   d e m o n s t r a t i o n ,   I ' l l   s i m u l a t e   t h i s   p r o c e s s   v i a   a   f u n c t i o n   t h a t   a p p l i e s   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s   w h e n e v e r   i t   i s   r u n .   I n   a   r e a l   s y s t e m ,   y o u   w o u l d   i m p l e m e n t   a   s c h e d u l e d   j o b   ( e . g . ,   u s i n g   a   c r o n   j o b   o r   a   b a c k g r o u n d   w o r k e r   p r o c e s s ) . 
 
 2 .   E n h a n c e d   S e c u r i t y   f o r   P a s s w o r d   H a s h i n g 
 
 A p p r o a c h : 
 
         U s e   b c r y p t   f o r   h a s h i n g   p a s s w o r d s   s e c u r e l y . 
         A d d   r a t e   l i m i t i n g   o n   l o g i n   a t t e m p t s   b y   t r a c k i n g   l o g i n   f a i l u r e s   i n   t h e   d a t a b a s e . 
 
 B e l o w   i s   t h e   u p d a t e d   c o d e : 
 E n h a n c e d   P y t h o n   C o d e   w i t h   A u t o m a t e d   I n t e r e s t   a n d   I m p r o v e d   S e c u r i t y 
 
 p y t h o n 
 
 i m p o r t   s q l i t e 3 
 i m p o r t   b c r y p t 
 i m p o r t   d a t e t i m e 
 
 #   S e t t i n g   u p   t h e   d a t a b a s e   c o n n e c t i o n   w i t h   a   p e r s i s t e n t   f i l e - b a s e d   d a t a b a s e 
 c o n n   =   s q l i t e 3 . c o n n e c t ( " b a n k . d b " )     #   U s i n g   a   p e r s i s t e n t   f i l e   f o r   d a t a b a s e 
 c u r s o r   =   c o n n . c u r s o r ( ) 
 
 #   C r e a t i n g   a c c o u n t s   t a b l e   i f   n o t   e x i s t s 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   I F   N O T   E X I S T S   a c c o u n t s   ( 
                 a c c o u n t _ i d   T E X T   P R I M A R Y   K E Y , 
                 o w n e r   T E X T , 
                 p a s s w o r d _ h a s h   T E X T , 
                 b a l a n c e   R E A L , 
                 a c c o u n t _ t y p e   T E X T , 
                 i n t e r e s t _ r a t e   R E A L   D E F A U L T   0 , 
                 f a i l e d _ a t t e m p t s   I N T E G E R   D E F A U L T   0 , 
                 l a s t _ f a i l e d _ a t t e m p t   D A T E T I M E   D E F A U L T   N U L L 
         ) 
 " " " ) 
 
 #   C r e a t i n g   t r a n s a c t i o n s   t a b l e   i f   n o t   e x i s t s 
 c u r s o r . e x e c u t e ( " " " 
         C R E A T E   T A B L E   I F   N O T   E X I S T S   t r a n s a c t i o n s   ( 
                 t r a n s a c t i o n _ i d   I N T E G E R   P R I M A R Y   K E Y   A U T O I N C R E M E N T , 
                 a c c o u n t _ i d   T E X T , 
                 t r a n s a c t i o n _ t y p e   T E X T , 
                 a m o u n t   R E A L , 
                 t i m e s t a m p   D A T E T I M E   D E F A U L T   C U R R E N T _ T I M E S T A M P , 
                 F O R E I G N   K E Y ( a c c o u n t _ i d )   R E F E R E N C E S   a c c o u n t s ( a c c o u n t _ i d ) 
         ) 
 " " " ) 
 
 c o n n . c o m m i t ( ) 
 
 
 c l a s s   A c c o u n t : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ) : 
                 s e l f . a c c o u n t _ i d   =   a c c o u n t _ i d 
                 s e l f . o w n e r   =   o w n e r 
                 s e l f . p a s s w o r d _ h a s h   =   b c r y p t . h a s h p w ( p a s s w o r d . e n c o d e ( ) ,   b c r y p t . g e n s a l t ( ) ) 
                 s e l f . b a l a n c e   =   b a l a n c e 
 
         d e f   s a v e _ t o _ d b ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   O R   R E P L A C E   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ) 
                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ' S t a n d a r d ' ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   s e l f . o w n e r ,   s e l f . p a s s w o r d _ h a s h ,   s e l f . b a l a n c e ) ) 
                 c o n n . c o m m i t ( ) 
 
         @ s t a t i c m e t h o d 
         d e f   l o a d _ f r o m _ d b ( a c c o u n t _ i d ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( a c c o u n t _ i d , ) ) 
                 r o w   =   c u r s o r . f e t c h o n e ( ) 
                 i f   r o w : 
                         i f   r o w [ 4 ]   = =   " S a v i n g s " : 
                                 r e t u r n   S a v i n g s A c c o u n t ( a c c o u n t _ i d = r o w [ 0 ] ,   o w n e r = r o w [ 1 ] ,   p a s s w o r d = " " ,   b a l a n c e = r o w [ 3 ] ,   i n t e r e s t _ r a t e = r o w [ 5 ] ) 
                         a c c o u n t   =   A c c o u n t ( a c c o u n t _ i d = r o w [ 0 ] ,   o w n e r = r o w [ 1 ] ,   p a s s w o r d = " " ,   b a l a n c e = r o w [ 3 ] ) 
                         a c c o u n t . p a s s w o r d _ h a s h   =   r o w [ 2 ]     #   L o a d   h a s h e d   p a s s w o r d 
                         r e t u r n   a c c o u n t 
                 r e t u r n   N o n e 
 
         d e f   a u t h e n t i c a t e ( s e l f ,   p a s s w o r d ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   f a i l e d _ a t t e m p t s ,   l a s t _ f a i l e d _ a t t e m p t   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( s e l f . a c c o u n t _ i d , ) ) 
                 r o w   =   c u r s o r . f e t c h o n e ( ) 
 
                 i f   r o w : 
                         f a i l e d _ a t t e m p t s ,   l a s t _ f a i l e d _ a t t e m p t   =   r o w 
                         n o w   =   d a t e t i m e . d a t e t i m e . n o w ( ) 
 
                         #   L o c k o u t   m e c h a n i s m :   I f   t o o   m a n y   f a i l e d   a t t e m p t s   i n   t h e   l a s t   1 5   m i n u t e s 
                         i f   f a i l e d _ a t t e m p t s   > =   3   a n d   l a s t _ f a i l e d _ a t t e m p t : 
                                 t i m e _ d i f f e r e n c e   =   ( n o w   -   d a t e t i m e . d a t e t i m e . s t r p t i m e ( l a s t _ f a i l e d _ a t t e m p t ,   " % Y - % m - % d   % H : % M : % S " ) ) . t o t a l _ s e c o n d s ( ) 
                                 i f   t i m e _ d i f f e r e n c e   <   9 0 0 : 
                                         r a i s e   P e r m i s s i o n E r r o r ( " A c c o u n t   l o c k e d   d u e   t o   m u l t i p l e   f a i l e d   a t t e m p t s .   P l e a s e   t r y   a g a i n   l a t e r . " ) 
 
                 #   C h e c k   p a s s w o r d   u s i n g   b c r y p t 
                 i f   b c r y p t . c h e c k p w ( p a s s w o r d . e n c o d e ( ) ,   s e l f . p a s s w o r d _ h a s h ) : 
                         #   R e s e t   f a i l e d   a t t e m p t s   o n   s u c c e s s f u l   l o g i n 
                         c u r s o r . e x e c u t e ( " " " 
                                 U P D A T E   a c c o u n t s   S E T   f a i l e d _ a t t e m p t s   =   0 ,   l a s t _ f a i l e d _ a t t e m p t   =   N U L L   W H E R E   a c c o u n t _ i d   =   ? 
                         " " " ,   ( s e l f . a c c o u n t _ i d , ) ) 
                         c o n n . c o m m i t ( ) 
                         r e t u r n   T r u e 
                 e l s e : 
                         #   U p d a t e   f a i l e d   a t t e m p t s   a n d   r e c o r d   t h e   t i m e 
                         c u r s o r . e x e c u t e ( " " " 
                                 U P D A T E   a c c o u n t s   S E T   f a i l e d _ a t t e m p t s   =   f a i l e d _ a t t e m p t s   +   1 ,   l a s t _ f a i l e d _ a t t e m p t   =   ? 
                                 W H E R E   a c c o u n t _ i d   =   ? 
                         " " " ,   ( n o w . s t r f t i m e ( " % Y - % m - % d   % H : % M : % S " ) ,   s e l f . a c c o u n t _ i d ) ) 
                         c o n n . c o m m i t ( ) 
                         r e t u r n   F a l s e 
 
         d e f   d e p o s i t ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   + =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " D e p o s i t " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   w i t h d r a w ( s e l f ,   a m o u n t ) : 
                 i f   a m o u n t   >   s e l f . b a l a n c e : 
                         r a i s e   V a l u e E r r o r ( f " I n s u f f i c i e n t   f u n d s   i n   a c c o u n t   { s e l f . a c c o u n t _ i d } . " ) 
                 i f   a m o u n t   < =   0 : 
                         r a i s e   V a l u e E r r o r ( " W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . " ) 
                 s e l f . b a l a n c e   - =   a m o u n t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " W i t h d r a w a l " ,   a m o u n t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   g e t _ t r a n s a c t i o n _ h i s t o r y ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " S E L E C T   t r a n s a c t i o n _ t y p e ,   a m o u n t ,   t i m e s t a m p   F R O M   t r a n s a c t i o n s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( s e l f . a c c o u n t _ i d , ) ) 
                 r e t u r n   c u r s o r . f e t c h a l l ( ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ) " 
 
 
 c l a s s   S a v i n g s A c c o u n t ( A c c o u n t ) : 
         d e f   _ _ i n i t _ _ ( s e l f ,   a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e = 0 . 0 ,   i n t e r e s t _ r a t e = 0 . 0 1 ) : 
                 s u p e r ( ) . _ _ i n i t _ _ ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ) 
                 s e l f . i n t e r e s t _ r a t e   =   i n t e r e s t _ r a t e 
 
         d e f   s a v e _ t o _ d b ( s e l f ) : 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   O R   R E P L A C E   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ,   i n t e r e s t _ r a t e ) 
                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ' S a v i n g s ' ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   s e l f . o w n e r ,   s e l f . p a s s w o r d _ h a s h ,   s e l f . b a l a n c e ,   s e l f . i n t e r e s t _ r a t e ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   a p p l y _ i n t e r e s t ( s e l f ) : 
                 #   S i m p l e   i n t e r e s t   f o r m u l a   a p p l i e d 
                 i n t e r e s t   =   s e l f . b a l a n c e   *   s e l f . i n t e r e s t _ r a t e 
                 s e l f . b a l a n c e   + =   i n t e r e s t 
                 s e l f . s a v e _ t o _ d b ( ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ? ,   ? ) 
                 " " " ,   ( s e l f . a c c o u n t _ i d ,   " I n t e r e s t " ,   i n t e r e s t ) ) 
                 c o n n . c o m m i t ( ) 
 
         d e f   _ _ s t r _ _ ( s e l f ) : 
                 r e t u r n   f " S a v i n g s A c c o u n t ( { s e l f . a c c o u n t _ i d } ,   O w n e r :   { s e l f . o w n e r } ,   B a l a n c e :   { s e l f . b a l a n c e } ,   I n t e r e s t   R a t e :   { s e l f . i n t e r e s t _ r a t e } ) " 
 
 
 d e f   a p p l y _ i n t e r e s t _ t o _ a l l _ s a v i n g s _ a c c o u n t s ( ) : 
         c u r s o r . e x e c u t e ( " S E L E C T   a c c o u n t _ i d   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ t y p e   =   ' S a v i n g s ' " ) 
         r o w s   =   c u r s o r . f e t c h a l l ( ) 
         f o r   r o w   i n   r o w s : 
                 a c c o u n t _ i d   =   r o w [ 0 ] 
                 a c c o u n t   =   A c c o u n t . l o a d _ f r o m _ d b ( a c c o u n t _ i d ) 
                 i f   i s i n s t a n c e ( a c c o u n t ,   S a v i n g s A c c o u n t ) : 
                         a c c o u n t . a p p l y _ i n t e r e s t ( ) 
                         p r i n t ( f " I n t e r e s t   a p p l i e d   t o   a c c o u n t   { a c c o u n t _ i d } " ) 
 
 
 #   C L I   S y s t e m   f o r   U s e r   I n t e r a c t i o n   w i t h   E n h a n c e d   S e c u r i t y   a n d   I n t e r e s t 
 d e f   m a i n ( ) : 
         w h i l e   T r u e : 
                 p r i n t ( " \ n - - -   B a n k i n g   S y s t e m   - - - " ) 
                 p r i n t ( " 1 .   C r e a t e   S t a n d a r d   A c c o u n t " ) 
                 p r i n t ( " 2 .   C r e a t e   S a v i n g s   A c c o u n t " ) 
                 p r i n t ( " 3 .   L o g i n   t o   A c c o u n t " ) 
                 p r i n t ( " 4 .   A p p l y   I n t e r e s t   t o   A l l   S a v i n g s   A c c o u n t s   ( A d m i n ) " ) 
                 p r i n t ( " 5 .   E x i t " ) 
                 c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                 i f   c h o i c e   = =   " 1 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         o w n e r   =   i n p u t ( " E n t e r   O w n e r   N a m e :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
                         b a l a n c e   =   f l o a t ( i n p u t ( " E n t e r   I n i t i a l   B a l a n c e :   " ) ) 
 
                         n e w _ a c c o u n t   =   A c c o u n t ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ) 
                         n e w _ a c c o u n t . s a v e _ t o _ d b ( ) 
                         p r i n t ( f " A c c o u n t   { a c c o u n t _ i d }   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 e l i f   c h o i c e   = =   " 2 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         o w n e r   =   i n p u t ( " E n t e r   O w n e r   N a m e :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
                         b a l a n c e   =   f l o a t ( i n p u t ( " E n t e r   I n i t i a l   B a l a n c e :   " ) ) 
                         i n t e r e s t _ r a t e   =   f l o a t ( i n p u t ( " E n t e r   I n t e r e s t   R a t e   ( a s   a   d e c i m a l ,   e . g . ,   0 . 0 2   f o r   2 % ) :   " ) ) 
 
                         n e w _ a c c o u n t   =   S a v i n g s A c c o u n t ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d ,   b a l a n c e ,   i n t e r e s t _ r a t e ) 
                         n e w _ a c c o u n t . s a v e _ t o _ d b ( ) 
                         p r i n t ( f " S a v i n g s   A c c o u n t   { a c c o u n t _ i d }   c r e a t e d   s u c c e s s f u l l y . " ) 
 
                 e l i f   c h o i c e   = =   " 3 " : 
                         a c c o u n t _ i d   =   i n p u t ( " E n t e r   A c c o u n t   I D :   " ) 
                         p a s s w o r d   =   i n p u t ( " E n t e r   P a s s w o r d :   " ) 
 
                         a c c o u n t   =   A c c o u n t . l o a d _ f r o m _ d b ( a c c o u n t _ i d ) 
                         i f   a c c o u n t   a n d   a c c o u n t . a u t h e n t i c a t e ( p a s s w o r d ) : 
                                 p r i n t ( f " W e l c o m e   { a c c o u n t . o w n e r } ! " ) 
                                 w h i l e   T r u e : 
                                         p r i n t ( " \ n - - -   A c c o u n t   M e n u   - - - " ) 
                                         p r i n t ( " 1 .   D e p o s i t " ) 
                                         p r i n t ( " 2 .   W i t h d r a w " ) 
                                         p r i n t ( " 3 .   C h e c k   B a l a n c e " ) 
                                         p r i n t ( " 4 .   V i e w   T r a n s a c t i o n   H i s t o r y " ) 
                                         i f   i s i n s t a n c e ( a c c o u n t ,   S a v i n g s A c c o u n t ) : 
                                                 p r i n t ( " 5 .   A p p l y   I n t e r e s t " ) 
                                         p r i n t ( " 6 .   L o g o u t " ) 
                                         s u b _ c h o i c e   =   i n p u t ( " C h o o s e   a n   o p t i o n :   " ) 
 
                                         i f   s u b _ c h o i c e   = =   " 1 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   d e p o s i t :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . d e p o s i t ( a m o u n t ) 
                                                         p r i n t ( " D e p o s i t   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e 
 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 C o n t i n u i n g   f r o m   w h e r e   w e   l e f t   o f f ,   I ' l l   c o m p l e t e   t h e   C L I   i n t e r a c t i o n   t h a t   i n c l u d e s   e n h a n c e d   s e c u r i t y   a n d   a u t o m a t e d   i n t e r e s t   f e a t u r e s . 
 
 H e r e ' s   t h e   c o m p l e t e ,   e n h a n c e d   P y t h o n   c o d e : 
 
 p y t h o n 
 
                                         e l i f   s u b _ c h o i c e   = =   " 2 " : 
                                                 a m o u n t   =   f l o a t ( i n p u t ( " E n t e r   a m o u n t   t o   w i t h d r a w :   " ) ) 
                                                 t r y : 
                                                         a c c o u n t . w i t h d r a w ( a m o u n t ) 
                                                         p r i n t ( " W i t h d r a w a l   s u c c e s s f u l . " ) 
                                                 e x c e p t   V a l u e E r r o r   a s   e : 
                                                         p r i n t ( e ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 3 " : 
                                                 p r i n t ( a c c o u n t ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 4 " : 
                                                 h i s t o r y   =   a c c o u n t . g e t _ t r a n s a c t i o n _ h i s t o r y ( ) 
                                                 f o r   t r a n s   i n   h i s t o r y : 
                                                         p r i n t ( f " { t r a n s [ 0 ] } :   { t r a n s [ 1 ] }   a t   { t r a n s [ 2 ] } " ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 5 "   a n d   i s i n s t a n c e ( a c c o u n t ,   S a v i n g s A c c o u n t ) : 
                                                 #   O n l y   f o r   s a v i n g s   a c c o u n t s 
                                                 a c c o u n t . a p p l y _ i n t e r e s t ( ) 
                                                 p r i n t ( " I n t e r e s t   a p p l i e d   s u c c e s s f u l l y . " ) 
 
                                         e l i f   s u b _ c h o i c e   = =   " 6 " : 
                                                 p r i n t ( " L o g g i n g   o u t . . . " ) 
                                                 b r e a k 
 
                                         e l s e : 
                                                 p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
                         e l s e : 
                                 p r i n t ( " I n v a l i d   A c c o u n t   I D   o r   P a s s w o r d . " ) 
 
                 e l i f   c h o i c e   = =   " 4 " : 
                         #   A d m i n   o p t i o n   t o   a p p l y   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s 
                         a p p l y _ i n t e r e s t _ t o _ a l l _ s a v i n g s _ a c c o u n t s ( ) 
 
                 e l i f   c h o i c e   = =   " 5 " : 
                         p r i n t ( " G o o d b y e ! " ) 
                         b r e a k 
 
                 e l s e : 
                         p r i n t ( " I n v a l i d   o p t i o n .   P l e a s e   t r y   a g a i n . " ) 
 
 
 #   R u n   t h e   C L I   f o r   u s e r   i n t e r a c t i o n 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
         m a i n ( ) 
 
 E n h a n c e m e n t s   B r e a k d o w n : 
 
         E n h a n c e d   S e c u r i t y : 
                 P a s s w o r d   H a s h i n g   w i t h   b c r y p t : 
                         T h e   A c c o u n t   c l a s s   n o w   u s e s   b c r y p t   f o r   h a s h i n g   p a s s w o r d s ,   w h i c h   m a k e s   p a s s w o r d s   r e s i s t a n t   t o   b r u t e   f o r c e   a t t a c k s . 
                         W h e n   a n   a c c o u n t   i s   c r e a t e d ,   t h e   p a s s w o r d   i s   h a s h e d   u s i n g   b c r y p t . g e n s a l t ( ) . 
                         D u r i n g   a u t h e n t i c a t i o n ,   t h e   s y s t e m   c h e c k s   t h e   h a s h e d   p a s s w o r d   w i t h   t h e   p r o v i d e d   p a s s w o r d   u s i n g   b c r y p t . c h e c k p w ( ) . 
                 R a t e   L i m i t i n g   f o r   L o g i n   A t t e m p t s : 
                         E a c h   a c c o u n t   k e e p s   t r a c k   o f   t h e   n u m b e r   o f   f a i l e d   l o g i n   a t t e m p t s . 
                         I f   t h e r e   a r e   t h r e e   o r   m o r e   f a i l e d   a t t e m p t s   w i t h i n   t h e   l a s t   1 5   m i n u t e s ,   t h e   a c c o u n t   i s   t e m p o r a r i l y   l o c k e d   t o   p r e v e n t   b r u t e - f o r c e   a t t a c k s . 
                         T h i s   m e c h a n i s m   r e d u c e s   t h e   r i s k   o f   u n a u t h o r i z e d   a c c e s s   b y   l i m i t i n g   t h e   r a t e   o f   l o g i n   a t t e m p t s . 
 
         A u t o m a t e d   I n t e r e s t   C a l c u l a t i o n : 
                 A   n e w   f u n c t i o n ,   a p p l y _ i n t e r e s t _ t o _ a l l _ s a v i n g s _ a c c o u n t s ( ) ,   i s   a v a i l a b l e   f o r   a d m i n i s t r a t i v e   u s e . 
                 T h i s   f u n c t i o n   a p p l i e s   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s   i n   t h e   d a t a b a s e . 
                 T h i s   w o u l d   t y p i c a l l y   b e   r u n   o n   a   m o n t h l y   b a s i s ,   b u t   f o r   d e m o n s t r a t i o n ,   a n   a d m i n   c a n   r u n   i t   a n y t i m e . 
                 E a c h   t i m e   i n t e r e s t   i s   a p p l i e d ,   i t   i s   r e c o r d e d   i n   t h e   t r a n s a c t i o n s   l o g . 
 
         M u l t i - U s e r   C L I   E n h a n c e m e n t s : 
                 T h e   C L I   s y s t e m   n o w   h a s   a n   A d m i n   O p t i o n   ( c h o i c e   4 )   t o   a p p l y   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s . 
                 U s e r s   c a n   i n t e r a c t i v e l y   l o g   i n ,   c r e a t e   a c c o u n t s ,   d e p o s i t ,   w i t h d r a w ,   a n d   v i e w   t r a n s a c t i o n   h i s t o r y . 
                 U s e r s   w i t h   s a v i n g s   a c c o u n t s   c a n   d i r e c t l y   a p p l y   i n t e r e s t   f r o m   t h e i r   a c c o u n t   m e n u . 
 
         L o c k o u t   M e c h a n i s m : 
                 T o   e n h a n c e   s e c u r i t y ,   a   l o c k o u t   m e c h a n i s m   i s   i m p l e m e n t e d . 
                 U s e r s   w h o   f a i l   a u t h e n t i c a t i o n   t h r e e   t i m e s   i n   a   r o w   w i t h i n   a   1 5 - m i n u t e   w i n d o w   w i l l   b e   t e m p o r a r i l y   l o c k e d   o u t . 
                 T h i s   p r e v e n t s   b r u t e - f o r c e   a t t e m p t s   f r o m   s u c c e e d i n g   q u i c k l y . 
 
 P o s s i b l e   F u t u r e   I m p r o v e m e n t s : 
 
         C o n c u r r e n c y   a n d   S c a l a b i l i t y : 
                 M o v e   t o   a   m o r e   r o b u s t   d a t a b a s e   m a n a g e m e n t   s y s t e m   l i k e   P o s t g r e S Q L   o r   M y S Q L   f o r   b e t t e r   s c a l a b i l i t y . 
                 I m p l e m e n t   t r a n s a c t i o n   m a n a g e m e n t   w i t h   A C I D   p r o p e r t i e s   f o r   r e l i a b l e   a n d   c o n c u r r e n t   a c c e s s   b y   m u l t i p l e   u s e r s . 
                 C o n s i d e r   u s i n g   a n   O R M   l i k e   S Q L A l c h e m y   t o   a b s t r a c t   a w a y   d i r e c t   S Q L   q u e r i e s   a n d   h a n d l e   m o r e   c o m p l e x   r e l a t i o n s h i p s   b e t w e e n   d a t a . 
 
         S c h e d u l e d   I n t e r e s t   A p p l i c a t i o n : 
                 A u t o m a t e   t h e   i n t e r e s t   a p p l i c a t i o n   b y   i n t e g r a t i n g   w i t h   a   t a s k   s c h e d u l e r   l i k e   C e l e r y   o r   u s i n g   c r o n   j o b s   t o   p e r i o d i c a l l y   r u n   t h e   a p p l y _ i n t e r e s t _ t o _ a l l _ s a v i n g s _ a c c o u n t s ( )   f u n c t i o n . 
                 T h i s   e n s u r e s   t h a t   i n t e r e s t   c a l c u l a t i o n s   h a p p e n   w i t h o u t   m a n u a l   i n t e r v e n t i o n . 
 
         A d v a n c e d   S e c u r i t y   E n h a n c e m e n t s : 
                 I m p l e m e n t   t w o - f a c t o r   a u t h e n t i c a t i o n   ( 2 F A )   f o r   a d d i t i o n a l   s e c u r i t y   d u r i n g   l o g i n . 
                 U s e   t o k e n s   o r   s e s s i o n s   f o r   m a n a g i n g   l o g g e d - i n   u s e r s ,   e n a b l i n g   a   m o r e   r o b u s t   a n d   s e c u r e   a u t h e n t i c a t i o n   p r o c e s s . 
 
         W e b   I n t e r f a c e : 
                 D e v e l o p   a   w e b - b a s e d   i n t e r f a c e   u s i n g   a   f r a m e w o r k   l i k e   F l a s k   o r   D j a n g o   t o   m a k e   t h e   b a n k i n g   s y s t e m   m o r e   u s e r - f r i e n d l y . 
                 T h i s   a l l o w s   u s e r s   t o   i n t e r a c t   t h r o u g h   a   w e b   b r o w s e r   i n s t e a d   o f   a   c o m m a n d   l i n e ,   i m p r o v i n g   u s a b i l i t y . 
 
         N o t i f i c a t i o n s   a n d   A l e r t s : 
                 A d d   s u p p o r t   f o r   e m a i l   o r   S M S   n o t i f i c a t i o n s   w h e n   c e r t a i n   a c t i o n s   a r e   p e r f o r m e d ,   s u c h   a s : 
                         L o w   b a l a n c e   w a r n i n g s . 
                         C o n f i r m a t i o n   f o r   d e p o s i t s   a n d   w i t h d r a w a l s . 
                         L o g i n   a l e r t s   f o r   a d d e d   s e c u r i t y . 
 
         I n t e r e s t   C a l c u l a t i o n   C o n f i g u r a t i o n : 
                 A l l o w   u s e r s   t o   c h o o s e   b e t w e e n   d i f f e r e n t   t y p e s   o f   a c c o u n t s :   f i x e d   i n t e r e s t   r a t e ,   c o m p o u n d   i n t e r e s t ,   e t c . 
                 O f f e r   m o r e   f l e x i b l e   c o n f i g u r a t i o n s   f o r   i n t e r e s t   r a t e   t y p e s   ( e . g . ,   m o n t h l y   o r   q u a r t e r l y   c o m p o u n d i n g ) . 
 
         A c c o u n t   L o c k   a n d   U n l o c k   R e q u e s t s : 
                 U s e r s   s h o u l d   b e   a b l e   t o   r e q u e s t   u n l o c k i n g   t h e i r   a c c o u n t   i f   l o c k e d   o u t . 
                 T h i s   c o u l d   b e   i m p l e m e n t e d   t h r o u g h   a   s e c u r e   r e c o v e r y   m e c h a n i s m ,   l i k e   a n s w e r i n g   s e c u r i t y   q u e s t i o n s   o r   u s i n g   e m a i l - b a s e d   v e r i f i c a t i o n   l i n k s . 
 
 W o u l d   y o u   l i k e   t o   p r o c e e d   w i t h   o n e   o f   t h e s e   f u t u r e   i m p r o v e m e n t s ,   s u c h   a s   a d d i n g   a n   a u t o m a t e d   i n t e r e s t   a p p l i c a t i o n   u s i n g   a   t a s k   s c h e d u l e r   o r   b u i l d i n g   a   w e b   i n t e r f a c e   u s i n g   F l a s k   o r   D j a n g o ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 I ' l l   p r o c e e d   b y   o u t l i n i n g   h o w   t o   b u i l d   a   w e b - b a s e d   i n t e r f a c e   u s i n g   F l a s k   f o r   t h e   b a n k i n g   s y s t e m .   T h i s   t r a n s i t i o n   w i l l   s i g n i f i c a n t l y   i m p r o v e   u s e r   a c c e s s i b i l i t y   a n d   u s a b i l i t y   b y   p r o v i d i n g   a   w e b   i n t e r f a c e   f o r   p e r f o r m i n g   a l l   a c c o u n t   o p e r a t i o n s . 
 T r a n s i t i o n   t o   a   W e b   A p p l i c a t i o n   U s i n g   F l a s k 
 O b j e c t i v e s : 
 
         F l a s k   W e b   I n t e r f a c e : 
                 I m p l e m e n t   t h e   b a s i c   b a n k i n g   s y s t e m   a s   a   w e b   s e r v i c e   u s i n g   t h e   F l a s k   f r a m e w o r k . 
                 C r e a t e   e n d p o i n t s   f o r   u s e r   a c t i o n s :   c r e a t i n g   a c c o u n t s ,   l o g g i n g   i n ,   d e p o s i t i n g ,   w i t h d r a w i n g ,   a n d   v i e w i n g   t r a n s a c t i o n   h i s t o r y . 
 
         F e a t u r e   T r a n s i t i o n : 
                 P r e s e r v e   a l l   t h e   f u n c t i o n a l i t i e s ,   i n c l u d i n g   a c c o u n t   c r e a t i o n ,   s a v i n g s   a c c o u n t s   w i t h   i n t e r e s t ,   d e p o s i t s ,   w i t h d r a w a l s ,   a n d   a u t h e n t i c a t i o n . 
                 A l l o w   u s e r s   t o   i n t e r a c t   t h r o u g h   a   b r o w s e r   w i t h   a   m o r e   i n t u i t i v e   i n t e r f a c e . 
 
         T e m p l a t e   I n t e g r a t i o n : 
                 U t i l i z e   H T M L   t e m p l a t e s   f o r   r e n d e r i n g   t h e   w e b   p a g e s . 
                 U s e   F l a s k   f o r m s   t o   a c c e p t   u s e r   i n p u t s . 
 
 S t e p - b y - S t e p   P l a n : 
 
         I n s t a l l   F l a s k : 
                 I n s t a l l   F l a s k   i n   y o u r   P y t h o n   e n v i r o n m e n t   u s i n g   p i p   i n s t a l l   F l a s k . 
 
         D a t a b a s e   I n t e g r a t i o n : 
                 T h e   e x i s t i n g   S Q L i t e   d a t a b a s e   ( b a n k . d b )   w i l l   c o n t i n u e   t o   b e   u s e d . 
                 F l a s k   w i l l   c o n n e c t   t o   t h i s   d a t a b a s e   t o   m a n a g e   a c c o u n t   a n d   t r a n s a c t i o n   r e c o r d s . 
 
         F l a s k   A p p l i c a t i o n   S t r u c t u r e : 
                 H o m e   P a g e :   D i s p l a y s   o p t i o n s   f o r   l o g g i n g   i n   o r   c r e a t i n g   a n   a c c o u n t . 
                 C r e a t e   A c c o u n t :   A   f o r m   f o r   c r e a t i n g   b o t h   s t a n d a r d   a n d   s a v i n g s   a c c o u n t s . 
                 L o g i n :   U s e r s   l o g   i n   t o   a c c e s s   t h e i r   a c c o u n t s . 
                 A c c o u n t   D a s h b o a r d :   D i s p l a y s   a c c o u n t   d e t a i l s ,   o p t i o n s   f o r   d e p o s i t ,   w i t h d r a w a l ,   a n d   t r a n s a c t i o n   h i s t o r y . 
                 A d m i n   A c t i o n s :   A d m i n s   c a n   t r i g g e r   t h e   i n t e r e s t   c a l c u l a t i o n   f o r   a l l   s a v i n g s   a c c o u n t s . 
 
 F l a s k   C o d e   I m p l e m e n t a t i o n : 
 
 B e l o w   i s   t h e   P y t h o n   c o d e   t h a t   i m p l e m e n t s   t h e   F l a s k - b a s e d   w e b   i n t e r f a c e   f o r   t h e   b a n k i n g   s y s t e m . 
 
 p y t h o n 
 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e ,   r e q u e s t ,   r e d i r e c t ,   u r l _ f o r ,   f l a s h ,   s e s s i o n 
 i m p o r t   s q l i t e 3 
 i m p o r t   b c r y p t 
 i m p o r t   d a t e t i m e 
 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y '     #   S e c r e t   k e y   f o r   s e s s i o n   m a n a g e m e n t 
 
 #   D a t a b a s e   s e t u p 
 D A T A B A S E   =   ' b a n k . d b ' 
 
 d e f   g e t _ d b _ c o n n e c t i o n ( ) : 
         c o n n   =   s q l i t e 3 . c o n n e c t ( D A T A B A S E ) 
         c o n n . r o w _ f a c t o r y   =   s q l i t e 3 . R o w 
         r e t u r n   c o n n 
 
 @ a p p . r o u t e ( ' / ' ) 
 d e f   i n d e x ( ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' i n d e x . h t m l ' ) 
 
 @ a p p . r o u t e ( ' / c r e a t e _ a c c o u n t ' ,   m e t h o d s = ( ' G E T ' ,   ' P O S T ' ) ) 
 d e f   c r e a t e _ a c c o u n t ( ) : 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
                 a c c o u n t _ t y p e   =   r e q u e s t . f o r m [ ' a c c o u n t _ t y p e ' ] 
                 a c c o u n t _ i d   =   r e q u e s t . f o r m [ ' a c c o u n t _ i d ' ] 
                 o w n e r   =   r e q u e s t . f o r m [ ' o w n e r ' ] 
                 p a s s w o r d   =   r e q u e s t . f o r m [ ' p a s s w o r d ' ] 
                 b a l a n c e   =   f l o a t ( r e q u e s t . f o r m [ ' b a l a n c e ' ] ) 
                 i n t e r e s t _ r a t e   =   f l o a t ( r e q u e s t . f o r m [ ' i n t e r e s t _ r a t e ' ] )   i f   ' i n t e r e s t _ r a t e '   i n   r e q u e s t . f o r m   e l s e   0 . 0 
 
                 p a s s w o r d _ h a s h   =   b c r y p t . h a s h p w ( p a s s w o r d . e n c o d e ( ) ,   b c r y p t . g e n s a l t ( ) ) 
                 c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
                 c u r s o r   =   c o n n . c u r s o r ( ) 
 
                 t r y : 
                         i f   a c c o u n t _ t y p e   = =   ' S a v i n g s ' : 
                                 c u r s o r . e x e c u t e ( " " " 
                                         I N S E R T   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ,   i n t e r e s t _ r a t e ) 
                                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ? ,   ? ) 
                                 " " " ,   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   ' S a v i n g s ' ,   i n t e r e s t _ r a t e ) ) 
                         e l s e : 
                                 c u r s o r . e x e c u t e ( " " " 
                                         I N S E R T   I N T O   a c c o u n t s   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ,   a c c o u n t _ t y p e ) 
                                         V A L U E S   ( ? ,   ? ,   ? ,   ? ,   ' S t a n d a r d ' ) 
                                 " " " ,   ( a c c o u n t _ i d ,   o w n e r ,   p a s s w o r d _ h a s h ,   b a l a n c e ) ) 
                         c o n n . c o m m i t ( ) 
                         f l a s h ( ' A c c o u n t   c r e a t e d   s u c c e s s f u l l y ! ' ,   ' s u c c e s s ' ) 
                 e x c e p t   s q l i t e 3 . I n t e g r i t y E r r o r : 
                         f l a s h ( ' A c c o u n t   I D   a l r e a d y   e x i s t s .   P l e a s e   c h o o s e   a   d i f f e r e n t   o n e . ' ,   ' d a n g e r ' ) 
                 f i n a l l y : 
                         c o n n . c l o s e ( ) 
 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' c r e a t e _ a c c o u n t . h t m l ' ) 
 
 @ a p p . r o u t e ( ' / l o g i n ' ,   m e t h o d s = ( ' G E T ' ,   ' P O S T ' ) ) 
 d e f   l o g i n ( ) : 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
                 a c c o u n t _ i d   =   r e q u e s t . f o r m [ ' a c c o u n t _ i d ' ] 
                 p a s s w o r d   =   r e q u e s t . f o r m [ ' p a s s w o r d ' ] 
 
                 c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
                 c u r s o r   =   c o n n . c u r s o r ( ) 
                 c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( a c c o u n t _ i d , ) ) 
                 a c c o u n t   =   c u r s o r . f e t c h o n e ( ) 
                 c o n n . c l o s e ( ) 
 
                 i f   a c c o u n t : 
                         p a s s w o r d _ h a s h   =   a c c o u n t [ ' p a s s w o r d _ h a s h ' ] 
                         i f   b c r y p t . c h e c k p w ( p a s s w o r d . e n c o d e ( ) ,   p a s s w o r d _ h a s h ) : 
                                 #   R e s e t   f a i l e d   a t t e m p t s   a f t e r   a   s u c c e s s f u l   l o g i n 
                                 c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
                                 c o n n . e x e c u t e ( " " " 
                                         U P D A T E   a c c o u n t s   S E T   f a i l e d _ a t t e m p t s   =   0 ,   l a s t _ f a i l e d _ a t t e m p t   =   N U L L   W H E R E   a c c o u n t _ i d   =   ? 
                                 " " " ,   ( a c c o u n t _ i d , ) ) 
                                 c o n n . c o m m i t ( ) 
                                 c o n n . c l o s e ( ) 
 
                                 s e s s i o n [ ' a c c o u n t _ i d ' ]   =   a c c o u n t _ i d 
                                 f l a s h ( f ' W e l c o m e ,   { a c c o u n t [ " o w n e r " ] } ! ' ,   ' s u c c e s s ' ) 
                                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' d a s h b o a r d ' ) ) 
                         e l s e : 
                                 #   I n c r e m e n t   f a i l e d   a t t e m p t s   a n d   u p d a t e   l a s t   f a i l e d   t i m e 
                                 c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
                                 n o w   =   d a t e t i m e . d a t e t i m e . n o w ( ) . s t r f t i m e ( " % Y - % m - % d   % H : % M : % S " ) 
                                 c o n n . e x e c u t e ( " " " 
                                         U P D A T E   a c c o u n t s   S E T   f a i l e d _ a t t e m p t s   =   f a i l e d _ a t t e m p t s   +   1 ,   l a s t _ f a i l e d _ a t t e m p t   =   ? 
                                         W H E R E   a c c o u n t _ i d   =   ? 
                                 " " " ,   ( n o w ,   a c c o u n t _ i d ) ) 
                                 c o n n . c o m m i t ( ) 
                                 c o n n . c l o s e ( ) 
                                 f l a s h ( ' I n v a l i d   p a s s w o r d .   P l e a s e   t r y   a g a i n . ' ,   ' d a n g e r ' ) 
                 e l s e : 
                         f l a s h ( ' I n v a l i d   A c c o u n t   I D .   P l e a s e   t r y   a g a i n . ' ,   ' d a n g e r ' ) 
 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' l o g i n . h t m l ' ) 
 
 @ a p p . r o u t e ( ' / d a s h b o a r d ' ,   m e t h o d s = ( ' G E T ' ,   ' P O S T ' ) ) 
 d e f   d a s h b o a r d ( ) : 
         i f   ' a c c o u n t _ i d '   n o t   i n   s e s s i o n : 
                 f l a s h ( ' Y o u   n e e d   t o   l o g   i n   f i r s t . ' ,   ' d a n g e r ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' l o g i n ' ) ) 
 
         a c c o u n t _ i d   =   s e s s i o n [ ' a c c o u n t _ i d ' ] 
         c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
         c u r s o r   =   c o n n . c u r s o r ( ) 
         c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ i d   =   ? " ,   ( a c c o u n t _ i d , ) ) 
         a c c o u n t   =   c u r s o r . f e t c h o n e ( ) 
 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
                 i f   ' d e p o s i t '   i n   r e q u e s t . f o r m : 
                         a m o u n t   =   f l o a t ( r e q u e s t . f o r m [ ' a m o u n t ' ] ) 
                         i f   a m o u n t   < =   0 : 
                                 f l a s h ( ' D e p o s i t   a m o u n t   m u s t   b e   p o s i t i v e . ' ,   ' d a n g e r ' ) 
                         e l s e : 
                                 n e w _ b a l a n c e   =   a c c o u n t [ ' b a l a n c e ' ]   +   a m o u n t 
                                 c o n n . e x e c u t e ( " " " 
                                         U P D A T E   a c c o u n t s   S E T   b a l a n c e   =   ?   W H E R E   a c c o u n t _ i d   =   ? 
                                 " " " ,   ( n e w _ b a l a n c e ,   a c c o u n t _ i d ) ) 
                                 c o n n . e x e c u t e ( " " " 
                                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                                         V A L U E S   ( ? ,   ' D e p o s i t ' ,   ? ) 
                                 " " " ,   ( a c c o u n t _ i d ,   a m o u n t ) ) 
                                 c o n n . c o m m i t ( ) 
                                 f l a s h ( ' D e p o s i t   s u c c e s s f u l ! ' ,   ' s u c c e s s ' ) 
 
                 e l i f   ' w i t h d r a w '   i n   r e q u e s t . f o r m : 
                         a m o u n t   =   f l o a t ( r e q u e s t . f o r m [ ' a m o u n t ' ] ) 
                         i f   a m o u n t   < =   0 : 
                                 f l a s h ( ' W i t h d r a w a l   a m o u n t   m u s t   b e   p o s i t i v e . ' ,   ' d a n g e r ' ) 
                         e l i f   a m o u n t   >   a c c o u n t [ ' b a l a n c e ' ] : 
                                 f l a s h ( ' I n s u f f i c i e n t   f u n d s . ' ,   ' d a n g e r ' ) 
                         e l s e : 
                                 n e w _ b a l a n c e   =   a c c o u n t [ ' b a l a n c e ' ]   -   a m o u n t 
                                 c o n n . e x e c u t e ( " " " 
                                         U P D A T E   a c c o u n t s   S E T   b a l a n c e   =   ?   W H E R E   a c c o u n t _ i d   =   ? 
                                 " " " ,   ( n e w _ b a l a n c e ,   a c c o u n t _ i d ) ) 
                                 c o n n . e x e c u t e ( " " " 
                                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                                         V A L U E S   ( ? ,   ' W i t h d r a w a l ' ,   ? ) 
                                 " " " ,   ( a c c o u n t _ i d ,   a m o u n t ) ) 
                                 c o n n . c o m m i t ( ) 
                                 f l a s h ( ' W i t h d r a w a l   s u c c e s s f u l ! ' ,   ' s u c c e s s ' ) 
 
         c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   t r a n s a c t i o n s   W H E R E   a c c o u n t _ i d   =   ?   O R D E R   B Y   t i m e s t a m p   D E S C " ,   ( a c c o u n t _ i d , ) ) 
         t r a n s a c t i o n s   =   c u r s o r . f e t c h a l l ( ) 
         c o n n . c l o s e ( ) 
 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' d a s h b o a r d . h t m l ' ,   a c c o u n t = a c c o u n t ,   t r a n s a c t i o n s = t r a n s a c t i o n s ) 
 
 @ a p p . r o u t e ( ' / l o g o u t ' ) 
 d e f   l o g o u t ( ) : 
         s e s s i o n . p o p ( ' a c c o u n t _ i d ' ,   N o n e ) 
         f l a s h ( ' Y o u   h a v e   b e e n   l o g g e d   o u t . ' ,   ' i n f o ' ) 
         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
 @ a p p . r o u t e ( ' / a p p l y _ i n t e r e s t ' ) 
 d e f   a p p l y _ i n t e r e s t ( ) : 
         #   A d m i n   a c t i o n   t o   a p p l y   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s 
         c o n n   =   g e t _ d b _ c o n n e c t i o n ( ) 
         c u r s o r   =   c o n n . c u r s o r ( ) 
         c u r s o r . e x e c u t e ( " S E L E C T   *   F R O M   a c c o u n t s   W H E R E   a c c o u n t _ t y p e   =   ' S a v i n g s ' " ) 
         s a v i n g s _ a c c o u n t s   =   c u r s o r . f e t c h a l l ( ) 
 
         f o r   a c c o u n t   i n   s a v i n g s _ a c c o u n t s : 
                 i n t e r e s t   =   a c c o u n t [ ' b a l a n c e ' ]   *   a c c o u n t [ ' i n t e r e s t _ r a t e ' ] 
                 n e w _ b a l a n c e   =   a c c o u n t [ ' b a l a n c e ' ]   +   i n t e r e s t 
                 c u r s o r . e x e c u t e ( " " " 
                         U P D A T E   a c c o u n t s   S E T   b a l a n c e   =   ?   W H E R E   a c c o u n t _ i d   =   ? 
                 " " " ,   ( n e w _ b a l a n c e ,   a c c o u n t [ ' a c c o u n t _ i d ' ] ) ) 
                 c u r s o r . e x e c u t e ( " " " 
                         I N S E R T   I N T O   t r a n s a c t i o n s   ( a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e ,   a m o u n t ) 
                         V A L U E S   ( ? ,   ' I n t e r e s t ' ,   ? ) 
                 " " " ,   ( a c c o u n t [ ' a c c o u n t _ i d ' ] ,   i n t e r e s t ) ) 
 
         c o n n . c o m m i t ( ) 
         c o n n . c l o s e ( ) 
 
         f l a s h ( ' I n t e r e s t   h a s   b e e n   a p p l i e d   t o   a l l   s a v i n g s   a c c o u n t s . ' ,   ' s u c c e s s ' ) 
         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
         a p p . r u n ( d e b u g = T r u e ) 
 
 E x p l a n a t i o n : 
 
         F l a s k   A p p l i c a t i o n   S e t u p : 
                 F l a s k   i s   u s e d   t o   b u i l d   a   w e b   a p p l i c a t i o n   t h a t   c a n   b e   a c c e s s e d   t h r o u g h   a   b r o w s e r . 
                 g e t _ d b _ c o n n e c t i o n ( )   i s   a   h e l p e r   f u n c t i o n   t o   c o n n e c t   t o   t h e   S Q L i t e   d a t a b a s e . 
 
         R o u t e s : 
                 /   ( H o m e   P a g e ) :   P r e s e n t s   o p t i o n s   f o r   l o g g i n g   i n   o r   c r e a t i n g   a n   a c c o u n t . 
                 / c r e a t e _ a c c o u n t :   A l l o w s   u s e r s   t o   c r e a t e   a   n e w   a c c o u n t   ( e i t h e r   s t a n d a r d   o r   s a v i n g s ) . 
                 / l o g i n :   P r o v i d e s   a   l o g i n   f o r m   f o r   u s e r s .   A f t e r   s u c c e s s f u l   l o g i n ,   t h e y   a r e   r e d i r e c t e d   t o   t h e   d a s h b o a r d . 
                 / d a s h b o a r d :   D i s p l a y s   t h e   a c c o u n t   d a s h b o a r d   w h e r e   u s e r s   c a n   d e p o s i t ,   w i t h d r a w ,   a n d   v i e w   t r a n s a c t i o n s . 
                 / l o g o u t :   L o g s   u s e r s   o u t   o f   t h e i r   s e s s i o n . 
                 / a p p l y _ i n t e r e s t :   A d m i n   a c t i o n   t o   a p p l y   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s . 
 
         T e m p l a t e   I n t e g r a t i o n : 
                 F l a s k   t e m p l a t e s   ( H T M L   f i l e s )   w o u l d   b e   u s e d   t o   c r e a t e   t h e   v i e w s   f o r   t h e   a p p l i c a t i o n   ( e . g . ,   i n d e x . h t m l ,   c r e a t e _ a c c o u n t . h t m l ,   l o g i n . h t m l ,   d a s h b o a r d . h t m l ) . 
                 T h e s e   t e m p l a t e s   w o u l d   p r o v i d e   a   u s e r - f r i e n d l y   i n t e r f a c e   f o r   i n t e r a c t i n g   w i t h   t h e   s y s t e m . 
 
         S e c u r i t y   F e a t u r e s : 
                 P a s s w o r d s   a r e   h a s h e d   u s i n g   b c r y p t . 
                 L o g i n   a t t e m p t s   a r e   t r a c k e d ,   a n d   f a i l e d   a t t e m p t s   a r e   r e c o r d e d . 
                 S e s s i o n s   a r e   u s e d   t o   m a n a g e   l o g i n   s t a t e ,   e n s u r i n g   s e c u r e   a c c e s s   t o   u s e r   a c c o u n t s . 
 
         I n t e r e s t   C a l c u l a t i o n : 
                 T h e   / a p p l y _ i n t e r e s t   r o u t e   a l l o w s 
 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 L e t ' s   p r o c e e d   w i t h   a   d e t a i l e d   e x p l a n a t i o n   o n   h o w   t o   e x p a n d   a n d   d e p l o y   t h i s   w e b   a p p l i c a t i o n   f o r   r e a l - w o r l d   u s e .   I ' l l   g u i d e   y o u   o n   t h e   f o l l o w i n g : 
 
         H T M L   T e m p l a t e   C r e a t i o n : 
                 P r o v i d e   b a s i c   H T M L   t e m p l a t e s   f o r   t h e   c o r e   p a g e s :   H o m e ,   C r e a t e   A c c o u n t ,   L o g i n ,   D a s h b o a r d ,   a n d   A d m i n   a c t i o n s . 
         R u n n i n g   t h e   A p p l i c a t i o n : 
                 S h o w   h o w   t o   r u n   t h e   F l a s k   a p p   l o c a l l y   a n d   i n t e r a c t   w i t h   i t   u s i n g   a   b r o w s e r . 
         D e p l o y m e n t   C o n s i d e r a t i o n s : 
                 E x p l a i n   o p t i o n s   f o r   d e p l o y i n g   t h i s   F l a s k   a p p   u s i n g   h o s t i n g   p l a t f o r m s   l i k e   H e r o k u   o r   R e n d e r . 
                 D i s c u s s   p o t e n t i a l   p r o d u c t i o n - l e v e l   c o n s i d e r a t i o n s   f o r   t h e   d a t a b a s e   a n d   t h e   w e b   s e r v e r . 
 
 1 .   H T M L   T e m p l a t e   C r e a t i o n 
 
 W e   n e e d   t o   c r e a t e   s i m p l e   H T M L   t e m p l a t e s   f o r   e a c h   o f   t h e   c o r e   f u n c t i o n a l i t i e s   o f   t h e   b a n k i n g   w e b   a p p l i c a t i o n .   B e l o w   a r e   e x a m p l e s   o f   H T M L   f i l e s   f o r   t h e   t e m p l a t e s . 
 t e m p l a t e s / i n d e x . h t m l 
 
 T h i s   i s   t h e   h o m e   p a g e   t h a t   w e l c o m e s   u s e r s   a n d   o f f e r s   t h e m   o p t i o n s   t o   l o g   i n   o r   c r e a t e   a   n e w   a c c o u n t . 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > B a n k i n g   S y s t e m < / t i t l e > 
 < / h e a d > 
 < b o d y > 
         < h 1 > W e l c o m e   t o   t h e   B a n k i n g   S y s t e m < / h 1 > 
         < a   h r e f = " { {   u r l _ f o r ( ' c r e a t e _ a c c o u n t ' )   } } " > C r e a t e   a n   A c c o u n t < / a > < b r > 
         < a   h r e f = " { {   u r l _ f o r ( ' l o g i n ' )   } } " > L o g i n   t o   A c c o u n t < / a > < b r > 
         < a   h r e f = " { {   u r l _ f o r ( ' a p p l y _ i n t e r e s t ' )   } } " > A d m i n :   A p p l y   I n t e r e s t   t o   S a v i n g s   A c c o u n t s < / a > 
 < / b o d y > 
 < / h t m l > 
 
 t e m p l a t e s / c r e a t e _ a c c o u n t . h t m l 
 
 T h i s   p a g e   a l l o w s   u s e r s   t o   c r e a t e   a   s t a n d a r d   o r   s a v i n g s   a c c o u n t . 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > C r e a t e   A c c o u n t < / t i t l e > 
 < / h e a d > 
 < b o d y > 
         < h 1 > C r e a t e   A c c o u n t < / h 1 > 
         < f o r m   m e t h o d = " P O S T " > 
                 < l a b e l   f o r = " a c c o u n t _ t y p e " > A c c o u n t   T y p e : < / l a b e l > 
                 < s e l e c t   n a m e = " a c c o u n t _ t y p e "   i d = " a c c o u n t _ t y p e " > 
                         < o p t i o n   v a l u e = " S t a n d a r d " > S t a n d a r d < / o p t i o n > 
                         < o p t i o n   v a l u e = " S a v i n g s " > S a v i n g s < / o p t i o n > 
                 < / s e l e c t > < b r > < b r > 
 
                 < l a b e l   f o r = " a c c o u n t _ i d " > A c c o u n t   I D : < / l a b e l > 
                 < i n p u t   t y p e = " t e x t "   n a m e = " a c c o u n t _ i d "   i d = " a c c o u n t _ i d "   r e q u i r e d > < b r > < b r > 
 
                 < l a b e l   f o r = " o w n e r " > O w n e r   N a m e : < / l a b e l > 
                 < i n p u t   t y p e = " t e x t "   n a m e = " o w n e r "   i d = " o w n e r "   r e q u i r e d > < b r > < b r > 
 
                 < l a b e l   f o r = " p a s s w o r d " > P a s s w o r d : < / l a b e l > 
                 < i n p u t   t y p e = " p a s s w o r d "   n a m e = " p a s s w o r d "   i d = " p a s s w o r d "   r e q u i r e d > < b r > < b r > 
 
                 < l a b e l   f o r = " b a l a n c e " > I n i t i a l   B a l a n c e : < / l a b e l > 
                 < i n p u t   t y p e = " n u m b e r "   n a m e = " b a l a n c e "   i d = " b a l a n c e "   s t e p = " 0 . 0 1 "   r e q u i r e d > < b r > < b r > 
 
                 < d i v   i d = " i n t e r e s t _ r a t e _ d i v "   s t y l e = " d i s p l a y :   n o n e ; " > 
                         < l a b e l   f o r = " i n t e r e s t _ r a t e " > I n t e r e s t   R a t e   ( d e c i m a l   f o r m a t ,   e . g . ,   0 . 0 2   f o r   2 % ) : < / l a b e l > 
                         < i n p u t   t y p e = " n u m b e r "   n a m e = " i n t e r e s t _ r a t e "   i d = " i n t e r e s t _ r a t e "   s t e p = " 0 . 0 1 " > < b r > < b r > 
                 < / d i v > 
 
                 < b u t t o n   t y p e = " s u b m i t " > C r e a t e   A c c o u n t < / b u t t o n > 
         < / f o r m > 
 
         < s c r i p t > 
                 / /   S h o w   o r   h i d e   i n t e r e s t   r a t e   i n p u t   b a s e d   o n   a c c o u n t   t y p e   s e l e c t i o n 
                 d o c u m e n t . g e t E l e m e n t B y I d ( " a c c o u n t _ t y p e " ) . a d d E v e n t L i s t e n e r ( " c h a n g e " ,   f u n c t i o n ( )   { 
                         i f   ( t h i s . v a l u e   = = =   " S a v i n g s " )   { 
                                 d o c u m e n t . g e t E l e m e n t B y I d ( " i n t e r e s t _ r a t e _ d i v " ) . s t y l e . d i s p l a y   =   " b l o c k " ; 
                         }   e l s e   { 
                                 d o c u m e n t . g e t E l e m e n t B y I d ( " i n t e r e s t _ r a t e _ d i v " ) . s t y l e . d i s p l a y   =   " n o n e " ; 
                         } 
                 } ) ; 
         < / s c r i p t > 
         < a   h r e f = " { {   u r l _ f o r ( ' i n d e x ' )   } } " > B a c k   t o   H o m e < / a > 
 < / b o d y > 
 < / h t m l > 
 
 t e m p l a t e s / l o g i n . h t m l 
 
 A   s i m p l e   l o g i n   f o r m   f o r   u s e r s   t o   a c c e s s   t h e i r   a c c o u n t s . 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > L o g i n < / t i t l e > 
 < / h e a d > 
 < b o d y > 
         < h 1 > L o g i n < / h 1 > 
         < f o r m   m e t h o d = " P O S T " > 
                 < l a b e l   f o r = " a c c o u n t _ i d " > A c c o u n t   I D : < / l a b e l > 
                 < i n p u t   t y p e = " t e x t "   n a m e = " a c c o u n t _ i d "   i d = " a c c o u n t _ i d "   r e q u i r e d > < b r > < b r > 
 
                 < l a b e l   f o r = " p a s s w o r d " > P a s s w o r d : < / l a b e l > 
                 < i n p u t   t y p e = " p a s s w o r d "   n a m e = " p a s s w o r d "   i d = " p a s s w o r d "   r e q u i r e d > < b r > < b r > 
 
                 < b u t t o n   t y p e = " s u b m i t " > L o g i n < / b u t t o n > 
         < / f o r m > 
         < a   h r e f = " { {   u r l _ f o r ( ' i n d e x ' )   } } " > B a c k   t o   H o m e < / a > 
 < / b o d y > 
 < / h t m l > 
 
 t e m p l a t e s / d a s h b o a r d . h t m l 
 
 T h e   d a s h b o a r d   f o r   u s e r s   t o   d e p o s i t ,   w i t h d r a w ,   o r   v i e w   t h e i r   a c c o u n t   i n f o r m a t i o n   a n d   t r a n s a c t i o n   h i s t o r y . 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > D a s h b o a r d < / t i t l e > 
 < / h e a d > 
 < b o d y > 
         < h 1 > A c c o u n t   D a s h b o a r d < / h 1 > 
         < h 3 > W e l c o m e   { {   a c c o u n t [ ' o w n e r ' ]   } } < / h 3 > 
         < p > A c c o u n t   I D :   { {   a c c o u n t [ ' a c c o u n t _ i d ' ]   } } < / p > 
         < p > A c c o u n t   B a l a n c e :   { {   a c c o u n t [ ' b a l a n c e ' ]   } } < / p > 
 
         < f o r m   m e t h o d = " P O S T " > 
                 < h 2 > D e p o s i t < / h 2 > 
                 < l a b e l   f o r = " d e p o s i t _ a m o u n t " > A m o u n t : < / l a b e l > 
                 < i n p u t   t y p e = " n u m b e r "   n a m e = " a m o u n t "   i d = " d e p o s i t _ a m o u n t "   s t e p = " 0 . 0 1 "   r e q u i r e d > 
                 < b u t t o n   t y p e = " s u b m i t "   n a m e = " d e p o s i t " > D e p o s i t < / b u t t o n > 
         < / f o r m > 
 
         < f o r m   m e t h o d = " P O S T " > 
                 < h 2 > W i t h d r a w < / h 2 > 
                 < l a b e l   f o r = " w i t h d r a w _ a m o u n t " > A m o u n t : < / l a b e l > 
                 < i n p u t   t y p e = " n u m b e r "   n a m e = " a m o u n t "   i d = " w i t h d r a w _ a m o u n t "   s t e p = " 0 . 0 1 "   r e q u i r e d > 
                 < b u t t o n   t y p e = " s u b m i t "   n a m e = " w i t h d r a w " > W i t h d r a w < / b u t t o n > 
         < / f o r m > 
 
         < h 2 > T r a n s a c t i o n   H i s t o r y < / h 2 > 
         < u l > 
                 { %   f o r   t r a n s a c t i o n   i n   t r a n s a c t i o n s   % } 
                 < l i > { {   t r a n s a c t i o n [ ' t r a n s a c t i o n _ t y p e ' ]   } } :   { {   t r a n s a c t i o n [ ' a m o u n t ' ]   } }   a t   { {   t r a n s a c t i o n [ ' t i m e s t a m p ' ]   } } < / l i > 
                 { %   e n d f o r   % } 
         < / u l > 
 
         < a   h r e f = " { {   u r l _ f o r ( ' l o g o u t ' )   } } " > L o g o u t < / a > 
 < / b o d y > 
 < / h t m l > 
 
 2 .   R u n n i n g   t h e   A p p l i c a t i o n   L o c a l l y 
 
 T o   r u n   t h e   F l a s k   a p p   l o c a l l y : 
 
         E n s u r e   D e p e n d e n c i e s   A r e   I n s t a l l e d : 
                 I n s t a l l   F l a s k   a n d   b c r y p t   u s i n g   p i p : 
 
                 b a s h 
 
         p i p   i n s t a l l   F l a s k   b c r y p t 
 
 R u n   t h e   F l a s k   A p p : 
 
         U s e   t h e   f o l l o w i n g   c o m m a n d   t o   r u n   t h e   F l a s k   a p p l i c a t i o n : 
 
         b a s h 
 
                 p y t h o n   y o u r _ f l a s k _ a p p . p y 
 
                 M a k e   s u r e   t o   r e p l a c e   y o u r _ f l a s k _ a p p . p y   w i t h   t h e   f i l e n a m e   o f   y o u r   F l a s k   P y t h o n   f i l e . 
                 O p e n   a   w e b   b r o w s e r   a n d   n a v i g a t e   t o   h t t p : / / 1 2 7 . 0 . 0 . 1 : 5 0 0 0   t o   i n t e r a c t   w i t h   t h e   w e b   a p p l i c a t i o n . 
 
 3 .   D e p l o y m e n t   C o n s i d e r a t i o n s 
 
 F o r   d e p l o y i n g   t h e   F l a s k   a p p   t o   a   p r o d u c t i o n   e n v i r o n m e n t ,   t h e r e   a r e   s e v e r a l   s t e p s   a n d   h o s t i n g   o p t i o n s   t o   c o n s i d e r : 
 H o s t i n g   P l a t f o r m s : 
 
         H e r o k u : 
                 H e r o k u   i s   a   p o p u l a r   p l a t f o r m - a s - a - s e r v i c e   t h a t   s u p p o r t s   e a s y   d e p l o y m e n t   o f   F l a s k   a p p s . 
                 C r e a t e   a   P r o c f i l e   f o r   H e r o k u   t o   r u n   t h e   a p p . 
                 E x a m p l e   P r o c f i l e : 
 
                 m a k e f i l e 
 
                 w e b :   g u n i c o r n   y o u r _ f l a s k _ a p p : a p p 
 
                 P u s h   t h e   p r o j e c t   t o   a   G i t   r e p o s i t o r y   a n d   c o n n e c t   i t   t o   H e r o k u   f o r   a u t o m a t i c   d e p l o y m e n t . 
 
         R e n d e r : 
                 R e n d e r   i s   a n o t h e r   p l a t f o r m   t h a t   c a n   b e   u s e d   t o   e a s i l y   h o s t   P y t h o n   w e b   a p p l i c a t i o n s . 
                 F o l l o w   t h e   s t e p s   f o r   s e t t i n g   u p   a   w e b   s e r v i c e   i n   R e n d e r ,   p o i n t i n g   t o   y o u r   G i t H u b   r e p o s i t o r y . 
 
         A W S   E C 2 ,   D i g i t a l O c e a n ,   o r   A z u r e : 
                 S e t   u p   a   v i r t u a l   m a c h i n e ,   i n s t a l l   n e c e s s a r y   s o f t w a r e ,   a n d   r u n   t h e   F l a s k   a p p l i c a t i o n   u s i n g   a   p r o d u c t i o n   s e r v e r   l i k e   G u n i c o r n   o r   u W S G I   b e h i n d   N g i n x . 
                 T h i s   s e t u p   p r o v i d e s   g r e a t e r   f l e x i b i l i t y   a n d   c o n t r o l ,   b u t   i t   r e q u i r e s   m o r e   e x p e r t i s e   i n   s e r v e r   c o n f i g u r a t i o n . 
 
 P r o d u c t i o n - L e v e l   C o n s i d e r a t i o n s : 
 
         W e b   S e r v e r : 
                 G u n i c o r n   o r   u W S G I   s h o u l d   b e   u s e d   a s   p r o d u c t i o n   s e r v e r s . 
                 T h e s e   s e r v e r s   a r e   m o r e   e f f i c i e n t   a n d   s e c u r e   c o m p a r e d   t o   F l a s k ' s   b u i l t - i n   d e v e l o p m e n t   s e r v e r . 
 
         D a t a b a s e : 
                 S Q L i t e   i s   s u i t a b l e   f o r   p r o t o t y p i n g   o r   s m a l l - s c a l e   a p p l i c a t i o n s ,   b u t   f o r   p r o d u c t i o n   u s e ,   c o n s i d e r   m i g r a t i n g   t o   P o s t g r e S Q L   o r   M y S Q L   f o r   b e t t e r   p e r f o r m a n c e   a n d   s c a l a b i l i t y . 
                 U s e   S Q L A l c h e m y ,   a n   O R M   l i b r a r y ,   t o   a b s t r a c t   a n d   m a k e   m i g r a t i o n   t o   o t h e r   d a t a b a s e s   e a s i e r . 
 
         S e c u r i t y   E n h a n c e m e n t s : 
                 H T T P S :   U s e   L e t ' s   E n c r y p t   o r   a n o t h e r   S S L   c e r t i f i c a t e   a u t h o r i t y   t o   s e r v e   y o u r   a p p l i c a t i o n   o v e r   H T T P S . 
                 E n v i r o n m e n t   V a r i a b l e s :   S t o r e   s e n s i t i v e   d a t a   ( e . g . ,   d a t a b a s e   c o n n e c t i o n   s t r i n g s ,   s e c r e t   k e y s )   i n   e n v i r o n m e n t   v a r i a b l e s   r a t h e r   t h a n   h a r d c o d i n g   t h e m   i n   y o u r   s o u r c e   c o d e . 
 
         S c a l i n g   a n d   C o n c u r r e n c y : 
                 T o   h a n d l e   m u l t i p l e   c o n c u r r e n t   u s e r s ,   m a k e   u s e   o f   l o a d   b a l a n c e r s   a n d   d e p l o y   y o u r   a p p   a c r o s s   m u l t i p l e   s e r v e r s . 
                 C o n s i d e r   u s i n g   R e d i s   f o r   c a c h i n g   f r e q u e n t l y   a c c e s s e d   d a t a   a n d   C e l e r y   f o r   m a n a g i n g   b a c k g r o u n d   t a s k s   ( l i k e   a p p l y i n g   i n t e r e s t   a u t o m a t i c a l l y ) . 
 
         M o n i t o r i n g   a n d   L o g g i n g : 
                 I m p l e m e n t   l o g g i n g   f o r   t r a c k i n g   e r r o r s   a n d   u n d e r s t a n d i n g   a p p l i c a t i o n   b e h a v i o r . 
                 U s e   a   m o n i t o r i n g   t o o l   l i k e   P r o m e t h e u s   o r   N e w   R e l i c   t o   k e e p   a n   e y e   o n   a p p l i c a t i o n   p e r f o r m a n c e   a n d   a v a i l a b i l i t y . 
 
 C o n c l u s i o n 
 
 T h i s   s e t u p   t r a n s f o r m s   t h e   c o m m a n d - l i n e   b a n k i n g   s y s t e m   i n t o   a n   i n t e r a c t i v e   w e b - b a s e d   a p p l i c a t i o n   u s i n g   F l a s k ,   o f f e r i n g : 
 
         U s e r - f r i e n d l y   W e b   I n t e r f a c e :   E n h a n c e d   u s e r   e x p e r i e n c e   v i a   t e m p l a t e s   a n d   f o r m s . 
         P e r s i s t e n t   D a t a b a s e   I n t e g r a t i o n :   W i t h   S Q L i t e   a s   t h e   i n i t i a l   c h o i c e ,   t h i s   c a n   b e   s c a l e d   t o   m o r e   r o b u s t   s y s t e m s   l i k e   P o s t g r e S Q L   f o r   p r o d u c t i o n . 
         S c a l a b l e   D e p l o y m e n t   O p t i o n s :   U s e   c l o u d   s e r v i c e s   l i k e   H e r o k u ,   R e n d e r ,   o r   A W S   f o r   h o s t i n g . 
         S e c u r i t y :   S t r o n g   p a s s w o r d   h a s h i n g   ( b c r y p t ) ,   s e s s i o n   m a n a g e m e n t ,   a n d   p l a n s   f o r   f u r t h e r   e n h a n c e m e n t s   s u c h   a s   H T T P S   a n d   s c a l i n g . 
 
 W o u l d   y o u   l i k e   m o r e   d e t a i l e d   g u i d a n c e   o n   a n y   o f   t h e s e   d e p l o y m e n t   o p t i o n s ,   o r   h e l p   w i t h   o t h e r   f e a t u r e s ,   s u c h   a s   a d d i n g   a n   a d m i n   p a n e l   f o r   e a s i e r   m a n a g e m e n t ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 I ' l l   d i v e   d e e p e r   i n t o   t h e   d e p l o y m e n t   o p t i o n s   a n d   p r o v i d e   m o r e   d e t a i l e d   g u i d a n c e   f o r   d e p l o y i n g   t h e   F l a s k - b a s e d   b a n k i n g   s y s t e m ,   f o c u s i n g   o n   t w o   p o p u l a r   a p p r o a c h e s : 
 
         D e p l o y i n g   t h e   F l a s k   A p p l i c a t i o n   o n   H e r o k u . 
         D e p l o y i n g   t h e   F l a s k   A p p l i c a t i o n   o n   A W S   E C 2 . 
 
 A d d i t i o n a l l y ,   I ' l l   p r o v i d e   d e t a i l s   o n   s e t t i n g   u p   a n   A d m i n   P a n e l   u s i n g   F l a s k - A d m i n ,   w h i c h   w i l l   a l l o w   f o r   e a s i e r   m a n a g e m e n t   o f   t h e   a c c o u n t s ,   t r a n s a c t i o n s ,   a n d   o t h e r   f e a t u r e s   o f   t h e   s y s t e m . 
 1 .   D e p l o y i n g   o n   H e r o k u 
 
 H e r o k u   i s   o n e   o f   t h e   e a s i e s t   w a y s   t o   d e p l o y   s m a l l   t o   m e d i u m - s i z e d   F l a s k   a p p l i c a t i o n s .   I t ' s   u s e r - f r i e n d l y   a n d   f r e e   t o   g e t   s t a r t e d . 
 S t e p s   t o   D e p l o y   o n   H e r o k u : 
 
         I n s t a l l   H e r o k u   C L I : 
                 D o w n l o a d   a n d   i n s t a l l   t h e   H e r o k u   C L I . 
 
         P r e p a r e   Y o u r   P r o j e c t   f o r   D e p l o y m e n t : 
                 M a k e   s u r e   y o u r   p r o j e c t   d i r e c t o r y   h a s   t h e   f o l l o w i n g : 
 
                         P r o c f i l e :   S p e c i f i e s   t h e   c o m m a n d s   H e r o k u   w i l l   u s e   t o   s t a r t   y o u r   a p p . 
 
                         p l a i n t e x t 
 
 w e b :   g u n i c o r n   y o u r _ f l a s k _ a p p : a p p 
 
 R e p l a c e   y o u r _ f l a s k _ a p p   w i t h   t h e   n a m e   o f   y o u r   P y t h o n   s c r i p t   ( w i t h o u t   . p y ) . 
 
 r e q u i r e m e n t s . t x t :   L i s t   a l l   y o u r   p r o j e c t   d e p e n d e n c i e s .   G e n e r a t e   t h i s   f i l e   u s i n g : 
 
 b a s h 
 
 p i p   f r e e z e   >   r e q u i r e m e n t s . t x t 
 
 T h i s   f i l e   h e l p s   H e r o k u   k n o w   w h i c h   l i b r a r i e s   t o   i n s t a l l . 
 
 r u n t i m e . t x t   ( o p t i o n a l ) :   S p e c i f i e s   t h e   P y t h o n   v e r s i o n . 
 
 p l a i n t e x t 
 
                 p y t h o n - 3 . 9 . 1 2 
 
 C r e a t e   a   G i t   R e p o s i t o r y : 
 
         I n i t i a l i z e   a   G i t   r e p o s i t o r y   i f   y o u   h a v e n  t   a l r e a d y : 
 
         b a s h 
 
         g i t   i n i t 
         g i t   a d d   . 
         g i t   c o m m i t   - m   " I n i t i a l   c o m m i t " 
 
 L o g i n   t o   H e r o k u   a n d   C r e a t e   a n   A p p : 
 
         L o g i n   u s i n g   t h e   H e r o k u   C L I : 
 
         b a s h 
 
 h e r o k u   l o g i n 
 
 C r e a t e   a   n e w   H e r o k u   a p p : 
 
 b a s h 
 
         h e r o k u   c r e a t e   y o u r - a p p - n a m e 
 
         R e p l a c e   y o u r - a p p - n a m e   w i t h   a   u n i q u e   n a m e   f o r   y o u r   a p p l i c a t i o n . 
 
 A d d   H e r o k u   R e m o t e   a n d   P u s h   C o d e : 
 
         H e r o k u   c r e a t e s   a   G i t   r e m o t e   r e p o s i t o r y   f o r   y o u .   P u s h   y o u r   c o d e   t o   H e r o k u : 
 
         b a s h 
 
         g i t   p u s h   h e r o k u   m a s t e r 
 
 S c a l e   Y o u r   A p p : 
 
         S t a r t   a   w e b   i n s t a n c e : 
 
         b a s h 
 
         h e r o k u   p s : s c a l e   w e b = 1 
 
 O p e n   Y o u r   A p p : 
 
         O p e n   t h e   n e w l y   d e p l o y e d   a p p   i n   y o u r   b r o w s e r : 
 
         b a s h 
 
         h e r o k u   o p e n 
 
 E n v i r o n m e n t   V a r i a b l e s : 
 
         T o   a d d   y o u r   e n v i r o n m e n t   v a r i a b l e s   ( l i k e   s e c r e t   k e y s ) ,   u s e : 
 
         b a s h 
 
                 h e r o k u   c o n f i g : s e t   S E C R E T _ K E Y = ' y o u r _ s e c r e t _ k e y ' 
 
 2 .   D e p l o y i n g   o n   A W S   E C 2 
 
 A W S   E C 2   i s   s u i t a b l e   f o r   m o r e   r o b u s t   d e p l o y m e n t s ,   w h e r e   y o u   h a v e   f u l l   c o n t r o l   o v e r   y o u r   s e r v e r   e n v i r o n m e n t . 
 S t e p s   t o   D e p l o y   o n   A W S   E C 2 : 
 
         L a u n c h   a n   E C 2   I n s t a n c e : 
                 G o   t o   A W S   E C 2   C o n s o l e   a n d   l a u n c h   a   n e w   i n s t a n c e . 
                 C h o o s e   a n   U b u n t u   A M I   ( A m a z o n   M a c h i n e   I m a g e )   a s   i t   i s   b e g i n n e r - f r i e n d l y . 
                 S e l e c t   a n   i n s t a n c e   t y p e   ( e . g . ,   t 2 . m i c r o   f o r   t h e   f r e e   t i e r ) . 
                 C o n f i g u r e   s e c u r i t y   g r o u p s   t o   a l l o w   i n b o u n d   t r a f f i c   o n   p o r t s   2 2   ( S S H )   a n d   5 0 0 0   ( F l a s k   s e r v e r ) . 
 
         C o n n e c t   t o   Y o u r   E C 2   I n s t a n c e : 
                 D o w n l o a d   t h e   k e y   p a i r   ( e . g . ,   m y - k e y . p e m ) . 
                 C o n n e c t   u s i n g   S S H : 
 
                 b a s h 
 
         s s h   - i   " m y - k e y . p e m "   u b u n t u @ y o u r - e c 2 - p u b l i c - i p 
 
 I n s t a l l   R e q u i r e d   S o f t w a r e : 
 
         U p d a t e   t h e   p a c k a g e   l i s t   a n d   i n s t a l l   n e c e s s a r y   s o f t w a r e : 
 
         b a s h 
 
 s u d o   a p t   u p d a t e 
 s u d o   a p t   i n s t a l l   p y t h o n 3 - p i p   p y t h o n 3 - d e v   n g i n x   g i t 
 
 I n s t a l l   v i r t u a l e n v   t o   m a n a g e   p r o j e c t   d e p e n d e n c i e s : 
 
 b a s h 
 
         s u d o   p i p 3   i n s t a l l   v i r t u a l e n v 
 
 C l o n e   Y o u r   P r o j e c t   a n d   S e t   U p : 
 
         C l o n e   y o u r   G i t H u b   r e p o s i t o r y   i n t o   t h e   E C 2   i n s t a n c e : 
 
         b a s h 
 
 g i t   c l o n e   h t t p s : / / g i t h u b . c o m / y o u r _ u s e r n a m e / y o u r _ r e p o s i t o r y . g i t 
 c d   y o u r _ r e p o s i t o r y 
 
 C r e a t e   a   v i r t u a l   e n v i r o n m e n t   a n d   a c t i v a t e   i t : 
 
 b a s h 
 
 v i r t u a l e n v   v e n v 
 s o u r c e   v e n v / b i n / a c t i v a t e 
 
 I n s t a l l   t h e   d e p e n d e n c i e s : 
 
 b a s h 
 
         p i p   i n s t a l l   - r   r e q u i r e m e n t s . t x t 
 
 R u n   t h e   A p p l i c a t i o n   U s i n g   G u n i c o r n : 
 
         G u n i c o r n   i s   a   p r o d u c t i o n - g r a d e   W S G I   s e r v e r . 
         T e s t   r u n n i n g   y o u r   a p p : 
 
         b a s h 
 
         g u n i c o r n   - - b i n d   0 . 0 . 0 . 0 : 5 0 0 0   y o u r _ f l a s k _ a p p : a p p 
 
         T h i s   s h o u l d   s t a r t   t h e   a p p   o n   p o r t   5 0 0 0 . 
 
 C o n f i g u r e   N g i n x : 
 
         N g i n x   w i l l   a c t   a s   a   r e v e r s e   p r o x y ,   f o r w a r d i n g   r e q u e s t s   t o   G u n i c o r n . 
         C r e a t e   a   n e w   c o n f i g u r a t i o n   f i l e   f o r   N g i n x : 
 
         b a s h 
 
 s u d o   n a n o   / e t c / n g i n x / s i t e s - a v a i l a b l e / y o u r _ a p p 
 
 P a s t e   t h e   f o l l o w i n g   c o n t e n t : 
 
 n g i n x 
 
 s e r v e r   { 
         l i s t e n   8 0 ; 
         s e r v e r _ n a m e   y o u r - e c 2 - p u b l i c - i p ; 
 
         l o c a t i o n   /   { 
                 p r o x y _ p a s s   h t t p : / / 1 2 7 . 0 . 0 . 1 : 5 0 0 0 ; 
                 p r o x y _ s e t _ h e a d e r   H o s t   $ h o s t ; 
                 p r o x y _ s e t _ h e a d e r   X - R e a l - I P   $ r e m o t e _ a d d r ; 
                 p r o x y _ s e t _ h e a d e r   X - F o r w a r d e d - F o r   $ p r o x y _ a d d _ x _ f o r w a r d e d _ f o r ; 
                 p r o x y _ s e t _ h e a d e r   X - F o r w a r d e d - P r o t o   $ s c h e m e ; 
         } 
 } 
 
 E n a b l e   t h e   c o n f i g u r a t i o n   b y   c r e a t i n g   a   s y m b o l i c   l i n k : 
 
 b a s h 
 
 s u d o   l n   - s   / e t c / n g i n x / s i t e s - a v a i l a b l e / y o u r _ a p p   / e t c / n g i n x / s i t e s - e n a b l e d 
 
 T e s t   a n d   r e s t a r t   N g i n x : 
 
 b a s h 
 
                 s u d o   n g i n x   - t 
                 s u d o   s y s t e m c t l   r e s t a r t   n g i n x 
 
         A c c e s s   Y o u r   A p p l i c a t i o n : 
                 V i s i t   y o u r   E C 2   p u b l i c   I P   a d d r e s s   i n   t h e   b r o w s e r .   N g i n x   w i l l   f o r w a r d   r e q u e s t s   t o   G u n i c o r n ,   w h i c h   s e r v e s   y o u r   F l a s k   a p p . 
 
 3 .   A d d i n g   a n   A d m i n   P a n e l   U s i n g   F l a s k - A d m i n 
 
 F l a s k - A d m i n   p r o v i d e s   a   p o w e r f u l ,   o u t - o f - t h e - b o x   a d m i n i s t r a t i v e   i n t e r f a c e   f o r   m a n a g i n g   d a t a   w i t h i n   F l a s k   a p p l i c a t i o n s .   H e r e ' s   h o w   t o   s e t   u p   a n   a d m i n   p a n e l : 
 
         I n s t a l l   F l a s k - A d m i n : 
                 I n s t a l l   F l a s k - A d m i n : 
 
                 b a s h 
 
         p i p   i n s t a l l   F l a s k - A d m i n 
 
 I n t e g r a t e   F l a s k - A d m i n : 
 
         A d d   F l a s k - A d m i n   t o   y o u r   F l a s k   a p p l i c a t i o n : 
 
 p y t h o n 
 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e d i r e c t ,   u r l _ f o r ,   s e s s i o n 
 f r o m   f l a s k _ a d m i n   i m p o r t   A d m i n ,   e x p o s e ,   A d m i n I n d e x V i e w 
 f r o m   f l a s k _ a d m i n . c o n t r i b . s q l a   i m p o r t   M o d e l V i e w 
 f r o m   f l a s k _ s q l a l c h e m y   i m p o r t   S Q L A l c h e m y 
 
 #   F l a s k   s e t u p 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ D A T A B A S E _ U R I ' ]   =   ' s q l i t e : / / / b a n k . d b ' 
 d b   =   S Q L A l c h e m y ( a p p ) 
 
 #   C r e a t e   a   b a s i c   U s e r   m o d e l   a s   a n   e x a m p l e 
 c l a s s   A c c o u n t ( d b . M o d e l ) : 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   p r i m a r y _ k e y = T r u e ) 
         o w n e r   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   n u l l a b l e = F a l s e ) 
         p a s s w o r d _ h a s h   =   d b . C o l u m n ( d b . S t r i n g ( 1 2 8 ) ,   n u l l a b l e = F a l s e ) 
         b a l a n c e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         a c c o u n t _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 2 0 ) ) 
         i n t e r e s t _ r a t e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
 
 #   A d m i n   w i t h   c u s t o m   i n d e x   v i e w   f o r   a u t h e n t i c a t i o n 
 c l a s s   M y A d m i n I n d e x V i e w ( A d m i n I n d e x V i e w ) : 
         @ e x p o s e ( ' / ' ) 
         d e f   i n d e x ( s e l f ) : 
                 i f   ' a d m i n '   n o t   i n   s e s s i o n : 
                         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
                 r e t u r n   s u p e r ( M y A d m i n I n d e x V i e w ,   s e l f ) . i n d e x ( ) 
 
 #   M o d e l   v i e w   f o r   m a n a g i n g   A c c o u n t   m o d e l s   i n   a d m i n 
 c l a s s   A c c o u n t M o d e l V i e w ( M o d e l V i e w ) : 
         d e f   i s _ a c c e s s i b l e ( s e l f ) : 
                 r e t u r n   ' a d m i n '   i n   s e s s i o n 
 
 #   F l a s k   r o u t e s   f o r   l o g i n   t o   a c c e s s   a d m i n 
 @ a p p . r o u t e ( ' / a d m i n / l o g i n ' ,   m e t h o d s = [ ' G E T ' ,   ' P O S T ' ] ) 
 d e f   a d m i n _ l o g i n ( ) : 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
                 u s e r n a m e   =   r e q u e s t . f o r m [ ' u s e r n a m e ' ] 
                 p a s s w o r d   =   r e q u e s t . f o r m [ ' p a s s w o r d ' ] 
                 i f   u s e r n a m e   = =   ' a d m i n '   a n d   p a s s w o r d   = =   ' p a s s w o r d ' : 
                         s e s s i o n [ ' a d m i n ' ]   =   T r u e 
                         r e t u r n   r e d i r e c t ( ' / a d m i n ' ) 
                 e l s e : 
                         f l a s h ( ' I n v a l i d   c r e d e n t i a l s ' ,   ' d a n g e r ' ) 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a d m i n _ l o g i n . h t m l ' ) 
 
 @ a p p . r o u t e ( ' / a d m i n / l o g o u t ' ) 
 d e f   a d m i n _ l o g o u t ( ) : 
         s e s s i o n . p o p ( ' a d m i n ' ,   N o n e ) 
         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
 #   F l a s k - A d m i n   s e t u p 
 a d m i n   =   A d m i n ( a p p ,   i n d e x _ v i e w = M y A d m i n I n d e x V i e w ( ) ) 
 a d m i n . a d d _ v i e w ( A c c o u n t M o d e l V i e w ( A c c o u n t ,   d b . s e s s i o n ) ) 
 
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' : 
         a p p . r u n ( d e b u g = T r u e ) 
 
 E x p l a n a t i o n : 
 
         S Q L A l c h e m y   D a t a b a s e :   H e r e ,   S Q L A l c h e m y   i s   u s e d   t o   m a n a g e   d a t a b a s e   m o d e l s   a n d   e n a b l e   i n t e g r a t i o n   w i t h   F l a s k - A d m i n . 
         C u s t o m   A d m i n   I n d e x   V i e w :   T h e   M y A d m i n I n d e x V i e w   i s   u s e d   t o   a d d   a u t h e n t i c a t i o n   t o   a c c e s s   t h e   a d m i n   p a n e l . 
         M o d e l   M a n a g e m e n t :   T h e   A c c o u n t M o d e l V i e w   a l l o w s   C R U D   o p e r a t i o n s   o n   t h e   A c c o u n t   m o d e l ,   m a k i n g   i t   e a s i e r   t o   m a n a g e   a c c o u n t s . 
 
 A d m i n   L o g i n   T e m p l a t e   ( t e m p l a t e s / a d m i n _ l o g i n . h t m l ) : 
 
 h t m l 
 
         < ! D O C T Y P E   h t m l > 
         < h t m l   l a n g = " e n " > 
         < h e a d > 
                 < m e t a   c h a r s e t = " U T F - 8 " > 
                 < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
                 < t i t l e > A d m i n   L o g i n < / t i t l e > 
         < / h e a d > 
         < b o d y > 
                 < h 1 > A d m i n   L o g i n < / h 1 > 
                 < f o r m   m e t h o d = " P O S T " > 
                         < l a b e l   f o r = " u s e r n a m e " > U s e r n a m e : < / l a b e l > 
                         < i n p u t   t y p e = " t e x t "   n a m e = " u s e r n a m e "   i d = " u s e r n a m e "   r e q u i r e d > < b r > < b r > 
 
                         < l a b e l   f o r = " p a s s w o r d " > P a s s w o r d : < / l a b e l > 
                         < i n p u t   t y p e = " p a s s w o r d "   n a m e = " p a s s w o r d "   i d = " p a s s w o r d "   r e q u i r e d > < b r > < b r > 
 
                         < b u t t o n   t y p e = " s u b m i t " > L o g i n < / b u t t o n > 
                 < / f o r m > 
         < / b o d y > 
         < / h t m l > 
 
 C o n c l u s i o n 
 
 W i t h   t h e   a b o v e   s e t u p : 
 
         D e p l o y m e n t   o n   H e r o k u   o r   A W S   E C 2 : 
                 H e r o k u   i s   i d e a l   f o r   e a s y   d e p l o y m e n t ,   w h i l e   A W S   E C 2   o f f e r s   m o r e   c o n t r o l   f o r   s c a l i n g   a n d   p e r f o r m a n c e . 
         A d m i n   P a n e l   w i t h   F l a s k - A d m i n : 
                 A d d i n g   F l a s k - A d m i n   h e l p s   t o   e f f i c i e n t l y   m a n a g e   a c c o u n t s ,   u s e r s ,   a n d   t r a n s a c t i o n s   f r o m   a   c e n t r a l   d a s h b o a r d . 
                 Y o u   c a n   r e s t r i c t   a c c e s s   t o   t h e   a d m i n   p a n e l   u s i n g   c u s t o m   v i e w s   a n d   a u t h e n t i c a t i o n . 
 
 W o u l d   y o u   l i k e   m o r e   d e t a i l e d   i n s t r u c t i o n s   o n   a n y   o f   t h e s e   s t e p s ,   o r   p e r h a p s   a   g u i d e   o n   s e t t i n g   u p   a n   a d m i n   d a s h b o a r d   w i t h   m o r e   a d v a n c e d   f e a t u r e s   l i k e   v i s u a l   a n a l y t i c s   o r   m a n a g i n g   o t h e r   a s p e c t s   o f   t h e   s y s t e m ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 L e t ' s   e n h a n c e   t h e   A d m i n   D a s h b o a r d   f u r t h e r   t o   p r o v i d e   a d v a n c e d   f e a t u r e s ,   s u c h   a s : 
 
         V i s u a l   A n a l y t i c s : 
                 I n t e g r a t e   d a t a   v i s u a l i z a t i o n   t o   p r o v i d e   i n s i g h t s   i n t o   a c c o u n t s ,   t r a n s a c t i o n s ,   a n d   b a l a n c e s . 
                 C h a r t s   f o r   d e p o s i t s ,   w i t h d r a w a l s ,   a n d   a c c o u n t   b a l a n c e s   o v e r   t i m e   t o   h e l p   a d m i n s   u n d e r s t a n d   t h e   s y s t e m   u s a g e . 
 
         A d v a n c e d   A d m i n   M a n a g e m e n t : 
                 A d d   m o r e   c o m p r e h e n s i v e   u s e r   m a n a g e m e n t   c a p a b i l i t i e s . 
                 A l l o w   a d m i n   u s e r s   t o   a c t i v a t e ,   d e a c t i v a t e ,   a n d   m a n a g e   a c c o u n t s . 
                 C r e a t e   a   m o r e   d e t a i l e d   v i e w   o f   a c c o u n t   a c t i v i t i e s   w i t h   f i l t e r i n g   c a p a b i l i t i e s . 
 
         S t e p s   f o r   S e t t i n g   U p   T h e s e   F e a t u r e s : 
                 W e ' l l   e n h a n c e   t h e   e x i s t i n g   F l a s k   a p p l i c a t i o n   a n d   a d m i n   d a s h b o a r d   b y   i n t e g r a t i n g   a d d i t i o n a l   F l a s k   e x t e n s i o n s   l i k e   F l a s k - A d m i n ,   F l a s k - S Q L A l c h e m y ,   a n d   F l a s k - S e s s i o n . 
                 W e ' l l   u s e   C h a r t . j s   f o r   d a t a   v i s u a l i z a t i o n   t o   c r e a t e   i n t e r a c t i v e   c h a r t s   f o r   a d m i n   u s e r s . 
 
 E n h a n c i n g   t h e   A d m i n   D a s h b o a r d 
 1 .   A d v a n c e d   A d m i n   P a n e l   U s i n g   F l a s k - A d m i n 
 
 R e q u i r e m e n t s : 
 
         I n s t a l l   n e c e s s a r y   F l a s k   p a c k a g e s : 
 
         b a s h 
 
         p i p   i n s t a l l   F l a s k   F l a s k - S Q L A l c h e m y   F l a s k - A d m i n 
 
         S Q L A l c h e m y   i s   u s e d   t o   i n t e g r a t e   a   m o r e   f l e x i b l e   O R M   f o r   t h e   d a t a b a s e . 
 
         F l a s k - A d m i n   w i l l   h e l p   c r e a t e   a n   i n t e r a c t i v e   i n t e r f a c e   f o r   m a n a g i n g   a c c o u n t s   a n d   t r a n s a c t i o n s . 
 
         C h a r t . j s   i s   a   J a v a S c r i p t   l i b r a r y   t h a t   p r o v i d e s   d y n a m i c   c h a r t s   f o r   v i s u a l   r e p r e s e n t a t i o n . 
 
 U p d a t e d   F l a s k   A p p l i c a t i o n   C o d e 
 
 B e l o w   i s   t h e   e n h a n c e d   v e r s i o n   o f   t h e   F l a s k   b a n k i n g   s y s t e m   i n t e g r a t e d   w i t h   F l a s k - A d m i n   f o r   i m p r o v e d   u s e r   m a n a g e m e n t ,   a l o n g   w i t h   C h a r t . j s   f o r   v i s u a l   a n a l y t i c s . 
 F l a s k   A p p l i c a t i o n   w i t h   A d m i n   D a s h b o a r d 
 
 p y t h o n 
 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e ,   r e q u e s t ,   r e d i r e c t ,   u r l _ f o r ,   f l a s h ,   s e s s i o n 
 f r o m   f l a s k _ s q l a l c h e m y   i m p o r t   S Q L A l c h e m y 
 f r o m   f l a s k _ a d m i n   i m p o r t   A d m i n ,   A d m i n I n d e x V i e w ,   e x p o s e 
 f r o m   f l a s k _ a d m i n . c o n t r i b . s q l a   i m p o r t   M o d e l V i e w 
 i m p o r t   b c r y p t 
 i m p o r t   d a t e t i m e 
 i m p o r t   j s o n 
 
 #   F l a s k   S e t u p 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ D A T A B A S E _ U R I ' ]   =   ' s q l i t e : / / / b a n k . d b ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ T R A C K _ M O D I F I C A T I O N S ' ]   =   F a l s e 
 d b   =   S Q L A l c h e m y ( a p p ) 
 
 #   D a t a b a s e   M o d e l s 
 c l a s s   A c c o u n t ( d b . M o d e l ) : 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   p r i m a r y _ k e y = T r u e ) 
         o w n e r   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   n u l l a b l e = F a l s e ) 
         p a s s w o r d _ h a s h   =   d b . C o l u m n ( d b . S t r i n g ( 1 2 8 ) ,   n u l l a b l e = F a l s e ) 
         b a l a n c e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         a c c o u n t _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 2 0 ) ) 
         i n t e r e s t _ r a t e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         i s _ a c t i v e   =   d b . C o l u m n ( d b . B o o l e a n ,   d e f a u l t = T r u e ) 
 
         d e f   _ _ r e p r _ _ ( s e l f ) : 
                 r e t u r n   f ' < A c c o u n t   { s e l f . a c c o u n t _ i d } ,   O w n e r   { s e l f . o w n e r } ,   B a l a n c e   { s e l f . b a l a n c e } > ' 
 
 c l a s s   T r a n s a c t i o n ( d b . M o d e l ) : 
         t r a n s a c t i o n _ i d   =   d b . C o l u m n ( d b . I n t e g e r ,   p r i m a r y _ k e y = T r u e ,   a u t o i n c r e m e n t = T r u e ) 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   d b . F o r e i g n K e y ( ' a c c o u n t . a c c o u n t _ i d ' ) ) 
         t r a n s a c t i o n _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ) 
         a m o u n t   =   d b . C o l u m n ( d b . F l o a t ) 
         t i m e s t a m p   =   d b . C o l u m n ( d b . D a t e T i m e ,   d e f a u l t = d a t e t i m e . d a t e t i m e . n o w ) 
 
         a c c o u n t   =   d b . r e l a t i o n s h i p ( ' A c c o u n t ' ,   b a c k r e f = ' t r a n s a c t i o n s ' ) 
 
         d e f   _ _ r e p r _ _ ( s e l f ) : 
                 r e t u r n   f ' < T r a n s a c t i o n   { s e l f . t r a n s a c t i o n _ t y p e }   o f   { s e l f . a m o u n t }   f o r   A c c o u n t   { s e l f . a c c o u n t _ i d } > ' 
 
 #   F l a s k - A d m i n   S e t u p 
 c l a s s   M y A d m i n I n d e x V i e w ( A d m i n I n d e x V i e w ) : 
         @ e x p o s e ( ' / ' ) 
         d e f   i n d e x ( s e l f ) : 
                 i f   ' a d m i n '   n o t   i n   s e s s i o n : 
                         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
                 #   R e t r i e v e   a c c o u n t s   a n d   t r a n s a c t i o n s   f o r   v i s u a l i z a t i o n 
                 t o t a l _ a c c o u n t s   =   A c c o u n t . q u e r y . c o u n t ( ) 
                 a c t i v e _ a c c o u n t s   =   A c c o u n t . q u e r y . f i l t e r _ b y ( i s _ a c t i v e = T r u e ) . c o u n t ( ) 
                 t o t a l _ b a l a n c e   =   d b . s e s s i o n . q u e r y ( d b . f u n c . s u m ( A c c o u n t . b a l a n c e ) ) . s c a l a r ( )   o r   0 
 
                 r e t u r n   s e l f . r e n d e r ( ' a d m i n _ i n d e x . h t m l ' ,   t o t a l _ a c c o u n t s = t o t a l _ a c c o u n t s ,   a c t i v e _ a c c o u n t s = a c t i v e _ a c c o u n t s ,   t o t a l _ b a l a n c e = t o t a l _ b a l a n c e ) 
 
 c l a s s   A c c o u n t M o d e l V i e w ( M o d e l V i e w ) : 
         d e f   i s _ a c c e s s i b l e ( s e l f ) : 
                 r e t u r n   ' a d m i n '   i n   s e s s i o n 
 
         c o l u m n _ f i l t e r s   =   [ ' a c c o u n t _ t y p e ' ,   ' i s _ a c t i v e ' ] 
         c a n _ c r e a t e   =   T r u e 
         c a n _ e d i t   =   T r u e 
         c a n _ d e l e t e   =   F a l s e 
 
 c l a s s   T r a n s a c t i o n M o d e l V i e w ( M o d e l V i e w ) : 
         d e f   i s _ a c c e s s i b l e ( s e l f ) : 
                 r e t u r n   ' a d m i n '   i n   s e s s i o n 
 
         c o l u m n _ f i l t e r s   =   [ ' t r a n s a c t i o n _ t y p e ' ] 
         c a n _ c r e a t e   =   F a l s e 
         c a n _ e d i t   =   F a l s e 
         c a n _ d e l e t e   =   F a l s e 
 
 a d m i n   =   A d m i n ( a p p ,   i n d e x _ v i e w = M y A d m i n I n d e x V i e w ( ) ,   t e m p l a t e _ m o d e = ' b o o t s t r a p 3 ' ) 
 a d m i n . a d d _ v i e w ( A c c o u n t M o d e l V i e w ( A c c o u n t ,   d b . s e s s i o n ) ) 
 a d m i n . a d d _ v i e w ( T r a n s a c t i o n M o d e l V i e w ( T r a n s a c t i o n ,   d b . s e s s i o n ) ) 
 
 #   F l a s k   R o u t e s   f o r   A d m i n   L o g i n 
 @ a p p . r o u t e ( ' / a d m i n / l o g i n ' ,   m e t h o d s = [ ' G E T ' ,   ' P O S T ' ] ) 
 d e f   a d m i n _ l o g i n ( ) : 
         i f   r e q u e s t . m e t h o d   = =   ' P O S T ' : 
                 u s e r n a m e   =   r e q u e s t . f o r m [ ' u s e r n a m e ' ] 
                 p a s s w o r d   =   r e q u e s t . f o r m [ ' p a s s w o r d ' ] 
                 i f   u s e r n a m e   = =   ' a d m i n '   a n d   p a s s w o r d   = =   ' p a s s w o r d ' : 
                         s e s s i o n [ ' a d m i n ' ]   =   T r u e 
                         r e t u r n   r e d i r e c t ( ' / a d m i n ' ) 
                 e l s e : 
                         f l a s h ( ' I n v a l i d   c r e d e n t i a l s ' ,   ' d a n g e r ' ) 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a d m i n _ l o g i n . h t m l ' ) 
 
 @ a p p . r o u t e ( ' / a d m i n / l o g o u t ' ) 
 d e f   a d m i n _ l o g o u t ( ) : 
         s e s s i o n . p o p ( ' a d m i n ' ,   N o n e ) 
         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
 #   R o u t e   t o   A p p l y   I n t e r e s t 
 @ a p p . r o u t e ( ' / a p p l y _ i n t e r e s t ' ) 
 d e f   a p p l y _ i n t e r e s t ( ) : 
         i f   ' a d m i n '   i n   s e s s i o n : 
                 s a v i n g s _ a c c o u n t s   =   A c c o u n t . q u e r y . f i l t e r _ b y ( a c c o u n t _ t y p e = ' S a v i n g s ' ) . a l l ( ) 
                 f o r   a c c o u n t   i n   s a v i n g s _ a c c o u n t s : 
                         i n t e r e s t   =   a c c o u n t . b a l a n c e   *   a c c o u n t . i n t e r e s t _ r a t e 
                         a c c o u n t . b a l a n c e   + =   i n t e r e s t 
                         d b . s e s s i o n . a d d ( T r a n s a c t i o n ( a c c o u n t _ i d = a c c o u n t . a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e = ' I n t e r e s t ' ,   a m o u n t = i n t e r e s t ) ) 
                 d b . s e s s i o n . c o m m i t ( ) 
                 f l a s h ( ' I n t e r e s t   a p p l i e d   t o   a l l   s a v i n g s   a c c o u n t s . ' ,   ' s u c c e s s ' ) 
         e l s e : 
                 f l a s h ( ' U n a u t h o r i z e d   a c c e s s . ' ,   ' d a n g e r ' ) 
         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' i n d e x ' ) ) 
 
 #   D a s h b o a r d   R o u t e   w i t h   V i s u a l i z a t i o n s 
 @ a p p . r o u t e ( ' / a d m i n / a n a l y t i c s ' ) 
 d e f   a n a l y t i c s ( ) : 
         i f   ' a d m i n '   n o t   i n   s e s s i o n : 
                 f l a s h ( ' U n a u t h o r i z e d   a c c e s s . ' ,   ' d a n g e r ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
 
         #   P r e p a r e   d a t a   f o r   v i s u a l i z a t i o n 
         t r a n s a c t i o n _ d a t a   =   d b . s e s s i o n . q u e r y ( T r a n s a c t i o n . t r a n s a c t i o n _ t y p e ,   d b . f u n c . s u m ( T r a n s a c t i o n . a m o u n t ) ) . g r o u p _ b y ( T r a n s a c t i o n . t r a n s a c t i o n _ t y p e ) . a l l ( ) 
         l a b e l s   =   [ t [ 0 ]   f o r   t   i n   t r a n s a c t i o n _ d a t a ] 
         a m o u n t s   =   [ t [ 1 ]   f o r   t   i n   t r a n s a c t i o n _ d a t a ] 
 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a n a l y t i c s . h t m l ' ,   l a b e l s = j s o n . d u m p s ( l a b e l s ) ,   a m o u n t s = j s o n . d u m p s ( a m o u n t s ) ) 
 
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' : 
         d b . c r e a t e _ a l l ( ) 
         a p p . r u n ( d e b u g = T r u e ) 
 
 H T M L   T e m p l a t e s   f o r   E n h a n c e d   A d m i n   P a n e l 
 1 .   A d m i n   I n d e x   T e m p l a t e   ( t e m p l a t e s / a d m i n _ i n d e x . h t m l ) 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > A d m i n   D a s h b o a r d < / t i t l e > 
 < / h e a d > 
 < b o d y > 
         < h 1 > A d m i n   D a s h b o a r d < / h 1 > 
         < p > T o t a l   A c c o u n t s :   { {   t o t a l _ a c c o u n t s   } } < / p > 
         < p > A c t i v e   A c c o u n t s :   { {   a c t i v e _ a c c o u n t s   } } < / p > 
         < p > T o t a l   B a l a n c e   i n   S y s t e m :   { {   t o t a l _ b a l a n c e   } } < / p > 
         < a   h r e f = " { {   u r l _ f o r ( ' a d m i n . i n d e x ' )   } } " > M a n a g e   A c c o u n t s   a n d   T r a n s a c t i o n s < / a > < b r > 
         < a   h r e f = " { {   u r l _ f o r ( ' a n a l y t i c s ' )   } } " > V i e w   A n a l y t i c s < / a > < b r > 
         < a   h r e f = " { {   u r l _ f o r ( ' a p p l y _ i n t e r e s t ' )   } } " > A p p l y   I n t e r e s t   t o   S a v i n g s   A c c o u n t s < / a > < b r > 
         < a   h r e f = " { {   u r l _ f o r ( ' a d m i n _ l o g o u t ' )   } } " > L o g o u t < / a > 
 < / b o d y > 
 < / h t m l > 
 
 2 .   A n a l y t i c s   T e m p l a t e   ( t e m p l a t e s / a n a l y t i c s . h t m l ) 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > A n a l y t i c s < / t i t l e > 
         < s c r i p t   s r c = " h t t p s : / / c d n . j s d e l i v r . n e t / n p m / c h a r t . j s " > < / s c r i p t > 
 < / h e a d > 
 < b o d y > 
         < h 1 > B a n k i n g   S y s t e m   A n a l y t i c s < / h 1 > 
         < c a n v a s   i d = " t r a n s a c t i o n C h a r t "   w i d t h = " 4 0 0 "   h e i g h t = " 2 0 0 " > < / c a n v a s > 
         < s c r i p t > 
                 v a r   c t x   =   d o c u m e n t . g e t E l e m e n t B y I d ( ' t r a n s a c t i o n C h a r t ' ) . g e t C o n t e x t ( ' 2 d ' ) ; 
                 v a r   t r a n s a c t i o n C h a r t   =   n e w   C h a r t ( c t x ,   { 
                         t y p e :   ' b a r ' , 
                         d a t a :   { 
                                 l a b e l s :   { {   l a b e l s   |   s a f e   } } , 
                                 d a t a s e t s :   [ { 
                                         l a b e l :   ' T r a n s a c t i o n   A m o u n t s ' , 
                                         d a t a :   { {   a m o u n t s   |   s a f e   } } , 
                                         b a c k g r o u n d C o l o r :   ' r g b a ( 7 5 ,   1 9 2 ,   1 9 2 ,   0 . 2 ) ' , 
                                         b o r d e r C o l o r :   ' r g b a ( 7 5 ,   1 9 2 ,   1 9 2 ,   1 ) ' , 
                                         b o r d e r W i d t h :   1 
                                 } ] 
                         } , 
                         o p t i o n s :   { 
                                 s c a l e s :   { 
                                         y :   { 
                                                 b e g i n A t Z e r o :   t r u e 
                                         } 
                                 } 
                         } 
                 } ) ; 
         < / s c r i p t > 
         < a   h r e f = " { {   u r l _ f o r ( ' a d m i n . i n d e x ' )   } } " > B a c k   t o   D a s h b o a r d < / a > 
 < / b o d y > 
 < / h t m l > 
 
 E n h a n c e m e n t s   S u m m a r y : 
 
         A d m i n   D a s h b o a r d : 
                 A d m i n   A u t h e n t i c a t i o n :   A d d e d   a   l o g i n   p a g e   f o r   a d m i n   t o   s e c u r e   a c c e s s   t o   t h e   a d m i n   p a n e l . 
                 A c c o u n t   O v e r v i e w :   T h e   d a s h b o a r d   p r o v i d e s   m e t r i c s   l i k e   t h e   t o t a l   n u m b e r   o f   a c c o u n t s ,   a c t i v e   a c c o u n t s ,   a n d   t o t a l   b a l a n c e ,   g i v i n g   a   h i g h - l e v e l   o v e r v i e w   o f   t h e   s y s t e m . 
 
         A d v a n c e d   U s e r   M a n a g e m e n t : 
                 F l a s k - A d m i n   I n t e g r a t i o n :   A c c o u n t M o d e l V i e w   a l l o w s   f o r   c r e a t i n g   a n d   m a n a g i n g   a c c o u n t s ,   w h i l e   T r a n s a c t i o n M o d e l V i e w   p r o v i d e s   a   v i e w   o f   a l l   s y s t e m   t r a n s a c t i o n s . 
                 A c c o u n t   A c t i v a t i o n :   A c c o u n t s   h a v e   a n   i s _ a c t i v e   f i e l d   t h a t   a l l o w s   a d m i n s   t o   d e a c t i v a t e   t h e m   i f   n e e d e d . 
 
         A n a l y t i c s   U s i n g   C h a r t . j s : 
                 A   n e w   A n a l y t i c s   P a g e   v i s u a l i z e s   t r a n s a c t i o n   d a t a   u s i n g   C h a r t . j s .   T h i s   h e l p s   a d m i n s   u n d e r s t a n d   u s a g e   p a t t e r n s ,   s u c h   a s   t h e   d i s t r i b u t i o n   o f   d e p o s i t s ,   w i t h d r a w a l s ,   a n d   i n t e r e s t   a p p l i e d . 
                 D y n a m i c   C h a r t s :   A   b a r   c h a r t   i s   g e n e r a t e d   d y n a m i c a l l y   b a s e d   o n   t r a n s a c t i o n   d a t a   r e t r i e v e d   f r o m   t h e   d a t a b a s e . 
 
         I n t e r e s t   C a l c u l a t i o n : 
                 T h e   / a p p l y _ i n t e r e s t   r o u t e   a l l o w s   a d m i n s   t o   m a n u a l l y   t r i g g e r   i n t e r e s t   a p p l i c a t i o n   t o   a l l   s a v i n g s   a c c o u n t s .   E a c h   a p p l i c a t i o n   i s   l o g g e d   a s   a   t r a n s a c t i o n . 
 
 N e x t   S t e p s   a n d   F u r t h e r   I m p r o v e m e n t s : 
 
         D a t a   S e c u r i t y   a n d   L o g g i n g : 
                 I m p l e m e n t   s e c u r e   c o m m u n i c a t i o n   ( e . g . ,   H T T P S   w i t h   S S L   c e r t i f i c a t e s ) . 
                 A d d   l o g g i n g   t o   r e c o r d   a d m i n   a c t i o n s   f o r   a u d i t i n g   p u r p o s e s . 
 
         A d v a n c e d   A n a l y t i c s : 
                 U s e   m o r e   a d v a n c e d   a n a l y t i c s   t o o l s   t o   c r e a t e   v i s u a l i z a t i o n s ,   s u c h   a s   m o n t h l y   t r e n d s ,   a c c o u n t   a c t i v i t y   h e a t m a p s ,   a n d   f r a u d   d e t e c t i o n   i n d i c a t o r s . 
 
         B a c k g r o u n d   S c h e d u l e r : 
                 U s e   a   t a s k   q u e u e   s u c h   a s   C e l e r y   t o   a u t o m a t i c a l l y   a p p l y   i n t e r e s t   a t   s e t   i n t e r v a l s . 
 
         R o l e - B a s e d   A c c e s s   C o n t r o l   ( R B A C ) : 
                 I n t r o d u c e   d i f f e r e n t   u s e r   r o l e s   ( e . g . ,   a d m i n ,   m a n a g e r )   w i t h   v a r i e d   p e r m i s s i o n s   u s i n g   l i b r a r i e s   l i k e   F l a s k - P r i n c i p a l . 
 
 W o u l d   y o u   l i k e   m o r e   d e t a i l e d   g u i d a n c e   o n   o n e   o f   t h e s e   i m p r o v e m e n t s ,   s u c h   a s   s e t t i n g   u p   C e l e r y   f o r   a u t o m a t e d   i n t e r e s t   c a l c u l a t i o n   o r   i m p l e m e n t i n g   m o r e   a d v a n c e d   v i s u a l   a n a l y t i c s   w i t h   r e a l - t i m e   c a p a b i l i t i e s ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 L e t ' s   p r o c e e d   w i t h   i m p l e m e n t i n g   a u t o m a t e d   i n t e r e s t   c a l c u l a t i o n   u s i n g   C e l e r y   a n d   a d v a n c e d   v i s u a l   a n a l y t i c s   w i t h   r e a l - t i m e   c a p a b i l i t i e s .   B e l o w   i s   a   d e t a i l e d   g u i d e   o n   h o w   t o   a c h i e v e   t h e s e   g o a l s : 
 1 .   A u t o m a t e d   I n t e r e s t   C a l c u l a t i o n   U s i n g   C e l e r y 
 
 C e l e r y   i s   a   d i s t r i b u t e d   t a s k   q u e u e   t h a t   c a n   h a n d l e   a s y n c h r o n o u s   a n d   p e r i o d i c   t a s k s .   W e ' l l   u s e   i t   t o   a u t o m a t e   i n t e r e s t   a p p l i c a t i o n   f o r   a l l   s a v i n g s   a c c o u n t s   p e r i o d i c a l l y ,   w i t h o u t   m a n u a l   i n t e r v e n t i o n . 
 S t e p s   t o   S e t   U p   C e l e r y : 
 
         I n s t a l l   R e q u i r e d   P a c k a g e s : 
                 I n s t a l l   C e l e r y   a n d   R e d i s   a s   a   m e s s a g e   b r o k e r . 
 
         b a s h 
 
 p i p   i n s t a l l   c e l e r y   r e d i s 
 
         R e d i s   w i l l   a c t   a s   t h e   m e s s a g e   b r o k e r   f o r   C e l e r y   t o   h a n d l e   t a s k s   e f f i c i e n t l y . 
 
 R e d i s   I n s t a l l a t i o n : 
 
         Y o u   n e e d   t o   i n s t a l l   a n d   r u n   a   R e d i s   s e r v e r .   O n   L i n u x ,   u s e : 
 
         b a s h 
 
 s u d o   a p t - g e t   i n s t a l l   r e d i s - s e r v e r 
 
 S t a r t   R e d i s : 
 
 b a s h 
 
                 s u d o   s e r v i c e   r e d i s - s e r v e r   s t a r t 
 
         C o n f i g u r e   C e l e r y   i n   t h e   F l a s k   A p p l i c a t i o n : 
 
 U p d a t e   t h e   F l a s k   A p p l i c a t i o n   t o   I n t e g r a t e   C e l e r y 
 
         W e ' l l   c o n f i g u r e   C e l e r y   t o   r u n   a l o n g s i d e   F l a s k   a n d   s c h e d u l e   a n   i n t e r e s t   a p p l i c a t i o n   t a s k   t o   b e   e x e c u t e d   p e r i o d i c a l l y . 
 
 D i r e c t o r y   S t r u c t u r e : 
 
         W e ' l l   s e p a r a t e   C e l e r y   c o n f i g u r a t i o n s   i n t o   a   n e w   f i l e ,   c r e a t i n g   a   c l e a n e r   a n d   m o r e   m a i n t a i n a b l e   c o d e b a s e . 
 
 b a s h 
 
 . 
 % % %  y o u r _ f l a s k _ a p p . p y       #   M a i n   F l a s k   a p p l i c a t i o n 
 % % %  c e l e r y _ c o n f i g . p y         #   C e l e r y   c o n f i g u r a t i o n s   a n d   t a s k s 
 % % %  b a n k . d b                           #   S Q L i t e   d a t a b a s e 
 % % %  t e m p l a t e s /                     #   H T M L   t e m p l a t e s 
 % % %  r e q u i r e m e n t s . t x t         #   L i s t   o f   d e p e n d e n c i e s 
 
 c e l e r y _ c o n f i g . p y      C e l e r y   C o n f i g u r a t i o n   a n d   T a s k s 
 
 C r e a t e   a   n e w   f i l e   c a l l e d   c e l e r y _ c o n f i g . p y   t o   m a n a g e   t h e   C e l e r y   s e t u p : 
 
 p y t h o n 
 
 f r o m   c e l e r y   i m p o r t   C e l e r y 
 f r o m   y o u r _ f l a s k _ a p p   i m p o r t   d b ,   A c c o u n t ,   T r a n s a c t i o n 
 i m p o r t   d a t e t i m e 
 
 #   I n i t i a l i z e   C e l e r y 
 d e f   m a k e _ c e l e r y ( a p p ) : 
         c e l e r y   =   C e l e r y ( 
                 a p p . i m p o r t _ n a m e , 
                 b a c k e n d = ' r e d i s : / / l o c a l h o s t : 6 3 7 9 / 0 ' , 
                 b r o k e r = ' r e d i s : / / l o c a l h o s t : 6 3 7 9 / 0 ' 
         ) 
         c e l e r y . c o n f . u p d a t e ( a p p . c o n f i g ) 
         r e t u r n   c e l e r y 
 
 #   I m p o r t   t h e   F l a s k   a p p l i c a t i o n 
 f r o m   y o u r _ f l a s k _ a p p   i m p o r t   a p p 
 
 c e l e r y   =   m a k e _ c e l e r y ( a p p ) 
 
 #   D e f i n e   a   p e r i o d i c   t a s k   t o   a p p l y   i n t e r e s t   t o   a l l   s a v i n g s   a c c o u n t s 
 @ c e l e r y . t a s k 
 d e f   a p p l y _ i n t e r e s t _ t o _ s a v i n g s ( ) : 
         w i t h   a p p . a p p _ c o n t e x t ( ) : 
                 s a v i n g s _ a c c o u n t s   =   A c c o u n t . q u e r y . f i l t e r _ b y ( a c c o u n t _ t y p e = ' S a v i n g s ' ) . a l l ( ) 
                 f o r   a c c o u n t   i n   s a v i n g s _ a c c o u n t s : 
                         i n t e r e s t   =   a c c o u n t . b a l a n c e   *   a c c o u n t . i n t e r e s t _ r a t e 
                         a c c o u n t . b a l a n c e   + =   i n t e r e s t 
                         d b . s e s s i o n . a d d ( T r a n s a c t i o n ( 
                                 a c c o u n t _ i d = a c c o u n t . a c c o u n t _ i d , 
                                 t r a n s a c t i o n _ t y p e = ' I n t e r e s t ' , 
                                 a m o u n t = i n t e r e s t , 
                                 t i m e s t a m p = d a t e t i m e . d a t e t i m e . n o w ( ) 
                         ) ) 
                 d b . s e s s i o n . c o m m i t ( ) 
 
 y o u r _ f l a s k _ a p p . p y      U p d a t e d   F l a s k   A p p l i c a t i o n   w i t h   C e l e r y   I n t e g r a t i o n 
 
 U p d a t e   t h e   m a i n   F l a s k   a p p l i c a t i o n   ( y o u r _ f l a s k _ a p p . p y )   t o   i n c l u d e   C e l e r y : 
 
 p y t h o n 
 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e ,   r e q u e s t ,   r e d i r e c t ,   u r l _ f o r ,   f l a s h ,   s e s s i o n 
 f r o m   f l a s k _ s q l a l c h e m y   i m p o r t   S Q L A l c h e m y 
 f r o m   f l a s k _ a d m i n   i m p o r t   A d m i n ,   e x p o s e ,   A d m i n I n d e x V i e w 
 f r o m   f l a s k _ a d m i n . c o n t r i b . s q l a   i m p o r t   M o d e l V i e w 
 f r o m   c e l e r y _ c o n f i g   i m p o r t   m a k e _ c e l e r y 
 i m p o r t   d a t e t i m e 
 i m p o r t   b c r y p t 
 
 #   F l a s k   S e t u p 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ D A T A B A S E _ U R I ' ]   =   ' s q l i t e : / / / b a n k . d b ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ T R A C K _ M O D I F I C A T I O N S ' ]   =   F a l s e 
 
 #   C e l e r y   C o n f i g u r a t i o n 
 a p p . c o n f i g . u p d a t e ( 
         C E L E R Y _ B R O K E R _ U R L = ' r e d i s : / / l o c a l h o s t : 6 3 7 9 / 0 ' , 
         C E L E R Y _ R E S U L T _ B A C K E N D = ' r e d i s : / / l o c a l h o s t : 6 3 7 9 / 0 ' 
 ) 
 
 #   I n i t i a l i z e   S Q L A l c h e m y   a n d   C e l e r y 
 d b   =   S Q L A l c h e m y ( a p p ) 
 c e l e r y   =   m a k e _ c e l e r y ( a p p ) 
 
 #   D e f i n e   D a t a b a s e   M o d e l s   ( a s   d e s c r i b e d   p r e v i o u s l y ) 
 c l a s s   A c c o u n t ( d b . M o d e l ) : 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   p r i m a r y _ k e y = T r u e ) 
         o w n e r   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   n u l l a b l e = F a l s e ) 
         p a s s w o r d _ h a s h   =   d b . C o l u m n ( d b . S t r i n g ( 1 2 8 ) ,   n u l l a b l e = F a l s e ) 
         b a l a n c e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         a c c o u n t _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 2 0 ) ) 
         i n t e r e s t _ r a t e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         i s _ a c t i v e   =   d b . C o l u m n ( d b . B o o l e a n ,   d e f a u l t = T r u e ) 
 
 c l a s s   T r a n s a c t i o n ( d b . M o d e l ) : 
         t r a n s a c t i o n _ i d   =   d b . C o l u m n ( d b . I n t e g e r ,   p r i m a r y _ k e y = T r u e ,   a u t o i n c r e m e n t = T r u e ) 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   d b . F o r e i g n K e y ( ' a c c o u n t . a c c o u n t _ i d ' ) ) 
         t r a n s a c t i o n _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ) 
         a m o u n t   =   d b . C o l u m n ( d b . F l o a t ) 
         t i m e s t a m p   =   d b . C o l u m n ( d b . D a t e T i m e ,   d e f a u l t = d a t e t i m e . d a t e t i m e . n o w ) 
         a c c o u n t   =   d b . r e l a t i o n s h i p ( ' A c c o u n t ' ,   b a c k r e f = ' t r a n s a c t i o n s ' ) 
 
 #   E x a m p l e   T a s k   T r i g g e r   R o u t e 
 @ a p p . r o u t e ( ' / a d m i n / a p p l y _ i n t e r e s t _ n o w ' ) 
 d e f   a p p l y _ i n t e r e s t _ n o w ( ) : 
         i f   ' a d m i n '   i n   s e s s i o n : 
                 a p p l y _ i n t e r e s t _ t o _ s a v i n g s . d e l a y ( ) 
                 f l a s h ( ' I n t e r e s t   a p p l i c a t i o n   t a s k   h a s   b e e n   i n i t i a t e d . ' ,   ' s u c c e s s ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n . i n d e x ' ) ) 
         e l s e : 
                 f l a s h ( ' U n a u t h o r i z e d   a c c e s s . ' ,   ' d a n g e r ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
 
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' : 
         d b . c r e a t e _ a l l ( ) 
         a p p . r u n ( d e b u g = T r u e ) 
 
 R u n n i n g   C e l e r y 
 
 T o   r u n   C e l e r y   i n   t h e   b a c k g r o u n d ,   u s e   t h e   c o m m a n d : 
 
 b a s h 
 
 c e l e r y   - A   c e l e r y _ c o n f i g . c e l e r y   w o r k e r   - - l o g l e v e l = i n f o 
 
 T h i s   s t a r t s   a   C e l e r y   w o r k e r   t h a t   l i s t e n s   f o r   t a s k s   t o   e x e c u t e ,   s u c h   a s   t h e   p e r i o d i c   i n t e r e s t   a p p l i c a t i o n . 
 R u n n i n g   P e r i o d i c   T a s k s   w i t h   C e l e r y   B e a t 
 
 T o   a u t o m a t e   t h e   i n t e r e s t   a p p l i c a t i o n   p e r i o d i c a l l y   ( e . g . ,   e v e r y   m o n t h ) ,   y o u   c a n   u s e   C e l e r y   B e a t   t o   s c h e d u l e   t h e   t a s k . 
 
         I n s t a l l   C e l e r y   B e a t : 
 
         b a s h 
 
         p i p   i n s t a l l   c e l e r y [ r e d i s ] 
 
         U p d a t e   t h e   c e l e r y _ c o n f i g . p y   t o   s c h e d u l e   t h e   i n t e r e s t   a p p l i c a t i o n : 
 
 p y t h o n 
 
 f r o m   c e l e r y . s c h e d u l e s   i m p o r t   c r o n t a b 
 
 c e l e r y . c o n f . b e a t _ s c h e d u l e   =   { 
         ' a p p l y - i n t e r e s t - e v e r y - m o n t h ' :   { 
                 ' t a s k ' :   ' c e l e r y _ c o n f i g . a p p l y _ i n t e r e s t _ t o _ s a v i n g s ' , 
                 ' s c h e d u l e ' :   c r o n t a b ( 0 ,   0 ,   1 ,   ' * ' ) ,     #   R u n s   a t   m i d n i g h t   o n   t h e   1 s t   o f   e v e r y   m o n t h 
         } , 
 } 
 
         R u n   C e l e r y   B e a t   a l o n g s i d e   t h e   C e l e r y   w o r k e r : 
 
 b a s h 
 
 c e l e r y   - A   c e l e r y _ c o n f i g . c e l e r y   b e a t   - - l o g l e v e l = i n f o 
 
 T h i s   s e t u p   w i l l   e n s u r e   t h a t   i n t e r e s t   i s   a p p l i e d   a u t o m a t i c a l l y   a t   t h e   s t a r t   o f   e a c h   m o n t h . 
 2 .   A d v a n c e d   V i s u a l   A n a l y t i c s   w i t h   R e a l - T i m e   C a p a b i l i t i e s 
 
 T o   p r o v i d e   a   m o r e   i n t e r a c t i v e ,   r e a l - t i m e   e x p e r i e n c e   f o r   v i s u a l   a n a l y t i c s ,   y o u   c a n   u s e   F l a s k - S o c k e t I O   w i t h   C h a r t . j s .   T h i s   a l l o w s   f o r   p u s h i n g   l i v e   u p d a t e s   t o   t h e   a d m i n   p a n e l   a s   n e w   t r a n s a c t i o n s   o c c u r . 
 S e t t i n g   U p   F l a s k - S o c k e t I O   f o r   R e a l - T i m e   A n a l y t i c s 
 
 F l a s k - S o c k e t I O   h e l p s   t o   c r e a t e   r e a l - t i m e   c o n n e c t i o n s   b e t w e e n   t h e   s e r v e r   a n d   c l i e n t s .   H e r e  s   h o w   t o   s e t   i t   u p : 
 
         I n s t a l l   F l a s k - S o c k e t I O : 
 
         b a s h 
 
         p i p   i n s t a l l   F l a s k - S o c k e t I O 
 
         U p d a t e   t h e   F l a s k   A p p l i c a t i o n : 
 
 y o u r _ f l a s k _ a p p . p y      A d d   F l a s k - S o c k e t I O 
 
 p y t h o n 
 
 f r o m   f l a s k _ s o c k e t i o   i m p o r t   S o c k e t I O ,   e m i t 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e ,   r e q u e s t ,   r e d i r e c t ,   u r l _ f o r ,   f l a s h ,   s e s s i o n 
 f r o m   f l a s k _ s q l a l c h e m y   i m p o r t   S Q L A l c h e m y 
 f r o m   f l a s k _ a d m i n   i m p o r t   A d m i n ,   e x p o s e ,   A d m i n I n d e x V i e w 
 f r o m   f l a s k _ a d m i n . c o n t r i b . s q l a   i m p o r t   M o d e l V i e w 
 f r o m   c e l e r y _ c o n f i g   i m p o r t   m a k e _ c e l e r y 
 i m p o r t   d a t e t i m e 
 i m p o r t   b c r y p t 
 
 #   F l a s k   S e t u p 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ D A T A B A S E _ U R I ' ]   =   ' s q l i t e : / / / b a n k . d b ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ T R A C K _ M O D I F I C A T I O N S ' ]   =   F a l s e 
 
 #   S o c k e t I O   s e t u p 
 s o c k e t i o   =   S o c k e t I O ( a p p ) 
 
 #   I n i t i a l i z e   S Q L A l c h e m y 
 d b   =   S Q L A l c h e m y ( a p p ) 
 
 #   D e f i n e   D a t a b a s e   M o d e l s   ( A c c o u n t ,   T r a n s a c t i o n   -   a s   b e f o r e ) 
 
 #   R e a l - T i m e   T r a n s a c t i o n   D a s h b o a r d 
 @ a p p . r o u t e ( ' / a d m i n / r e a l t i m e _ a n a l y t i c s ' ) 
 d e f   r e a l t i m e _ a n a l y t i c s ( ) : 
         i f   ' a d m i n '   n o t   i n   s e s s i o n : 
                 f l a s h ( ' U n a u t h o r i z e d   a c c e s s . ' ,   ' d a n g e r ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' r e a l t i m e _ a n a l y t i c s . h t m l ' ) 
 
 #   E m i t   e v e n t s   f o r   r e a l - t i m e   u p d a t e s   w h e n   a   n e w   t r a n s a c t i o n   o c c u r s 
 @ s o c k e t i o . o n ( ' n e w _ t r a n s a c t i o n ' ) 
 d e f   h a n d l e _ n e w _ t r a n s a c t i o n ( d a t a ) : 
         #   B r o a d c a s t   t h e   n e w   t r a n s a c t i o n   t o   a l l   c o n n e c t e d   c l i e n t s 
         e m i t ( ' u p d a t e _ d a s h b o a r d ' ,   d a t a ,   b r o a d c a s t = T r u e ) 
 
 #   E x a m p l e   r o u t e   f o r   c r e a t i n g   a   n e w   t r a n s a c t i o n   t o   t r i g g e r   t h e   e v e n t 
 @ a p p . r o u t e ( ' / a d m i n / n e w _ t r a n s a c t i o n ' ,   m e t h o d s = [ ' P O S T ' ] ) 
 d e f   n e w _ t r a n s a c t i o n ( ) : 
         i f   ' a d m i n '   i n   s e s s i o n : 
                 a c c o u n t _ i d   =   r e q u e s t . f o r m [ ' a c c o u n t _ i d ' ] 
                 t r a n s a c t i o n _ t y p e   =   r e q u e s t . f o r m [ ' t r a n s a c t i o n _ t y p e ' ] 
                 a m o u n t   =   f l o a t ( r e q u e s t . f o r m [ ' a m o u n t ' ] ) 
                 
                 n e w _ t r a n s   =   T r a n s a c t i o n ( a c c o u n t _ i d = a c c o u n t _ i d ,   t r a n s a c t i o n _ t y p e = t r a n s a c t i o n _ t y p e ,   a m o u n t = a m o u n t ,   t i m e s t a m p = d a t e t i m e . d a t e t i m e . n o w ( ) ) 
                 d b . s e s s i o n . a d d ( n e w _ t r a n s ) 
                 d b . s e s s i o n . c o m m i t ( ) 
 
                 #   E m i t   e v e n t   f o r   n e w   t r a n s a c t i o n 
                 s o c k e t i o . e m i t ( ' n e w _ t r a n s a c t i o n ' ,   { 
                         ' a c c o u n t _ i d ' :   a c c o u n t _ i d , 
                         ' t r a n s a c t i o n _ t y p e ' :   t r a n s a c t i o n _ t y p e , 
                         ' a m o u n t ' :   a m o u n t 
                 } ) 
                 f l a s h ( ' T r a n s a c t i o n   a d d e d   s u c c e s s f u l l y   a n d   b r o a d c a s t e d   i n   r e a l - t i m e . ' ,   ' s u c c e s s ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n . i n d e x ' ) ) 
 
         e l s e : 
                 f l a s h ( ' U n a u t h o r i z e d   a c c e s s . ' ,   ' d a n g e r ' ) 
                 r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
 
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' : 
         d b . c r e a t e _ a l l ( ) 
         s o c k e t i o . r u n ( a p p ,   d e b u g = T r u e ) 
 
 H T M L   T e m p l a t e   f o r   R e a l - T i m e   A n a l y t i c s   ( t e m p l a t e s / r e a l t i m e _ a n a l y t i c s . h t m l ) 
 
 h t m l 
 
 < ! D O C T Y P E   h t m l > 
 < h t m l   l a n g = " e n " > 
 < h e a d > 
         < m e t a   c h a r s e t = " U T F - 8 " > 
         < m e t a   n a m e = " v i e w p o r t "   c o n t e n t = " w i d t h = d e v i c e - w i d t h ,   i n i t i a l - s c a l e = 1 . 0 " > 
         < t i t l e > R e a l - T i m e   A n a l y t i c s < / t i t l e > 
         < s c r i p t   s r c = " h t t p s : / / c d n . j s d e l i v r . n e t / n p m / c h a r t . j s " > < / s c r i p t > 
         < s c r i p t   s r c = " h t t p s : / / c d n j s . c l o u d f l a r e . c o m / a j a x / l i b s / s o c k e t . i o / 4 . 0 . 0 / s o c k e t . i o . j s " > < / s c r i p t > 
 < / h e a d > 
 < b o d y > 
         < h 1 > R e a l - T i m e   T r a n s a c t i o n   A n a l y t i c s < / h 1 > 
         < c a n v a s   i d = " t r a n s a c t i o n C h a r t "   w i d t h = " 4 0 0 "   h e i g h t = " 2 0 0 " > < / c a n v a s > 
 
         < s c r i p t > 
                 v a r   c t x   =   d o c u m e n t . g e t E l e m e n t B y I d ( ' t r a n s a c t i o n C h a r t ' ) . g e t C o n t e x t ( ' 2 d ' ) ; 
                 v a r   t r a n s a c t i o n C h a r t   =   n e w   C h a r t ( c t x ,   { 
                         t y p e :   ' b a r ' , 
                         d a t a :   { 
                                 l a b e l s :   [ ] , 
                                 d a t a s e t s :   [ { 
                                         l a b e l :   ' T r a n s a c t i o n   A m o u n t s ' , 
                                         d a t a :   [ ] , 
                                         b a c k g r o u n d C o l o r :   ' r g b a ( 7 5 ,   1 9 2 ,   1 9 2 ,   0 . 2 ) ' , 
                                         b o r d e r C o l o r :   ' r g b a ( 7 5 ,   1 9 2 ,   1 9 2 ,   1 ) ' , 
                                         b o r d e r W i d t h :   1 
                                 } ] 
                         } , 
                         o p t i o n s :   { 
                                 s c a l e s :   { 
                                         y :   { 
                                                 b e g i n A t Z e r o :   t r u e 
                                         } 
                                 } 
                         } 
                 } ) ; 
 
                 / /   C o n n e c t   t o   t h e   S o c k e t I O   s e r v e r 
                 v a r   s o c k e t   =   i o ( ) ; 
 
                 / /   L i s t e n   f o r   n e w   t r a n s a c t i o n   e v e n t s 
                 s o c k e t . o n ( ' u p d a t e _ d a s h b o a r d ' ,   f u n c t i o n ( d a t a )   { 
                         t r a n s a c t i o n C h a r t . d a t a . l a b e l s . p u s h ( d a t a . t r a n s a c t i o n _ t y p e ) ; 
                         t r a n s a c t i o n C h a r t . d a t a . d a t a s e t s [ 0 ] . d a t a . p u s h ( d a t a . a m o u n t ) ; 
                         t r a n s a c t i o n C h a r t . u p d a t e ( ) ; 
                 } ) ; 
         < / s c r i p t > 
 
         < a   h r e f = " { {   u r l _ f o r ( ' a d m i n . i n d e x ' )   } } " > B a c k   t o   A d m i n   D a s h b o a r d < / a > 
 < / b o d y > 
 < / h t m l > 
 
 S u m m a r y   o f   R e a l - T i m e   E n h a n c e m e n t s : 
 
         A u t o m a t e d   I n t e r e s t   C a l c u l a t i o n : 
                 U s i n g   C e l e r y   a n d   R e d i s ,   w e   a u t o m a t e d   t h e   i n t e r e s t   a p p l i c a t i o n   f o r   s a v i n g s   a c c o u n t s . 
                 I n t e r e s t   i s   a p p l i e d   a u t o m a t i c a l l y   e v e r y   m o n t h   v i a   C e l e r y   B e a t ,   e n s u r i n g   c o n s i s t e n c y   a n d   r e d u c i n g   m a n u a l   o v e r h e a d . 
 
         R e a l - T i m e   A n a l y t i c s   w i t h   F l a s k - S o c k e t I O   a n d   C h a r t . j s : 
                 F l a s k - S o c k e t I O   a l l o w s   t h e   s e r v e r   t o   p u s h   u p d a t e s   t o   c o n n e c t e d   c l i e n t s   i n   r e a l   t i m e . 
                 A d m i n s   c a n   v i e w   a   l i v e   d a s h b o a r d   ( / a d m i n / r e a l t i m e _ a n a l y t i c s )   t h a t   u p d a t e s   w i t h   e a c h   n e w   t r a n s a c t i o n ,   g i v i n g   i m m e d i a t e   i n s i g h t s   i n t o   s y s t e m   a c t i v i t i e s . 
 
         D e p l o y m e n t   o f   A d v a n c e d   F e a t u r e s : 
                 T h e   C e l e r y   w o r k e r   a n d   R e d i s   n e e d   t o   r u n   a l o n g s i d e   t h e   F l a s k   a p p l i c a t i o n ,   w h i c h   c a n   b e   a c h i e v e d   b y   c o n t a i n e r i z i n g   t h e   a p p l i c a t i o n   u s i n g   D o c k e r . 
                 F o r   p r o d u c t i o n   d e p l o y m e n t s   o n   p l a t f o r m s   l i k e   A W S ,   s e t t i n g   u p   a   m a n a g e d   R e d i s   i n s t a n c e   ( e . g . ,   A W S   E l a s t i C a c h e )   e n s u r e s   s c a l a b i l i t y . 
 
 W o u l d   y o u   l i k e   f u r t h e r   g u i d a n c e   o n   D o c k e r i z i n g   t h e   a p p l i c a t i o n   f o r   e a s i e r   d e p l o y m e n t   w i t h   C e l e r y   a n d   R e d i s ,   o r   m o r e   d e t a i l s   o n   i m p l e m e n t i n g   a d v a n c e d   s e c u r i t y   f e a t u r e s ,   s u c h   a s   J W T   f o r   a d m i n   a u t h e n t i c a t i o n ? 
 Y o u   s a i d : 
 y e s 
 C h a t G P T   s a i d : 
 C h a t G P T 
 
 L e t ' s   m o v e   o n   t o   D o c k e r i z i n g   t h e   a p p l i c a t i o n   f o r   e a s i e r   d e p l o y m e n t   a n d   s c a l a b i l i t y ,   p a r t i c u l a r l y   w h e n   u s i n g   C e l e r y   a n d   R e d i s   a l o n g s i d e   F l a s k .   D o c k e r   w i l l   a l l o w   u s   t o   c r e a t e   c o n t a i n e r i z e d   s e r v i c e s   t h a t   m a k e   t h e   a p p l i c a t i o n   e a s i e r   t o   d e p l o y ,   m a n a g e ,   a n d   s c a l e   a c r o s s   d i f f e r e n t   e n v i r o n m e n t s . 
 O b j e c t i v e s : 
 
         D o c k e r i z e   t h e   F l a s k   A p p l i c a t i o n : 
                 C r e a t e   D o c k e r   c o n t a i n e r s   f o r   F l a s k ,   C e l e r y ,   a n d   R e d i s   t o   m a n a g e   t h e   b a n k i n g   s y s t e m . 
                 U s e   D o c k e r   C o m p o s e   t o   o r c h e s t r a t e   t h e   m u l t i - c o n t a i n e r   s e t u p . 
 
         C o n f i g u r e   D o c k e r   f o r   F l a s k ,   C e l e r y ,   a n d   R e d i s : 
                 F l a s k   C o n t a i n e r :   R u n s   t h e   m a i n   a p p l i c a t i o n . 
                 C e l e r y   W o r k e r   C o n t a i n e r :   P r o c e s s e s   b a c k g r o u n d   t a s k s ,   l i k e   a u t o m a t e d   i n t e r e s t   c a l c u l a t i o n s . 
                 R e d i s   C o n t a i n e r :   A c t s   a s   t h e   m e s s a g e   b r o k e r   f o r   C e l e r y   t a s k s . 
 
         E n h a n c e   A d m i n   A u t h e n t i c a t i o n   w i t h   J W T : 
                 S e c u r e   t h e   a d m i n   d a s h b o a r d   u s i n g   J W T   ( J S O N   W e b   T o k e n s )   f o r   a u t h e n t i c a t i o n ,   m a k i n g   t h e   a d m i n   p a n e l   m o r e   s e c u r e . 
 
 S t e p   1 :   D o c k e r i z i n g   t h e   F l a s k   A p p l i c a t i o n 
 D i r e c t o r y   S t r u c t u r e 
 
 p l a i n t e x t 
 
 . 
 % % %  D o c k e r f i l e 
 % % %  d o c k e r - c o m p o s e . y m l 
 % % %  r e q u i r e m e n t s . t x t 
 % % %  y o u r _ f l a s k _ a p p . p y 
 % % %  c e l e r y _ c o n f i g . p y 
 % % %  b a n k . d b 
 % % %  t e m p l a t e s / 
 
 1 .   D o c k e r f i l e   f o r   F l a s k   A p p l i c a t i o n 
 
 C r e a t e   a   D o c k e r f i l e   t o   d e f i n e   h o w   t o   b u i l d   t h e   F l a s k   c o n t a i n e r : 
 
 D o c k e r f i l e : 
 
 D o c k e r f i l e 
 
 #   U s e   a n   o f f i c i a l   P y t h o n   r u n t i m e   a s   a   b a s e   i m a g e 
 F R O M   p y t h o n : 3 . 9 - s l i m 
 
 #   S e t   e n v i r o n m e n t   v a r i a b l e s 
 E N V   P Y T H O N D O N T W R I T E B Y T E C O D E   1 
 E N V   P Y T H O N U N B U F F E R E D   1 
 
 #   S e t   t h e   w o r k i n g   d i r e c t o r y   i n   t h e   c o n t a i n e r 
 W O R K D I R   / a p p 
 
 #   C o p y   t h e   c u r r e n t   d i r e c t o r y   c o n t e n t s   i n t o   t h e   c o n t a i n e r   a t   / a p p 
 C O P Y   .   / a p p 
 
 #   I n s t a l l   a n y   n e e d e d   p a c k a g e s   s p e c i f i e d   i n   r e q u i r e m e n t s . t x t 
 R U N   p i p   i n s t a l l   - - u p g r a d e   p i p 
 R U N   p i p   i n s t a l l   - r   r e q u i r e m e n t s . t x t 
 
 #   E x p o s e   t h e   p o r t   t h e   a p p   r u n s   o n 
 E X P O S E   5 0 0 0 
 
 #   R u n   t h e   F l a s k   s e r v e r 
 C M D   [ " f l a s k " ,   " r u n " ,   " - - h o s t = 0 . 0 . 0 . 0 " ] 
 
 2 .   D o c k e r   C o m p o s e   F i l e   t o   O r c h e s t r a t e   F l a s k ,   C e l e r y ,   a n d   R e d i s 
 
 C r e a t e   a   d o c k e r - c o m p o s e . y m l   f i l e   t o   m a n a g e   t h e   m u l t i - c o n t a i n e r   a p p l i c a t i o n : 
 
 d o c k e r - c o m p o s e . y m l : 
 
 y a m l 
 
 v e r s i o n :   ' 3 . 8 ' 
 
 s e r v i c e s : 
     f l a s k - a p p : 
         b u i l d :   . 
         c o n t a i n e r _ n a m e :   f l a s k _ a p p 
         p o r t s : 
             -   " 5 0 0 0 : 5 0 0 0 " 
         e n v i r o n m e n t : 
             -   F L A S K _ E N V = d e v e l o p m e n t 
             -   C E L E R Y _ B R O K E R _ U R L = r e d i s : / / r e d i s : 6 3 7 9 / 0 
             -   C E L E R Y _ R E S U L T _ B A C K E N D = r e d i s : / / r e d i s : 6 3 7 9 / 0 
         v o l u m e s : 
             -   . : / a p p 
         d e p e n d s _ o n : 
             -   r e d i s 
         c o m m a n d :   f l a s k   r u n   - - h o s t = 0 . 0 . 0 . 0 
 
     c e l e r y - w o r k e r : 
         b u i l d :   . 
         c o n t a i n e r _ n a m e :   c e l e r y _ w o r k e r 
         e n v i r o n m e n t : 
             -   C E L E R Y _ B R O K E R _ U R L = r e d i s : / / r e d i s : 6 3 7 9 / 0 
             -   C E L E R Y _ R E S U L T _ B A C K E N D = r e d i s : / / r e d i s : 6 3 7 9 / 0 
         v o l u m e s : 
             -   . : / a p p 
         d e p e n d s _ o n : 
             -   r e d i s 
         c o m m a n d :   c e l e r y   - A   c e l e r y _ c o n f i g . c e l e r y   w o r k e r   - - l o g l e v e l = i n f o 
 
     r e d i s : 
         i m a g e :   r e d i s : l a t e s t 
         c o n t a i n e r _ n a m e :   r e d i s 
         p o r t s : 
             -   " 6 3 7 9 : 6 3 7 9 " 
 
 3 .   R e q u i r e m e n t s . t x t   f o r   D e p e n d e n c i e s 
 
 A d d   a l l   t h e   n e c e s s a r y   P y t h o n   p a c k a g e s   i n t o   t h e   r e q u i r e m e n t s . t x t   f i l e : 
 
 r e q u i r e m e n t s . t x t : 
 
 p l a i n t e x t 
 
 F l a s k 
 F l a s k - S Q L A l c h e m y 
 F l a s k - A d m i n 
 F l a s k - S o c k e t I O 
 C e l e r y 
 r e d i s 
 b c r y p t 
 g u n i c o r n 
 f l a s k - j w t - e x t e n d e d 
 
 4 .   U p d a t i n g   F l a s k   A p p l i c a t i o n   f o r   D o c k e r 
 
 U p d a t e   t h e   F l a s k   a p p l i c a t i o n   ( y o u r _ f l a s k _ a p p . p y )   t o   h a n d l e   c o n f i g u r a t i o n s   f o r   D o c k e r   a n d   J W T - b a s e d   a u t h e n t i c a t i o n . 
 S e t t i n g   U p   J W T   A u t h e n t i c a t i o n   f o r   A d m i n   A c c e s s 
 
 T o   e n h a n c e   a d m i n   s e c u r i t y ,   a d d   J W T - b a s e d   a u t h e n t i c a t i o n .   I n s t a l l   t h e   F l a s k - J W T - E x t e n d e d   l i b r a r y   f o r   J W T   s u p p o r t : 
 
 b a s h 
 
 p i p   i n s t a l l   f l a s k - j w t - e x t e n d e d 
 
 U p d a t e d   y o u r _ f l a s k _ a p p . p y   w i t h   J W T : 
 
 p y t h o n 
 
 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e ,   r e q u e s t ,   r e d i r e c t ,   u r l _ f o r ,   f l a s h ,   s e s s i o n ,   j s o n i f y 
 f r o m   f l a s k _ s q l a l c h e m y   i m p o r t   S Q L A l c h e m y 
 f r o m   f l a s k _ j w t _ e x t e n d e d   i m p o r t   J W T M a n a g e r ,   c r e a t e _ a c c e s s _ t o k e n ,   j w t _ r e q u i r e d ,   g e t _ j w t _ i d e n t i t y 
 f r o m   f l a s k _ a d m i n   i m p o r t   A d m i n ,   e x p o s e ,   A d m i n I n d e x V i e w 
 f r o m   f l a s k _ a d m i n . c o n t r i b . s q l a   i m p o r t   M o d e l V i e w 
 f r o m   f l a s k _ s o c k e t i o   i m p o r t   S o c k e t I O 
 i m p o r t   b c r y p t 
 i m p o r t   d a t e t i m e 
 
 #   F l a s k   S e t u p 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 a p p . s e c r e t _ k e y   =   ' y o u r _ s e c r e t _ k e y ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ D A T A B A S E _ U R I ' ]   =   ' s q l i t e : / / / b a n k . d b ' 
 a p p . c o n f i g [ ' S Q L A L C H E M Y _ T R A C K _ M O D I F I C A T I O N S ' ]   =   F a l s e 
 a p p . c o n f i g [ ' J W T _ S E C R E T _ K E Y ' ]   =   ' y o u r _ j w t _ s e c r e t _ k e y ' 
 
 #   I n i t i a l i z e   E x t e n s i o n s 
 d b   =   S Q L A l c h e m y ( a p p ) 
 j w t   =   J W T M a n a g e r ( a p p ) 
 s o c k e t i o   =   S o c k e t I O ( a p p ) 
 
 #   D e f i n e   D a t a b a s e   M o d e l s   ( A c c o u n t   a n d   T r a n s a c t i o n ) 
 c l a s s   A c c o u n t ( d b . M o d e l ) : 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   p r i m a r y _ k e y = T r u e ) 
         o w n e r   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   n u l l a b l e = F a l s e ) 
         p a s s w o r d _ h a s h   =   d b . C o l u m n ( d b . S t r i n g ( 1 2 8 ) ,   n u l l a b l e = F a l s e ) 
         b a l a n c e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         a c c o u n t _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 2 0 ) ) 
         i n t e r e s t _ r a t e   =   d b . C o l u m n ( d b . F l o a t ,   d e f a u l t = 0 ) 
         i s _ a c t i v e   =   d b . C o l u m n ( d b . B o o l e a n ,   d e f a u l t = T r u e ) 
 
 c l a s s   T r a n s a c t i o n ( d b . M o d e l ) : 
         t r a n s a c t i o n _ i d   =   d b . C o l u m n ( d b . I n t e g e r ,   p r i m a r y _ k e y = T r u e ,   a u t o i n c r e m e n t = T r u e ) 
         a c c o u n t _ i d   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ,   d b . F o r e i g n K e y ( ' a c c o u n t . a c c o u n t _ i d ' ) ) 
         t r a n s a c t i o n _ t y p e   =   d b . C o l u m n ( d b . S t r i n g ( 5 0 ) ) 
         a m o u n t   =   d b . C o l u m n ( d b . F l o a t ) 
         t i m e s t a m p   =   d b . C o l u m n ( d b . D a t e T i m e ,   d e f a u l t = d a t e t i m e . d a t e t i m e . n o w ) 
         a c c o u n t   =   d b . r e l a t i o n s h i p ( ' A c c o u n t ' ,   b a c k r e f = ' t r a n s a c t i o n s ' ) 
 
 #   J W T   A d m i n   A u t h e n t i c a t i o n   R o u t e s 
 @ a p p . r o u t e ( ' / a d m i n / l o g i n ' ,   m e t h o d s = [ ' P O S T ' ] ) 
 d e f   a d m i n _ l o g i n ( ) : 
         u s e r n a m e   =   r e q u e s t . j s o n . g e t ( ' u s e r n a m e ' ,   N o n e ) 
         p a s s w o r d   =   r e q u e s t . j s o n . g e t ( ' p a s s w o r d ' ,   N o n e ) 
         
         #   R e p l a c e   ' a d m i n '   a n d   ' p a s s w o r d '   w i t h   s e c u r e   c r e d e n t i a l s 
         i f   u s e r n a m e   = =   ' a d m i n '   a n d   p a s s w o r d   = =   ' p a s s w o r d ' : 
                 a c c e s s _ t o k e n   =   c r e a t e _ a c c e s s _ t o k e n ( i d e n t i t y = u s e r n a m e ) 
                 r e t u r n   j s o n i f y ( a c c e s s _ t o k e n = a c c e s s _ t o k e n ) ,   2 0 0 
         e l s e : 
                 r e t u r n   j s o n i f y ( { " m s g " :   " I n v a l i d   c r e d e n t i a l s " } ) ,   4 0 1 
 
 @ a p p . r o u t e ( ' / a d m i n / s e c u r e _ d a s h b o a r d ' ) 
 @ j w t _ r e q u i r e d ( ) 
 d e f   s e c u r e _ d a s h b o a r d ( ) : 
         c u r r e n t _ a d m i n   =   g e t _ j w t _ i d e n t i t y ( ) 
         i f   c u r r e n t _ a d m i n   = =   ' a d m i n ' : 
                 r e t u r n   r e n d e r _ t e m p l a t e ( ' a d m i n _ d a s h b o a r d . h t m l ' ) 
         e l s e : 
                 r e t u r n   j s o n i f y ( { " m s g " :   " U n a u t h o r i z e d " } ) ,   4 0 3 
 
 #   F l a s k - A d m i n   S e t u p   w i t h   J W T   A u t h e n t i c a t i o n 
 c l a s s   M y A d m i n I n d e x V i e w ( A d m i n I n d e x V i e w ) : 
         @ e x p o s e ( ' / ' ) 
         d e f   i n d e x ( s e l f ) : 
                 i f   ' a d m i n '   n o t   i n   s e s s i o n : 
                         r e t u r n   r e d i r e c t ( u r l _ f o r ( ' a d m i n _ l o g i n ' ) ) 
                 r e t u r n   s e l f . r e n d e r ( ' a d m i n _ i n d e x . h t m l ' ) 
 
 c l a s s   A c c o u n t M o d e l V i e w ( M o d e l V i e w ) : 
         d e f   i s _ a c c e s s i b l e ( s e l f ) : 
                 r e t u r n   ' a d m i n '   i n   s e s s i o n 
 
         c o l u m n _ f i l t e r s   =   [ ' a c c o u n t _ t y p e ' ,   ' i s _ a c t i v e ' ] 
         c a n _ c r e a t e   =   T r u e 
         c a n _ e d i t   =   T r u e 
         c a n _ d e l e t e   =   F a l s e 
 
 a d m i n   =   A d m i n ( a p p ,   i n d e x _ v i e w = M y A d m i n I n d e x V i e w ( ) ,   t e m p l a t e _ m o d e = ' b o o t s t r a p 3 ' ) 
 a d m i n . a d d _ v i e w ( A c c o u n t M o d e l V i e w ( A c c o u n t ,   d b . s e s s i o n ) ) 
 
 #   R e a l - T i m e   T r a n s a c t i o n   D a s h b o a r d 
 @ a p p . r o u t e ( ' / a d m i n / r e a l t i m e _ a n a l y t i c s ' ) 
 @ j w t _ r e q u i r e d ( ) 
 d e f   r e a l t i m e _ a n a l y t i c s ( ) : 
         c u r r e n t _ a d m i n   =   g e t _ j w t _ i d e n t i t y ( ) 
         i f   c u r r e n t _ a d m i n   = =   ' a d m i n ' : 
                 r e t u r n   r e n d e r _ t e m p l a t e ( ' r e a l t i m e _ a n a l y t i c s . h t m l ' ) 
         e l s e : 
                 r e t u r n   j s o n i f y ( { " m s g " :   " U n a u t h o r i z e d " } ) ,   4 0 3 
 
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' : 
         d b . c r e a t e _ a l l ( ) 
         s o c k e t i o . r u n ( a p p ,   h o s t = ' 0 . 0 . 0 . 0 ' ,   p o r t = 5 0 0 0 ,   d e b u g = T r u e ) 
 
 5 .   B u i l d i n g   a n d   R u n n i n g   D o c k e r   C o n t a i n e r s 
 
 N o w   t h a t   e v e r y t h i n g   i s   c o n f i g u r e d ,   i t ' s   t i m e   t o   b u i l d   a n d   r u n   t h e   D o c k e r   c o n t a i n e r s : 
 
         B u i l d   t h e   C o n t a i n e r s : 
 
         b a s h 
 
 d o c k e r - c o m p o s e   b u i l d 
 
 R u n   t h e   C o n t a i n e r s : 
 
 b a s h 
 
         d o c k e r - c o m p o s e   u p 
 
         T h i s   c o m m a n d   w i l l   s t a r t   t h e   F l a s k   a p p l i c a t i o n ,   C e l e r y   w o r k e r ,   a n d   R e d i s   s e r v e r   i n   s e p a r a t e   c o n t a i n e r s .   Y o u   s h o u l d   b e   a b l e   t o   a c c e s s   t h e   a p p l i c a t i o n   a t   h t t p : / / l o c a l h o s t : 5 0 0 0 . 
 
 6 .   S e c u r i n g   t h e   A p p l i c a t i o n   a n d   D e p l o y m e n t   C o n s i d e r a t i o n s 
 S e c u r i n g   t h e   F l a s k   A p p l i c a t i o n : 
 
         H T T P S   w i t h   S S L   C e r t i f i c a t e s : 
                 F o r   a   p r o d u c t i o n   d e p l o y m e n t ,   t h e   a p p l i c a t i o n   s h o u l d   b e   s e r v e d   o v e r   H T T P S .   Y o u   c a n   u s e   L e t ' s   E n c r y p t   t o   g e n e r a t e   a   f r e e   S S L   c e r t i f i c a t e . 
                 I f   u s i n g   N g i n x   a s   a   r e v e r s e   p r o x y ,   c o n f i g u r e   i t   t o   h a n d l e   S S L   t e r m i n a t i o n   a n d   f o r w a r d   s e c u r e   r e q u e s t s   t o   t h e   F l a s k   c o n t a i n e r . 
 
         E n v i r o n m e n t   V a r i a b l e s : 
                 U s e   a   . e n v   f i l e   o r   s e t   e n v i r o n m e n t   v a r i a b l e s   i n   D o c k e r   t o   s t o r e   s e n s i t i v e   i n f o r m a t i o n   l i k e   J W T   s e c r e t   k e y s . 
                 Y o u   c a n   a d d   e n v i r o n m e n t   e n t r i e s   i n   t h e   d o c k e r - c o m p o s e . y m l   t o   r e f e r e n c e   . e n v   v a r i a b l e s : 
 
                 y a m l 
 
                 e n v i r o n m e n t : 
                     -   J W T _ S E C R E T _ K E Y = $ { J W T _ S E C R E T _ K E Y } 
 
         R a t e   L i m i t i n g : 
                 I m p l e m e n t   r a t e   l i m i t i n g   ( e . g . ,   u s i n g   F l a s k - L i m i t e r )   t o   p r o t e c t   a g a i n s t   b r u t e   f o r c e   a t t a c k s   o n   t h e   l o g i n   r o u t e s . 
 
 D e p l o y m e n t   C o n s i d e r a t i o n s : 
 
         C o n t a i n e r   O r c h e s t r a t i o n   w i t h   K u b e r n e t e s : 
                 F o r   l a r g e r   d e p l o y m e n t s ,   c o n s i d e r   u s i n g   K u b e r n e t e s   t o   o r c h e s t r a t e   t h e   c o n t a i n e r s   a c r o s s   m u l t i p l e   n o d e s ,   e n s u r i n g   s c a l a b i l i t y   a n d   r e s i l i e n c e . 
                 H e l m   c h a r t s   c a n   s i m p l i f y   d e p l o y i n g   t h e   F l a s k ,   C e l e r y ,   a n d   R e d i s   c o n t a i n e r s   o n   a   K u b e r n e t e s   c l u s t e r . 
 
         M a n a g e d   R e d i s   S e r v i c e : 
                 I n s t e a d   o f   r u n n i n g   R e d i s   i n   a   c o n t a i n e r ,   y o u   c a n   u s e   a   m a n a g e d   R e d i s   s e r v i c e ,   s u c h   a s   A W S   E l a s t i C a c h e   o r   A z u r e   C a c h e   f o r   R e d i s .   T h i s   e n s u r e s   h i g h   a v a i l a b i l i t y   a n d   r e l i a b i l i t y   f o r   t h e   m e s s a g e   b r o k e r . 
 
         S c a l i n g   C e l e r y   W o r k e r s : 
                 I f   t h e   a p p l i c a t i o n   r e q u i r e s   h a n d l i n g   m a n y   b a c k g r o u n d   t a s k s   s i m u l t a n e o u s l y ,   y o u   c a n   e a s i l y   s c a l e   t h e   n u m b e r   o f   C e l e r y   w o r k e r s   b y   u p d a t i n g   t h e   D o c k e r   C o m p o s e   f i l e : 
 
                 y a m l 
 
                 c e l e r y - w o r k e r : 
                     b u i l d :   . 
                     e n v i r o n m e n t : 
                         -   C E L E R Y _ B R O K E R _ U R L = r e d i s : / / r e d i s : 6 3 7 9 / 0 
                         -   C E L E R Y _ R E S U L T _ B A C K E N D = r e d i s : / / r e d i s : 6 3 7 9 / 0 
                     c o m m a n d :   c e l e r y   - A   c e l e r y _ c o n f i g . c e l e r y   w o r k e r   - - l o g l e v e l = i n f o 
                     d e p l o y : 
                         r e p l i c a s :   3 
 
 S u m m a r y 
 
         D o c k e r i z i n g   t h e   A p p l i c a t i o n :   W e   c o n t a i n e r i z e d   t h e   e n t i r e   a p p l i c a t i o n   u s i n g   D o c k e r ,   a n d   D o c k e r   C o m p o s e   o r c h e s t r a t e s   t h e   F l a s k   a p p ,   C e l e r y   w o r k e r ,   a n d   R e d i s . 
         J W T   A u t h e n t i c a t i o n   f o r   A d m i n   A c c e s s :   E n h a n c e d   t h e   a d m i n   d a s h b o a r d   w i t h   J W T - b a s e d   a u t h e n t i c a t i o n ,   p r o v i d i n g   a   m o r e   s e c u r e   l o g i n   m e c h a n i s m . 
         A u t o m a t e d   T a s k s   w i t h   C e l e r y :   W e   c o n f i g u r e d   C e l e r y   t o   p e r i o d i c a l l y   a p p l y   i n t e r e s t   t o   s a v i n g s   a c c o u n t s ,   u s i n g   R e d i s   a s   a   m e s s a g e   b r o k e r . 
         R e a l - T i m e   A n a l y t i c s   w i t h   F l a s k - S o c k e t I O :   C o n t i n u e d   s u p p o r t   f o r   r e a l - t i m e   a n a l y t i c s ,   p r o v i d i n g   a d m i n s   w i t h   i n s t a n t   i n s i g h t s   i n t o   t r a n s a c t i o n   a c t i v i t y . 
 
 N e x t   S t e p s : 
 
         D e p l o y   t h e   D o c k e r i z e d   c o n t a i n e r s   t o   a   c l o u d   p r o v i d e r   l i k e   A W S   u s i n g   E C S   ( E l a s t i c   C o n t a i n e r   S e r v i c e )   o r   F a r g a t e   f o r   s e r v e r l e s s   c o n t a i n e r   d e p l o y m e n t . 
         I m p l e m e n t   H e l m   f o r   e a s i e r   m a n a g e m e n t   o f   K u b e r n e t e s   d e p l o y m e n t s   i f   s c a l i n g   b e c o m e s   e s s e n t i a l . 
         S e t   u p   C I / C D   p i p e l i n e s   u s i n g   G i t H u b   A c t i o n s   o r   J e n k i n s   t o   a u t o m a t e   t h e   d e p l o y m e n t   o f   u p d a t e s   t o   t h e   c l o u d . 