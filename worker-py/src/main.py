import asyncio
import os

import httpx

API_URL = os.getenv("API_URL", "http://incident-api:8080")
INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "30"))


async def tick() -> None:
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{API_URL}/healthz")
            print("healthz", resp.status_code)
        except Exception as exc:
            print("healthz_error", str(exc))


async def main() -> None:
    while True:
        await tick()
        await asyncio.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(main())
