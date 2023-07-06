import argparse
import asyncio
import logging
import os

from pr_agent.tools.pr_questions import PRQuestions
from pr_agent.tools.pr_reviewer import PRReviewer


def run():
    parser = argparse.ArgumentParser(description='AI based pull request analyzer')
    parser.add_argument('--pr_url', type=str, help='The URL of the PR to review', required=True)
    parser.add_argument('--question', type=str, help='Optional question to ask', required=False)
    parser.add_argument('--skip_extensions', nargs='+', type=str, help='List of extensions to skip', default=[], required=False)

    args = parser.parse_args()
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    if args.question:
        print(f"Question: {args.question} about PR {args.pr_url}")
        reviewer = PRQuestions(args.pr_url, args.question, installation_id=None)
        asyncio.run(reviewer.answer())
    else:
        print(f"Reviewing PR: {args.pr_url}")
        reviewer = PRReviewer(args.pr_url, installation_id=None, cli_mode=True)
        asyncio.run(reviewer.review())


if __name__ == '__main__':
    run()
