import json
full_object="""{
    "obj":[
    {
        "lake":{
            "img":"lake.PNG",
            "terrain":[[1,1,1],[1,1,1]]
        }
    },
    {
        "wiotrok":{
            "img":"wiotrok.gif",
            "terrain":[[0,0,0],[0,0,2]]
        }
    }
]
}
"""
my_list=json.loads(full_object)
print(my_list)