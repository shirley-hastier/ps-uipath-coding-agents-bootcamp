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

// Checklist items ("- [ ] ...") render as clickable checkboxes via
// pymdownx.tasklist. Persist their checked state to localStorage, keyed by
// page path + item text, so ticking off a prerequisite/checkpoint survives
// a reload -- purely client-side, this browser only, nothing sent anywhere.
document.addEventListener("DOMContentLoaded", function () {
  var boxes = document.querySelectorAll(
    ".md-content .task-list-control input[type='checkbox']"
  );
  boxes.forEach(function (box, index) {
    var item = box.closest("li");
    var text = item ? item.innerText.trim().replace(/\s+/g, " ") : "item-" + index;
    var key = "checklist::" + location.pathname + "::" + text;

    var saved = window.localStorage ? localStorage.getItem(key) : null;
    if (saved !== null) {
      box.checked = saved === "true";
    }

    box.addEventListener("change", function () {
      if (window.localStorage) {
        localStorage.setItem(key, box.checked);
      }
    });
  });
});
