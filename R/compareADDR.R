compareADDR <- function(a1, a2){
    fixup = function(a){
        a = a[,c("GPID","POSTCODE")]
        a
    }
    a1 = fixup(a1)
    a2 = fixup(a2)

    d3 = list(
        d12 = dplyr::setdiff(a1,a2),
        i12 = dplyr::intersect(a1,a2),
        d21 = dplyr::setdiff(a2,a1)
    )
    d3
    
}

