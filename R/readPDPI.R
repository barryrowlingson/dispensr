readPDPI <- function(f,...){
    d = read.csv(f,  ...)

    ## drop the column from the trailing comma
    d$X=NULL

    ## split period into year/month
    d$YEAR = as.numeric(substr(d$PERIOD,1,4))
    d$MONTH = as.numeric(substr(d$PERIOD,5,7))

    ## extract chemical portion of BNF
    d$BNF.CHEMICAL = substr(d$BNF.CODE,1,9)
    
    d
}
