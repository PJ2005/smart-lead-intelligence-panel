import React from "react";
import { Box, Typography, FormControl, InputLabel, Select, MenuItem } from "@mui/material";

function FiltersPanel({ filters, setFilters }) {
  const industries = ["Fintech", "Health", "SaaS"];
  const sizes = ["1-10", "11-50", "51-200", "201-1000"];
  const techStacks = ["Modern", "Legacy", "Mixed"];

  return (
    <Box>
      <Typography variant="h6" gutterBottom>Filters</Typography>
      <FormControl fullWidth margin="normal">
        <InputLabel>Industry</InputLabel>
        <Select
          value={filters.industry || ""}
          label="Industry"
          onChange={e => setFilters(f => ({ ...f, industry: e.target.value }))}
        >
          <MenuItem value="">All</MenuItem>
          {industries.map(ind => <MenuItem key={ind} value={ind}>{ind}</MenuItem>)}
        </Select>
      </FormControl>
      <FormControl fullWidth margin="normal">
        <InputLabel>Employee Size</InputLabel>
        <Select
          value={filters.size || ""}
          label="Employee Size"
          onChange={e => setFilters(f => ({ ...f, size: e.target.value }))}
        >
          <MenuItem value="">All</MenuItem>
          {sizes.map(size => <MenuItem key={size} value={size}>{size}</MenuItem>)}
        </Select>
      </FormControl>
      <FormControl fullWidth margin="normal">
        <InputLabel>Tech Stack</InputLabel>
        <Select
          value={filters.tech_stack || ""}
          label="Tech Stack"
          onChange={e => setFilters(f => ({ ...f, tech_stack: e.target.value }))}
        >
          <MenuItem value="">All</MenuItem>
          {techStacks.map(ts => <MenuItem key={ts} value={ts}>{ts}</MenuItem>)}
        </Select>
      </FormControl>
    </Box>
  );
}

export default FiltersPanel;
