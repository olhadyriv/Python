a = {
    "data": {
        "id": 23172,
        "email": "var.byte.aqa@gmail.com",
        "locale": "en",
        "confirmed": 1,
        "tester": True,
        "corporate": True,
        "payments": [
            {
                "id": 83085,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2023-08-10T07:26:07+00:00"
            },
            {
                "id": 7987,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2022-09-21T09:13:08+00:00"
            },
            {
                "id": 7986,
                "gateway_key": "btc",
                "status": 5,
                "amount": "9.99",
                "currency": "USD",
                "created_at": "2022-09-21T09:11:11+00:00"
            },
            {
                "id": 7985,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2022-09-21T09:09:08+00:00"
            },
            {
                "id": 7984,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2022-09-21T09:09:08+00:00"
            },
            {
                "id": 7983,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2022-09-21T09:09:07+00:00"
            },
            {
                "id": 7981,
                "gateway_key": "btc",
                "status": 5,
                "amount": "95.55",
                "currency": "USD",
                "created_at": "2022-09-21T09:06:09+00:00"
            }
        ],
        "allow_config_page": True,
        "access": {
            "id": 105806,
            "type": "premium",
            "ends_at": "2024-07-01T00:00:00+00:00",
            "days_left": 132,
            "subscription": None
        }
    }
}
new_list = a.copy()

for ids in a["data"]["payments"]:
    print(ids["id"])

copy_dict = a.copy()
del a["data"]["payments"]
print(copy_dict)

copy_dict = a.copy()
a["data"]["access"]["type"] = "free"
print(copy_dict)

a["data"]["payments"] = [
    {
        "id": 83085,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2023-08-10T07:26:07+00:00"
    },
    {
        "id": 7987,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2022-09-21T09:13:08+00:00"
    },
    {
        "id": 7986,
        "gateway_key": "btc",
        "status": 5,
        "amount": "9.99",
        "currency": "USD",
        "created_at": "2022-09-21T09:11:11+00:00"
    },
    {
        "id": 7985,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2022-09-21T09:09:08+00:00"
    },
    {
        "id": 7984,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2022-09-21T09:09:08+00:00"
    },
    {
        "id": 7983,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2022-09-21T09:09:07+00:00"
    },
    {
        "id": 7981,
        "gateway_key": "btc",
        "status": 5,
        "amount": "95.55",
        "currency": "USD",
        "created_at": "2022-09-21T09:06:09+00:00"
    }
]

new_list = ["e-mail:" + str(a["data"]["email"]), "tester: " + str(a["data"]["tester"]), "payments:" + str(a["data"]
                                                                                                          ["payments"])]
print(new_list)
