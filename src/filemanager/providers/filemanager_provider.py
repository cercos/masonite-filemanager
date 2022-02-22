"""A FileManagerProvider Service Provider."""

import os
import pathlib
from masonite.packages import PackageProvider

class FileManagerProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("filemanager")
            .name("filemanager")
            .config("config/filemanager.py", publish=True)
            .views("templates", publish=False)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
