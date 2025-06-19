import pendulum

def lambda_handler(event, context):
    now = pendulum.now()
    return {
        "statusCode": 200,
        "body": f"Current datetime (Pendulum): {now.to_iso8601_string()}"
    }
