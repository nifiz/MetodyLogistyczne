import random

def DK(i, zakres):
    percentages = [23, 61, 100]

    if i > zakres:
        i = zakres
    decider = random.randint(1, 100)

    if decider <= percentages[0]:
        alfa = random.randint(16000, i)
        # if abs(i - alfa) < 1000:
        #     return i
        # else:
        return alfa
    elif decider <= percentages[1] and i > 20000:
        alfa = random.randint(20000, i)
        # if abs(i - alfa) < 1000:
        #     return i
        # else:
        return alfa
    elif decider <= percentages[2] and i > 25000:
        alfa = random.randint(25000, i)
        # if abs(i - alfa) < 1000:
        #     return i
        # else:
        return alfa
    else:
        return random.randint(16000, i)


def TOTAL(days):
    percentages = [4, 100]

    results = {}

    zero_percentages = [23, 29, 81, 100]


    for i in range(days):
        decider = random.randint(1,100)

        if decider <= percentages[0]:
            results[i+1] = [{'TOTAL' : random.randint(17000, 30001)}]
            results[i+1].append({'ULG95' : 0})
            results[i+1].append({'DK' : results[i+1][0]['TOTAL']})
            results[i+1].append({'ULTSU': 0})
            results[i+1].append({'ULTDK': 0})

        else:
            total = random.randint(30001, 36001)
            results[i+1] = [{'TOTAL' : total}]
            decider_zero = random.randint(1,100)
            if decider_zero <= zero_percentages[0]:
                results[i + 1].append({'ULG95': 0})
                results[i + 1].append({'DK': results[i + 1][0]['TOTAL']})
                results[i + 1].append({'ULTSU': 0})
                results[i + 1].append({'ULTDK': 0})

            elif decider_zero <= zero_percentages[1]:
                zero_one = random.choice(['ULG95', 'ULTSU', 'ULTDK'])
                oil = results[i + 1][0]['TOTAL']
                dkvalue = DK(25000, oil)
                if zero_one == 'ULG95':
                    results[i + 1].append({'ULG95': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULTSU': random.randint(1000, (oil - dkvalue)//2)})
                    results[i + 1].append({'ULTDK': oil - dkvalue - results[i + 1][3]['ULTSU']})
                elif zero_one == 'ULTSU':
                    results[i + 1].append({'ULTSU': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULG95': random.randint(1000, (oil - dkvalue)//2)})
                    results[i + 1].append({'ULTDK': oil - dkvalue - results[i + 1][3]['ULG95']})
                elif zero_one == 'ULTDK':
                    results[i + 1].append({'ULTDK': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULG95': random.randint(1000, (oil - dkvalue)//2)})
                    results[i + 1].append({'ULTSU': oil - dkvalue - results[i + 1][3]['ULG95']})

            elif decider_zero <= zero_percentages[2]:
                zero_one = random.sample(['ULG95', 'ULTSU', 'ULTDK'], 2)
                oil = results[i + 1][0]['TOTAL']
                dkvalue = DK(32000, oil)
                if 'ULG95' and 'ULTSU' in zero_one:
                    results[i + 1].append({'ULG95': 0})
                    results[i + 1].append({'ULTSU': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULTDK': oil - dkvalue})
                elif 'ULG95' and 'ULTDK' in zero_one:
                    results[i + 1].append({'ULG95': 0})
                    results[i + 1].append({'ULTDK': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULTSU': oil - dkvalue})
                else:
                    results[i + 1].append({'ULTSU': 0})
                    results[i + 1].append({'ULTDK': 0})
                    results[i + 1].append({'DK': dkvalue})
                    results[i + 1].append({'ULG95': oil - dkvalue})
            else:
                oil = results[i + 1][0]['TOTAL']
                dkvalue = DK(22000, oil)
                results[i + 1].append({'DK': dkvalue})
                results[i + 1].append({'ULG95': random.randint(1000, (oil - dkvalue) // 2)})
                results[i + 1].append({'ULTDK': (oil - dkvalue) // 3})
                results[i + 1].append({'ULTSU': oil - dkvalue - results[i + 1][2]['ULG95'] - results[i + 1][3]['ULTDK']})

    return results


