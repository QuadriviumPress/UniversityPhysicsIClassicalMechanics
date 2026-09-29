const base = new URL(self.registration.scope);
const VERSION = 'v1';
// CacheStorage is shared by every application on this origin, including books
// installed under other paths. Never read or remove another scope's caches.
const CACHE_PREFIX = `university-physics-i-classical-mechanics:${encodeURIComponent(base.href)}:`;
const STATIC_CACHE = `${CACHE_PREFIX}static-${VERSION}`;
const PAGE_CACHE = `${CACHE_PREFIX}pages-${VERSION}`;
const scoped = (path = '') => new URL(path, base).toString();

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then((cache) => cache.addAll([scoped(''), scoped('offline.html'), scoped('manifest.webmanifest')]))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys
        .filter((key) => key.startsWith(CACHE_PREFIX) && ![STATIC_CACHE, PAGE_CACHE].includes(key))
        .map((key) => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  const target = new URL(request.url);
  if (request.method !== 'GET' || target.origin !== base.origin || !target.pathname.startsWith(base.pathname)) return;

  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(PAGE_CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(async () => {
          const pages = await caches.open(PAGE_CACHE);
          const cached = await pages.match(request);
          if (cached) return cached;
          const staticAssets = await caches.open(STATIC_CACHE);
          return (await staticAssets.match(request)) || staticAssets.match(scoped('offline.html'));
        })
    );
    return;
  }

  event.respondWith(
    caches.open(PAGE_CACHE).then(async (pages) => {
      const cached = await pages.match(request);
      if (cached) return cached;
      const staticAssets = await caches.open(STATIC_CACHE);
      const precached = await staticAssets.match(request);
      if (precached) return precached;
      const response = await fetch(request);
      if (response.ok) pages.put(request, response.clone());
      return response;
    })
  );
});
