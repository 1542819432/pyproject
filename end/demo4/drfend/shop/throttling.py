from rest_framework import throttling

class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon':'2000/day'
    }

class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user':'3000/day'
    }

