from send_mail import EmailThread

image = open("./static/testing_pics/Logo.png", "rb")
EmailThread("jianxingliao168@gmail.com",csv, image).start()
