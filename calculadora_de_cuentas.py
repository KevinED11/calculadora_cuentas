from enum import Enum


class TipoDeMoneda(Enum):
    MXN = "MXN"
    USD = "USD"


monedas_soportadas: list[str] = [moneda.value for moneda in TipoDeMoneda]


def total_cuenta_a_pagar(factura_cuenta: float,
                         propina: int = 10,
                         moneda: str = "USD") -> str:

    moneda = moneda.upper()

    def manejo_de_moneda(moneda: str) -> str:
        match moneda:
            case tipo_moneda if tipo_moneda in monedas_soportadas:
                return moneda

            case _:
                print("Moneda no soportada, por lo tanto por \
defecto se le enviara en dolares su cuenta")

                return TipoDeMoneda.USD.value

    moneda_elegida = manejo_de_moneda(moneda=moneda)

    if propina < 10:
        propina = 10

    propina_a_pagar = propina / 100

    def calcular_propina() -> float:
        return factura_cuenta * propina_a_pagar

    def total_a_pagar(factura_cuenta: float,
                      propina: float,
                      ) -> float:
        return factura_cuenta + propina

    dinero_total_a_pagar = total_a_pagar(
        factura_cuenta=factura_cuenta,
        propina=calcular_propina(),
    )

    return f"\nLa cuenta total a pagar incluida la propina es de:\
 {dinero_total_a_pagar} {moneda_elegida}"


if __name__ == "__main__":
    print(total_cuenta_a_pagar(factura_cuenta=1500,
                               propina=10,
                               moneda="mdxn"))
