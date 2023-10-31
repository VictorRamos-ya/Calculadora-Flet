import flet as ft
from flet import colors
from decimal import Decimal

buttons = [
    {'operador': 'AC','fonte': colors.BLACK,'bg': colors.BLUE_GREY_100},
    {'operador': '±','fonte': colors.BLACK,'bg': colors.BLUE_GREY_100},
    {'operador': '%','fonte': colors.BLACK,'bg': colors.BLUE_GREY_100},
    {'operador': '/','fonte': colors.WHITE,'bg': colors.ORANGE},
    {'operador': '7','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '8','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '9','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '*','fonte': colors.WHITE,'bg': colors.ORANGE},
    {'operador': '4','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '5','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '6','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '-','fonte': colors.WHITE,'bg': colors.ORANGE},
    {'operador': '1','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '2','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '3','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '+','fonte': colors.WHITE,'bg': colors.ORANGE},
    {'operador': '.','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '0','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': 'del','fonte': colors.WHITE,'bg': colors.WHITE24},
    {'operador': '=','fonte': colors.WHITE,'bg': colors.ORANGE},
] 


def main(page: ft.Page):
    page.bgcolor = 'black'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 380
    page.window_always_on_top = True

    result = ft.Text(value='0',color=colors.WHITE, size=20)

    def calculo(operador, valor_at):
        try:
            value = eval(valor_at)

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return ';-;'    
        digitos = min(abs(Decimal(value).as_tuple().exponent),5)
        return format(value, f'.{digitos}f')
        

    def select(x):
        valor_at = result.value if result.value not in ('0',';-;') else ''
        value = x.control.content.value

        if value.isdigit ():
            value = valor_at + value
        elif value == 'AC':
            value = '0'
        elif value == 'del':
            value = valor_at[:-1]
        else:
            if valor_at and valor_at[-1] in ('/','*','-','+','.'):
                valor_at = valor_at[:-1]           
                
            value = valor_at + value

            if value [-1] in ('=','%','±'):
                value = calculo(operador=value[-1], valor_at=valor_at)

        result.value = value
        result.update()


    barra = ft.Row(
        width=240,
        controls=[result],
        alignment= 'end',
    )
    
    button = [ft.Container(
        content=ft.Text(value=button['operador'], color=button['fonte']),
        width=50,
        height=50,
        bgcolor=button['bg'],
        border_radius=100,
        alignment= ft.alignment.center,
        on_click=select,
    ) for button in buttons]

    teclado = ft.Row(
        width=275,
        wrap=True,
        controls=button,

    )




    page.add(barra,teclado)



ft.app(target = main)
