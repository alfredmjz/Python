class VisualizeTraffic:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def display(self):
        while (self.up != 0) and (self.down != 0) and (self.left != 0) and (self.right != 0):
            print("\t| \t |\t",
                  "\t| \t |\t",
                f"\t|   {self.up}\t |\t",
                sep="\n")
            print("________|\t |________",
                "\t\t\t",
                f" {self.left}\t\t\t{self.right}",
                "________\t  ________",
                sep="\n")
            print("\t| \t |\t",
                f"\t|   {self.down}\t |\t",
                "\t| \t |\t",
                "\t| \t |\t",
                sep="\n")