from django.contrib import admin
from EnsPost.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','publishing_date']  # post listesinde tarih ve vaşlık görünsün
    list_display_links = ['publishing_date'] # tarihe ve başlığa tıklayıp içine girilebilsin
    list_filter = ['publishing_date'] # filtreleme eklendi
    search_fields = ['title', 'content'] # arama çubuğu eklendi
    list_editable = ['title'] # listeden başlıkları değiştirmek için 

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
