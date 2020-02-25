import twitter2
import json


def find_key(element, given_key):
    '''
    dict -> str
    Find a value of a key, written by user and return it.
    '''
    result_lst = []
    if type(element) == list:
        for el in element:
            result = find_key(el, given_key)
            if result is not None and result != []:
                result_lst.append(result)
    if type(element) == dict:
        for key in element:
            if given_key == key:
                result_lst.append(str(element[key]) + ',')
            else:
                result = find_key(element[key], given_key)
                if result is not None and result != []:
                    result_lst.append(result)
    result_ = ''.join(result_lst)
    final_result = result_.replace(',', '\n')

    return final_result


if __name__ == '__main__':
    data = twitter2.friends_information()
    js = json.loads(data)
    key_input = input('Please write any key and you will get all its values: ')
    print(find_key(js, key_input))