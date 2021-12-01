SELECT products.productCode, productName ,SUM(quantityOrdered * priceEach) AS totalPrice FROM product_orders_plusplus.products 
JOIN product_orders_plusplus.orderdetails ON products.productCode = orderdetails.productCode
GROUP BY productCode ORDER BY totalPrice ASC;