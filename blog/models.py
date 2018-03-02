from django.db import models
from accounts.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s#%s' % (slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    content = models.TextField()

    def __str__(self):
        return self.post.title+'=>'+self.user.email
