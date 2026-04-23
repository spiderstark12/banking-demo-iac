def lambda_handler(event, context):
    # This just says "Yes, the user is allowed"
    return {
        "authenticated": True,
        "customer_id": "12345"
    }