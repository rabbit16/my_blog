from django.db import models
from utils.ModelBases import ModelBase
# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name='标签',help_text='输入标签',max_length=64)
    class Meta:
        verbose_name = '标签'
        db_table = 'db_tag'
        verbose_name_plural = verbose_name

class Article(ModelBase):
    title = models.CharField(verbose_name='文章标题',help_text='文章标题',max_length=150)
    content = models.TextField(verbose_name='文章内容',help_text='文章标题')
    abstract = models.TextField(verbose_name='摘要',help_text='文章标签',default=None)
    click = models.IntegerField(verbose_name='点击量',help_text='点击量',default=0)
    like_num = models.IntegerField(verbose_name='点赞数',help_text='点赞数',default=0)
    tag = models.ForeignKey('Tag',on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering=['-update_time','-id']
        db_table = 'tb_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Comments(ModelBase):
    content = models.TextField(verbose_name='评论',help_text='评论')
    author = models.ForeignKey('user.User',on_delete=models.SET_NULL,null=True)
    article = models.ForeignKey('blog.Article',on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_comment"  # 指明数据库表名
        verbose_name = "评论"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def to_dict_data(self):
        comment_dict = {
            'news_id': self.article.id,
            'content_id': self.id,
            'content': self.content,
            'author': self.author.username,
            'update_time': self.update_time.strftime('%Y年%m月%d日 %H:%M'),
            'parent': self.parent.to_dict_data() if self.parent else None,#这个想法是一个递归，这个需要重点掌握。
        }
        return comment_dict







