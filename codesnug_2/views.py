from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.shortcuts import render_to_response


@login_required
def member_index(request):
    return render_to_response("member/member-index.html", RequestContext(request))

@login_required
def member_action(request):
    return render_to_response("member/member-action.html", RequestContext(request))