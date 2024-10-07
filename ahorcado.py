import flet as ft

palabraAdivinar = "popote"

escondido = ["_" for i in palabraAdivinar]

intentosMax = 7
intengtosRes = intentosMax

imagenes = [
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\0.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\1.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\2.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\3.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\4.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\5.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\6.png",
    r"C:\Users\roll-\OneDrive\Escritorio\Programacion2\venv\Include\7.png"
]

def crearBoton (letra, page, muestraEscondida, muestraImagenes,mensaje): 
    def on_click(e):

        global intengtosRes
        e.control.disabled = True
        e.control.update()
        if letra in palabraAdivinar:
            for idx,letter in enumerate(palabraAdivinar) :
                if letter == letra:
                    escondido[idx] = letra
            muestraEscondida.value = " ".join(escondido)
            page.update()

            if "_" not in escondido:
                mensaje.value = " felicidades"  
                mensaje.update()
                disableAll(page)
        else:
            intengtosRes -= 1
            muestraImagenes.src = imagenes[intentosMax-intengtosRes]
            muestraImagenes.update()
            if intengtosRes == 0:
                disableAll(page)
                mensaje.value = "perdiste"
                mensaje.update()
    return ft.ElevatedButton(letra,on_click=on_click)

def disableAll(page):
    for controles in page.controls[1].controls:
        controles.disabled = True
    page.update()
def main (page: ft.Page):
    page.tittle = "Ahorcado"
    muestraEscondida = ft.Text(" ".join(escondido), size = 30)
    muestraImagenes = ft.Image(src = imagenes[0],width=500, height=500)
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensaje = ft.Text("mensaje", size = 20, color = "red")
    
    letraBoton = [crearBoton(letra, page, muestraEscondida, muestraImagenes,mensaje) for letra in alfabeto]

    page.add(
        muestraEscondida,
        ft.Row(controls=letraBoton, wrap=True, spacing=5),
        muestraImagenes, 
        mensaje
        
    )   

ft.app(main)