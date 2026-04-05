# travel_log = {
#     "France" : ["Paris" , "Lille" , " Djion"],
#     "Germany" : ["Berlin" , "Frankfurt"]
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France" : {
        "num_times_visited": 8,
        "citites_visited": ["Paris" , "Lille" , " Djion"]
    },
    "Germany" : {
        "cities_visited" : ["Berlin" , "Frankfurt", "Hamburg"],
        "total_visits" : 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])