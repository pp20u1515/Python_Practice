

def check(i,j):
	if(str_[i]=="(" and str_[j]==")"):
		return 1
	if(str_[i]=="(" and str_[j]=="?"):
		return 1
	if(str_[i]=="?" and str_[j]==")"):
		return 1
	if(str_[i]=="?" and str_[j]=="?"):
		return 1
	return 0

def count(start,end):
	sum=0
	if(start>end):
		return 1
	if(dp[start][end]!=-1):
		return dp[start][end]
	for i in range(start+1,end+1,2):
		if(check(start,i)):
			sum+=count(start+1,i-1)*count(i+1,end)
	dp[start][end]=sum
	return dp[start][end]





str_ = None
while str_ != "0":

    print("Пожалуйста, введите выражение, используя символы '?', '(', и ')'.")
    print("Выведите '0' для выхода из программы")
    str_ = input("Ваше выражение: ")                    # Ввод выражения
    l = len(str_)
    dp=[[-1 for i in range(l)] for i in range(l)]       # мы создаем матрицу размера (len(выражение) X len(выражение))

    if str_ == "0":
        print("Выход из программы")
        break

    list_ = list(str_)
    possible_close = 0                                  # Параметры для количества возможных закрывающих скобок

    all_sympols = True                                         # Чтобы проверить правильность всех используемых символов
    for c in list_:
        if c == "?" or c == ")":
            possible_close += 1
        elif c == "(":
            possible_close -= 1
        else:
            all_sympols = False
            break
    
    if not all_sympols:
        print("\nСимволы, которые вы использовали, неверны!")
        print("Пожалуйста, попробуйте еще раз.\n")
        continue

    n=len(str_)
    if n%2!=0:
        print(0)
    else:
        res = count(0,n-1)



    # res, poss = Calc_num(list_, 0, possible_close, "")
    print("Количество различных комбинаций: ", res)
    # print("\nРазличные комбинации:")
    # print(poss)
    print("\n")
