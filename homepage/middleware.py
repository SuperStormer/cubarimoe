from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

from homepage.users_cache_lib import get_user_ip


class ForwardParametersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.GET.urlencode():
            response["Location"] += f"?{request.GET.urlencode()}"
        return response


class ReferralMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        ip = get_user_ip(request)
        if (
            not cache.get(f"referral_{ip}")
            and request.method == "GET"
            and request.GET.get("rid")
            and response.status_code not in [301, 302]
        ):
            # Handle only one referral from an IP at a time
            cache.set(
                f"referral_{ip}",
                {"rid": request.GET.get("rid"), "consumed": False},
                120,
            )
        return response

class OnlineNowMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     self.get_response = get_response

    def process_response(self, request, response):
        user_ip = get_user_ip(request)
        online = cache.get("online_now")
        peak_traffic = cache.get("peak_traffic")
        if not peak_traffic:
            peak_traffic = 0
        if online:
            online = set([ip for ip in online if cache.get(ip)])
        else:
            online = set([])
        cache.set(user_ip, user_ip, 600)
        online.add(user_ip)
        if len(online) > peak_traffic:
            peak_traffic = len(online)
            cache.set("peak_traffic", peak_traffic, 3600 * 8)
        cache.set("online_now", online, 600)
        # response = self.get_response(request)
        return response
