import json

# import requests
# 指定した金額を100円玉と10円玉と1円玉だけで、できるだけ少ない枚数で支払いたい。
# 金額を入力するとそれぞれの枚数を計算して表示するプログラムを作成せよ

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def is_pay_money(n): 
    a = n // 100
    b = n % 100
    b //= 10
    c = n - (100*a) - (10*b)
    return [a,b,c]


def validate_number(x):
    if x < 0:
        raise InvalidError("2以上の整数値を入力してください。")

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = number(n)
        validate_number(n)
        print(n)
    except Exception as e:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":str(e)
        },ensure_ascii=False).encode("utf8"),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    results = is_pay_money(n)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "100YEN": results[0],
            "10YEN": results[1],
            "1YEN":results[2],
            # "location": ip.text.replace("\n", "")
        }),
    }