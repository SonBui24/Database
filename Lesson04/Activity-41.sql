SELECT * FROM store_cms_plusplus.laptop;

-- 1. Trả ra 5 laptop có giá nhỏ nhất.
SELECT * FROM store_cms_plusplus.laptop ORDER BY price ASC LIMIT 0,5;

-- 2. Trả ra các hãng sản xuất laptop và sắp xếp theo thứ tự Alphabet.
SELECT DISTINCT maker FROM store_cms_plusplus.laptop ORDER BY maker ASC;

-- 3. Viết câu query trả ra doanh số laptop bán được và doanh thu của cửa hàng.
SELECT SUM(sold) AS 'Doanh So', SUM(sold * price) AS 'Doanh Thu' FROM store_cms_plusplus.laptop;