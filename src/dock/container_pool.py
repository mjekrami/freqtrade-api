from docker import DockerClient
from schema import ContainerSchema

from docker.errors import NotFound


class ContainerPool:
    def __init__(self) -> None:
        self.client = DockerClient("unix:///var/run/docker.sock")

    def get_running_bots(self) -> list[ContainerSchema]:
        containers = self.client.containers.list()
        res = []
        for container in containers:
            if container.name != "freqtrade-api":
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
            if container.name != "freqtrade-api":
                res.append(
                    ContainerSchema(
                        container_id=container.id,
                        name=container.name,
                        status=container.status,
                    )
                )
        return res

    def get_bot_by_name(self, name: str):
        try:
            container = self.client.containers.get(name)
            container_name = container.attrs["Name"]
            return container_name.strip("/")
        except NotFound:
            raise f"Container with name {name} was not found"
