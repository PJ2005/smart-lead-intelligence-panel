import React from "react";
import { Box, Typography, Chip, Stack } from "@mui/material";

function InsightsPanel({ insights }) {
  if (!insights) {
    return <Typography variant="body1">Select a lead to view insights.</Typography>;
  }
  return (
    <Box>
      <Typography variant="h6" gutterBottom>Insights</Typography>
      <Typography variant="subtitle1" gutterBottom>
        {insights.summary}
      </Typography>
      <Typography variant="body2" gutterBottom>
        <strong>Intent Flags:</strong> {insights.intent_flags && insights.intent_flags.length > 0 ? insights.intent_flags.join(", ") : "None"}
      </Typography>
      <Typography variant="body2" gutterBottom>
        <strong>Score:</strong> {insights.score}
      </Typography>
      <Typography variant="body2" gutterBottom>
        <strong>GDPR Badges:</strong>
      </Typography>
      <Stack direction="row" spacing={1} sx={{ mb: 2 }}>
        {insights.gdpr_badges && insights.gdpr_badges.map((badge, idx) => (
          <Chip key={idx} label={badge} color="info" size="small" />
        ))}
      </Stack>
      <Typography variant="body2" gutterBottom>
        <strong>Company Data:</strong>
      </Typography>
      <pre style={{ fontSize: 12, background: "#f5f5f5", padding: 8, borderRadius: 4 }}>
        {JSON.stringify(insights.company, null, 2)}
      </pre>
      <Typography variant="body2" gutterBottom>
        <strong>LinkedIn Data:</strong>
      </Typography>
      <pre style={{ fontSize: 12, background: "#f5f5f5", padding: 8, borderRadius: 4 }}>
        {JSON.stringify(insights.linkedin, null, 2)}
      </pre>
    </Box>
  );
}

export default InsightsPanel;
