from Setup import Setup
from RepoHandler.RepoHandler import RepoHandler

if __name__ == "__main__":
    # validate python version and packages and update the neu repo
    Setup.setup()

    # get all forge items
    repoPath = "vendor/neu-repo"
    repoHandler = RepoHandler(repoPath)
    forgeItems = repoHandler.getForgeItems()
    print("\n")

    test = forgeItems["AMBER_POLISHED_DRILL_ENGINE"]
    print(test)