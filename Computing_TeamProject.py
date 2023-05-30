Menu_Archive = {
    "브리또" : ["돼지고기","양파","피망"],
    "정진교" : ["안경","노트북"]
}

'''
'Menu_Archive'라는 딕셔너리 생성

딕셔너리란?
key - velue 쌍으로 데이터를 저장하는 자료구조. 
'''

def Recommended_Menu(User_Input_Ingredient) :
    Recommended_Menu_List = []
    # 'User Inputed Menu'라는 함수 정의
    '''
    User_Input_Ingerdient 라는 매개변수 생성

    매개변수란?
    함수 정의시 사용하는 변수, 함수가 호출될때 외부에서 값을 받음.
    ex) def 짱구(상태) :
            print("짱구",상태,"입니다.")
    짱구(무야호)
    짱구(짱구는 못말려)
    
    출력값: 
    짱구 무야호 입니다.
    짱구 짱구는못말려 입니다.
    '''
    for Menu, Ingredients in Menu_Archive.items():
        #.item:딕셔너리의 key:value 반환
        #여기서는 meuu와 ingredient에 각각 key와 value 넣어줌.
        if all(Ingredient in Ingredients for Ingredient in User_Input_Ingredient):
            Recommended_Menu_List.append(Menu)
        # all() 함수 : 주어진 iterable(리스트,튜블 등등)의 모든 요소가 참인지?
        #.append:리스트의 끝에 값 추가
        '''
        해석:일단 'User_Input_Ingredient' 값을 변수'Ingredient'에 넣으시고
        'Ingredient 가 Ingredients에 있으면 리스트에 메뉴를 추가해라.
        '''

