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
