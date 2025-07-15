import React, { useRef, useEffect } from "react";
import * as d3 from "d3";
import { Tooltip } from "@mui/material";

function getColor(score) {
  if (score < 40) return "#e53935";
  if (score < 70) return "#fb8c00";
  return "#43a047";
}

function ScoreCircle({ score, size }) {
  const ref = useRef();
  useEffect(() => {
    const radius = size / 2 - 4;
    const arc = d3.arc()
      .innerRadius(radius - 6)
      .outerRadius(radius)
      .startAngle(0)
      .endAngle((score / 100) * 2 * Math.PI);

    const svg = d3.select(ref.current);
    svg.selectAll("*").remove();
    svg
      .attr("width", size)
      .attr("height", size);

    svg.append("circle")
      .attr("cx", size / 2)
      .attr("cy", size / 2)
      .attr("r", radius)
      .attr("fill", "#eee");

    svg.append("path")
      .attr("d", arc)
      .attr("fill", getColor(score))
      .attr("transform", `translate(${size / 2},${size / 2})`);

    svg.append("text")
      .attr("x", size / 2)
      .attr("y", size / 2 + 5)
      .attr("text-anchor", "middle")
      .attr("font-size", 14)
      .attr("fill", "#222")
      .text(score);
  }, [score, size]);

  return (
    <Tooltip title={`Score: ${score}`}>
      <svg ref={ref} />
    </Tooltip>
  );
}

export default ScoreCircle;
