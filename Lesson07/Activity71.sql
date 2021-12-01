-- 1. Đưa ra thông tin đơn hàng (gồm orderDate, requiredDate, Status) và giá trị của mỗi đơn hàng các ngày trong tháng 3/2003.
SELECT orderDate, requiredDate, `Status`, (quantityOrdered * priceEach) AS price
FROM product_orders_plusplus.orderdetails
JOIN product_orders_plusplus.orders ON orderdetails.orderNumber = orders.orderNumber
WHERE orderDate LIKE '2003-03-%';

-- 2. Đưa ra tên sản phẩm của các đơn hàng bị huỷ đơn.
SELECT productName FROM product_orders_plusplus.orderdetails
JOIN product_orders_plusplus.orders ON orderdetails.orderNumber = orders.orderNumber
JOIN product_orders_plusplus.products ON orderdetails.productCode = products.productCode
WHERE `status` = "Cancelled";