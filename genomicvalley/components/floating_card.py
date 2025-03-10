import reflex as rx

def floating_card() -> rx.Component:
    return rx.box(
        rx.link(
            rx.box(
                rx.text(
                    "Visit genomicvalley.in",
                    size="4",
                    weight="bold",
                    color="white",
                ),
                rx.text(
                    "for Genomics Healthcare Solutions",
                    size="3",
                    color="white",
                ),
                padding="1.5em",
                background="rgba(39,162,85,0.9)",
                border_radius="2xl",
                border="2px solid black",
                box_shadow="lg",
                _hover={
                    "transform": "translateY(-2px)",
                    "box_shadow": "xl",
                    "background": "rgba(39,162,85,1)",
                },
                transition="all 0.3s ease-in-out",
            ),
            href="https://genomicvalley.in",
            position="fixed",
            bottom="2em",
            right="2em",
            z_index="1000",
        ),
    ) 