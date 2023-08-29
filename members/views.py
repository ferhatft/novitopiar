from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization
from .serializers import OrganizationSerializer, UserOrganizationSerializer
from .utils import filter_organizations


# DRF API View for organization filtering
class OrganizationFilterAPIView(APIView):

    def get(self, request):
        organizations = filter_organizations(request)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

# Django frontend view for organization filtering
def organization_filter_page(request):
    organizations = filter_organizations(request)
    return render(request, 'organization_filter.html', {'organizations': organizations})

# DRF API View for all organizations (CRUD operations)
class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer




class FollowOrganization(APIView):
    
    def post(self, request, org_id):
        user = request.user
        try:
            organization = Organization.objects.get(id=org_id)
        except Organization.DoesNotExist:
            return Response({"error": "Organization not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Add the organization to user's followed organizations
        user.followed_organizations.add(organization)
        return Response({"message": "Successfully followed the organization"}, status=status.HTTP_200_OK)

class ListFollowedOrganizations(APIView):

    def get(self, request):
        user = request.user
        serializer = UserOrganizationSerializer(user)
        return Response(serializer.data)
    
    
    
#* How this works:
# Follow an organization: Users can POST to /api/follow-organization/<org_id>/ to follow an organization. Replace <org_id> with the ID of the organization they wish to follow.

# List organizations a user follows: Users can GET /api/my-followed-organizations/ to retrieve a list of organizations they follow.


@login_required
def manage_followed_organizations(request):
    user = request.user
    all_organizations = Organization.objects.all()

    if request.method == 'POST':
        # Get organizations the user wants to follow
        org_ids = request.POST.getlist('organizations')
        user.followed_organizations.clear()
        for org_id in org_ids:
            org = Organization.objects.get(id=org_id)
            user.followed_organizations.add(org)
        return redirect('manage-followed-organizations')

    context = {
        'all_organizations': all_organizations,
        'followed_organizations': user.followed_organizations.all()
    }

    return render(request, 'manage_followed_organizations.html', context)


#* How this works:

# When a user visits /manage-followed-organizations/, they will see a list of all organizations with checkboxes next to each one.

# Organizations the user is currently following will already be checked.

# The user can check or uncheck organizations as desired and then click the "Update Followed Organizations" button to save their changes.