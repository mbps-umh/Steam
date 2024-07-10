# Code Example of Biology ANOVA
# Data enter
P1 <- c(2, 0, 1, 0, 2, 3, 1)
P2 <- c(6, 6, 5, 4, 7, 6, 5)
P3 <- c(5, 3, 2, 6, 4, 5, 7)
P4 <- c(4, 5, 3, 4, 7, 6, 5)
P5 <- c(1, 0, 0, 2, 1, 2, 1)
NT <- c(10, 8, 9, 7, 9, 10, 12)
ninsectos <- c(2, 0, 1, 0, 2, 3, 1, 6, 6, 5, 4, 7, 6, 5, 5, 3, 2, 6, 4, 5, 7, 4, 5, 3, 4, 7, 6, 5, 1, 0, 0, 2, 1, 2, 1, 10, 8, 9, 7, 9, 10, 12)
Tratamientos <- as.factor(c(rep(c("P1" , "P2" , "P3" , "P4" , "P5", "NT"), each=7)))
#
# Test of Normality Shapiro-Wilk
shapiro.test(NT)
shapiro.test(P1)
shapiro.test(P2)
shapiro.test(P3)
shapiro.test(P4)
shapiro.test(P5)
#
# Test of homogeneity Bartlett
bartlett.test(ninsectos ~ Tratamientos)
#
# ANOVA
modeloanova <- aov(ninsectos ~ Tratamientos)
summary(modeloanova)
#
# Multiple comparison Bonferroni
pairwise.t.test(ninsectos, Tratamientos, p.adj = "bonferroni")
#
# Multiple comparison Tukey
tukey <- TukeyHSD(aov(modeloanova))
tukey
