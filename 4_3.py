# error exception
# try:
#     # with open('f.txt','r') as f:
#     #     for line in f:
#     #         x = int(line.strip())
#     x = 5
# except FileNotFoundError as err:
#     print('沒有檔案',err)
# except ValueError:
#     print('資料錯誤')
# else:
#     print('沒有錯誤')
# finally:
#     print('不管有沒有錯最後定會執行')



# try:
#     s = input('enter a number:')
#     n = int(s)
# except ValueError:
#     print('只能輸入數字')
# except NameError:
#     print('名子錯誤')

err_count = 0
i = 0
while True:
    try:
        s = input('enter a number:')
        n = int(s)
    except ValueError:
        err_count +=1
        if err_count >= 3:
            print('已經三次了')
            break
        print('錯了')        
    finally:
        i=i+1
        print(f'這是第{i}次玩')








