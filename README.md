# Assignment 4 – FastAPI Implementation

This project implements a simple FastAPI application for Software Engineering Assignment 4.  
It includes two parts:

---

## Part 1 – Basic FastAPI Endpoints

The initial version of the API includes:

- `GET /` – returns a simple JSON message.
- `GET /items/{item_id}` – returns an item ID and optional query parameter.

To run the server:

---

## Part 2 – PUT Request with Pydantic Model

A Pydantic `Item` model was added, along with a `PUT /items/{item_id}` endpoint that accepts a JSON body.

Example body:

```json
{
  "name": "Laptop",
  "price": 999.99,
  "is_offer": true
}