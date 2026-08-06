/** GitHub-Pages-like static routing for enclosure-concepts-site assets. */
export default {
  async fetch(request, env) {
    const incoming = new URL(request.url);
    const path = incoming.pathname;

    const asset = (pathname) => {
      const u = new URL(incoming.origin + pathname + incoming.search);
      return env.ASSETS.fetch(u);
    };

    // Files with an extension: serve as-is.
    const leaf = path === "/" ? "" : path.split("/").filter(Boolean).pop() || "";
    if (path !== "/" && leaf.includes(".")) {
      return env.ASSETS.fetch(request);
    }

    // `/`, `/dir`, `/dir/` → try index.html
    const base = path.endsWith("/") ? path : path + "/";
    const indexed = await asset(base + "index.html");
    if (indexed.ok) return indexed;

    // Fallbacks
    if (path !== "/" && !path.endsWith("/")) {
      const withSlash = await asset(path + "/index.html");
      if (withSlash.ok) return withSlash;
    }
    return env.ASSETS.fetch(request);
  },
};
