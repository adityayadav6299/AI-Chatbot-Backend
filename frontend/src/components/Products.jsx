import React, { useState, useEffect } from 'react';
import { productAPI } from '../services/api';

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    sku: '',
    price: '',
    quantity_in_stock: ''
  });
  const [editing, setEditing] = useState(false);
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await productAPI.getAll();
      setProducts(response.data);
      setError(null);
    } catch (err) {
      setError(err.message || 'Failed to fetch products');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editing) {
        await productAPI.update(editingId, {
          ...formData,
          price: parseFloat(formData.price),
          quantity_in_stock: parseInt(formData.quantity_in_stock)
        });
        setEditing(false);
        setEditingId(null);
      } else {
        await productAPI.create({
          ...formData,
          price: parseFloat(formData.price),
          quantity_in_stock: parseInt(formData.quantity_in_stock)
        });
      }
      setFormData({ name: '', sku: '', price: '', quantity_in_stock: '' });
      fetchProducts();
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'Error saving product');
    }
  };

  const handleEdit = (product) => {
    setFormData(product);
    setEditing(true);
    setEditingId(product.id);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure?')) {
      try {
        await productAPI.delete(id);
        fetchProducts();
      } catch (err) {
        setError(err.message || 'Error deleting product');
      }
    }
  };

  return (
    <div className="section">
      <h2>Products</h2>
      
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <input
            type="text"
            name="name"
            placeholder="Product Name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            name="sku"
            placeholder="SKU"
            value={formData.sku}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="number"
            name="price"
            placeholder="Price"
            step="0.01"
            value={formData.price}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="number"
            name="quantity_in_stock"
            placeholder="Quantity"
            value={formData.quantity_in_stock}
            onChange={handleInputChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          {editing ? 'Update Product' : 'Add Product'}
        </button>
        {editing && (
          <button
            type="button"
            onClick={() => {
              setEditing(false);
              setFormData({ name: '', sku: '', price: '', quantity_in_stock: '' });
            }}
            className="btn btn-secondary"
          >
            Cancel
          </button>
        )}
      </form>

      {error && <div className="error">{error}</div>}
      {loading && <div className="loading">Loading...</div>}

      <table className="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>SKU</th>
            <th>Price</th>
            <th>Stock</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map(product => (
            <tr key={product.id}>
              <td>{product.name}</td>
              <td>{product.sku}</td>
              <td>${product.price.toFixed(2)}</td>
              <td>{product.quantity_in_stock}</td>
              <td>
                <button onClick={() => handleEdit(product)} className="btn btn-sm btn-edit">Edit</button>
                <button onClick={() => handleDelete(product.id)} className="btn btn-sm btn-delete">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Products;
