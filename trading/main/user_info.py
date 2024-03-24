
def info():
    type=input()
    if type.lower() =='инвестор':
        periods =input('Выберите таймфрейд:день неделя месяц квартал ')
        if periods.lower()=='день':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =24
            n=0
            return data_start,data_end,interval,n
        if periods.lower()=='неделя':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =7
            n=0
            return data_start,data_end,interval,n
        if periods.lower()=='месяц':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =31
            n=0
            return data_start,data_end,interval,n
        if periods.lower()=='квартал':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =4
            n=0
            return data_start,data_end,interval,n
                
               
            
    if type.lower()=='трейдер':
        periods =input('Выберите таймфрейд: минута десять час день ')
        if periods.lower()=='минута':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =1
            n1=1
            return data_start,data_end,interval,n1
        if periods.lower()=='десять':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =10
            n1=1
            return data_start,data_end,interval,n1
        if periods.lower()=='час':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =60
            n1=1
            return data_start,data_end,interval,n1
        if periods.lower()=='день':
            data_start=input('введите дату с которой хотите насчать просмотр(год-месяц-день) ')
            data_end=input('введите дату до которой нужен график (год-месяц-день) ')
            interval =24
            n1=1
            return data_start,data_end,interval,n1
           
            

    
   
        

    
    
