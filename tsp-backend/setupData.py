import django, os
django.setup()
from api.models import Point


def main():
    rssFile = open("cityPoints.txt", "r")
    lines = rssFile.readlines()
    count = 1
    for line in lines:
        try:
            if "\n" in line:
                line = line.replace("\n","")
            Point.objects.create(id=count, name=line)
            count = count + 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    main()
