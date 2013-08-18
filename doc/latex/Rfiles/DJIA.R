#!/usr/bin/env Rscript
print('Script started!')
library(lattice)
load('DJIA.RData')
attach(recs)
#setEPS()
#trellis.device("postscript", color=TRUE)
#postscript("../image/try.eps", onefile=FALSE, horizonal=FALSE, paper='special')

pdf("../image/revenue-hist.pdf", onefile=FALSE, paper='special')
par(fig=c(0,1,0,.35))
boxplot(revenue, horizontal=TRUE, bty='n')
par(fig=c(0,1,.25,1), new=TRUE)
hist(revenue, prob=TRUE, main='', col=gray(.9), xlab='Revenue', ylim=c(0, .0035))
lines(density(revenue), lty=2)
curve(dnorm(x, mean(revenue), sd(revenue)), lwd=2, add=TRUE)
#rug(revenue)

#hist(revenue, prob=TRUE, ylim=c(0, .0035))
#lines(density(revenue))
tmp=dev.off()

pdf("../image/revenue-nfast%1d.pdf", onefile=FALSE, paper='special')
bwplot(revenue~factor(nfast), pch='|', xlab='n_fast', ylab='revenue')
boxplot(revenue~factor(nfast))
tmp=dev.off()

pdf("../image/revenue-nslow%1d.pdf", onefile=FALSE, paper='special')
bwplot(revenue~factor(nslow), pch='|', xlab='n_fast', ylab='revenue')
boxplot(revenue~factor(nslow))
tmp=dev.off()

pdf("../image/revenue-nmacd%1d.pdf", onefile=FALSE, paper='special')
bwplot(revenue~factor(nmacd), pch='|', xlab='n_fast', ylab='revenue')
boxplot(revenue~factor(nmacd))
tmp=dev.off()

pdf("../image/revenue-nfast-nslow.pdf", onefile=FALSE, paper='special')
bwplot(revenue~factor(nfast)|factor(nslow), pch='|', xlab='n_fast', ylab='revenue')
tmp=dev.off()

print('Script finished!')

