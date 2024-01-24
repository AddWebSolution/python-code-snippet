class SendMail:
    def __init__(self, context):
        self.context = context

    def email_send(self, subject, email, page):
        html_page = render_to_string(page, self.context)
        msg = EmailMessage(subject, html_page, to=[email])
        msg.content_subtype = "html"
        msg.send()
    
    def register(self, email):
        page = html_path("registration")
        subject = "Thank You For Register Account"
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start()

    def verify(self, action, email):
        self.context['action'] = action
        page = html_path("verify")
        if action == "set-otp":
            subject = "Otp For Verification "
        else:
            subject = "Your Account has been verified."
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start() 

    def reset_password(self, email):
        page = html_path("reset_password")
        subject = "Reset your password!"
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start()

    def order(self, email):
        page = html_path("order")
        status = self.context['order'].get_order_status
        subject = f"{status}"
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start()

    def invoice(self, email):
        page = html_path("invoice")
        subject = f"Membership Invoice"
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start()

    def add_staff(self, email):
        page = html_path("add_staff")
        subject = f"Credentials"
        task = Thread(target=self.email_send, args=(subject, email, page))
        task.start()
