from django.test import TestCase

# Create your tests here.
from codesnug_2.auth.models import CodesnugUser
from codesnug_2.goals.models import Tag, Workspace, Goal


class GoalTestCaseBase(TestCase):
    def setUp(self):
        self.user1 = CodesnugUser.objects.create_user('prueba@prueba.com', '1111')
        self.user2 = CodesnugUser.objects.create_user('prueba2@prueba2.com', '1111')

        self.tag1 = Tag.objects.create(title="tag1", owner=self.user1)
        self.tag2 = Tag.objects.create(title="tag2", owner=self.user2)

        self.workspace1 = Workspace.objects.create(title="workspace1", owner=self.user1)
        self.workspace2 = Workspace.objects.create(title="workspace2", owner=self.user2)

        self.goal1 = Goal.objects.create(title="Goal 1", description="Description 1", owner=self.user1)
        self.goal1.tags.add(self.tag1)
        self.goal1.workspaces.add(self.workspace1)


class TagTestCase(GoalTestCaseBase):
    def test_create_tags(self):
        tag1 = Tag.objects.get(title="tag1")
        tag2 = Tag.objects.get(title="tag2")
        self.assertIsNotNone(tag1)
        self.assertIsNotNone(tag2)


class WorkspaceTestCase(GoalTestCaseBase):
    def test_create_workspaces(self):
        workspace1 = Workspace.objects.get(title="workspace1")
        workspace2 = Workspace.objects.get(title="workspace2")
        self.assertIsNotNone(workspace1)
        self.assertIsNotNone(workspace2)


class GoalTestCase(GoalTestCaseBase):
    def test_create_goals(self):
        goal1 = Goal.objects.get(title="Goal 1")
        self.assertIsNotNone(goal1)
        self.assertEqual(goal1.tags.count(), 1)
        self.assertEqual(goal1.workspaces.count(), 1)
