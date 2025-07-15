import React, { useEffect, useState } from "react";
import { Grid, Box } from "@mui/material";
import FiltersPanel from "./FiltersPanel.jsx";
import LeadList from "./LeadList.jsx";
import InsightsPanel from "./InsightsPanel.jsx";

function App() {
  const [leads, setLeads] = useState([]);
  const [selectedLead, setSelectedLead] = useState(null);
  const [filters, setFilters] = useState({});
  const [insights, setInsights] = useState(null);

  useEffect(() => {
    fetch("/api/leads")
      .then((res) => res.json())
      .then((data) => setLeads(data));
  }, []);

  const handleLeadClick = (lead) => {
    setSelectedLead(lead);
    fetch("/api/leads/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        linkedin_url: lead.linkedin_url,
        company_name: lead.company_name,
      }),
    })
      .then((res) => res.json())
      .then((data) => setInsights(data));
  };

  const filteredLeads = leads.filter((lead) => {
    if (filters.industry && lead.industry !== filters.industry) return false;
    if (filters.size && lead.size !== filters.size) return false;
    if (filters.tech_stack && lead.tech_stack !== filters.tech_stack) return false;
    return true;
  });

  return (
    <Box sx={{ flexGrow: 1, height: "100vh", padding: 2 }}>
      <Grid container spacing={2} sx={{ height: "100%" }}>
        <Grid item xs={12} md={3}>
          <FiltersPanel filters={filters} setFilters={setFilters} />
        </Grid>
        <Grid item xs={12} md={5}>
          <LeadList leads={filteredLeads} onLeadClick={handleLeadClick} selectedLead={selectedLead} />
        </Grid>
        <Grid item xs={12} md={4}>
          <InsightsPanel insights={insights} />
        </Grid>
      </Grid>
    </Box>
  );
}

export default App;
