import json
import progressbar

from FileHandler import FileHandler

class RepoHandler:

    def __init__(self, path: str) -> None:
        self.path = path
    
    def getForgeItems(self) -> list:
        print("Retrieving all item names")
        itemPath = self.path + "/items"
        fileNames = FileHandler.getFileNames(itemPath)
        forgeItems = []

        # progress bar
        print("\nFiltering forge items")
        widgets = ['[', progressbar.Percentage(), '] Processed ', progressbar.SimpleProgress(), ' files']
        bar = progressbar.ProgressBar(maxval=len(fileNames), widgets=widgets).start()

        # filter items:
        # every forge item has a list of recipes, if one recipe has the 
        # 'type' of 'forge' its a forge item
        for index, fileName in enumerate(fileNames):
            content: object = RepoHandler.getJsonContent(itemPath + "/" + fileName)
            add: bool = False
            recipeObject = {}

            if RepoHandler.containsKey(content, "recipes"):
                for recipe in content["recipes"]:
                    if RepoHandler.containsKey(recipe, "type"):
                        if recipe["type"] == "forge":
                            recipeObject["name"] = fileName[:-5] # remove '.json'
                            recipeObject["recipe"] = recipe
                            add = True

            if add: 
                forgeItems.append(recipeObject)
            
            bar.update(index + 1);

        bar.finish()
        return forgeItems

    @classmethod
    def getJsonContent(cls, path: str) -> object:
        if path.endswith(".json"):
                with open(path, 'rb') as file:
                    return json.load(file)

    @classmethod     
    def containsKey(cls, jsonObject: object, key: str) -> bool:
        return key in jsonObject.keys()



if __name__ == "__main__":
    repoHandler = RepoHandler("vendor/neu-repo")
    forgeItems = repoHandler.getForgeItems()
    print(len(forgeItems))