from django.db import models
from django.utils.timezone import now
from user.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=10, null=False, verbose_name="카테고리 이름")

    def __str__(self):
        return self.cat_name


class Board(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, verbose_name="카테고리")
    bd_name = models.CharField(max_length=10, null=False, verbose_name="게시판 이름")
    bd_right = models.BooleanField(null=True, default=False, verbose_name="게시판 열람 권한")

    def __str__(self):
        return self.bd_name


class Post(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, verbose_name="카테고리")
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, null=False, verbose_name="게시판")
    post_notice = models.BooleanField(null=True, default=False, verbose_name="게시물 공지여부")
    post_name = models.CharField(max_length=50, null=False, verbose_name="게시물 제목")
    post_modifydate = models.DateTimeField(default=now, verbose_name="게시물 등록(수정)일")
    #    post_deletedate = models.DateTimeField(null=True, verbose_name="게시물 삭제일")
    post_content = RichTextUploadingField(null=False, verbose_name="게시물 내용")

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, verbose_name="게시물 번호")
    reply_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name="대댓글")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="댓글 작성자")
    cmt_content = models.CharField(max_length=200, blank=False, verbose_name="댓글 내용")
    cmt_history = models.CharField(max_length=200, blank=False, verbose_name="댓글 수정 내역")
    cmt_modifydate = models.DateTimeField(default=now, verbose_name="댓글 등록(수정)일")
#    cmt_deletedate = models.DateTimeField(null=True, verbose_name="댓글 삭제일")
