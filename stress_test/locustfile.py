from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO

    @task(3)
    def index(self):
        self.client.get("/")

    @task
    def predict(self):
        files = [("file", ("dog.jpeg", open("dog.jpeg", "rb"), "image/jpeg"))]
        headers = {}
        payload = {}
        self.client.post(
            "/predict",
            headers=headers,
            data=payload,
            files=files
        )
