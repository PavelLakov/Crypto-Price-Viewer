function fetchCryptoData() {
  console.log("fetchCryptoData called");

  const coin = document.getElementById("coin-select").value;
  const startDate = document.getElementById("start-date").value;
  const endDate = document.getElementById("end-date").value;

  fetch(`/crypto/${coin}`)
    .then(response => response.json())
    .then(data => {
      console.log("Data received:", data);

      const tableBody = document.querySelector("#crypto-table tbody");
      tableBody.innerHTML = "";

      const filtered = data.filter(entry => {
        const entryDate = new Date(entry.Date);
        const from = startDate ? new Date(startDate) : null;
        const to = endDate ? new Date(endDate) : null;

        return (!from || entryDate >= from) && (!to || entryDate <= to);
      });

      filtered.forEach(entry => {
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
    .catch(error => {
      console.error("Error fetching data:", error);
    });
}

console.log("script.js loaded");