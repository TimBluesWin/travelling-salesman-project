from api.models import Point
import copy
import json, os
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class SearchRouteAPI:
    def __init__(self):
        super().__init__()

    def create_data_model(self, q):
        """Stores the data for the problem."""
        data = {}
        path = os.path.dirname(__file__)
        file = open(path + '/matrix.json')
        distanceData = json.load(file)
        matrix=[]
        for i in distanceData:
            distances = []
            for distance in i:
                distances.append(float(distance))
            matrix.append(distances)
        file.close()
        data['distance_matrix'] = matrix
        data['num_vehicles'] = 1
        data['depot'] = 0
        data['starts'] = [int(q) - 1]
        data['ends'] = [int(q) - 1]
        return data

    def get_results(self, manager, routing, solution):
        resultList = []
        index = routing.Start(0)
        pointName = Point.objects.get(id=(manager.IndexToNode(index) + 1))
        point = {"id": int(manager.IndexToNode(index) + 1), "name": pointName.name, "distance": 0}
        resultList.append(point)
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            id = index + 1
            pointName = Point.objects.get(id=(manager.IndexToNode(index) + 1))
            point = {
                "id": manager.IndexToNode(index) + 1,
                "name": pointName.name,
                "distance": routing.GetArcCostForVehicle(previous_index, index, 0),
            }
            resultList.append(point)
        return resultList

    def googleOrApi(self, q):
        """Entry point of the program."""
        # Instantiate the data problem.
        data = self.create_data_model(q)

        # Create the routing index manager.
        # matrix = [
        #     [0, 25, 15, 45],
        #     [25, 0, 20, 35],
        #     [15, 20, 0, 30],
        #     [45, 35, 30, 0]
        # ]
        # data = {}
        # path = os.path.dirname(__file__)
        # file = open(path + '/matrix.json')
        # data = json.load(file)
        # matrix=[]
        # for i in data:
        #     distances = []
        #     for distance in i:
        #         distances.append(float(distance))
        #     matrix.append(distances)
        # file.close()
        # file.close()
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)


        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        results = []

        # Print solution on console.
        if solution:
            results = self.get_results(manager, routing, solution)
        
        return results


def googleOr(q):
    api = SearchRouteAPI()
    return api.googleOrApi(q)
