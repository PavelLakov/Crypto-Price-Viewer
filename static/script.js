function fetchCryptoData() {
  const coin = document.getElementById("coin-select").value;
  const startDate = document.getElementById("start-date").value; // YYYY-MM-DD
  const endDate = document.getElementById("end-date").value;     // YYYY-MM-DD

  const params = new URLSearchParams();
  if (startDate) params.append("start", startDate);
  if (endDate) params.append("end", endDate);

  fetch(`/crypto/${coin}?${params.toString()}`)
    .then(r => r.json())
    .then(data => {
      const tableBody = document.querySelector("#crypto-table tbody");
      tableBody.innerHTML = "";

      data.forEach(entry => {
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
    .catch(err => console.error("Error fetching data:", err));
}


