function calculateKPIs(employees) {
  const kpis = {
    totalCollaborators: employees.length,
    overdueVacations: 0,
    expiringVacations: 0,
    paidVacations: 0,
    incompleteVacations: 0,
  };

  employees.forEach((employee) => {
    switch (employee.STATUS) {
      case "Férias Vencida":
        kpis.overdueVacations++;
        break;
      case "Férias à Vencer":
        kpis.expiringVacations++;
        break;
      case "Férias Abonada":
        kpis.paidVacations++;
        break;
      case "Férias Incompleta":
        kpis.incompleteVacations++;
        break;
      default:
        NaN;
    }
  });

  return kpis;
}

async function populateKPIs() {
  try {
    const response = await fetch("api/data-ferias/");
    const data = await response.json();
    const kpis = calculateKPIs(data);

    // Update KPI values in the HTML
    const totalEl = document.getElementById("kpi-total-collaborators");
    const overdueEl = document.getElementById("kpi-overdue");
    const expiringEl = document.getElementById("kpi-expiring");
    const paidEl = document.getElementById("kpi-paid");
    const incompleteEl = document.getElementById("kpi-incomplete-vacation");

    if (totalEl) {
      totalEl.textContent = kpis.totalCollaborators;
    }

    if (overdueEl) {
      overdueEl.textContent = kpis.overdueVacations;
    }

    if (expiringEl) {
      expiringEl.textContent = kpis.expiringVacations;
    }

    if (paidEl) {
      paidEl.textContent = kpis.paidVacations;
    }

    if (incompleteEl) {
      incompleteEl.textContent = kpis.incompleteVacations;
    }
  } catch (error) {
    NaN;
  }
}

// Load KPI data when page loads
document.addEventListener("DOMContentLoaded", function () {
  populateKPIs();
});
