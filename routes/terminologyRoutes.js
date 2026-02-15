const express = require("express");
const router = express.Router();
const controller = require("../controller/terminologyController");

router.get("/search", controller.search);
router.get("/translate", controller.translate);
router.get("/autocomplete", controller.autocomplete);
router.get("/expand", controller.expand);

module.exports = router;
