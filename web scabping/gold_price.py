import requests
from bs4 import BeautifulSoup

def get_gold_price():
    url = "https://www.goldtraders.or.th/default.aspx"

    # ส่งคำขอ HTTP GET เพื่อดึงเนื้อหาของหน้าเว็บ
    response = requests.get(url)

    # ตรวจสอบว่าการขอเนื้อหาสำเร็จหรือไม่ (สถานะรหัส 200 หมายถึงสำเร็จ)
    if response.status_code == 200:
        # ใช้ BeautifulSoup เพื่อวิเคราะห์ HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # ค้นหาข้อมูลราคาทอง
        gold_price_buy = soup.find("span", id="DetailPlace_uc_goldprices1_lblBLBuy")
        gold_price_sell = soup.find("span", id="DetailPlace_uc_goldprices1_lblBLSell")

        # ถ้าพบข้อมูลราคาทอง
        if gold_price_buy and gold_price_sell:
            buy_price = gold_price_buy.text.strip()
            sell_price = gold_price_sell.text.strip()
            return buy_price, sell_price
        else:
            return "ไม่พบข้อมูลราคาทอง"
    else:
        return "เกิดข้อผิดพลาดในการเชื่อมต่อกับเซิร์ฟเวอร์"

# เรียกใช้ฟังก์ชันเพื่อดึงข้อมูลราคาทอง
buy_price, sell_price = get_gold_price()
print("ราคาทองประจำวัน (รับซื้อ): ", buy_price)
print("ราคาทองประจำวัน (ขายออก): ", sell_price)
