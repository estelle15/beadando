def tizes_szamrendszerbe():

    if y == 11 or y == 12 or y == 13 or y == 14 or y == 15 or y == 16:
        x_ketto = []
        for i in x:
            if i == 'A':
                x_ketto.append('10')
            elif i == 'B':
                x_ketto.append('11')
            elif i == 'C':
                x_ketto.append('12')
            elif i == 'D':
                x_ketto.append('13')
            elif i == 'E':
                x_ketto.append('14')
            elif i == 'F':
                x_ketto.append('15')
            else:
                x_ketto.append(i)

        s = x_ketto[::-1]
        m_tiz = 0
        a = 0
        for j in s:
            m_tiz += int(j)*(y**a)
            a += 1
        return m_tiz

 
  
