import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "rahasia"
)

def register():
    cursor = db.cursor()
    while True:
        username = input("Username : ")
        while username == "":
            username = input("Username tidak boleh kosong : ")
        
        email = input("Email :")
        while email == "":
            email = input("Email tidak boleh kosong! : ")    
            
        password = input("Password : ")
        while password == "":
            password = input("Password tidak boleh kosong! : ")
        
        konfirmasi = input("\napakah data sudah sesuai? y/n : ")
        if konfirmasi == "y":            
            sql = "INSERT INTO users (username, password, email) VALUES (%s,%s,%s)"
            val = (username, password, email)
            cursor.execute(sql,val)
            db.commit()
            
            if cursor.rowcount > 0 :
                print("Pendaftaran berhasil, silakan login")
            else : 
                print("Pendaftaran gagal ")
                
        lanjut = input("\n klik enter untuk beralih ke login page ...")
        if lanjut == "":
            login()
        else :
            break

def login():
    cursor = db.cursor()
    print("Login page\n")
    username = input("Username : ")
    while username == "":
        username = input("Username tidak bole kosong : ")
    password = input("Password : ").encode('utf-8')
    while password ==  "":
        password = input("Password tidak bole kosong : ").encode('utf-8')

    konfirmasi = input("klik enter untuk login!")
    if konfirmasi == "":
        sql = "SELECT password FROM users WHERE username=%s"
        val = (username,)
        cursor.execute(sql,val)
        cek = cursor.fetchone()
        if cek is not None and len(cek) > 0:
            res = cek[0]        
            if res.encode('utf-8') == password:
                print(f"login berhasil, selamat datang {username}")
            else:
                print("Password salah")
                login()
        else :
            print("User tidak ditemukan")
            login()
        
        
menu = input("pilih login/reg : ")

if menu == "login":
    login()
elif menu == "reg":
    register()
else:
    print("program berakhir")
    exit()

