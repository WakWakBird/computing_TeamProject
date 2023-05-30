menuArchive = {   #'Menu_Archive 라는 딕셔너리를 생성후 '음식' 딕셔너리 중첩.
    "스테이크": { #'음식' 딕셔너리 안에 '재료' 리스트와 '레시피' 문자열 생성.
        "재료": ["소고기", "소금", "후추"],
        "레시피": "스테이크 레시피입니다."
    },
    "스파게티": {
        "재료": ["면", "토마토소스", "고기", "야채"],
        "레시피": "스파게티 레시피입니다."
    },
    "샐러드": {
        "재료": ["상추", "토마토", "양파", "드레싱"],
        "레시피": "샐러드 레시피입니다."
    },
    "피자": {
        "재료": ["밀가루", "토마토소스", "치즈", "토핑"],
        "레시피": "피자 레시피입니다."
    },
    "스시": {
        "재료": ["생선", "쌀", "미역", "간장"],
        "레시피": "스시 레시피입니다."
    },
    "라면": {
        "재료": ["면", "스프", "계란", "고기"],
        "레시피": "라면 레시피입니다."
    },
     "김밥": {  
        "재료": ["김", "밥", "단무지", "참치캔", "당근", "계란", "맛술", "참기름", "소금"],
        "레시피": "김밥 레시피입니다."
    }
  
}

'''
딕셔너리란?
key - velue 쌍으로 데이터를 저장하는 자료구조임.
중괄호를 사용함니당.
'''

def recommendedMenu(userInputIngredients): #'recommendedMenu라는 함수 정의 후 'userInputIngredients라는 매개변수 생성.
    recommendedMenuList = []# 우리가 선택한 재료가 들어가는 메뉴를 저장할 빈 리스트 생성
    for menu, info in menuArchive.items(): #'menu','info' 라는 변수 생성 후 '.items'()를 이용해 'menuArchive'의 Key : Value값을 각각 'menu'와'info'에 할당
        ingredients = info["재료"] #ingredients의 값을 info 중 ["재료"] 리스트로 한정. (유저를 통해 입력받은 값이 재료 리스트에 들어있나 확인하기 위함)
        if all(ingredient in ingredients for ingredient in userInputIngredients):# 'all'함수 : all안에 있는 값이 참이면 조건 실행.
        #ingredient 라는 변수 생성후 for문을 통해 그 안에 userInputIngredients값을 넣는다. ingredients 안에 ingredient가 있으면  조건 실행
            recommendedMenuList.append((menu, ingredients, info["레시피"]))
            '''.append : 리스트에 단일 인자를 추가함. 그러니까 여기서는 menu,ingredients,info["레시피"] 라는 단일 인자들을 recommenedeMenuList에 추가하는 것.
            '''
    return recommendedMenuList #return으로 함수 결과값 호출

    '''
    매개변수란?
    함수 정의시 사용하는 변수, 함수가 호출될때 외부에서 값을 받음.
    ex) def 짱구(상태) :
            print("짱구",상태,"입니다.")
    짱구(무야호)
    짱구(짱구는 못말려)
    
    출력값: 
    짱구 무야호 입니다.
    짱구 짱구는못말려 입니다
    '''

while True: # 루프가 항상 실행되게 해용. 이렇게 하면 특정 조건이 성립될때까지 항상 프로그램이 돌아가게 할수 있음.
    inputIngredients = [] #우리가 입력한 재료들을 저장할 리스트임미다요. 빈 리스트를 만들었어요.
    userInputIngredients = input("사용할 재료를 입력하세요 (공백으로 구분): ").split() 
    #아까 매개변수를 선언했었죠?(39번줄에서) 이 변수안에 input으로 입력받은 값들을 받습니다.
    '''
    .spilt() : 공백을 기준으로 분리하여 리스트로 반환해요. 문자열 매서드죠.
    '''
    inputIngredients.extend(userInputIngredients) #.extend를 이용해서 방금 만든 리스트에 넣습니다. 합니다. (사용자가 한번에 여러가지 재료를 입력할수도 있으니까)
    '''
    .extend : 아까 .append와 비슷한 녀석인데 각 요소들을 개별적으로 추가하는거에요.
    당연히 split를 통해 값을 리스트로 반환받을 수 있으니까 inputIngredients 리스트에 각각의 값을 추가해줘야겠죠?
    '''
    recommendedMenuList = recommendedMenu(inputIngredients) 
    #아까 매개변수 기억나죠? recommendMenu함수가 inputIngredients를 인자로 받아서 여기에 해당하는 메뉴를 recommendedMuntList에 저장하는 거에용. 
    
    if len(recommendedMenuList) == 0: #만약 문자열의 개수? 그냥 개수라고 할게요 즉, recommendedMunuList에 추천된 메뉴가 하나도 없으면? -> 다시입력하세요
        print("그런 재료를 포함하는 메뉴는 없습니다.\n다시 입력하세요!")
        inputIngredients = [] # 잘못된 재료를 입력했다면 재료 리스트를 초기화 시킵니다.
        continue
        
    elif len(recommendedMenuList) <= 3: # 문자열 개수가 3보다 작으면 아래 내용들을 출력해요.
        for menu, ingredients, recipe in recommendedMenuList:
            print("음식 이름:", menu)
            print("재료:", ", ".join(ingredients))
            print("레시피:", recipe)
        break
    
    else: 
        print("추천 메뉴가 너무 많습니다. 구체적으로 입력하세요!")
  



   
