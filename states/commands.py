from data.config import SITE
from keyboards.inline.callback_datas import menu_cd
from requests import get, post, delete


def make_callback_data(level, category="0", item_id="0"):
    return menu_cd.new(level=level, category=category, item_id=item_id)


def get_categories():
    return get(f'{SITE}/api/v2/categories').json()


def get_image(name):
    url = f'{SITE}/static/img/{name}'
    img = get(url)
    with open('keyboards/inline/img/' + name, 'wb') as data:
        data.write(img.content)


async def count_items(index):
    inf = await get_items()
    items = inf['items']
    count = 0
    for i in range(len(items)):
        if items[i][1] == index:
            count += 1
    return count


async def get_items():
    return get(f'{SITE}/api/v2/items').json()


async def get_cat_items(category):
    inf = await get_items()
    items = inf['items']
    right_items = []
    for i in range(len(items)):
        if items[i][1] == category:
            right_items.append(items[i])
    return right_items


async def get_users():
    return get(f'{SITE}/api/v2/users').json()['users']


async def get_item(id):
    return get(f'{SITE}/api/v2/items/{id}').json()['items']


async def get_quest():
    return get(f'{SITE}/api/v2/questions').json()['questions']


async def post_question(email, question, theme):
    jsn = {
        'email': email,
        'question': question,
        'theme': theme
    }
    post(f'{SITE}/api/v2/questions', json=jsn)


async def del_question(id):
    delete(f'{SITE}/api/v2/question/{str(id)}')


async def post_item(name, content, category, about, characteristics, price, img):
    jst = {'name': name,
           'content': content,
           'category': category,
           'about': about,
           'characteristics': characteristics,
           'img': img,
           'price': price}
    '''await post_item(name='ppp', content='ll.jpg', category="Телефоны", about='sdfdsf', characteristics='sdfsdfds',
                        price='15450')'''
    post(f'{SITE}/api/v2/items', json=jst)
