import sys 
import os
import smtplib, ssl
import tkinter
import re
import tkinter.messagebox
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE
from email.mime.base import MIMEBase
from email import encoders


def main_menu():

    root = tkinter.Tk()
    
    root.configure(background="black")

    root.geometry("400x400")


    # Main menu buttons 

    menu_tab = tkinter.Label(root, bg="black", fg="white", text="Phishing Simulator", font=("Monda", 17, "bold"))
    menu_tab.pack(pady=20)

    send_email_button = tkinter.Button(root, bg="black", fg="white", highlightcolor="white", highlightthickness= 3, text="Send A Phishing Simulated Email", font=("Monda", 11), command=phishing_sim)
    send_email_button.pack(pady=10)

    instruction_button = tkinter.Button(root, width=26, bg="black", fg="white", highlightcolor="white", highlightthickness= 3, text="About", font=("Monda", 11), command=about_info)
    instruction_button.pack(pady=10)

    exit_button = tkinter.Button(root, width=26, bg="black", fg="white", highlightcolor="white", highlightthickness= 3, text="Exit", font=("Monda", 11), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()



def phishing_sim():

    root = tkinter.Tk()
    
    root.configure(background="black")

    root.geometry("400x600")

    # Entry widget email address

    email_tab = tkinter.Label(root, bg="black", fg="white", text="Enter Recipient Email Address:", font=("Monda", 11))
    email_tab.pack(pady=10)
    email_entry = tkinter.Entry(root, font=("Monda", 13))
    email_entry.pack(pady=10)


    # Email listing box 

    email_box = tkinter.Label(root, bg="black",  fg="white", text="Please Select A Phishing Email")
    email_box.pack(pady=10)
    email_list = tkinter.Listbox(root, font=("Monda", 13))
    email_list.insert(1, "martshop@phishingtest.co")
    email_list.insert(2, "martbank@phishingtest.co")
    email_list.insert(3, "martmovie@phishingtest.co")
    email_list.pack(pady=10)


    # Validating input functionality

    def validate_email():
        recipient_email = email_entry.get()
        send_email = email_list.get(email_list.curselection())
        if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient_email):
            tkinter.messagebox.showerror("Email you entered is invalid." , "Please enter a valid email address.")
            return False
        return True
    
    
    # Submit button

    submit_button = tkinter.Button(root, bg="black", fg="white", highlightcolor="white", highlightthickness= 2, text="Send", font=("Monda", 13), command=lambda: send_email(email_list.get(email_list.curselection()), email_entry.get())
    if validate_email() else None)
    submit_button.pack(pady=10)

    root.mainloop()

    # About functionality

def about_info():
        
    root = tkinter.Tk()

    root.configure(background="black")
    
    root.geometry("500x700")

    about = tkinter.Label(root, bg="black", fg="white", text="About", font=("Monda", 14, "bold" ))
    about.pack(pady=20)
    about_msg = tkinter.Message(root, bg="black",  fg="white", font=("Monda", 11), text="This is a GUI python-based script which enables you to send a phishing simulated email to help rise phishing awarness. Chosen recipient will be sent a simulated phishing email with a scenario, if user clicks a link within simulated phishing email, it would then direct user to a phishing test website informing user that this was a test, websites will also contain tips on how to avoid such emails, in addition users can then download the script from the website and test others to raise phishing awareness.")
    about_msg.pack(pady=10)
    about_msg = tkinter.Message(root, bg="black",  fg="white", font=("Monda", 11), text="(1) Click on a button Send A Phishing Simulated Email.", width=400)
    about_msg.pack(pady=10)
    about_msg = tkinter.Message(root, bg="black",  fg="white", font=("Monda", 11), text="(2) Enter recipient’s email address in the entry box that you would like to test.", width=400)
    about_msg.pack(pady=10)
    about_msg = tkinter.Message(root, bg="black",  fg="white", font=("Monda", 11), text="(3) Select one of the simulated phishing emails that you would like to send to the recipient. – note each email contains a different scenario.", width=400)
    about_msg.pack(pady=10)
    about_msg = tkinter.Message(root, bg="black",  fg="white", font=("Monda", 11), text="(4) Click button Send", width=300)
    about_msg.pack(pady=10)
    root.mainloop()


    # Sendning email  function

def send_email(send_email, recipient_email):  

    # Email Sender Messgaes
    
    emailmsg = MIMEMultipart()
    emailmsg['From'] = send_email
    emailmsg['To'] = recipient_email
    emailmsg['Subject'] = "Important: Please Read"

    if send_email == "martshop@phishingtest.co":
        body = "Hello user,<br><br><br><b>80% Discount & FREE SHIPPING</b><br><br>MartShop is offering 80% discount on tech gadgets and FREE shipping for a month.<br><br>To claim your coupon code, simply register with MartShop by clicking <a href='https://6434c0fa3618ad5441b7504d--magical-queijadas-a7b013.netlify.app/#home'>HERE</a> <br>It is that simple. <br><br><br>MartShop,<br>MartShop Team"
    elif send_email == "martbank@phishingtest.co":
        body = "Dear user,<br><br><br><b>Security Update</b><br><br>MartBank is announcing the new security update for better banking services, against fraudulent activities.<br><br> Due to recent upgrade, you are requested to update your account details by clicking the link bellow.<br><br> <a href='https://6434c0fa3618ad5441b7504d--magical-queijadas-a7b013.netlify.app/#home'>Update Your Account Details</a><br><br><br>MartShop,<br>Security Advisor"
    elif send_email == "martmovie@phishingtest.co":
        body = "Dear user,<br><br><br><b>Resetting Your Password</b><br><br> If you did not ask to reset your password you may want to review your recent account access for any unusual activity,<br><br> <a href='https://6434c0fa3618ad5441b7504d--magical-queijadas-a7b013.netlify.app/#home'>Check Your Account Now</a><br><br><br>MartMovie,<br>MartMovie Team"


    emailmsg.attach(MIMEText(body, 'html'))


    # Establishing a connection with a mail server

    connection = smtplib.SMTP("phishingtest.co" , 587)
    connection.starttls()
    if send_email == "martshop@phishingtest.co":
        connection.login(user="martshop@phishingtest.co", password="MartShop963" )
        connection.sendmail(from_addr=send_email, to_addrs=recipient_email, msg=emailmsg.as_string())
    elif send_email == "martbank@phishingtest.co":
        connection.login(user="martbank@phishingtest.co", password="MartBank963")
        connection.sendmail(from_addr=send_email, to_addrs=recipient_email, msg=emailmsg.as_string())
    elif send_email == "martmovie@phishingtest.co":
        connection.login(user="martmovie@phishingtest.co", password="MartMovie963")
        connection.sendmail(from_addr=send_email, to_addrs=recipient_email, msg=emailmsg.as_string())
        connection.quit

    tkinter.messagebox.showinfo("Eamil has been sent!", "Email has been sent!")


main_menu()
            

