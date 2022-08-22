import qrcode

file_path = r'QR코드 생성하기/QR코드모음.txt'

with open(file_path, 'rt', encoding= 'UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = 'QR코드 생성하기/' + 'qr_data' + '.png'
        qr_img.save(save_path)