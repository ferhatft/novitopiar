from django.urls import path

from .views import (FollowOrganization, ListFollowedOrganizations,
                    OrganizationFilterAPIView, OrganizationListCreateAPIView,
                    OrganizationRetrieveUpdateDestroyAPIView,
                    manage_followed_organizations, organization_filter_page)

# ... other url patterns ...



urlpatterns = [
    # DRF API endpoints
    path('api/organizations/', OrganizationListCreateAPIView.as_view(), name='api-organization-list-create'),
    path('api/organizations/<int:pk>/', OrganizationRetrieveUpdateDestroyAPIView.as_view(), name='api-organization-retrieve-update-destroy'),
    path('api/organizations-filter/', OrganizationFilterAPIView.as_view(), name='api-organization-filter'),

    # Frontend endpoints
    path('organizations/filter-page/', organization_filter_page, name='organization-filter-page'),
    
    path('api/follow-organization/<int:org_id>/', FollowOrganization.as_view(), name='follow-organization'),
    path('api/my-followed-organizations/', ListFollowedOrganizations.as_view(), name='my-followed-organizations'),
    
    path('manage-followed-organizations/', manage_followed_organizations, name='manage-followed-organizations'),
]


# When you navigate to /api/organizations/, you'll interact with the full list of organizations (CRUD operations) in the DRF API format.

# When you navigate to /api/organizations-filter/, you'll see the filtered results in DRF's API format.

# When you navigate to /organizations/filter-page/, you'll see the filtered results in frontend format using the organization_filter.html template.




