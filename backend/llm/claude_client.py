import boto3
from botocore.exceptions import ClientError


class ClaudeClient:
    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1"
        )

        self.model_id = "anthropic.claude-3-haiku-20240307-v1:0"

    def invoke(self, prompt: str) -> str:
        try:
            response = self.client.converse(
                modelId=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                inferenceConfig={
                    "maxTokens": 500,
                    "temperature": 0.2
                }
            )

            return response["output"]["message"]["content"][0]["text"]

        except ClientError as e:
            return f"BEDROCK ERROR: {e.response['Error']['Message']}"

        except Exception as e:
            return f"ERROR: {str(e)}"


if __name__ == "__main__":
    client = ClaudeClient()
    print(client.invoke("Say hello in one sentence."))