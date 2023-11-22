import argparse
from app.guardar_agentes_cloud import guardar_agentes_cloud
from app import app


email = "michluna@cisco.com"
auth_token = "l2qxth9d44cgqrp5n4xgyvi845ekxodh"
guardar_agentes_cloud(email, auth_token)

if __name__ == "__main__":
    app.run(debug=True)
