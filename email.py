from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME= "",
    MAIL_PASSWORD= "",
    MAIL_FROM= "",
    MAIL_PORT= 587,
    MAIL_SERVER= "smpt.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS= True
)