with open('Day02/input.txt') as file:
    safecount = 0
    for line in file:
        prev = 0
        unsafe = False
        inc = None
        for report in line.split():
            report = int(report)
            if prev == 0:
                print(report, prev, 'prev = 0')
                prev = report
            else:
                if prev == report: #equal case
                    print(report, prev, 'equal')
                    unsafe = True
                    break
                if prev < report: #increasing case
                    if inc == False:
                        print(report, prev, 'increase after decrease')
                        unsafe = 1
                        break
                    inc = True
                    if report - prev > 3: #increasing too much
                        print(report, prev, 'inc too much')
                        unsafe = True
                        break
                    else:
                        print(report, prev, 'inc fine')
                        prev = report
                if prev > report: #decreasing case
                    if inc == True:
                        print(report, prev, 'dec after inc')
                        unsafe = 1
                        break
                    inc = False
                    if prev - report > 3: #decreasing too much
                        print(report, prev, 'dec too much')
                        unsafe = 1
                        break
                    else:
                        print(report, prev, 'dec fine')
                        prev = report
            if unsafe:
                break
        if not unsafe:
            print('SAFE')
            safecount += 1
    print(safecount)

                        

