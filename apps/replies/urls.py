from django.conf.urls.defaults import patterns, url

scope_url = (r'(?P<scope_model>[\w ]+)/(?P<scope_app_label>[\w ]+)/' +
    '(?P<scope_pk>\d+)')
page_url = (r'(?P<page_model>[\w ]+)/(?P<page_app_label>[\w ]+)/' +
    '(?P<page_pk>\d+)')

urlpatterns = patterns('replies.views',
  url(r'^create/%s/%s/$' % (scope_url, page_url), 'comment_page',
      name='page_comment'),
  url(r'^(?P<comment_id>\d+)/$', 'show_comment',
      name='comment_show'),
  url(r'^(?P<comment_id>\d+)/edit/$', 'edit_comment',
      name='comment_edit'),
  url(r'^(?P<comment_id>\d+)/delete/$', 'delete_restore_comment',
      name='comment_delete'),
  url(r'^(?P<comment_id>\d+)/restore/$', 'delete_restore_comment',
      name='comment_restore'),
  url(r'^(?P<comment_id>\d+)/reply/$', 'reply_comment',
      name='comment_reply'),
)
