"use strict";
const menu = document.querySelector(".menu-button");
const sidebar = document.querySelector(".sidebar");
menu?.addEventListener("click", () => {
  const open = menu.getAttribute("aria-expanded") !== "true";
  menu.setAttribute("aria-expanded", String(open));
  sidebar.classList.toggle("open", open);
});
document.addEventListener("keydown", event => {
  if (event.key === "Escape") {
    sidebar?.classList.remove("open");
    menu?.setAttribute("aria-expanded", "false");
    document.getElementById("search-results").hidden = true;
  }
});

const search = document.getElementById("site-search");
const results = document.getElementById("search-results");
let searchData;
search.addEventListener("input", async () => {
  const query = search.value.trim().toLowerCase();
  results.replaceChildren();
  results.hidden = !query;
  if (!query) return;
  try {
    searchData ??= fetch("assets/search-index.json").then(response => {
      if (!response.ok) throw new Error("search unavailable");
      return response.json();
    });
    const pages = await searchData;
    if (query !== search.value.trim().toLowerCase()) return;
    const terms = query.split(/\s+/);
    const matches = pages.filter(page => terms.every(term => (page.title + " " + page.text).toLowerCase().includes(term)))
      .sort((a, b) => Number(b.title.toLowerCase().includes(query)) - Number(a.title.toLowerCase().includes(query)));
    for (const page of matches.slice(0, 8)) {
      const link = document.createElement("a");
      link.href = page.url;
      link.textContent = page.title;
      const snippet = document.createElement("small");
      const position = Math.max(0, page.text.toLowerCase().indexOf(terms[0]) - 45);
      snippet.textContent = (position ? "…" : "") + page.text.slice(position, position + 140) + "…";
      link.append(snippet);
      results.append(link);
    }
    if (!matches.length) {
      const empty = document.createElement("p");
      empty.textContent = "No matching pages. Try a GPIO number, device, or interface.";
      results.append(empty);
    }
  } catch {
    searchData = undefined;
    results.textContent = "Search is unavailable. Use the documentation menu.";
  }
});
document.addEventListener("click", event => {
  if (!event.target.closest(".search-wrap")) results.hidden = true;
});
search.addEventListener("focus", () => {
  if (search.value && results.childNodes.length) results.hidden = false;
});

const filter = document.getElementById("pin-filter");
filter?.addEventListener("input", () => {
  const query = filter.value.trim().toLowerCase();
  let visible = 0;
  document.querySelectorAll("article .table-scroll").forEach(wrapper => {
    let count = 0;
    wrapper.querySelectorAll("tbody tr").forEach(row => {
      row.hidden = !row.textContent.toLowerCase().includes(query);
      if (!row.hidden) count++;
    });
    wrapper.hidden = count === 0;
    visible += count;
  });
  document.getElementById("pin-filter-status").textContent = query
    ? `${visible} matching row${visible === 1 ? "" : "s"}. Clear the search to show all pins.` : "";
});

document.querySelectorAll("pre > code").forEach(code => {
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = "Copy";
  button.setAttribute("aria-label", "Copy code example");
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(code.textContent);
      button.textContent = "Copied";
      setTimeout(() => { button.textContent = "Copy"; }, 1800);
    } catch {
      button.textContent = "Select text to copy";
    }
  });
  code.parentElement.append(button);
});
