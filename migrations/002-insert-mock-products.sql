--! Message: Insert mock product data
--! Previous: 001-products

-- Only insert if no products exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM products) THEN
        INSERT INTO products (name, category, price) VALUES
            ('T-shirt', 'Apparel', 19.99),
            ('Sneakers', 'Apparel', 49.99),
            ('Coffee Mug', 'Home', 9.99),
            ('Laptop Sleeve', 'Electronics', 25.00),
            ('Bluetooth Speaker', 'Electronics', 39.50);
    END IF;
END
$$;
