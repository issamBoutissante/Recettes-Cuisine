import requests
from bs4 import BeautifulSoup
from .models import *

def fill_database():
    #hna kan7to link dyal website lighadi scrapiw mno and kanstartiw awla kandero initialisation page number
    base_url = 'https://www.elle.fr/Elle-a-Table/Recettes-de-cuisine'
    page_num = 1
    while True:
        # hnaya kan buildew url dyal la page actuelle
        page_url = base_url + f'?page={page_num}'

        # hnaya kansifto wahd request l page bach der wahd analyse b bautifulsoup
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # hnaya kankalbo 3la div li fih the recipes
        recipes_div = soup.find('div', {'class': 'more_articles'})
        if recipes_div is None:
            #hnaya ila malkina div safi kader wahd break
            break

        # hnaya kandero extract l recipes f la page
        recipes = recipes_div.find('ul').findAll('li')
        for recipe in recipes:
            # bach njbdo url dyal recipe
            recipe_link = recipe.find('a')
            if recipe_link is None:
                #  hnaya fihalat makaynach kan skipiw l next recipe
                continue
            recipe_url = recipe_link['href']

            # hnaya kansifto wahd request l page bach der wahd analyse b bautifulsoup
            recipe_response = requests.get(recipe_url)
            recipe_soup = BeautifulSoup(recipe_response.content, 'html.parser')

            # kanjbdo the recipe title and print it
            recipe_title = recipe_soup.find('h1', {'class': 'article__title'}).text
            recipe_duration =recipe_soup.find('dd', {'class': 'article__detail-value'}).text
            # hnaya kandero extract recipe image
            recipe_image_url = recipe_soup.find('div', {'class': 'article__summary'}).find('img', {'class': 'responsive-media'})['src']
            # hnaya data explemple nbr people ola time dyal recipe
            recipe_data = recipe_soup.find('dl', {'class':'article__data'}).findAll('div')
            #print(recipe_data)

            # extract ingredients
            ingredients_list = recipe_soup.find('ul', {'class': 'article-body__list'})
            print("Ingredients:")
            for ingredient in ingredients_list.findAll('li'):
                print("- " + ingredient.text.strip())

            # extract preparation steps
            preparation_list = recipe_soup.find('ol', {'class': 'article-body__list'})
            print("Preparation steps:")
            for step in preparation_list.findAll('li'):
                print("- " + step.text.strip())

            print("\n")
            recipe = Recipe(title=recipe_title , imageUrl=recipe_image_url,duration=recipe_duration)
            recipe.save()
            print("saved _-----------------------------------------------------------------------")

        # Increment the page
        page_num += 1
