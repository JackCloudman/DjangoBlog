from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import hashlib,os
from tagging.fields import TagField
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

def update_filename(instance, filename):
    path = "img"
    fileName, fileExtension = os.path.splitext(filename)
    filename = filename+str(timezone.now())
    name = hashlib.sha256((filename).encode()).hexdigest()+fileExtension
    path  = os.path.join(path, name)
    return path
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,null=True)
    descripcion = models.CharField(max_length=200)
    foto_encabezado = models.ImageField(upload_to=update_filename,null=True,blank=True)
    contenido = MarkdownxField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True,null=True)
    tags = TagField(null=True)
    post_views=models.IntegerField(default=0)
    @property
    def publicar(self):
        if not self.slug:
            self.slug = slugify(self.titulo)
        self.fecha_creado = timezone.now()
        self.save()
    def formatted_markdown(self):
        return markdownify(self.contenido)
    '''def get_description(self):
        text = markdownify(self.text)
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', text)
        return cleantext[:125]+"..."'''
    def __str__(self):
        return self.titulo
# Create your models here.
