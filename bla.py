from api.serializers import ForeclosureSerializer

def update_list(some_list):
    for d in some_list:
        d["name"] = d["defendant"]["name"]
        for k, v in d.items():
            print(k)


            if k == "sale_date":
                s = d[k]
                list_of_parts = s.split("/")
                for index, part in enumerate(list_of_parts):
                    if len(part) == 1:
                        list_of_parts[index] = "0" + list_of_parts[index]
                new_list = [list_of_parts[2], list_of_parts[0], list_of_parts[1]]
                new_string = "-".join(new_list)
                d[k] = new_string
            elif k == "foreclosure_history":
                for forclosure in v:
                    for key, val in forclosure.items():
                        if key == "date":
                            st = forclosure[key]
                            list_of_parts = st.split("/")
                            print(list_of_parts)
                            for index, part in enumerate(list_of_parts):
                                if len(part) == 1:
                                    list_of_parts[index] = "0" + list_of_parts[index]
                            print(list_of_parts)
                            new_list = [list_of_parts[2], list_of_parts[0], list_of_parts[1]]
                            new_string = "-".join(new_list)
                            forclosure[key] = new_string
    return some_list

def do_it(l):
    for i in update_list(l):
        f= ForeclosureSerializer(data=i)
        if f.is_valid():
            f.save()
        else:
            print(f.errors)