from django.test import TestCase
from owner.models import Video, Business, Tag

# Create your tests here.
class BasicTestCase(TestCase):
    def set_up(self):
        Video.objects.create(title='epic', num_views=5)
    def test_if_title_works(self):
        epic = Video.objects.get(title='epic')
        self.assertEqual(epic.get_title(), 'epic')

