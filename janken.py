import random

def int2hand(i: int) -> str:
    if i == 1:
        return 'グー'
    if i == 2:
        return 'チョキ'
    if i == 3:
        return 'パー'

def judge(user: int, computer: int) -> str:
    diff = user - computer
    if diff % 3 == 2:
        return 'user'
    if diff % 3 == 1:
        return 'computer'
    else:
        return 'draw'


def janken():
    print('＜＜＜じゃんけんをしましょう！＞＞＞')
    print('以下から出す手を選んでください')
    print('グー:1 / チョキ:2 / パー:3')

#コンピュータがランダムに手を出す
    rnd = random.randrange(1, 4, 1)

#1~3以外をユーザーが出した時の処理   
    while True:
        user_input = input('じゃんけん...')
        try:
            user = int(user_input)
        except Exception:
            print("入力が不正です。1~3の整数を入力してください。")
            continue

        if user not in (1, 2, 3):
            print('間違っています。1~3の数字を入力してください。')
            continue

        print(f"あなたの手: {int2hand(user)}")
        print(f"コンピュータの手: {int2hand(rnd)}")

        if judge(user=user, computer=rnd) == 'user':
            print("あなたの勝ち")
            break

        if judge(user=user, computer=rnd) == 'computer':
            print("コンピュータの勝ち")
            break

        if judge(user=user, computer=rnd) == 'draw':
            print("あいこです。もう一回。")
            continue

        # if user == 1:
        #     if rnd == 1:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。もう一度じゃんけんしましょう。')
        #     elif rnd == 2:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの勝ちです。')
        #         break
        #     elif rnd == 3:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの負けです。')
        #         break
        
        # if user == 2:
        #     if rnd == 2:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。もう一度じゃんけんしましょう。')
        #     elif rnd == 3:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの勝ちです。')
        #         break
        #     elif rnd == 1:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの負けです。')
        #         break
        
        # if user == 3:
        #     if rnd == 3:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。もう一度じゃんけんしましょう。')
        #     elif rnd == 2:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの勝ちです。')
        #         break
        #     elif rnd == 1:
        #         print(f'コンピュータは{int2hand(rnd)}を出しました。あなたの負けです。')
        #         break
                
if __name__ == '__main__':
    janken()
