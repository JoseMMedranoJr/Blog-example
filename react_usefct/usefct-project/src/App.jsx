import { useEffect, useMemo, useState } from "react";
import "./App.css";

export default function App() {
  const [query, setQuery] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  // simple interaction toggles
  const [onlyEbooks, setOnlyEbooks] = useState(false);
  const [hasCover, setHasCover] = useState(false);
  const [sortMode, setSortMode] = useState("relevance"); // relevance | newest | oldest | title

  // 1) useEffect runs when the user clicks Search (searchTerm changes)
  useEffect(() => {
    let ignore = false; // prevents setting state if component unmounts quickly

    async function fetchBooks() {
      setLoading(true);
      setErr("");

      try {
        const url = `https://openlibrary.org/search.json?q=${encodeURIComponent(
          searchTerm
        )}&limit=40`;

        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const data = await res.json();

        if (!ignore) {
          // Keep only what you need
          const cleaned = (data.docs || []).map((d) => ({
            key: d.key,
            title: d.title ?? "Untitled",
            author: (d.author_name && d.author_name[0]) || "Unknown",
            firstYear: d.first_publish_year ?? null,
            coverId: d.cover_i ?? null,
            ebook: Array.isArray(d.ebook_access) ? d.ebook_access[0] : d.ebook_access, // sometimes varies
            hasFulltext: Boolean(d.has_fulltext),
            pages: d.number_of_pages_median ?? null,
          }));

          setBooks(cleaned);
        }
      } catch (e) {
        if (!ignore) setErr(e.message || "Something went wrong");
      } finally {
        if (!ignore) setLoading(false);
      }
    }

    fetchBooks();
    return () => {
      ignore = true;
    };
  }, [searchTerm]);

  // 2) Filter + sort without extra API calls (innovative UX)
  const visibleBooks = useMemo(() => {
    let list = [...books];

    if (onlyEbooks) {
      list = list.filter((b) => b.hasFulltext);
    }
    if (hasCover) {
      list = list.filter((b) => b.coverId);
    }

    if (sortMode === "newest") {
      list.sort((a, b) => (b.firstYear ?? -1) - (a.firstYear ?? -1));
    } else if (sortMode === "oldest") {
      list.sort((a, b) => (a.firstYear ?? 999999) - (b.firstYear ?? 999999));
    } else if (sortMode === "title") {
      list.sort((a, b) => a.title.localeCompare(b.title));
    }

    return list;
  }, [books, onlyEbooks, hasCover, sortMode]);

  function onSubmit(e) {
    e.preventDefault();
    setSearchTerm(query.trim() || "react");
  }

  return (
    <div className="page">
      <h1>Book Finder 📚</h1>

      <form className="controls" onSubmit={onSubmit}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search by title or author..."
        />
        <button type="submit">Search</button>

        <label>
          <input
            type="checkbox"
            checked={onlyEbooks}
            onChange={(e) => setOnlyEbooks(e.target.checked)}
          />
          Only readable (full text)
        </label>

        <label>
          <input
            type="checkbox"
            checked={hasCover}
            onChange={(e) => setHasCover(e.target.checked)}
          />
          Has cover
        </label>

        <select value={sortMode} onChange={(e) => setSortMode(e.target.value)}>
          <option value="relevance">Sort: Relevance</option>
          <option value="newest">Sort: Newest</option>
          <option value="oldest">Sort: Oldest</option>
          <option value="title">Sort: Title A–Z</option>
        </select>
      </form>

      {loading && <p>Loading books…</p>}
      {err && <p className="error">Error: {err}</p>}

      {!loading && !err && visibleBooks.length === 0 && (
        <p>No results. Try a different search.</p>
      )}

      <div className="shelf">
        {visibleBooks.map((b) => (
          <BookCard key={b.key} book={b} />
        ))}
      </div>
    </div>
  );
}

function BookCard({ book }) {
  const coverUrl = book.coverId
    ? `https://covers.openlibrary.org/b/id/${book.coverId}-M.jpg`
    : null;

  // “innovative” little computed detail
  const readTime =
    book.pages ? `${Math.max(1, Math.round(book.pages / 35))} hrs` : "—";

  return (
    <article className="book">
      <div className="cover">
        {coverUrl ? (
          <img src={coverUrl} alt={`${book.title} cover`} />
        ) : (
          <div className="noCover">No Cover</div>
        )}
      </div>

      <h3 title={book.title}>{book.title}</h3>
      <p className="meta">
        {book.author} • {book.firstYear ?? "Year ?"} • Read time: {readTime}
      </p>

      {book.hasFulltext && <span className="tag">Full text</span>}
    </article>
  );
}