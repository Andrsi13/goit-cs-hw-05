import asyncio
import logging
from pathlib import Path
from aiofiles import open as aio_open
from aiofiles.os import wrap

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


async def copy_file(source, destination):
    try:
        async with aio_open(source, "rb") as src_file:
            content = await src_file.read()
            async with aio_open(destination, "wb") as dst_file:
                await dst_file.write(content)
    except Exception as e:
        logger.error(f"Error copying {source} to {destination}: {e}")


async def create_directory(directory):
    try:
        await wrap(directory.mkdir)(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(f"Error creating directory {directory}: {e}")


async def process_files(source_dir, target_dir):
    tasks = []
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    for file_path in source_path.rglob("*.*"):
        file_extension = file_path.suffix[
            1:
        ].lower()  # Отримати розширення файлу без крапки
        target_folder = target_path / file_extension
        target_file = target_folder / file_path.name

        if not target_folder.exists():
            await create_directory(target_folder)

        task = asyncio.create_task(copy_file(file_path, target_file))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python task1.py <source_dir> <target_dir>")
        sys.exit(1)

    source_dir = sys.argv[1]
    target_dir = sys.argv[2]

    asyncio.run(process_files(source_dir, target_dir))
