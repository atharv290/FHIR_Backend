const fs = require("fs");
const path = require("path");

const BASE_DIR = path.join(__dirname, "..");

const codesystem = JSON.parse(
  fs.readFileSync(
    path.join(BASE_DIR, "static/files/atharva_codesystem.json"),
    "utf-8"
  )
);

const conceptmap = JSON.parse(
  fs.readFileSync(
    path.join(BASE_DIR, "static/files/atharva_conceptmap.json"),
    "utf-8"
  )
);

module.exports = { codesystem, conceptmap };
