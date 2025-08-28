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
    tr.innerHTML = `\n      <td class="px-4 py-2 whitespace-nowrap">${tx.date}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.description}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.amount.toFixed(2)}</td>\n      <td class="px-4 py-2 whitespace-nowrap">${tx.category}</td>\n      <td class="px-4 py-2 whitespace-nowrap"><a href="/invoice/${tx.id}" target="_blank" class="text-blue-600">Invoice</a></td>\n    `;
    tbody.prepend(tr);
    updateChart();
    form.reset();
  }
});

document.querySelectorAll('th[data-index]').forEach(th => {
  th.addEventListener('click', () => {
    const idx = parseInt(th.dataset.index) - 1;
    const tbody = document.getElementById('tx-body');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    rows.sort((a, b) => {
      const av = a.children[idx].innerText;
      const bv = b.children[idx].innerText;
      if (idx === 0) {
        return new Date(av) - new Date(bv);
      }
      if (idx === 2) {
        return parseFloat(av) - parseFloat(bv);
      }
      return av.localeCompare(bv);
    });
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
  });
});
