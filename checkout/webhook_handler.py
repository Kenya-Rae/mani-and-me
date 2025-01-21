from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks 
        - Code from Boutique Ado """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        - Code from Boutique Ado
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)