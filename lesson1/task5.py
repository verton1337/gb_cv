def depo(qty, mnth, pay):
    if mnth >= 6 and mnth < 12:
        bet = 6
    elif mnth>=12 and mnth < 24:
        bet = 12
    elif mnth > 24:
        bet = 24
    else:
        return "Срок вклада слишком мал"

    result = qty

    recs = [
        {"min": 1000,
         "max": 10000,
         6: 5,
         12: 6,
         24: 5,
         },
         
        {"min": 10000,
         "max": 100000,
         6: 6,
         12: 7,
         24: 6.5,
         },

        {"min": 100000,
         "max": 1000000,
         6: 7,
         12: 8,
         24: 7.5,
         }
        ]
    for i in range(len(recs)):
        if qty>= recs[i]["min"] and qty<recs[i]["max"]:
            for j in range(1, mnth+1):

                result +=  result * recs[i][bet]/100 / 12 #средства на вкладе * годовая ставка / 12 месяцев
                if j > 1 and j < mnth:
                    result+=pay

    return result


if __name__ == "__main__":
    print(depo(150000, 12, 10000))
