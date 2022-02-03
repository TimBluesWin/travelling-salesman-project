import django, os, json
from urllib.request import urlopen
import csv  
django.setup()
from api.models import Point

def main():
    header = ['id', 'method', 'total']
    data = ['Afghanistan', 652090, 'AF', 'AFG']

    with open('results.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        for value in Point.objects.all():
            with urlopen(f"http://127.0.0.1:8000/api/cheapestinsertion/?q={value.id}") as url:
                cheapest = json.loads(url.read().decode())
                cheapest = cheapest["distance"]
                print(cheapest)
            writer.writerow([value.id, "CheapestIns", cheapest])
            with urlopen(f"http://127.0.0.1:8000/api/nneighbour/?q={value.id}") as url:
                cheapest = json.loads(url.read().decode())
                cheapest = cheapest["distance"]
                print(cheapest)
            writer.writerow([value.id, "NNeighbour", cheapest])
            with urlopen(f"http://127.0.0.1:8000/api/rinsertion/?q={value.id}") as url:
                cheapest = json.loads(url.read().decode())
                cheapest = cheapest["distance"]
                print(cheapest)
            writer.writerow([value.id, "RandomIns", cheapest])
            with urlopen(f"http://127.0.0.1:8000/api/christofidesalgorithm/?q={value.id}") as url:
                cheapest = json.loads(url.read().decode())
                cheapest = cheapest["distance"]
                print(cheapest)
            writer.writerow([value.id, "Christofides", cheapest])
            with urlopen(f"http://127.0.0.1:8000/api/googleor/?q={value.id}&optimize=0") as url:
                cheapest = json.loads(url.read().decode())
                cheapest = cheapest["distance"]
                print(cheapest)
            writer.writerow([value.id, "GoogleOR", cheapest])


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    main()
