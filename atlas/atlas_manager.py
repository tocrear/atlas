import os
import json
import click


class AtlasManagerError(Exception):
    """Error when calling atlas manager class functions"""


class AtlasManager:

    def __init__(self, system_root_folder=None):
        self.project_json = "atlas_project.json"
        self.project_folder = "manager"
        if system_root_folder is None:
            self.system_root_folder = self.get_system_root_folder_path()
        else:
            self.system_root_folder = system_root_folder
            tmp_info = {"project_root_path": self.system_root_folder}
            self.save_info_to_project_json(tmp_info)

        json_folder_path_ = os.path.join(self.project_folder, self.project_json)
        self.project_json_path = os.path.join(
            self.system_root_folder, json_folder_path_
        )

    def get_system_root_folder_path(self):
        """Get system root folder

        Parameters
        ----------

        Returns
        -------
        : bool
        """
        from .utils.system_utils import get_root_dir
        from config.atlas_config import ATLAS_HIDDEN_DIRECTORY

        root_dir = get_root_dir()
        root_hidden_file = os.path.join(root_dir, ATLAS_HIDDEN_DIRECTORY)
        return root_hidden_file

    def save_info_to_project_json(self, info: dict) -> True:
        """Saves information to project json file.

        Parameters
        ----------
        info:  dict
            information to  be save into json file.

        Returns
        -------
        : bool
        """
        if os.path.isfile(self.project_json_path):
            click.secho(f"Atlas has aready being intialized!", fg="red")
            return

        try:
            with open(self.project_json_path, "w") as json_file:
                json.dump(info, json_file)
            return True
        except:
            raise AtlasManagerError(f"Error saving information to {self.project_json}.")
