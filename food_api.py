from abc import ABC, abstractmethod
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# File Login


def load_users_from_file():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users


def save_user_to_file(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")


users_db = load_users_from_file()

#  OOp Classes

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu


class FoodOrder:
    def __init__(self, order_id, username, restaurant):
        self.order_id = order_id
        self.username = username
        self.restaurant = restaurant
        self.items = []
        self.total_amount = 0
        self.status = "CREATED"

    def add_food_item(self, item_name, quantity):
        if item_name not in self.restaurant.menu:
            return False

        price, food_type = self.restaurant.menu[item_name]
        item_total = price * quantity

        self.items.append({
            "name": item_name,
            "qty": quantity,
            "unit_price": price,
            "type": food_type,
            "item_total": item_total
        })

        self.total_amount += item_total
        return True


# Payment Types

class PaymentMethod(ABC):
    @abstractmethod
    def pay_bill(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay_bill(self, amount):
        return f"Paid {amount} using CARD"


class UPIPayment(PaymentMethod):
    def pay_bill(self, amount):
        return f"Paid {amount} using UPI"


class CashPayment(PaymentMethod):
    def pay_bill(self, amount):
        return f"Paid {amount} using CASH"



#  Data Storage


restaurants = {
    1: Restaurant("Spicy Hub", {
        "burger": (120, "nonveg"),
        "pizza": (200, "veg"),
        "salad": (90, "veg")
    }),
    2: Restaurant("Green Bowl", {
        "paneer": (180, "veg"),
        "tofu": (150, "veg"),
        "wrap": (130, "veg")
    })
}

all_orders = {}
next_order_id = 1


#  Pydantic Models


class RegisterModel(BaseModel):
    username: str
    password: str


class LoginModel(BaseModel):
    username: str
    password: str


class OrderItemModel(BaseModel):
    item: str
    qty: int


class OrderCreateModel(BaseModel):
    username: str
    restaurant_id: int
    items: List[OrderItemModel]
    payment: str



#  Home


@app.get("/")
async def api_home():
    return {
        "message": "Food Order FastAPI running"
        
    }


#  APIs

@app.post("/register")
async def register_user(data: RegisterModel):
    if data.username in users_db:
        raise HTTPException(400, "User exists")

    users_db[data.username] = data.password
    save_user_to_file(data.username, data.password)

    return {"message": "Registered successfully"}


@app.post("/login")
async def login_user(data: LoginModel):
    if not users_db:
        raise HTTPException(400, "No users registered")

    if users_db.get(data.username) == data.password:
        return {"message": "Login success"}

    raise HTTPException(401, "Invalid username or password")


# Restaurants

@app.get("/restaurants")
async def get_restaurants():
    return [
        {"restaurant_id": rid, "name": r.name}
        for rid, r in restaurants.items()
    ]


@app.get("/restaurants/{restaurant_id}/menu")
async def get_menu(restaurant_id: int, type: Optional[str] = None):
    restaurant = restaurants.get(restaurant_id)
    if not restaurant:
        raise HTTPException(404, "Restaurant not found")

    menu = []

    for item_name, (price, food_type) in restaurant.menu.items():
        if type and food_type != type:
            continue

        menu.append({
            "item": item_name,
            "price": price,
            "type": food_type
        })

    return menu



#  Orders

@app.post("/orders")
async def create_food_order(order_data: OrderCreateModel):
    global next_order_id

    if order_data.username not in users_db:
        raise HTTPException(401, "Login required")

    restaurant = restaurants.get(order_data.restaurant_id)
    if not restaurant:
        raise HTTPException(404, "Invalid restaurant")

    order = FoodOrder(next_order_id, order_data.username, restaurant)

    for item in order_data.items:
        ok = order.add_food_item(item.item, item.qty)
        if not ok:
            raise HTTPException(400, f"{item.item} not available")

    if order_data.payment == "card":
        payment = CardPayment()
    elif order_data.payment == "upi":
        payment = UPIPayment()
    else:
        payment = CashPayment()

    payment_msg = payment.pay_bill(order.total_amount)
    order.status = "PAID"

    all_orders[next_order_id] = order
    next_order_id += 1

    return {
        "order_id": order.order_id,
        "status": order.status,
        "bill_total": order.total_amount,
        "payment": payment_msg,
        "items": order.items
    }


@app.get("/orders")
async def list_orders():
    return [
        {
            "order_id": o.order_id,
            "user": o.username,
            "restaurant": o.restaurant.name,
            "total": o.total_amount,
            "status": o.status
        }
        for o in all_orders.values()
    ]


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    if order_id not in all_orders:
        raise HTTPException(404, "Order not found")

    del all_orders[order_id]
    return {"message": "Order deleted"}
