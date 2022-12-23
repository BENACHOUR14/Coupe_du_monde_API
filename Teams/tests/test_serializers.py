from django.test import TestCase
from Teams.serializers import TeamSerializer
from Teams.models import Teams
from Teams.tests.factory import TeamsFactory

class TeamSerializerTestCase(TestCase):
      def test_serializer(self):
        team = Teams.objects.create(name='Maroc', group='H', is_eliminated=False)
        serializer = TeamSerializer(team)
        self.assertEqual(list(serializer.data.keys()), ["id", "name", "group", "is_eliminated"])
        self.assertEqual(str(team.id), serializer.data["id"])
        self.assertEqual(team.name, serializer.data["name"])
        self.assertEqual(team.group, serializer.data["group"])
        self.assertEqual(team.is_eliminated, serializer.data["is_eliminated"])
        
      def test_serializer_required_fields(self):
        serializer = TeamSerializer(data={'name': '', 'group': '', 'is_eliminated':''}) 
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("name")[0].code, "blank")
        self.assertEqual(serializer.errors.get("group")[0].code, "invalid_choice")
        self.assertEqual(serializer.errors.get("is_eliminated")[0].code, "invalid")
        
      def test_serializer_unique_fields(self):
        team = TeamsFactory()
        serializer = TeamSerializer(data={'name': team.name})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("name")[0].code, "unique")
        
      def test_serializer_invalid_fields(self):
        serializer = TeamSerializer(data={'name':'Test', 'group':'Z'})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("group")[0].code, "invalid_choice")
        
      def test_serializer_required(self):
        serializer = TeamSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("name")[0].code, "required")
        self.assertEqual(serializer.errors.get("group")[0].code, "required")
