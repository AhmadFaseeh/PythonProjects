import os

class ClearTheCulture:
    def Create(self):
        if (not os.path.exists("lala")):
            os.mkdir("lala")
        for i in range(0,5):
            os.mkdir(f"lala/sdahfhjk {i+1}")

    def rename(self):
        for i in range (0,5):
            os.rename(f"lala/sdahfhjk {i+1}", f"lala/1.png {i+1}")

obj = ClearTheCulture()
obj.Create()
#obj.rename()