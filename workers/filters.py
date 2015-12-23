# from django.db import models
# from django.contrib.admin.filterspecs import FilterSpec, ChoicesFilterSpec,DateFieldFilterSpec
# from django.utils.encoding import smart_unicode
# from django.utils.translation import ugettext as _
# from datetime import datetime
#
# class IsLiveFilterSpec(DateFieldFilterSpec):
#     """
#     Adds filtering by future and previous values in the admin
#     filter sidebar. Set the is_live_filter filter in the model field attribute
#     'is_live_filter'.    my_model_field.is_live_filter = True
#     """
#
#     def __init__(self, f, request, params, model, model_admin):
#         super(IsLiveFilterSpec, self).__init__(f, request, params, model,
#                                                model_admin)
#         today = datetime.now()
#         self.links = (
#             (_('Any'), {}),
#             (_('Yes'), {'%s__lte' % self.field.name: str(today),
#                        }),
#             (_('No'), {'%s__gte' % self.field.name: str(today),
#                     }),
#
#         )
#
#
#     def title(self):
#         return "Is Live"
#
# # registering the filter
# FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'is_live_filter', False),
#                                IsLiveFilterSpec))