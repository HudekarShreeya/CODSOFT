# Define the product data (as previously defined)
products = {
    'product1': {'type': 'shampoo', 'brand': 'Brand A', 'price': 10, 'rating': 4.5},
    'product2': {'type': 'conditioner', 'brand': 'Brand B', 'price': 15, 'rating': 4.2},
    'product3': {'type': 'hair oil', 'brand': 'Brand C', 'price': 20, 'rating': 4.7},
    'product4': {'type': 'hair oil', 'brand': 'Brand D', 'price': 12, 'rating': 4.3},
    'product5': {'type': 'hair oil', 'brand': 'Brand E', 'price': 18, 'rating': 4.8},
    'product6': {'type': 'shampoo', 'brand': 'Brand B', 'price': 12, 'rating': 4.1},
    'product7': {'type': 'shampoo', 'brand': 'Brand C', 'price': 14, 'rating': 4.6},
    'product8': {'type': 'shampoo', 'brand': 'Brand D', 'price': 16, 'rating': 4.4},
    'product9': {'type': 'conditioner', 'brand': 'Brand A', 'price': 18, 'rating': 4.5},
    'product10': {'type': 'conditioner', 'brand': 'Brand C', 'price': 22, 'rating': 4.0}
}

def recommend_products(user_preferences, products):
    recommended_products = []
    
    for product_id, details in products.items():
        # Filter based on user preferences
        if details['type'] == user_preferences['type'] \
           and details['price'] <= user_preferences['max_price'] \
           and abs(details['rating'] - user_preferences['rating']) <= 0.5:  # Allow a tolerance of 0.5 in rating
            recommended_products.append((product_id, details))
    
    # Sort recommended products by rating (descending)
    recommended_products.sort(key=lambda x: x[1]['rating'], reverse=True)
    
    return recommended_products

# Function to get user preferences for hair products
def get_user_preferences():
    print("Welcome to the Hair Product Recommendation System!")
    print("Please enter your preferences:")
    user_preferences = {}
    user_preferences['type'] = input("Type of product (e.g., shampoo, conditioner, hair oil): ").strip().lower()
    user_preferences['max_price'] = float(input("Maximum price you want to pay ($): "))
    user_preferences['rating'] = float(input("Rating you prefer (out of 5): "))
    return user_preferences

# Main function to run the recommendation system
def main():
    user_preferences = get_user_preferences()
    recommended_products = recommend_products(user_preferences, products)
    
    # Display recommended products or message if no products match
    if recommended_products:
        print("\nRecommended Products:")
        for product_id, details in recommended_products:
            print(f"Product ID: {product_id}, Type: {details['type']}, Brand: {details['brand']}, Price: ${details['price']}, Rating: {details['rating']}")
    else:
        print("\nSorry, no products match your preferences.")

if __name__ == "__main__":
    main()
