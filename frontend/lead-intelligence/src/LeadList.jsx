import React from "react";
import { Card, CardContent, Typography, List, ListItem, ListItemButton, Box, Stack, Chip, Button } from "@mui/material";
import ScoreCircle from "./ScoreCircle.jsx";

function exportLeadsToCSV(leads) {
  if (!leads.length) return;
  const headers = Object.keys(leads[0]);
  const csvRows = [
    headers.join(","),
    ...leads.map(lead =>
      headers.map(h => JSON.stringify(lead[h] ?? "")).join(",")
    ),
  ];
  const blob = new Blob([csvRows.join("\n")], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "leads.csv";
  a.click();
  URL.revokeObjectURL(url);
}

function LeadList({ leads, onLeadClick, selectedLead }) {
  return (
    <>
      <Box sx={{ mb: 2 }}>
        <Button
          variant="outlined"
          size="small"
          onClick={() => exportLeadsToCSV(leads)}
        >
          Export to CSV
        </Button>
      </Box>
      <List>
        {leads.map(lead => (
          <ListItem key={lead.id} disablePadding>
            <ListItemButton
              selected={selectedLead && selectedLead.id === lead.id}
              onClick={() => onLeadClick(lead)}
            >
              <Card sx={{ width: "100%" }}>
                <CardContent sx={{ display: "flex", alignItems: "center" }}>
                  <ScoreCircle score={lead.score || 0} size={48} />
                  <Box sx={{ ml: 2, flex: 1 }}>
                    <Typography variant="h6">{lead.company_name}</Typography>
                    <Typography variant="body2">{lead.summary || "No summary"}</Typography>
                    <Stack direction="row" spacing={1} sx={{ mt: 1 }}>
                      {(lead.gdpr_badges || []).map((badge, idx) => (
                        <Chip key={idx} label={badge} color="info" size="small" />
                      ))}
                    </Stack>
                  </Box>
                </CardContent>
              </Card>
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </>
  );
}

export default LeadList;
