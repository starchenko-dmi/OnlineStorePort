from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:post_list')

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')