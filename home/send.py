import requests
from sms_ir import SmsIr

def send(phone):
	return requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={"cellphone": phone})

sms_ir = SmsIr(
    api_key = 'xyRznNIlNgbCXNgI9dipMXac4koaujviZVnNOapCLnaHSPs13H1mhQ0v1VHQFLBo',
    linenumber = '30007732900143',
)


def send_child(phone, fname):
    sms_ir.send_sms(
    phone,     
    f'{fname} عزیز ورودتان به جمع بزرگ قراری ها رو خوش آمد میگم. \nبا چارچوب رویات رو باور کن. \n\n آدرس ما در فضای مجازی... https://ble.ir/ir_4choob',
    '30007732900143',
)



def send_parent(phone, family_name):
    sms_ir.send_sms(
    phone,      
    f'خانم/آقا {family_name} ورود فرزندتان را به رویداد بزرگ قرار تبریک عرض میکنیم. \n\n گزارش لحظه به لحظه از اردوی قرار در کانال ما...https://ble.ir/ir_4choob \n\n با چارچوب رویات رو باور کن.',
    '30007732900143',
)

def test_send(phone):
    sms_ir.send_sms(
    phone,
    'این پیام جهت تست ارسال می شود.',
    '30007732900143',
)


