import runpy


def main():
    runpy.run_path("etl/extract.py") #EXTRACT
    runpy.run_path("etl/transform.py") 



if __name__ == "__main__":
    main()