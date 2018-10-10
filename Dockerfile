FROM python:alpine
ENV FLASK_ENV=development
ENV POD_NAME='[Set by using environment variables]'
ENV NAMESPACE='[Set by using environment variables]'
WORKDIR app
COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "run_app.py"]
