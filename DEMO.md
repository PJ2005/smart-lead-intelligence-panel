# AI Acquisition Readiness Dashboard Demo

## 1. Filtering SaaS Companies
- Use the Filters panel (left column) to select "SaaS" under Industry.
- The lead list updates to show only SaaS companies.

## 2. Hovering on High-Score Leads
- In the center column, leads are shown with a circular score indicator.
- Hover over a high-score (green) lead to see a tooltip with the exact score.
- Click a lead to load detailed insights in the right panel.

## 3. Explaining GDPR Badges
- Each lead card and the insights panel display GDPR badges.
- Badges indicate the compliance and data source for each lead (e.g., "gdpr-compliant", "opencorporates").

## 4. Exporting Lead List to CSV
- Click the "Export to CSV" button above the lead list to download the currently filtered leads as a CSV file.

## 5. Local Testing
- Start the backend: `flask run` (http://localhost:5000)
- Start the frontend: `npm start` (http://localhost:3000)
- Test all flows end-to-end, including filtering, viewing insights, GDPR badges, and CSV export.
