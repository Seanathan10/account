const txData = window.transactionsData.map(t => ({
  id: t[0],
  date: t[1],
  description: t[2],
  amount: t[3],
  category: t[4]
}));

const ctx = document.getElementById('spend-chart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: { labels: [], datasets: [{ label: 'Balance', data: [] }] },
  options: { responsive: true }
});

function updateChart() {
  const sorted = [...txData].sort((a, b) => new Date(a.date) - new Date(b.date));
  let total = 0;
  const labels = [];
  const data = [];
  sorted.forEach(t => {
    total += t.amount;
    labels.push(t.date);
    data.push(total);
  });
  chart.data.labels = labels;
  chart.data.datasets[0].data = data;
  chart.update();
}

updateChart();

function attachDelete(btn) {
  btn.addEventListener('click', async () => {
    const id = parseInt(btn.dataset.id);
    const resp = await fetch(`/delete/${id}`, { method: 'DELETE' });
    if (resp.ok) {
      const idx = txData.findIndex(t => t.id === id);
      if (idx !== -1) txData.splice(idx, 1);
      btn.closest('tr').remove();
      updateChart();
    }
  });
}

document.querySelectorAll('.delete-btn').forEach(attachDelete);

document.getElementById('tx-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;
  const data = {
    date: form.date.value,
    description: form.description.value,
    amount: parseFloat(form.amount.value),
    type: form.type.value,
    category: form.category.value,
  };
  const resp = await fetch('/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (resp.ok) {
    const tx = await resp.json();
    txData.push(tx);
    const tbody = document.getElementById('tx-body');
    const tr = document.createElement('tr');
    tr.innerHTML = `\n      <td class="px-4 py-2 whitespace-nowrap">${tx.date}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.description}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.amount.toFixed(2)}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.category}</td>\n      <td class="px-4 py-2 whitespace-nowrap"><a href="/invoice/${tx.id}" target="_blank" class="text-blue-600">Invoice</a> <button data-id="${tx.id}" class="delete-btn text-red-600 ml-2">Delete</button></td>\n    `;
    tbody.prepend(tr);
    attachDelete(tr.querySelector('.delete-btn'));
    updateChart();
    form.reset();
  }
});

let sortState = { col: null, dir: 1 };

function updateSortIcons() {
  document.querySelectorAll('th[data-index]').forEach(th => {
    const idx = parseInt(th.dataset.index) - 1;
    const icon = th.querySelector('.sort-icon');
    if (!icon) return;
    if (sortState.col === idx) {
      icon.textContent = sortState.dir === 1 ? '▲' : '▼';
    } else {
      icon.textContent = '';
    }
  });
}

function sortTable(idx) {
  const tbody = document.getElementById('tx-body');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  rows.sort((a, b) => {
    const av = a.children[idx].innerText;
    const bv = b.children[idx].innerText;
    let res;
    if (idx === 0) {
      res = new Date(av) - new Date(bv);
    } else if (idx === 2) {
      res = parseFloat(av) - parseFloat(bv);
    } else {
      res = av.localeCompare(bv);
    }
    return res * sortState.dir;
  });
  tbody.innerHTML = '';
  rows.forEach(r => tbody.appendChild(r));
}

document.querySelectorAll('th[data-index]').forEach(th => {
  th.addEventListener('click', () => {
    const idx = parseInt(th.dataset.index) - 1;
    if (sortState.col === idx) {
      sortState.dir *= -1;
    } else {
      sortState.col = idx;
      sortState.dir = 1;
    }
    sortTable(idx);
    updateSortIcons();
  });
});

updateSortIcons();

