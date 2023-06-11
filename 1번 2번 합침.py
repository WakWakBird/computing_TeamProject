menuArchive = {
    "스파게티": {
        "재료": ["스파게티 면", "토마토 소스", "양파", "마늘", "소고기", "파마산 치즈"],
        "순서": [
            "1. 양파와 마늘을 다져서 볼에 넣는다.",
            "2. 스파게티 면을 끓는 물에 삶는다.",
            "3. 볼에 있는 양파와 마늘을 팬에 볶는다.",
            "4. 소고기를 넣고 익힌다.",
            "5. 토마토 소스를 넣고 조리한다.",
            "6. 삶은 스파게티 면과 소스를 섞는다.",
            "7. 파마산 치즈를 곁들여 완성한다."
        ]
    },
    "초밥": {
        "재료": ["초밥용 밥", "생선 (참치, 연어 등)", "김", "식초", "간장", "와사비"],
        "순서": [
            "1. 초밥용 밥을 준비한다.",
            "2. 식초와 설탕을 섞어 간장을 만든다.",
            "3. 초밥용 밥에 간장을 조금 뿌린다.",
            "4. 생선을 얇게 썰어 준비한다.",
            "5. 김을 한 장씩 꺼내어 생선과 밥을 싸맨다.",
            "6. 와사비와 간장을 곁들여 완성한다."
        ]
    },
    # 다른 레시피도 추가할 수 있습니다.
}

def addRecipe(recipeName, ingredients, steps):
    menuArchive[recipeName] = {
        "재료": ingredients,
        "순서": steps
    }

def printRecipe(recipeName):
    if recipeName in menuArchive:
        recipe = menuArchive[recipeName]
        print(f"{recipeName} 레시피")
        print("재료:")
        for ingredient in recipe["재료"]:
            print("- " + ingredient)
        print("순서:")
        for step in recipe["순서"]:
            print(step)
    else:
        print("해당하는 레시피가 없습니다.")

while True:
    command = input("1. 레시피 보기 | 2. 레시피 추가 | 3. 종료\n원하는 작업을 선택하세요: ")
    if command == "1":
        recipeName = input("레시피 이름을 입력하세요: ")
        printRecipe(recipeName)
    elif command == "2":
        recipeName = input("레시피 이름을 입력하세요: ")
        ingredients = input("사용되는 재료를 입력하세요 (쉼표로 구분): ").split(",")
        steps = input("레시피 순서를 입력하세요 (한 줄씩): ").split(",")
        addRecipe(recipeName, ingredients, steps)
        print("레시피가 추가되었습니다.")
    elif command == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 명령을 입력하세요.")


