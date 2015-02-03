##' read BNF chapter/section/paragraph headings
##'
##' Using the handy BNF headings JSON file from OpenFormulary, https://github.com/openhealthcare/open-formulary
##' read into R
##' @title Read BNF headings into R
##' @param datafile JSON file from OpenFormulary
##' @return list of chapter, section, and paragraph headings as data frames.
##' @author Barry Rowlingson
headings <- function(datafile){
    d=rjson::fromJSON(file="./dispensr/inst/data/bnf.json")
    levels = c("chapter", "section","paragraph")
    bnfdata=list()
    for(level in levels){
        bnfdata[[level]] =
            do.call(
                rbind.data.frame, Map(function(D){D[["_id"]]=NULL;D$level=NULL;D}, Filter(function(D){D$level==level},d)
                                      )
                ) %>% dplyr::arrange(bnf)
    }
    bnfdata
}

    
##' save CSV versions of heading data
##'
##' writes three CSVs for the BNF headings
##' @title save CSV heading files
##' @param h read from JSON by headings function
##' @param path place to store the files
##' @return nothing
##' @author Barry Rowlingson
write_headings <- function(h,path){
    out = function(section, path){
        write.table(section, path, sep=",", row.names=FALSE)
    }
    out(h$chapter, file.path(path,"chapter.csv"))
    out(h$section, file.path(path,"section.csv"))
    out(h$paragraph, file.path(path,"paragraph.csv"))
}
