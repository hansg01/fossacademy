from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
  url(r'^create/$', 'content.views.create_page',
      name='page_create'),
  url(r'^index/page/(?P<counter>\d+)/up/$', 'content.views.page_index_up',
      name='page_index_up'),
  url(r'^index/page/(?P<counter>\d+)/down/$', 'content.views.page_index_down',
      name='page_index_down'),
  url(r'^index/link/(?P<counter>\d+)/up/$', 'content.views.link_index_up',
      name='link_index_up'),
  url(r'^index/link/(?P<counter>\d+)/down/$', 'content.views.link_index_down',
      name='link_index_down'),                       
  url(r'^sign-up/$', 'content.views.sign_up',
      name='sign_up'),
  url(r'^sign-up/comment/$', 'content.views.comment_sign_up',
      name='sign_up_comment'),
  url(r'^sign-up/comment/(?P<comment_id>\d+)/edit/$', 'content.views.edit_comment_sign_up',
      name='sign_up_edit_comment'),
  url(r'^sign-up/comment/(?P<comment_id>\d+)/reply/$', 'content.views.comment_sign_up',
      name='sign_up_reply'),
  url(r'^sign-up/comment/(?P<comment_id>\d+)/add_participant/$', 'content.views.accept_sign_up',
      name='sign_up_add_participant'),
  (r'^sign-up/comment/(?P<comment_id>\d+)/add_organizer/$', 'content.views.accept_sign_up',
      {'as_organizer': True}, 'sign_up_add_organizer'),
  url(r'^(?P<page_slug>[\w-]+)/$', 'content.views.show_page',
      name='page_show'),
  url(r'^(?P<page_slug>[\w-]+)/(?P<pagination_page>\d+)/$', 'content.views.show_page',
      name='page_show'),
  url(r'^(?P<page_slug>[\w-]+)/edit/$', 'content.views.edit_page',
      name='page_edit'),
  url(r'^(?P<page_slug>[\w-]+)/delete/$', 'content.views.delete_page',
      name='page_delete'),
  url(r'^(?P<page_slug>[\w-]+)/comment/$', 'content.views.comment_page',
      name='page_comment'),
  url(r'^(?P<page_slug>[\w-]+)/comment/(?P<comment_id>\d+)/$', 'content.views.show_comment',
      name='comment_show'),
  url(r'^(?P<page_slug>[\w-]+)/comment/(?P<comment_id>\d+)/edit/$', 'content.views.edit_comment',
      name='comment_edit'),
  url(r'^(?P<page_slug>[\w-]+)/comment/(?P<comment_id>\d+)/delete/$', 'content.views.delete_restore_comment',
      name='comment_delete'),
  url(r'^(?P<page_slug>[\w-]+)/comment/(?P<comment_id>\d+)/restore/$', 'content.views.delete_restore_comment',
      name='comment_restore'),
  url(r'^(?P<page_slug>[\w-]+)/comment/(?P<comment_id>\d+)/reply/$', 'content.views.comment_page',
      name='comment_reply'),
  url(r'^(?P<page_slug>[\w-]+)/history/$', 'content.views.history_page',
      name='page_history'),
  url(r'^(?P<page_slug>[\w-]+)/history/(?P<version_id>\d+)/$', 'content.views.version_page',
      name='page_version'),
  url(r'^(?P<page_slug>[\w-]+)/history/(?P<version_id>\d+)/restore/$', 'content.views.restore_version',
      name='version_restore'),
)
