from django.db import models


class Article(models.Model):
    article_id = models.IntegerField(verbose_name='文章ID')
    title = models.CharField(verbose_name='标题', max_length=20)
    content = models.TextField(verbose_name='正文', max_length=3000, null=True, blank=True)
    editor_id = models.CharField(verbose_name='编辑者ID', max_length=15)
    edit_time = models.DateTimeField(verbose_name='编辑时间')

    def __str__(self):
        return str(self.title) + "-" + str(self.editor_id)

    class Meta:
        unique_together = ('article_id', 'edit_time')
        verbose_name = '文章'
        verbose_name_plural = '文章列表'


class column(models.Model):
    name = models.CharField(verbose_name='栏目名称', max_length=20)
    superior = models.ForeignKey('self', verbose_name='上级栏目', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        unique_together = ('name', 'superior')
        verbose_name = '栏目'
        verbose_name_plural = '栏目列表'
