import pandas as pd
from selenium import webdriver
import time

def fill_form():
    data = pd.read_csv('##')#data anda example data.csv
    recycle = data.shape[0]
    for i in range(recycle):
        print(i)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get('link googlefom')
        time.sleep(1)
        ##contoh link saya pakai = https://docs.google.com/forms/d/e/1FAIpQLSeYkqDq0o_kprSnZ3zI9euAy3Mh3-zqE2cXh1tzTA7zw5j9MQ/viewform?pli=1
     
        name = data.iloc[i]['Name']
        inputName = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        for j in name:
            inputName.send_keys(j)
            time.sleep(0.05)
        #jika ada data email
        # email = data.iloc[i]['email']
        # inputEmail = driver.find_element("xpath",'MASUKAN_DATA_XPATH')
        # for j in email:
        #     inputEmail.send_keys(j)
        #     time.sleep(0.05)

        # address = data.iloc[i]['address']
        # inputAddress = driver.find_element("xpath",'MASUKAN_DATA_XPATH')
        # for j in address:
        #     inputAddress.send_keys(j)
        #     time.sleep(0.05)

        #note sesuaikan bagian mana yang ingin di isi lalu inspect elemen pilih copy expath

        ukuran = driver.find_element("xpath",'linkxpath')#contoh //*[@id="i9"]/div[3]/div s
        ukuran.click()
        time.sleep(0.5)

        # sessuikan dengan google form yang di pakai

        # usia = driver.find_element("xpath",'//*[@id="i28"]/div[3]/div')
        # usia.click()
        # time.sleep(0.5)

        # pekerjaan = driver.find_element("xpath",'//*[@id="i44"]/div[3]/div')
        # pekerjaan.click()
        # time.sleep(0.5)

        # domisili = driver.find_element("xpath",'//*[@id="i54"]/div[3]/div') 
        # domisili.click()
        # time.sleep(1)

        next = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        next.click()
        time.sleep(0.5)
        ## menu ke 2
        time.sleep(1)
        odeng = driver.find_element("xpath",'//*[@id="i5"]/div[3]/div')#//*[@id="i5"]/div[3]/div/div
        odeng.click()
        time.sleep(0.5)

        medsos = driver.find_element("xpath",'//*[@id="i18"]/div[3]/div')
        medsos.click()
        time.sleep(0.5)

        kuah = driver.find_element("xpath",'//*[@id="i31"]/div[3]/div')
        kuah.click()
        time.sleep(0.5)


        ukuran = driver.find_element("xpath",'//*[@id="i38"]/div[3]/div')
        ukuran.click()
        time.sleep(0.5)

        
        wadah = driver.find_element("xpath",'//*[@id="i48"]/div[3]/div')
        wadah.click()
        time.sleep(0.5)

        time.sleep(0.5)
        harga = driver.find_element("xpath",'//*[@id="i61"]/div[3]/div')
        harga.click()
        time.sleep(0.5)

        uang = driver.find_element("xpath",'//*[@id="i71"]/div[3]/div')
        uang.click()
        time.sleep(0.5)

        tawar = driver.find_element("xpath",'//*[@id="i84"]/div[3]/div')
        tawar.click()
        time.sleep(1)

        ####menu 3
        time.sleep(1)
        submit2 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        submit2.click()
        time.sleep(0.5)

        time.sleep(0.5)
        ongkir = driver.find_element("xpath",'//*[@id="i14"]/div[3]/div')
        ongkir.click()
        time.sleep(0.5)

        a = driver.find_element("xpath",'//*[@id="i30"]/div[3]/div')
        a.click()
        time.sleep(0.5)

        b = driver.find_element("xpath",'//*[@id="i52"]/div[3]/div')
        b.click()
        time.sleep(0.5)
        
        time.sleep(0.5)
        c = driver.find_element("xpath",'//*[@id="i68"]/div[3]/div')
        c.click()
        time.sleep(0.5)

        d = driver.find_element("xpath",'//*[@id="i87"]/div[3]/div')
        d.click()
        time.sleep(0.5)

        e = driver.find_element("xpath",'//*[@id="i112"]/div[3]/div')
        e.click()
        time.sleep(0.5)

        kritik = data.iloc[i]['kritik']
        inputkritik = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
        for j in kritik:
            inputkritik.send_keys(j)
            time.sleep(0.05)

        kirim = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        kirim.click()
        time.sleep(0.5)
        #note crome akan otomatis terbuka dan terttutup sesuai jumlah data yang di masukan 
        # mohon maaf gweh masih pemula jadi cuma bisa looping kaya gitu xixix
        driver.close()
    driver.quit()   
        

fill_form()
time.sleep(1)