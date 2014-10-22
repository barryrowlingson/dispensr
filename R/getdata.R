##' get list of latest files
##'
##' scrape web page for list
##' @title Get latest list
##' @param url URL of listing
##' @return vector of links to pages
##' @author Barry Rowlingson
##' @export
getLatestList = function(
    url="http://www.hscic.gov.uk/searchcatalogue?q=title%3a%22presentation+level+data%22&sort=Most+recent&size=100&page=1"
    ){

    prescs = rvest::html(url)
    latest = prescs %>% rvest::html_nodes(".HSCICProducts a") %>% rvest::html_attr("href")
    latest
    
}

##' get a dispensing archive file
##'
##' get one exe file
##' @title get exe file
##' @param pageurl url of page
##' @param dir where to put file
##' @param overwrite overwrite existing file
##' @return nothing
##' @author Barry Rowlingson
##' @export
getExeFromPage <- function(pageurl, dir, overwrite=FALSE){
    page = rvest::html(pageurl)
    links = page %>% rvest::html_nodes("#resources a") %>% rvest::html_attr("href")
    which_exe = grepl(".exe$", links, ignore.case=TRUE)
    if(!any(which_exe)){
        stop("No .exe file found in resources links on page")
    }
    if(sum(which_exe)>1){
        stop("More than one exe file found in resources links on page")
    }
    get_this = links[which_exe]
    filename = sub(".*/","", get_this)
    destfile = file.path(dir, filename)
    if(file.exists(destfile) & !overwrite){
        stop("File ",destfile," exists and overwrite=FALSE")
    }
    download.file(get_this, destfile)
}
