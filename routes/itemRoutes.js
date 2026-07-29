const express = require("express");
const router = express.Router();

const {
  createItem,
  getItems,
  getItemById,
  updateItemStatus
} = require("../controllers/itemController");

// Get all lost/found items
router.get("/", getItems);

// Get one item by ID
router.get("/:id", getItemById);

// Update item status
router.patch("/:id/status", updateItemStatus);

// Create a new lost/found item
router.post("/", createItem);

module.exports = router;