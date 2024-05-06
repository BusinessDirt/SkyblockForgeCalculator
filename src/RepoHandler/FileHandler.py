import os
import progressbar

class FileHandler:
    
    @classmethod
    def getFileNames(cls, path: str) -> list:
        """
        Get all file names in a folder.

        Args:
        - path: The path to the folder

        Returns:
        - A list of file names
        """
        absolutePath = os.path.abspath(path)
        fileNames = []
        files = os.listdir(absolutePath)
        totalFiles = sum(1 for _ in files if os.path.isfile(os.path.join(absolutePath, _)))

        # progress bar
        widgets = ['[', progressbar.Percentage(), '] Processed ', progressbar.SimpleProgress(), ' files']
        bar = progressbar.ProgressBar(maxval=totalFiles, widgets=widgets).start()

        for index, fileName in enumerate(files):
            if os.path.isfile(os.path.join(absolutePath, fileName)):
                fileNames.append(fileName)
                bar.update(index + 1)
        bar.finish()

        return fileNames
    
if __name__ == "__main__":
    print("Getting all Item filenames")
    fileNames = FileHandler.getFileNames("vendor/neu-repo/items")
