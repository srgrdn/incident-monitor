# Incident Monitor (App Repo)

Учебный, но близкий к реальности проект для практики Kubernetes + GitHub Actions + Argo CD.

## Компоненты

- `api-go` — Go API для приема событий и выдачи состояния сервисов.
- `worker-py` — Python worker, который периодически проверяет целевые URL и отправляет события в API.
- `deploy/k8s` — локальные манифесты/оверлеи (можно использовать для smoke-локального деплоя).

## Целевой GitOps поток

1. Изменения кода в этом репозитории.
2. GitHub Actions собирает образы и пушит в GitHub Container Registry (GHCR).
3. CI обновляет теги образов в отдельном GitOps-репозитории.
4. Argo CD синхронизирует кластер из GitOps-репозитория.

## GitHub Actions secrets

Нужно добавить переменную проекта:

- `GITOPS_PUSH_TOKEN` — GitHub PAT с доступом `repo` для `incident-monitor-gitops`.
