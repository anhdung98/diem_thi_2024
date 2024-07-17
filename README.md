# Dữ liệu thô Điểm thi tốt nghiệp THPT 2024

Dữ liệu cập nhật ngày 18/07/2013, không bao gồm điểm phúc khảo.

Download tại đây: [https://github.com/anhdung98/diem_thi_2024/releases/download/240717/diem_thi_thpt_2024.csv](https://github.com/anhdung98/diem_thi_2024/releases/download/240717/diem_thi_thpt_2024.csv)

> Hai chữ số đầu tiên của số báo danh là mã Hội đồng thi (tỉnh/thành phố) của thí sinh dự thi

## Mã tỉnh/thành phố

- 01 - THÀNH PHỐ HÀ NỘI
- 02 - THÀNH PHỐ HỒ CHÍ MINH
- 03 - THÀNH PHỐ HẢI PHÒNG
- 04 - THÀNH PHỐ ĐÀ NẴNG
- 05 - TỈNH HÀ GIANG
- 06 - TỈNH CAO BẰNG
- 07 - TỈNH LAI CHÂU
- 08 - TỈNH LÀO CAI
- 09 - TỈNH TUYÊN QUANG
- 10 - TỈNH LẠNG SƠN
- 11 - TỈNH BẮC KẠN
- 12 - TỈNH THÁI NGUYÊN
- 13 - TỈNH YÊN BÁI
- 14 - TỈNH SƠN LA
- 15 - TỈNH PHÚ THỌ
- 16 - TỈNH VĨNH PHÚC
- 17 - TỈNH QUẢNG NINH
- 18 - TỈNH BẮC GIANG
- 19 - TỈNH BẮC NINH
- 21 - TỈNH HẢI DƯƠNG
- 22 - TỈNH HƯNG YÊN
- 23 - TỈNH HÒA BÌNH
- 24 - TỈNH HÀ NAM
- 25 - TỈNH NAM ĐỊNH
- 26 – TỈNH THÁI BÌNH
- 27 – TỈNH NINH BÌNH
- 28 – TỈNH THANH HÓA
- 29 – TỈNH NGHỆ AN
- 30 – TỈNH HÀ TĨNH
- 31 – TỈNH QUẢNG BÌNH
- 32 – TỈNH QUẢNG TRỊ
- 33 – TỈNH THỪA THIÊN - HUẾ
- 34 – TỈNH QUẢNG NAM
- 35 – TỈNH QUẢNG NGÃI
- 36 – TỈNH KON TUM
- 37 – TỈNH BÌNH ĐỊNH
- 38 – TỈNH GIA LAI
- 39 – TỈNH PHÚ YÊN
- 40 – TỈNH ĐẮK LẮK
- 41 – TỈNH KHÁNH HÒA
- 42 – TỈNH LÂM ĐỒNG
- 43 – TỈNH BÌNH PHƯỚC
- 44 – TỈNH BÌNH DƯƠNG
- 45 – TỈNH NINH THUẬN
- 46 – TỈNH TÂY NINH
- 47 – TỈNH BÌNH THUẬN
- 48 – TỈNH ĐỒNG NAI
- 49 – TỈNH LONG AN
- 50 – TỈNH ĐỒNG THÁP
- 51 – TỈNH AN GIANG
- 52 – TỈNH BÀ RỊA – VŨNG TÀU
- 53 – TỈNH TIỀN GIANG
- 54 – TỈNH KIÊN GIANG
- 55 – THÀNH PHỐ CẦN THƠ
- 56 – TỈNH BẾN TRE
- 57 – TỈNH VĨNH LONG
- 58 – TỈNH TRÀ VINH
- 59 – TỈNH SÓC TRĂNG
- 60 – TỈNH BẠC LIÊU
- 61 – TỈNH CÀ MAU
- 62 – TỈNH ĐIỆN BIÊN
- 63 – TỈNH ĐĂK NÔNG
- 64 – TỈNH HẬU GIANG

## Hướng dẫn cài đặt

### 1. Cài đặt Python

Vui lòng tải Python tại https://www.python.org/

### 2. Cài đặt framework Scrapy

Công cụ Crawl dữ liệu được viết bằng Python Framework [Scrapy](https://github.com/scrapy/scrapy). Để cài đặt framework Scrapy, bạn hãy chạy lệnh sau:

`pip3 install scrapy`

### 3. Tải source code bằng _git_

`git clone --branch source-code https://github.com/anhdung98/diem_thi_2024.git`

### 4. Crawl dữ liệu

`scrapy crawl diemthi2024 --nolog`
