'''
fetch data from an api to feed our recipes database
'''
import requests
import json
from models.recipe import Recipe
from models.user import User
from models import storage, encrypter
from uuid import uuid4

def parse_data(data):
    '''parse dict contain the data from tasti api'''

    recipes = data.get('results')
    objs = []
    track = 0
    user = storage.get(User,username='tasti_team') 
    erorrs_count = 0
    if not user:
        user =User(username='tasti_team', email='tasti@gmail.com' ,password=encrypter.generate_password_hash('TASTI.320.235.s').decode('utf-8'))
        storage.new(user)
        storage.save()


    for recipe in recipes:
        title = recipe.get('name')
        description = recipe.get('description')
        ingradianes = recipe.get('keywords')
        instructions = recipe.get('instructions')

        if not  description:
            description = 'no description added to this recipe.'
        if not ingradianes:
            ingradianes = 'no ingradianes found'
    
        if instructions:
            count = 1
            instructions_txt = ''
            for instruction in instructions:
                instruction_txt = instruction.get("display_text")
                if instruction_txt:
                    instructions_txt += f' step({count}) - {instruction_txt}' + '\n'
                    count +=1

        obj = Recipe(title=title,
                        descripion=description,
                        ingradiantes=ingradianes,
                        instructions=instructions_txt,
                        user_id=user.id,    # save the id of the user that created the recipe.
                            )
        objs.append(obj)
        track +=1
        print(f'- {track} objs added {obj.title}')
        try:
            storage.new(obj)
            storage.save()
        except Exception as e:
            print('erorrs: {}'.format(erorrs_count))
    print('\n\n finished.... \n\n')



    print('clearing ....')
    storage.delete(user)
        # print(f'{title} \n {description} \n {ingradianes} \n {instructions_txt}')


if __name__ == '__main__':
    order = input('enter the number of the set you want to add')
    order = (order * 40) + 1
    # try to play with from and size parameters to get a new results
    # you can't request more than 40 recipe per each request:
    response = requests.get(f'https://tasty.p.rapidapi.com/recipes/list?from={order}&size=40',
        headers={
        'x-rapidapi-host': 'tasty.p.rapidapi.com',
        'x-rapidapi-key': 'fdcf982831mshc7c533ed76269cfp1b7198jsnf11ea700051d'}
        )

    if response.status_code == 200:
        print("Success!")
        recipes = response.json()
        #data = json.dumps(recipes)
        print (type(recipes))
        #with open('recipes.json', 'w') as file:
            #json.dump(recipes,file, indent=4)
        parse_data(recipes)
    elif response.status_code == 404:
        print("Not Found.")
    else:
        print('another')

