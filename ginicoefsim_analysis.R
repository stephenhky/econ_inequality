ginisim.rawdata<-read.csv('ginicoef.csv', header=TRUE, stringsAsFactors=FALSE)
partitioned.rawdata<-mapply(function(df) {
  split(df, df$population)
}, split(ginisim.rawdata, ginisim.rawdata$alpha))

pops<-unlist(lapply(partitioned.rawdata, function(df) { mean(df$population)}))
alphas<-unlist(lapply(partitioned.rawdata, function(df) { mean(df$alpha)}))
gini_coef.mean<-unlist(lapply(partitioned.rawdata, function(df) { mean(df$gini_coef)}))
gini_coef.std<-unlist(lapply(partitioned.rawdata, function(df) { sqrt(var(df$gini_coef))}))
ginisim.statres<-data.frame(population=pops, alpha=alphas, gini_coef.mean=gini_coef.mean, gini_coef.std=gini_coef.std)

remove(partitioned.rawdata)
remove(alphas)
remove(pops)
remove(gini_coef.mean)
remove(gini_coef.std)

ggplot(ginisim.statres[ ginisim.statres$population>=100000,], aes(x=alpha, y=gini_coef.mean, colour=population, group=population))+geom_errorbar(aes(ymin=gini_coef.mean-gini_coef.std, ymax=gini_coef.mean+gini_coef.std))+ggtitle(expression(paste('Gini Coefficients vs ', alpha)))
