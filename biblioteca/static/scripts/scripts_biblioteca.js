$(document).ready(function () {
    var currentPath = window.location.pathname;

    $(".navbar-nav .nav-link").each(function () {
        var linkHref = $(this).attr("href");

        if (currentPath.includes(linkHref)) {
            $(".navbar-nav .nav-link").removeClass("active");
            $(this).addClass("active");
            $(this).attr("aria-current", "page");
        }
    });
    
    $("label").each(function () {
        $(this).addClass("form-label");
    });
});
