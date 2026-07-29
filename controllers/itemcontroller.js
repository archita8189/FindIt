const Item = require("../models/itemModel");

// Create a new lost/found item
const createItem = async (req, res) => {
  try {
    const item = await Item.create(req.body);

    res.status(201).json({
      message: "Item added successfully 🚀",
      item
    });
  } catch (error) {
    res.status(400).json({
      message: "Unable to add item",
      error: error.message
    });
  }
};
// Get all lost/found items
const getItems = async (req, res) => {
  try {
    const { type } = req.query;

const filter = {};

if (type) {
  filter.type = type;
}

const items = await Item.find(filter).sort({ createdAt: -1 });
    res.status(200).json({
      count: items.length,
      items
    });
  } catch (error) {
    res.status(500).json({
      message: "Unable to fetch items",
      error: error.message
    });
  }
};
// Get a single item by ID
const getItemById = async (req, res) => {
  try {
    const item = await Item.findById(req.params.id);

    if (!item) {
      return res.status(404).json({
        message: "Item not found"
      });
    }

    res.status(200).json(item);
  } catch (error) {
    res.status(400).json({
      message: "Invalid item ID",
      error: error.message
    });
  }
};
// Update item status
const updateItemStatus = async (req, res) => {
  try {
    const { status } = req.body;

    if (!["active", "resolved"].includes(status)) {
      return res.status(400).json({
        message: "Status must be active or resolved"
      });
    }

    const item = await Item.findByIdAndUpdate(
      req.params.id,
      { status },
      {
        new: true,
        runValidators: true
      }
    );

    if (!item) {
      return res.status(404).json({
        message: "Item not found"
      });
    }

    res.status(200).json({
      message: "Item status updated successfully",
      item
    });
  } catch (error) {
    res.status(400).json({
      message: "Unable to update item status",
      error: error.message
    });
  }
};
module.exports = {
  createItem,
  getItems,
  getItemById,
  updateItemStatus
};
