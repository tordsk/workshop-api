FROM python
ENV development
WORKDIR app
COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "./run_app.py"]
