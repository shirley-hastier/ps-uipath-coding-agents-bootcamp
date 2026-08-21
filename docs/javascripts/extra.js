// Open every link inside the page content (both cross-page lab-guide links
// and external resource links) in a new tab, so readers don't lose their
// place. Deliberately scoped to `.md-content` only -- site chrome (sidebar
// nav, top tabs, search, prev/next footer) is left alone so normal site
// browsing still works in the same tab. Same-page anchors (#section links,
// heading permalinks, "back to top") are also excluded.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".md-content a[href]").forEach(function (link) {
    var href = link.getAttribute("href");
    if (!href || href.charAt(0) === "#") {
      return;
    }
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener");
  });
});
