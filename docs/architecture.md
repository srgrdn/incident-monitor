# Architecture (MVP)

## Поток данных

1. `worker-py` читает список проверяемых сервисов (из API или конфигурации).
2. Worker делает HTTP-check (status/latency).
3. Worker отправляет событие в `api-go` (`POST /events`).
4. API сохраняет событие и обновляет агрегированный статус сервиса в Postgres.

## MVP endpoints

- `GET /healthz`
- `POST /events`
- `GET /services`
- `GET /services/{id}/status`

## MVP таблицы

- `services`
- `checks`
- `incidents`
