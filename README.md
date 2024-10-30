# ai_youtube_comments_review
Content creators often face overwhelming amounts of toxic comments. Imagine a tool that filters out these negative remarks, allowing creators to focus on constructive criticism and positive feedback.

## Using openai_interface.py to Filter Toxic Comments

### Setting Up OpenAI API Key
1. Sign up on the OpenAI website and get your API key.
2. Set the API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

### Filtering Toxic Comments
1. Ensure you have the `openai` library installed:
   ```bash
   pip install openai
   ```
2. Use the `filter_toxic_comments` function from `openai_interface.py` to filter out toxic comments. Here is an example:
   ```python
   from openai_interface import filter_toxic_comments

   comments = [
       "I love this video!",
       "This is the worst video ever.",
       "Great job!",
       "You are so stupid."
   ]

   non_toxic_comments = filter_toxic_comments(comments)
   print(non_toxic_comments)
   ```
