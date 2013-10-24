from django.views.generic import ListView
from .models import Post

class PostsView(ListView):
    template_name = 'posts.html'
    model = Post

    def get_queryset(self):
        return self.model.objects.published()
