# ModelMeta-DB
Establish REST APIs for DB and services to manage ML Models.

### Usage

1. Model Image Build

```bash
docker build -t baek/ml-system-in-actions:model_db_0.0.1 -f Dockerfile .
```

2. Docker Compose

```bash
docker-compose -f ./docker-compose.yml up -d
```

3. Check ModelMeta-DB

Open browser, and go to `localhost:8000/docs`.

4. Stop ModelMeta-DB

```bash
docker-compose -f ./docker-compose.yml down
```