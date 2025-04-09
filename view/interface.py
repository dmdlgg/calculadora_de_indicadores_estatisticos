import flet as ft
from controller.functions import calcular_media, calcular_mediana, calcular_desvio_padrao, calcular_quartis, calcular_variancia
def main (page: ft.Page):
    page.title = 'Calculadora de Indicadores Esatísticos'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    instrucoes = ft.Text(
        'No campo abaixo, insira os valores separados por espaço',
        text_align='center'
    )

    valores = ft.TextField(
        label='insira os valores aqui',
        width=200,
        text_align="center"
    )

    btn_media = ft.ElevatedButton(
        'Calcular média',
        on_click=lambda e: calcular_media(valores, valores.value, page, resultado)
    )

    btn_mediana = ft.ElevatedButton(
        'Calcular mediana',
        on_click=lambda e: calcular_mediana(valores, valores.value, page, resultado)
    )

    btn_desvio = ft.ElevatedButton(
        'Calcular desvio padrão',
        on_click=lambda e: calcular_desvio_padrao(valores, valores.value, page, resultado)
    )

    btn_quartis = ft.ElevatedButton(
        'Calcular quartis',
        on_click=lambda e: calcular_quartis(valores, valores.value, page, resultado)
    )

    btn_variância = ft.ElevatedButton(
        'Calcular variância',
        on_click=lambda e: calcular_variancia(valores, valores.value, page, resultado)
    )

    resultado = ft.Text(
        f'',
        text_align='center'
    )

    page.add(
        ft.Column(
            [
                instrucoes,
                valores,
                btn_media,
                btn_mediana,
                btn_desvio,
                btn_quartis,
                btn_variância,
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

  