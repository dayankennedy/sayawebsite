from django.forms import ModelForm
from .models import Post



class CommentForm(ModelForm):
    class Meta:
        model =Post
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs["placeholder"] = "Your comment"






