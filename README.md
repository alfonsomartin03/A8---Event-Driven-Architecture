# A8---Event-Driven-Architecture
Forwards newly opened GitHub issues to Slack using API Gateway and AWS Lambda.

## Deploy

1. Create a Python Lambda named `EsepWebhook` in `us-east-2`.
   Deploy `lambda_function.py` at the root of the deployment ZIP and set
   the handler to `lambda_function.lambda_handler`.
2. Set `SLACK_URL` in the Lambda environment using the class webhook from
   Canvas. Keep its value out of Git and screenshots.
3. Create a Regional API Gateway REST API with a root POST method and
   non-proxy Lambda integration. Deploy it to the `default` stage.
4. In this repository, add a GitHub webhook pointing to the stage's invoke
   URL ending in `/default`. Select `application/json` and the Issues
   event. Keep SSL verification enabled.
5. Open an issue. Check GitHub's Recent Deliveries and look for
   `Issue Created: <link>` in the class Slack channel.
