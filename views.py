from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Optional: Import your ML model function
# We'll add actual model integration later
# from .ml_model import predict_winner

class PredictMatch(APIView):
    def post(self, request):
        # Get input data from the request
        team1 = request.data.get("team1")
        team2 = request.data.get("team2")
        venue = request.data.get("venue")

        # For now, we'll return a dummy response
        # Later, you will call your model here

        result = {
            "team1": team1,
            "team2": team2,
            "venue": venue,
            "predicted_winner": team1  # dummy output
        }

        return Response(result, status=status.HTTP_200_OK)
