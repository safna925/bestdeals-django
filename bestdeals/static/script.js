const products = {
    iphone14: {
        name: "Apple iPhone 14",
        brand: "Apple",
        amazonPrice: "₹72,999",
        flipkartPrice: "₹70,999",
        description: "128GB, 6.1' Super Retina XDR display, A15 Bionic chip",
        reviews: "4.7/5",
        amazonLink: "https://www.amazon.in/dp/B0BDK62PDX",
        flipkartLink: "https://www.flipkart.com/apple-iphone-14/p/itm01941cdb2c72b",
        image: "https://m.media-amazon.com/images/I/61bK6PMOC3L.SX679.jpg"
    },
    samsungS23: {
        name: "Samsung Galaxy S23",
        brand: "Samsung",
        amazonPrice: "₹74,999",
        flipkartPrice: "₹73,499",
        description: "6.1' Dynamic AMOLED, Snapdragon 8 Gen 2, 50MP Camera",
        reviews: "4.6/5",
        amazonLink: "https://www.amazon.in/dp/B0BT9FHQG2",
        flipkartLink: "https://www.flipkart.com/samsung-galaxy-s23/p/itmfde1c7b374f32",
        image: "https://m.media-amazon.com/images/I/61RZDb2mQxL.SX679.jpg"
    },
    oneplus11: {
        name: "OnePlus 11 5G",
        brand: "OnePlus",
        amazonPrice: "₹56,999",
        flipkartPrice: "₹55,499",
        description: "Snapdragon 8 Gen 2, 120Hz AMOLED, Hasselblad Cameras",
        reviews: "4.5/5",
        amazonLink: "https://www.amazon.in/dp/B0B8C5C9B7",
        flipkartLink: "https://www.flipkart.com/oneplus-11-5g/p/itm05788c1eace94",
        image: "https://m.media-amazon.com/images/I/61amb0CfMGL.SX679.jpg"
    },
    // Add more products...
};

// Function to update product details when Compare button is clicked
document.getElementById("compare-btn").addEventListener("click", function () {
    const selectedProduct = document.getElementById("product-select").value;

    if (selectedProduct && products[selectedProduct]) {
        const product = products[selectedProduct];

        // Amazon details
        document.getElementById("amazon-image").src = product.image;
        document.getElementById("amazon-name").innerText = product.name;
        document.getElementById("amazon-brand").innerText = product.brand;
        document.getElementById("amazon-price").innerText = product.amazonPrice; // Different price for Amazon
        document.getElementById("amazon-description").innerText = product.description;
        document.getElementById("amazon-reviews").innerText = product.reviews;
        document.getElementById("amazon-link").href = product.amazonLink;

        // Flipkart details
        document.getElementById("flipkart-image").src = product.image;
        document.getElementById("flipkart-name").innerText = product.name;
        document.getElementById("flipkart-brand").innerText = product.brand;
        document.getElementById("flipkart-price").innerText = product.flipkartPrice; // Different price for Flipkart
        document.getElementById("flipkart-description").innerText = product.description;
        document.getElementById("flipkart-reviews").innerText = product.reviews;
        document.getElementById("flipkart-link").href = product.flipkartLink;
    } else {
        alert("Please select a valid product!");
    }
});
