from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q
from .forms import SearchForm
from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DeleteView):
    model = Post
    template_name = 'blog/post.html'


class SearchFormView(generic.View):
    form_class = SearchForm
    template_name = 'blog/search.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        search = form.data['search']

        posts = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        return render(request, 'blog/index.html', {
            'object_list': posts
        })


class PostLikeView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        print(slug)
        obj = get_object_or_404(Post, slug=slug)
        link = obj.get_absolute_url()
        user = self.request.user
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
        return link
