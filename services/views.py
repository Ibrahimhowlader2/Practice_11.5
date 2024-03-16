from django.shortcuts import render

# Create your views here.


def index(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "price": "$5.99",
            "rating": "4.5/5",
            "desc": "A Canadian pastry treat shaped like a beaver's tail, typically topped with various sweet toppings like cinnamon sugar, chocolate, or fruit."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "price": "$6.49",
            "rating": "4.2/5",
            "desc": "Crispy and seasoned potatoes served as a classic breakfast side dish."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "price": "$4.99",
            "rating": "4.7/5",
            "desc": "Sweet pastry tart filled with a rich, gooey mixture of butter, sugar, syrup, and egg."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "price": "$8.99",
            "rating": "4.6/5",
            "desc": "A type of kosher-style deli meat made by curing and smoking beef brisket with a blend of spices."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "price": "$3.99",
            "rating": "4.8/5",
            "desc": "Layered dessert bars consisting of a crumbly base, custard-flavored middle layer, and chocolate topping."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "price": "$7.49",
            "rating": "4.3/5",
            "desc": "A French-Canadian dish similar to shepherd's pie, made with layers of ground beef, corn, and mashed potatoes."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "price": "$5.99",
            "rating": "4.5/5",
            "desc": "A traditional Quebecois dessert made with a cake-like batter soaked in a rich maple syrup sauce."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "price": "$9.99",
            "rating": "4.9/5",
            "desc": "A Canadian dish consisting of fries topped with cheese curds and smothered in gravy."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "price": "$10.99",
            "rating": "4.4/5",
            "desc": "A traditional Acadian dish from Eastern Canada made with grated potatoes, meat (usually chicken or pork), and onions."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "price": "$6.99",
            "rating": "4.2/5",
            "desc": "A hearty soup made from dried split peas, often flavored with ham or bacon."
        }
    ]
    return render(request,'services/index.html',context={"meals": meals})

def about(request):
    return render(request,'services/about.html')

def menu(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "price": "$5.99",
            "rating": "4.5/5",
            "desc": "A Canadian pastry treat shaped like a beaver's tail, typically topped with various sweet toppings like cinnamon sugar, chocolate, or fruit."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "price": "$6.49",
            "rating": "4.2/5",
            "desc": "Crispy and seasoned potatoes served as a classic breakfast side dish."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "price": "$4.99",
            "rating": "4.7/5",
            "desc": "Sweet pastry tart filled with a rich, gooey mixture of butter, sugar, syrup, and egg."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "price": "$8.99",
            "rating": "4.6/5",
            "desc": "A type of kosher-style deli meat made by curing and smoking beef brisket with a blend of spices."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "price": "$3.99",
            "rating": "4.8/5",
            "desc": "Layered dessert bars consisting of a crumbly base, custard-flavored middle layer, and chocolate topping."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "price": "$7.49",
            "rating": "4.3/5",
            "desc": "A French-Canadian dish similar to shepherd's pie, made with layers of ground beef, corn, and mashed potatoes."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "price": "$5.99",
            "rating": "4.5/5",
            "desc": "A traditional Quebecois dessert made with a cake-like batter soaked in a rich maple syrup sauce."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "price": "$9.99",
            "rating": "4.9/5",
            "desc": "A Canadian dish consisting of fries topped with cheese curds and smothered in gravy."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "price": "$10.99",
            "rating": "4.4/5",
            "desc": "A traditional Acadian dish from Eastern Canada made with grated potatoes, meat (usually chicken or pork), and onions."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "price": "$6.99",
            "rating": "4.2/5",
            "desc": "A hearty soup made from dried split peas, often flavored with ham or bacon."
        }
    ]
    return render(request,'services/menu.html',context={"meals": meals})
