function fetchCryptoData() {
  const coin = document.getElementById("coin-select").value;

  let startDate = document.getElementById("start-date").value; // YYYY-MM-DD
  let endDate = document.getElementById("end-date").value;     // YYYY-MM-DD

  // If both are set and start > end, swap them
  if (startDate && endDate && startDate > endDate) {
    const tmp = startDate;
    startDate = endDate;
    endDate = tmp;

    document.getElementById("start-date").value = startDate;
    document.getElementById("end-date").value = endDate;
  }

  const params = new URLSearchParams();
  if (startDate) params.append("start", startDate);
  if (endDate) params.append("end", endDate);

  fetch(`/crypto/${coin}?${params.toString()}`)
    .then(async (res) => {
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Request failed");
      return data;
    })
    .then((data) => {
      const tableBody = document.querySelector("#crypto-table tbody");
      tableBody.innerHTML = "";

      if (!data.length) {
        tableBody.innerHTML = `<tr><td colspan="6">No data for this date range.</td></tr>`;
        return;
      }

      data.forEach((entry) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${entry.Date}</td>
          <td>${entry.Price}</td>
          <td>${entry.Open}</td>
          <td>${entry.High}</td>
          <td>${entry.Low}</td>
          <td>${entry["Change %"]}</td>
        `;
        tableBody.appendChild(row);
      });
    })
    .catch((err) => {
      console.error(err);
      const tableBody = document.querySelector("#crypto-table tbody");
      tableBody.innerHTML = `<tr><td colspan="6">Error: ${err.message}</td></tr>`;
    });
}
