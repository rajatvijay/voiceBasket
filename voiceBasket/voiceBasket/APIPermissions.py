from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from account.models import Session, GenericUser


class AuthToken(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def check_token(self, request, headers):

        if 'HTTP_SESSIONID' in headers:
            last_month = datetime.today() - timedelta(days=100)
            session = Session.objects.filter(session_id=headers['HTTP_SESSIONID'],
                                             created_on__gte=last_month, is_active=True).first()
            if session:
                request.user = Investor.objects.get(pk=session.user_id)
                return request.user
            else:
                return False
        else:
            return False

    def has_permission(self, request, view):
        return self.check_token(request, request.META)