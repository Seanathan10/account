document.getElementById('tx-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;
  const data = {
    date: form.date.value,
    description: form.description.value,
    amount: parseFloat(form.amount.value),
    category: form.category.value,
  };
  const resp = await fetch('/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (resp.ok) {
    const tx = await resp.json();
    const tbody = document.getElementById('tx-body');
    const tr = document.createElement('tr');
    tr.innerHTML = `\n      <td class="px-4 py-2 whitespace-nowrap">${tx.date}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.description}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.amount.toFixed(2)}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.category}</td>\n    `;
    tbody.prepend(tr);
    form.reset();
  }
});
