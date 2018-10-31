from django.utils.text import slugify


def get_unique_slug(self, table, *args, **kwargs):
    slug = slugify(self.title)
    try:
        if table.objects.get(slug=slug):
            tb_ob = table.objects.latest('id')
            slug += '-'+str(tb_ob.id)
    except table.DoesNotExist:
        pass
    return slug
