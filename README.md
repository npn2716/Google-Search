# Google Search

Get data from Google Search results. 

Output data is **n** refined .html file and **n** .csv file.

## Table of Contents
- [Google Search](#google-search)
  - [Table of Contents](#table-of-contents)
  - [Environment](#environment)
  - [Library (Module) Requirements](#library-module-requirements)
    - [Installation](#installation)
  - [Demo](#demo)

## Environment

Operating System: **Windows**, **MacOS**, **Linux**

Integrating Environment: **Python 3.x**

## Library (Module) Requirements

`codecs`, `request`, `ftfy`, `w3lib`, `csv`, `pandas`, `pyparsing`

### Installation

```console
$ pip install module_name
```

## Demo

```console
$ python __init__.py
```

```
html\python.html was created successfully!
html\python.html was read successfully!
csv\python.csv was created successfully!
html\hóa+dược.html was created successfully!
html\hóa+dược.html was read successfully!
csv\hóa+dược.csv was created successfully!
html\công+nghệ+thông+tin.html was created successfully!
html\công+nghệ+thông+tin.html was read successfully!
csv\công+nghệ+thông+tin.csv was created successfully!
html\bill+gates.html was created successfully!
html\bill+gates.html was read successfully!
csv\bill+gates.csv was created successfully!
html\shopee.html was created successfully!
html\shopee.html was read successfully!
csv\shopee.csv was created successfully!
html\2022.html was created successfully!
html\2022.html was read successfully!
csv\2022.csv was created successfully!
html\3d.html was created successfully!
html\3d.html was read successfully!
csv\3d.csv was created successfully!
html\đồ+họa+máy+tính.html was created successfully!
html\đồ+họa+máy+tính.html was read successfully!
csv\đồ+họa+máy+tính.csv was created successfully!
html\timpani.html was created successfully!
html\timpani.html was read successfully!
csv\timpani.csv was created successfully!

===== Google results for: python =====
                                            WebTitle          WebDomain                                             WebDir
0                                         Python.org     www.python.org                                     www.python.org
1  Học Python 3.x cơ bản, nâng cao, có bài tập co...    quantrimang.com            quantrimang.com › Công nghệ › Lập trình
2  Python (ngôn ngữ lập trình) – Wikipedia tiếng ...   vi.wikipedia.org  vi.wikipedia.org › wiki › Python_(ngôn_ngữ_lập...
3                          Python cơ bản - CodeLearn       codelearn.io            codelearn.io › learning › python-co-ban
4  Python là gì? - Hướng dẫn dành cho người mới b...     aws.amazon.com    aws.amazon.com › ... › Trung tâm nhà phát triển
5                        Python Tutorial - W3Schools  www.w3schools.com                         www.w3schools.com › python
6                 Introduction to Python - W3Schools  www.w3schools.com          www.w3schools.com › python › python_intro
7  Hướng Dẫn Lập Trình 6 Dự Án Python Cơ Bản Tron...    www.youtube.com                            www.youtube.com › watch


===== Google results for: hóa dược =====
                                            WebTitle             WebDomain                                             WebDir
0              Hóa dược - Tuyển sinh Đại học Cần Thơ  tuyensinh.ctu.edu.vn  tuyensinh.ctu.edu.vn › gioi-thieu-nganh › 745-...
1                    Hóa dược – Wikipedia tiếng Việt      vi.wikipedia.org                 vi.wikipedia.org › wiki › Hóa_dược
2  Ngành Hóa dược ra làm gì và thông tin về ngành...         timviec365.vn  timviec365.vn › Cẩm nang tìm việc › Định hướng...
3  Nên chọn học ngành Dược học hay Hóa dược? - Hi...                hiu.vn  hiu.vn › nen-chon-hoc-nganh-duoc-hoc-hay-hoa-duoc
4  Tìm hiểu ngành nghề: Hóa dược (Mã XT: 7720203)...          trangedu.com                          trangedu.com › Ngành nghề
5             Bộ môn Hóa dược, Giới thiệu, Khoa Dược       duoc.lhu.edu.vn                  duoc.lhu.edu.vn › Bo-mon-Hoa-duoc
6  Kỹ thuật Hóa dược (Chương trình tiên tiến) - Đ...        ts.hust.edu.vn  ts.hust.edu.vn › nganh-dao-tao › ky-thuat-hoa-...
7  Ngành hóa dược - Ngành học luôn được thí sinh ...        tuyensinhso.vn  tuyensinhso.vn › nhom-nganh-dao-tao › nganh-ho...
8                         giới thiệu bộ môn hóa dược      pharm.ump.edu.vn  pharm.ump.edu.vn › bo-mon › bo-mon-hoa-duoc › ...


===== Google results for: công nghệ thông tin =====
                                            WebTitle                WebDomain                                             WebDir
0  Công nghệ thông tin - Ngành học tiềm năng được...           tuyensinhso.vn  tuyensinhso.vn › nganh-cong-nghe-thong-tin-c16368
1          Tổng quan ngành Công nghệ thông tin - UIT     tuyensinh.uit.edu.vn         tuyensinh.uit.edu.vn › Công nghệ thông tin
2         Công nghệ thông tin – Wikipedia tiếng Việt         vi.wikipedia.org      vi.wikipedia.org › wiki › Công_nghệ_thông_tin
3  Ngành công nghệ thông tin là gì? Học xong ra t...                   hiu.vn  hiu.vn › nganh-cong-nghe-thong-tin-la-gi-hoc-x...
4                          Ngành Công nghệ thông tin       daotao.ptit.edu.vn                      daotao.ptit.edu.vn › nganhhoc
5    Học ngành Công nghệ thông tin ra trường làm gì?  daihocnguyentrai.edu.vn  daihocnguyentrai.edu.vn › Tin tức - Sự kiện › ...
6  Công nghệ thông tin là gì? Học những gì? Và ra...     daivietsaigon.edu.vn  daivietsaigon.edu.vn › dao-tao › bai-viet › co...


===== Google results for: bill gates =====
                                            WebTitle              WebDomain                                             WebDir
0                  Bill Gates – Wikipedia tiếng Việt       vi.wikipedia.org               vi.wikipedia.org › wiki › Bill_Gates
1                             Bill Gates - Wikipedia       en.wikipedia.org               en.wikipedia.org › wiki › Bill_Gates
2  Bill Gates là ai? Ông đã làm được những gì để ...  www.thegioididong.com   www.thegioididong.com › Tin Tức › Tin nhanh 24/7
3      Tin Tỷ phú Bill Gates mới nhất trên VnExpress          vnexpress.net           vnexpress.net › chu-de › bill-gates-1851
4                              Bill Gates - Facebook     vi-vn.facebook.com  vi-vn.facebook.com › Trang › Người của công chúng
5                                  Home | Bill Gates     www.gatesnotes.com                                 www.gatesnotes.com
6                              Bill Gates - Tuổi trẻ             tuoitre.vn                            tuoitre.vn › bill-gates


===== Google results for: shopee =====
                                            WebTitle           WebDomain                                             WebDir
0                                             Shopee           shopee.vn                                          shopee.vn
1  Shopee Xpress - Chuyển Phát Nhanh, Giao Hàng T...              spx.vn                                             spx.vn
2                           Shopee - Home | Facebook  vi-vn.facebook.com  vi-vn.facebook.com › Pages › Other › Brand › A...
3  Shopee: Mua Sắm Online - Ứng dụng trên Google ...     play.google.com  play.google.com › store › apps › details › id=...
4  Cách Xây Dựng Phễu Bán Hàng Trên Shopee - YouTube     www.youtube.com                            www.youtube.com › watch
5                           Shopee Vietnam - YouTube     www.youtube.com                          www.youtube.com › channel


===== Google results for: 2022 =====
                                            WebTitle            WebDomain                                             WebDir
0                        2022 – Wikipedia tiếng Việt     vi.wikipedia.org                     vi.wikipedia.org › wiki › 2022
1  Năm 2022 là năm con gì, mệnh gì? Sinh con năm ...         mediamart.vn  mediamart.vn › meo-vat-doi-song › nam-2022-la-...
2  Năm 2022 là năm con gì, mệnh gì, tuổi nào sẽ m...  www.bachhoaxanh.com  www.bachhoaxanh.com › kinh-nghiem-hay › nam-20...
3  TỨ KẾT AIC 2022 - NGÀY 3: V GAMING TIẾN THẲNG ...      www.youtube.com                            www.youtube.com › watch
4  [LIVESTREAM] CHUNG KẾT HOA HẬU HOÀN VŨ VIỆT NA...      www.youtube.com                            www.youtube.com › watch
5  Top 20 Bài Hát Hot Nhất Trên TikTok 2022 Nhạc ...      www.youtube.com                            www.youtube.com › watch
6  Sao nhập ngũ 2022 l TẬP CUỐI l HƯỚNG VỀ PHÍA M...      www.youtube.com                            www.youtube.com › watch
7  EDM TikTok Hay 2022 Hai Mươi Hai, Nhất Em Rồi,...      www.youtube.com                            www.youtube.com › watch


===== Google results for: 3d =====
                                            WebTitle                 WebDomain                                             WebDir
0                                       3D Warehouse  3dwarehouse.sketchup.com                           3dwarehouse.sketchup.com
1  SketchUp: 3D Design Software | 3D Modeling on ...          www.sketchup.com                                   www.sketchup.com
2  Tạo mô hình 3D cơ bản với Vẽ 3D - Microsoft Su...     support.microsoft.com  support.microsoft.com › vi-vn › windows › tạo-...
3                           Trình xem 3D - Microsoft         www.microsoft.com           www.microsoft.com › vi-vn › trinh-xem-3d
4        Kết quả quay số mở thưởng Max 3D - Vietlott               vietlott.vn  vietlott.vn › trung-thuong › ket-qua-trung-thu...
5                   Đồ họa 3D – Wikipedia tiếng Việt          vi.wikipedia.org                vi.wikipedia.org › wiki › Đồ_họa_3D
6                              3D Shop - Thế giới 3D             3dshop.com.vn                                      3dshop.com.vn
7  Trúng đến 30 tỉ từ xổ số tự chọn Max 3D - Báo ...                laodong.vn  laodong.vn › trung-den-30-ti-tu-xo-so-tu-chon-...


===== Google results for: đồ họa máy tính =====
                                            WebTitle                WebDomain                                             WebDir
0               Đồ họa máy tính là gì? - Hoàng Hà PC             hoanghapc.vn                      hoanghapc.vn › Tin tức › Wiki
1             Đồ họa máy tính – Wikipedia tiếng Việt         vi.wikipedia.org          vi.wikipedia.org › wiki › Đồ_họa_máy_tính
2  Đồ Họa Máy Tính Là Gì? Chuyên Ngành Nào Cần đồ...             itsystems.vn                          itsystems.vn › Tin Tức IT
3  Đồ họa máy tính Bài 1- initgraph khởi tạo màn ...          www.youtube.com                            www.youtube.com › watch
4  Đồ hoạ máy tính là gì? Những điều nên biết về ...               colorme.vn  colorme.vn › blog › do-hoa-may-tinh-la-gi-nhun...
5                              [PDF] ĐỒ HỌA MÁY TÍNH         fit.lqdtu.edu.vn       fit.lqdtu.edu.vn › files › FileMonHoc › KTDH
6  Học Thiết kế đồ họa trên máy tính nào? Dùng ph...  www.arena-multimedia.vn                  www.arena-multimedia.vn › Tin tức
7  PC đồ họa cấu hình cao, giá tốt nhất - Máy tín...           fptshop.com.vn                   fptshop.com.vn › Máy tính để bàn
8  [Lập trình đồ họa máy tính cơ bản] Vẽ các hình...      www.tinhoccoban.net  www.tinhoccoban.net › 2020/03 › lap-trinh-o-ho...


===== Google results for: timpani =====
                                            WebTitle                 WebDomain                                             WebDir
0                      Instrument: Timpani - YouTube           www.youtube.com                            www.youtube.com › watch
1                                Timpani - Wikipedia          en.wikipedia.org                  en.wikipedia.org › wiki › Timpani
2               Trống định âm – Wikipedia tiếng Việt          vi.wikipedia.org            vi.wikipedia.org › wiki › Trống_định_âm
3     Timpani - Nhạc cụ Bộ gõ - Yamaha Music Vietnam             vn.yamaha.com  vn.yamaha.com › Trang chủ › Sản phẩm › Nhạc cụ...
4  TIMPANI | Định nghĩa trong Từ điển tiếng Anh C...  dictionary.cambridge.org  dictionary.cambridge.org › dictionary › englis...
5  LUDWIG LKM232FH - TRỐNG TIMPANI - ACE Music - ...           acemusic.com.vn  acemusic.com.vn › Trống - Bộ Gõ › Bộ Gõ › Bộ g...
6       10 Things You Need to Know About the Timpani          www.bsomusic.org  www.bsomusic.org › stories › 10-things-you-nee...
7  timpani (Thiết bị & Công nghệ Âm nhạc) - Mimir...             mimirbook.com  mimirbook.com › ... › Thiết bị & Công nghệ Âm ...
8  timpani | musical instrument - Encyclopedia Br...        www.britannica.com     www.britannica.com › ... › Musical Instruments
```