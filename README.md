# Incident Monitor (App Repo)

Учебный, но близкий к реальности проект для практики Kubernetes + GitLab CI + Argo CD.

## Компоненты

- `api-go` — Go API для приема событий и выдачи состояния сервисов.
- `worker-py` — Python worker, который периодически проверяет целевые URL и отправляет события в API.
- `deploy/k8s` — локальные манифесты/оверлеи (можно использовать для smoke-локального деплоя).

## Целевой GitOps поток

1. Изменения кода в этом репозитории.
2. GitLab CI собирает образы и пушит в GitLab Container Registry.
3. CI обновляет теги образов в отдельном GitOps-репозитории.
4. Argo CD синхронизирует кластер из GitOps-репозитория.

## GitLab CI variables

Нужно добавить переменную проекта:

- `GITOPS_PUSH_TOKEN` — PAT/Project Access Token для `incident-monitor-gitops` с `write_repository`.
