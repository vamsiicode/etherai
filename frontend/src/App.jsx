import { useEffect, useState } from 'react'
import api from './services/api'
import './App.css'

function App() {
  const [products, setProducts] = useState([])
  const [customers, setCustomers] = useState([])
  const [orders, setOrders] = useState([])
  const [productForm, setProductForm] = useState({ name: '', sku: '', stock: 0, price: 0, description: '' })
  const [customerForm, setCustomerForm] = useState({ name: '', email: '', phone: '' })
  const [orderForm, setOrderForm] = useState({ product_id: '', customer_id: '', quantity: 1 })
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetchAll()
  }, [])

  const fetchAll = async () => {
    const [productsRes, customersRes, ordersRes] = await Promise.all([
      api.get('/products'),
      api.get('/customers'),
      api.get('/orders'),
    ])
    setProducts(productsRes.data)
    setCustomers(customersRes.data)
    setOrders(ordersRes.data)
  }

  const handleSubmit = async (event, type) => {
    event.preventDefault()
    try {
      setMessage('')
      if (type === 'product') {
        await api.post('/products', productForm)
        setProductForm({ name: '', sku: '', stock: 0, price: 0, description: '' })
      } else if (type === 'customer') {
        await api.post('/customers', customerForm)
        setCustomerForm({ name: '', email: '', phone: '' })
      } else if (type === 'order') {
        await api.post('/orders', { ...orderForm, quantity: Number(orderForm.quantity) })
        setOrderForm({ product_id: '', customer_id: '', quantity: 1 })
      }
      fetchAll()
      setMessage('Saved successfully!')
    } catch (error) {
      setMessage(error.response?.data?.detail || 'Failed to save')
    }
  }

  return (
    <div className="app-shell">
      <header>
        <h1>Inventory & Order System</h1>
      </header>
      <main>
        <section className="card">
          <h2>Add Product</h2>
          <form onSubmit={(event) => handleSubmit(event, 'product')}>
            <label>Name<input value={productForm.name} onChange={(e) => setProductForm({ ...productForm, name: e.target.value })} required /></label>
            <label>SKU<input value={productForm.sku} onChange={(e) => setProductForm({ ...productForm, sku: e.target.value })} required /></label>
            <label>Stock<input type="number" value={productForm.stock} onChange={(e) => setProductForm({ ...productForm, stock: Number(e.target.value) })} min="0" required /></label>
            <label>Price<input type="number" value={productForm.price} onChange={(e) => setProductForm({ ...productForm, price: Number(e.target.value) })} min="0" required /></label>
            <label>Description<textarea value={productForm.description} onChange={(e) => setProductForm({ ...productForm, description: e.target.value })} /></label>
            <button type="submit">Create Product</button>
          </form>
        </section>

        <section className="card">
          <h2>Add Customer</h2>
          <form onSubmit={(event) => handleSubmit(event, 'customer')}>
            <label>Name<input value={customerForm.name} onChange={(e) => setCustomerForm({ ...customerForm, name: e.target.value })} required /></label>
            <label>Email<input type="email" value={customerForm.email} onChange={(e) => setCustomerForm({ ...customerForm, email: e.target.value })} required /></label>
            <label>Phone<input value={customerForm.phone} onChange={(e) => setCustomerForm({ ...customerForm, phone: e.target.value })} /></label>
            <button type="submit">Create Customer</button>
          </form>
        </section>

        <section className="card">
          <h2>Create Order</h2>
          <form onSubmit={(event) => handleSubmit(event, 'order')}>
            <label>Product<select value={orderForm.product_id} onChange={(e) => setOrderForm({ ...orderForm, product_id: e.target.value })} required>
                <option value="">Choose product</option>
                {products.map((product) => (
                  <option key={product.id} value={product.id}>
                    {product.name} (stock: {product.stock})
                  </option>
                ))}
              </select></label>
            <label>Customer<select value={orderForm.customer_id} onChange={(e) => setOrderForm({ ...orderForm, customer_id: e.target.value })} required>
                <option value="">Choose customer</option>
                {customers.map((customer) => (
                  <option key={customer.id} value={customer.id}>
                    {customer.name}
                  </option>
                ))}
              </select></label>
            <label>Quantity<input type="number" value={orderForm.quantity} onChange={(e) => setOrderForm({ ...orderForm, quantity: Number(e.target.value) })} min="1" required /></label>
            <button type="submit">Place Order</button>
          </form>
        </section>

        <section className="card wide">
          <h2>Products</h2>
          <div className="table-grid">
            {products.map((product) => (
              <div key={product.id} className="table-row">
                <strong>{product.name}</strong>
                <span>SKU: {product.sku}</span>
                <span>Stock: {product.stock}</span>
                <span>Price: ₹{product.price}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="card wide">
          <h2>Orders</h2>
          <div className="table-grid">
            {orders.map((order) => (
              <div key={order.id} className="table-row">
                <span>Order #{order.id}</span>
                <span>Product: {order.product?.name ?? 'Unknown'}</span>
                <span>Customer: {order.customer?.name ?? 'Unknown'}</span>
                <span>Qty: {order.quantity}</span>
              </div>
            ))}
          </div>
        </section>
      </main>
      {message && <div className="message">{message}</div>}
    </div>
  )
}

export default App
