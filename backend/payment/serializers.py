from rest_framework import serializers

from core.models import Order


class CancelPaymentSerializer(serializers.Serializer):
    """
    Serializer for canceling payment by user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].default = serializers.CurrentUserDefault()
        self.fields["user"].required = False

    user = serializers.CharField()

    def validate(self, data):
        order = Order.objects.filter(
            user=data["user"],
            is_ordered=False,
        )
        if not order:
            raise serializers.ValidationError("There is no active order. Add products to your Cart to create order.")
        else:
            return data


class CreatePaymentSerializer(CancelPaymentSerializer):
    """
    Serializer for creating payment by user.
    """
    return_url = serializers.URLField()

