import requests
from sms_ir import SmsIr

# def send(phone):
# 	return requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={"cellphone": phone})

sms_ir = SmsIr(
    api_key = 'xyRznNIlNgbCXNgI9dipMXac4koaujviZVnNOapCLnaHSPs13H1mhQ0v1VHQFLBo',
    linenumber = '30007732900143',
)


def send_child(phone, fname):
    sms_ir.send_sms(
    phone,
    f'{fname} message',
    '30007732900143',
)



def send_parent(phone, family_name):
    sms_ir.send_sms(
    phone,
    f'{family_name} message',
    '30007732900143',
)

def test():
    sms_ir.send_sms(
    '09227503271',
    'https://web.bale.ai/chat/5307148829',
    '30007732900143',
)

test()