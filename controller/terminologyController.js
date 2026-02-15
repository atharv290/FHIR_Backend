const terminologyModel = require("../models/terminologyModel");

exports.search = (req, res) => {
  console.log("requested API : ",req.query);
  const { namc_term, namc_code, icd_code } = req.query;
  const results = terminologyModel.search(namc_term, namc_code, icd_code);

  if (!results.length)
    return res.json({ message: "No matches found" });

  res.json({ results });
};

exports.translate = (req, res) => {
  console.log("requested API : ",req.query);
  const { icd_code } = req.query;
  if (!icd_code)
    return res.status(400).json({ error: "icd_code is required" });

  const results = terminologyModel.translate(icd_code);

  if (!results.length)
    return res.json({ message: "No matches found" });

  res.json({ results });
};

exports.autocomplete = (req, res) => {
  console.log("requested API : ",req.query);
  const { query, limit = 10 } = req.query;
  if (!query)
    return res.status(400).json({ error: "query is required" });

  const suggestions = terminologyModel.autocomplete(
    query,
    Number(limit)
  );

  res.json({ suggestions });
};

exports.expand = (req, res) => {
  console.log("requested API : ",req.query);
  const { filter, count = 20, offset = 0 } = req.query;

  const { total, paged } = terminologyModel.expand(
    filter,
    Number(count),
    Number(offset)
  );

  res.json({
    resourceType: "ValueSet",
    expansion: {
      total,
      offset: Number(offset),
      count: paged.length,
      contains: paged,
    },
  });
};
