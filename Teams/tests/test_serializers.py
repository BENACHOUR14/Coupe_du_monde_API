from django.test import TestCase
from Teams.serializers import TeamSerializer
from Teams.models import Teams



class TeamSerializerTestCase(TestCase):
      def test_serializer(self):
        team = Teams.objects.create(name='Maroc', group='H', is_eliminated=False)
        serializer = TeamSerializer(team)
        self.assertEqual(list(serializer.data.keys()), ["id", "name", "group", "is_eliminated"])
        self.assertEqual(str(team.id), serializer.data["id"])
        self.assertEqual(team.name, serializer.data["name"])
        self.assertEqual(team.group, serializer.data["group"])
        self.assertEqual(team.is_eliminated, serializer.data["is_eliminated"])
