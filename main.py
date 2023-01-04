import uvicorn
from api import api_app
from Config import Settings


def main():
    settings = Settings()
    uvicorn.run(api_app, host="127.0.0.1", port=settings.app_port, log_level="info")


if __name__ == '__main__':
    main()
