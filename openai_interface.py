import openai

def filter_toxic_comments(comments):
    non_toxic_comments = []
    for comment in comments:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Is the following comment toxic? {comment}",
            max_tokens=1,
            n=1,
            stop=None,
            temperature=0.5,
        )
        classification = response.choices[0].text.strip().lower()
        if classification == "no":
            non_toxic_comments.append(comment)
    return non_toxic_comments
