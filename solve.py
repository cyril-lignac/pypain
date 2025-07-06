import zipfile, os

def main():
    with zipfile.ZipFile("pypain_extracted/PYZ-00.pyz") as z:
        print(z.namelist())
        print(z)
        with z.open('test.bin') as f:
            print(f.name)

main()