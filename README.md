## How run system
```shell
docker build -t bewise_flask_image:develop .;
docker-compose -f ./docker/docker-compose.yaml up -d
```

Пример запроса:
    
    form = {"questions_num": 1}
    
    response = requests.post("http://127.0.0.1:5000/questions", json=form)
    
    print(response)

Пример ответа:

    [
        {
            "create_date": "Mon, 16 Oct 2023 20:20:33 GMT",
            "id": 1,
            "question_answer": "an anchor",
            "question_created_at": "Fri, 30 Dec 2022 19:47:20 GMT",
            "question_id": 114836,
            "question_text": "The three elements that make up the Marine Corps seal are a globe, an eagle holding a scroll & this naval symbol",
            "update_date": "Mon, 16 Oct 2023 20:20:33 GMT"
        }
    ]
