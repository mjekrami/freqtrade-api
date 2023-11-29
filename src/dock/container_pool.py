from docker import DockerClient
from schema import ContainerSchema


class ContainerPool:
    def __init__(self) -> None:
        self.client = DockerClient("unix:///var/run/docker.sock")

    def get_running_bots(self) -> list[ContainerSchema]:
        containers = self.client.containers.list()
        res = []
        for container in containers:
            res.append(
                ContainerSchema(
                    container_id=container.id,
                    name=container.name,
                    status=container.status,
                )
            )
        return res

    def get_bot_by_id(self, id: str) -> ContainerSchema:
        container = self.client.containers.get(id)
        if container:
            return ContainerSchema(
                container_id=container.id, name=container.name, status=container.status
            )
        raise ValueError(f"container with id {id} not found")

    def get_bot_by_status(self, status: str) -> ContainerSchema:
        containers = self.client.containers.list(filters={"status": status})
        res = []
        for container in containers:
            res.append(
                ContainerSchema(
                    container_id=container.id,
                    name=container.name,
                    status=container.status,
                )
            )
        return res
