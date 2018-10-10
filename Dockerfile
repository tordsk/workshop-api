FROM python
ENV FLASK_ENV=development
ENV POD_NAME='pod-123'
ENV NAMESPACE='tord-kloster'
WORKDIR app
COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "run_app.py"]
