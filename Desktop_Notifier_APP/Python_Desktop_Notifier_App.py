from plyer import notification

title="Morning message"

message="Good Morning"

notification.notify(
    title=title,message=message,app_icon=None,timeout =10, toast=False)
