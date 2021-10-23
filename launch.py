# Modules
from app import app

# Run server
app.run(
    host = "0.0.0.0",
    port = 8080,
    debug = True
)
