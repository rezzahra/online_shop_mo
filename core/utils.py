from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6F7A763754784979626A61394B682F736D467A4D79626F4C4D445269455151384335695830774F4A6A6C453D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما : '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
