def get_login_name(first, last, id):
       if len(first) > 3:
              firstpart = (first[0:3])
       else:
              firstpart = first
              
       if len(last) > 3:
              lastpart = (last[0:3])
       else:
              lastpart = last
       
       if len(id) > 3:
              idpart = id[-3:]
       else:
              idpart = id
       
       username = (f"{firstpart}{lastpart}{idpart}")
       return username

def main():
       first = str("Amanda")
       last = str("Huckleberry")
       id = str("TEK5023")

       username = get_login_name(first, last, id)
       print(username)

main()