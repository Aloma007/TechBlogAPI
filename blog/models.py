from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # Basic fields
    title = models.CharField(max_length=250)
    content = models.TextField()

    # The Slug: This generates our clean URLs (e.g., /how-to-learn-django/)
    slug = models.SlugField(max_length=250, unique=True)

    # Foreign Key: Links this post to a specific User (One-to-Many)
    # on_delete=models.CASCADE means if the user is deleted, their posts are deleted too
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Foreign Key: Links this comment to a specific Post
    # related_name='comments' allows us to easily fetch all comments for a post later
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    # Foreign Key: Links this comment to the User who wrote it
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # The actual comment text
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"