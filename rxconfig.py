import reflex as rx

config = rx.Config(
    app_name="genomicvalley",
    db_url="sqlite:///reflex.db",
    frontend_port=53212,
    backend_port=58212,
    cors_allowed_origins=["*"],
)


# Create your app instance with this config
app = rx.App(config=config)
