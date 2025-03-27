from typing import NamedTuple

RestaurantsTuple = NamedTuple('RestaurantsTuple', [('restaurant_name', str), ('rating', int), ('distance', int), ('price', int)])
T_restaurants = list[RestaurantsTuple]

def ordered_suggestions(restaurants: T_restaurants, max_price: int) -> list[str]:
    """"
        Description:
            Suppose that you have a list of restaurants where each one is represented by a tuple of (restaurant name, rating, distance, price). So an example list would be:
            restaurants = [RestaurantsTuple("Bistro Fibonacci", 5, 1000, 50),
                RestaurantsTuple("Chez Germaine", 4, 800, 80),
                RestaurantsTuple("Das Bayerische Haus", 4, 1200, 50),
                RestaurantsTuple("Cantina del Piero", 5, 500, 60),
                RestaurantsTuple("Peking Wok", 3, 700, 25),
                RestaurantsTuple("Shokudo Ramen", 4, 1200, 30)]

        returns a list of the names of the restaurants below a given max_price. That list should be in 
        decreasing order of rating of the restaurant, and for restaurants with the same rating 
        the ones closer should appear first (increasing order of distance).
        
        E.g 
        >>> restaurants = [RestaurantsTuple("Bistro Fibonacci", 5, 1000, 50), RestaurantsTuple("Chez Germaine", 4, 800, 80), RestaurantsTuple("Das Bayerische Haus", 4, 1200, 50), RestaurantsTuple("Cantina del Piero", 5, 500, 60), RestaurantsTuple("Peking Wok", 3, 700, 25), RestaurantsTuple("Shokudo Ramen", 4, 1200, 30)]
        >>> ordered_suggestions(restaurants, 70) == ['Cantina del Piero', 'Bistro Fibonacci', 'Das Bayerische Haus', 'Shokudo Ramen', 'Peking Wok']
        True
    """
    filtered_restaurants = [restaurant for restaurant in restaurants if restaurant.price < max_price]
    sorted_restaurants = _sort_restaurants(filtered_restaurants)
    return [restaurant.restaurant_name for restaurant in sorted_restaurants]

def _sort_restaurants(restaurants: T_restaurants) -> T_restaurants:
    """"
        Description sort list based on the following rule:  
            That list should be in 
            decreasing order of rating of the restaurant, and for restaurants with the same rating 
            the ones closer should appear first (increasing order of distance)
        by maintaining the immutability of the original function 
        >>> restaurants = [RestaurantsTuple("Bistro Fibonacci", 5, 1000, 50),RestaurantsTuple("Chez Germaine", 4, 800, 80),RestaurantsTuple("Das Bayerische Haus", 4, 1200, 50),RestaurantsTuple("Cantina del Piero", 5, 500, 60),RestaurantsTuple("Peking Wok", 3, 700, 25),RestaurantsTuple("Shokudo Ramen", 4, 1200, 30)]
        >>> _sort_restaurants(restaurants) == [("Cantina del Piero", 5, 500, 60), ("Bistro Fibonacci", 5, 1000, 50), ("Chez Germaine", 4, 800, 80),  ("Das Bayerische Haus", 4, 1200, 50), ("Shokudo Ramen", 4, 1200, 30), ("Peking Wok", 3, 700, 25)]
        True
    """
    return sorted(restaurants, key=lambda restaurant: (-restaurant.rating, restaurant.distance))
    

if __name__ == '__main__':
    restaurants = [RestaurantsTuple("Bistro Fibonacci", 5, 1000, 50),
    RestaurantsTuple("Chez Germaine", 4, 800, 80),
    RestaurantsTuple("Das Bayerische Haus", 4, 1200, 50),
    RestaurantsTuple("Cantina del Piero", 5, 500, 60),
    RestaurantsTuple("Peking Wok", 3, 700, 25),
    RestaurantsTuple("Shokudo Ramen", 4, 1200, 30)]
    sort_expected = [("Cantina del Piero", 5, 500, 60), ("Bistro Fibonacci", 5, 1000, 50), ("Chez Germaine", 4, 800, 80),  ("Das Bayerische Haus", 4, 1200, 50), ("Shokudo Ramen", 4, 1200, 30), ("Peking Wok", 3, 700, 25)]
    sort_response = _sort_restaurants(restaurants)
    assert sort_expected == sort_response, f"expected {sort_expected}, but got {sort_response}"
    ordered_expected = ['Cantina del Piero', 'Bistro Fibonacci', 'Das Bayerische Haus', 'Shokudo Ramen', 'Peking Wok']
    ordered_response = ordered_suggestions(restaurants, 70)
    assert ordered_expected == ordered_response, f"expected {ordered_expected}, but got {ordered_response}"