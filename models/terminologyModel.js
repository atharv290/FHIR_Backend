const { codesystem, conceptmap } = require("../config/loadData");

exports.search = (namc_term, namc_code, icd_code) => {
  let results = [];

  conceptmap.group?.forEach((g) => {
    g.element?.forEach((e) => {
      let match = false;

      let entry = {
        namc_code: e.code,
        namc_term: e.display,
        icd_mappings: e.target || [],
      };

      if (namc_code && e.code?.toLowerCase() === namc_code.toLowerCase()) {
        match = true;
      }

      if (
        namc_term &&
        e.display?.toLowerCase().includes(namc_term.toLowerCase())
      ) {
        match = true;
      }

      if (icd_code) {
        e.target?.forEach((t) => {
          if (t.code?.toLowerCase() === icd_code.toLowerCase()) {
            entry = {
              namc_code: e.code,
              namc_term: e.display,
              icd_code: t.code,
              icd_term: t.display,
            };
            match = true;
          }
        });
      }

      if (match) results.push(entry);
    });
  });

  return results;
};

exports.translate = (icd_code) => {
  let results = [];

  conceptmap.group?.forEach((g) => {
    g.element?.forEach((e) => {
      e.target?.forEach((t) => {
        if (t.code?.toLowerCase() === icd_code.toLowerCase()) {
          results.push({
            namc_code: e.code,
            namc_term: e.display,
            icd_code: t.code,
            icd_term: t.display,
          });
        }
      });
    });
  });

  return results;
};

exports.autocomplete = (query, limit) => {
  let suggestions = [];

  codesystem.concept?.forEach((c) => {
    if (c.display?.toLowerCase().includes(query.toLowerCase())) {
      suggestions.push({
        code: c.code,
        display: c.display,
      });
    }
  });

  return suggestions.slice(0, limit);
};

exports.expand = (filter, count, offset) => {
  let results = [];

  codesystem.concept?.forEach((c) => {
    if (filter && !c.display?.toLowerCase().includes(filter.toLowerCase()))
      return;

    results.push({
      system:
        codesystem.url ||
        "http://example.com/fhir/CodeSystem/namaste",
      code: c.code,
      display: c.display,
    });
  });

  return {
    total: results.length,
    paged: results.slice(offset, offset + count),
  };
};
