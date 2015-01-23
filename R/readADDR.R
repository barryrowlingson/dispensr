readADDR <- function(path,...){
    a1 = read.csv(path, head=FALSE, stringsAsFactors=FALSE)

    # might not have an overflow X column
    names(a1)=c("PERIOD","GPID","A1","A2","A3","A4","A5","POSTCODE","X")[1:ncol(a1)]
    for(n in names(a1)){
        a1[[n]] = str_trim(a1[[n]])
    }
    a1
}

shortADDR <- function(addr){
    addr[,c("GPID","POSTCODE","PERIOD")]
}
