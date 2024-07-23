export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [items, list] of map.entries()) {
    if (list === 1) {
      map.set(items, 100);
    }
  }
}
