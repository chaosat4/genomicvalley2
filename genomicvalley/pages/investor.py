import reflex as rx

from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner

paragraph_style = {
    "font-size": "1.2rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

mobile_paragraph_style = {
    "font-size": "1rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

table_header_style = {
    "background_color": "teal",
    "color": "white",
    "font_weight": "bold",
    "padding": "1rem",
    "font_size": "1.1rem",
}

table_cell_style = {
    "color": "black",
    "font_size": "1.1rem",
    "padding": "1rem",
    "text-align": "center",
}

download_button_style = {
    "background_color": "teal",
    "color": "white",
    "padding": "0.5rem 1rem",
    "border_radius": "0.25rem",
    "cursor": "pointer",
    "_hover": {"background_color": "teal.600"},
}

@rx.page(route="/investor", title="Investor Relations")
def investor():
    return rx.section(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("Investor Relations"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Welcome to our Investor Relations page. Here you can find our annual reports and financial documents organized by fiscal year.",
                                style=paragraph_style,
                                margin_bottom="2rem",
                            ),
                            rx.tabs.root(
                                rx.tabs.list(
                                    rx.tabs.trigger(rx.text("FY 2025-26", color="teal"), value="fy2025"),
                                    rx.tabs.trigger(rx.text("FY 2024-25", color="teal"), value="fy2024"),
                                    rx.tabs.trigger(rx.text("FY 2023-24", color="teal"), value="fy2023"),
                                ),
                                rx.tabs.content(
                                    rx.table.root(
                                        rx.table.header(
                                            rx.table.row(
                                                rx.table.column_header_cell(
                                                    "S.No.",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Quarter",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Standalone",
                                                    style=table_header_style,
                                                ),
                                            ),
                                        ),
                                        rx.table.body(
                                            rx.table.row(
                                                rx.table.cell("1", style=table_cell_style),
                                                rx.table.cell("First Quarter", style=table_cell_style),
                                                rx.table.cell(
                                                    rx.button(
                                                        "Download",
                                                        style=download_button_style,
                                                        on_click=rx.download(url="/bmo.pdf"),
                                                    )
                                                ),
                                            ),
                                        ),
                                        width="100%",
                                        margin_bottom="2rem",
                                    ),
                                    value="fy2025",
                                ),
                                rx.tabs.content(
                                    rx.table.root(
                                        rx.table.header(
                                            rx.table.row(
                                                rx.table.column_header_cell(
                                                    "S.No",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Document",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Download",
                                                    style=table_header_style,
                                                ),
                                            ),
                                        ),
                                        rx.table.body(
                                            rx.table.row(
                                                rx.table.cell("1", style=table_cell_style),
                                                rx.table.cell("Audited Financial 31st March 2025", style=table_cell_style),
                                                rx.table.cell(
                                                    rx.button(
                                                        "Download",
                                                        style=download_button_style,
                                                        on_click=rx.download(url="/obm.pdf"),
                                                    )
                                                ),
                                            ),
                                        ),
                                        width="100%",
                                        margin_bottom="2rem",
                                    ),
                                    value="fy2024",
                                ),
                                rx.tabs.content(
                                    rx.table.root(
                                        rx.table.header(
                                            rx.table.row(
                                                rx.table.column_header_cell(
                                                    "S.No",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Document",
                                                    style=table_header_style,
                                                ),
                                                rx.table.column_header_cell(
                                                    "Download",
                                                    style=table_header_style,
                                                ),
                                            ),
                                        ),
                                        rx.table.body(
                                            rx.table.row(
                                                rx.table.cell("1", style=table_cell_style),
                                                rx.table.cell("Annual Report", style=table_cell_style),
                                                rx.table.cell(
                                                    rx.button(
                                                        "Download",
                                                        style=download_button_style,
                                                        on_click=rx.download(url="/ar.pdf"),
                                                    )
                                                ),
                                            ),
                                        ),
                                        width="100%",
                                        margin_bottom="2rem",
                                    ),
                                    value="fy2023",
                                ),
                                default_value="fy2025",
                                width="100%",
                            ),
                        ),
                        width="70vw",
                        p="4",
                        padding="4rem",
                    ),
                    width="100%",
                    justify_content="center",
                    align_items="center"
                ),
                footer(),
            ),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("Investor Relations"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Welcome to our Investor Relations page. Here you can find our annual reports and financial documents organized by fiscal year.",
                            style=mobile_paragraph_style,
                            margin_bottom="1rem",
                        ),
                        rx.tabs.root(
                            rx.tabs.list(
                                rx.tabs.trigger("FY 2025-26", value="fy2025"),
                                rx.tabs.trigger("FY 2024-25", value="fy2024"),
                                rx.tabs.trigger("FY 2023-24", value="fy2023"),
                            ),
                            rx.tabs.content(
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell(
                                                "S.No.",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Quarter",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Standalone",
                                                style=table_header_style,
                                            ),
                                        ),
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.cell("1", style=table_cell_style),
                                            rx.table.cell("First Quarter", style=table_cell_style),
                                            rx.table.cell(
                                                rx.button(
                                                    "Download",
                                                    style=download_button_style,
                                                    on_click=rx.download(url="/bmo.pdf"),
                                                )
                                            ),
                                        ),
                                    ),
                                    width="100%",
                                    margin_bottom="1rem",
                                ),
                                value="fy2025",
                            ),
                            rx.tabs.content(
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell(
                                                "S.No",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Document",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Download",
                                                style=table_header_style,
                                            ),
                                        ),
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.cell("1", style=table_cell_style),
                                            rx.table.cell("Audited Financial 31st March 2025", style=table_cell_style),
                                            rx.table.cell(
                                                rx.button(
                                                    "Download",
                                                    style=download_button_style,
                                                    on_click=rx.download(url="/obm.pdf"),
                                                )
                                            ),
                                        ),
                                    ),
                                    width="100%",
                                    margin_bottom="1rem",
                                ),
                                value="fy2024",
                            ),
                            rx.tabs.content(
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell(
                                                "S.No",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Document",
                                                style=table_header_style,
                                            ),
                                            rx.table.column_header_cell(
                                                "Download",
                                                style=table_header_style,
                                            ),
                                        ),
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.cell("1", style=table_cell_style),
                                            rx.table.cell("Annual Report", style=table_cell_style),
                                            rx.table.cell(
                                                rx.button(
                                                    "Download",
                                                    style=download_button_style,
                                                    on_click=rx.download(url="/ar.pdf"),
                                                )
                                            ),
                                        ),
                                    ),
                                    width="100%",
                                    margin_bottom="1rem",
                                ),
                                value="fy2023",
                            ),
                            default_value="fy2025",
                            width="100%",
                        ),
                    ),
                    width="100%",
                    p="2",
                    padding="1rem",
                ),
                footer(),
            ),
            width="100%",
        ),
        width="100%",
        margin="0",
        padding="0",
    )