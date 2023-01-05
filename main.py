import sys
from streamlit.web import cli as stcli
import uvicorn
from api import api_app
from Config import Settings
import multiprocessing


def server_api():
    settings = Settings()
    uvicorn.run(api_app, host="127.0.0.1", port=settings.app_port, log_level="info")


def streamlit_app():
    sys.argv = ["streamlit", "run", "streamlit_app.py"]
    sys.exit(stcli.main())


def main():
    api = multiprocessing.Process(target=server_api)
    st_app = multiprocessing.Process(target=streamlit_app)
    api.start()
    st_app.start()


if __name__ == '__main__':
    main()
