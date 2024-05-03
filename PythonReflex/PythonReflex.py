import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.button("Hola Dany :D")

app = rx.App()
app.add_page(index)
app.compile()