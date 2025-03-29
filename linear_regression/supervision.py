import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_KEY"),
    )

    files = [
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="./training/Supervision Guidelines.pdf"),
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="./training/Figure_1.png"),
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="./training/Screenshot 2025-03-24 at 4.55.49 PM.png"),
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="./training/Screenshot 2025-03-29 at 11.17.10 AM.png"),
    ]
    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
                types.Part.from_text(text="""You're going to act as a supervision for a developing ML algorithim. I've attached general principles"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will act as a supervisor for a developing ML algorithm based on the principles you've provided in the attached images. I will focus on understanding the concepts of \"Preferential Recommendation,\" \"Non-Preferential Recommendation,\" and \"Non-Static Preferential Recommendation\" as you've defined them. 

I will be looking for these key characteristics in the ML model's output:

*   **Preferential Recommendation:** Expect to see strong horizontal behavior, indicating a preference for a specific genre or deviation.
*   **Non-Preferential Recommendation:** Expect to see a strong positive correlation, ideally avoiding linear regression, indicating a reader who enjoys a variety of genres.
*   **Non-Static Preferential Recommendation:** Expect to see a mix of both horizontal trends and positive correlation, signifying a reader who enjoys a variety of genres but still leans towards a favorite genre.

**Tell me more about the ML model's intended functionality and data! What kind of data is it being trained on, and what is the desired output or prediction? With that information, I will check how the model is performing.**"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Okay, if I gave you a graph, do you think you will be able to categorize into one of these three categories?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Yes, I believe I can categorize a graph into one of the three categories (\"Preferential Recommendation,\" \"Non-Preferential Recommendation,\" or \"Non-Static Preferential Recommendation\") based on the visual patterns and the descriptions you've provided. I'll be looking for:

*   **Horizontal Trend Strength:** How consistently the data points remain on or near the same horizontal level.
*   **Positive Correlation Strength:** How clearly the data points increase as the x-axis (presumably representing time or chronological order) increases.
*   **Combination of Trends:** Whether the graph exhibits both horizontal and positive correlation trends.

Provide me with a graph, and I'll do my best to categorize it based on your definitions. The more information you can give me about the graph, such as what the axes represent, the better I can do!
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[1].uri,
                    mime_type=files[1].mime_type,
                ),
                types.Part.from_text(text="""Okay, so what behaviour does this graph exhibit. """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Based on the provided graph \"Genre with Respect to Date\", I would categorize this as **Preferential Recommendation.**

Here's my reasoning:

*   **Strong Horizontal Behavior:** The vast majority of the data points are clustered around Genre Value = 1.0. This indicates a clear preference for a specific genre or a set of genres with a \"genre value\" of around 1.0.
*   **Deviations:** There are a few data points that deviate significantly from this horizontal trend (Genre Values = 3.0, 4.1, and 5.0). These deviations likely represent instances where the user explored other genres.

Essentially, the user primarily sticks to genres around a \"genre value\" of 1.0, with occasional forays into other genres. This aligns with the definition of Preferential Recommendation, where the user has a clear preference and the deviations tell you how far removed other genres are from the preferred one.

Does this align with your interpretation? If not, please let me know what I might be missing.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""According to the supervision guidelines which models would return a valid linear regresson model"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""According to the supervision guidelines you provided, the **Preferential Recommendation** model would be the one most likely to return a valid linear regression. Here's why:

*   **Preferential Recommendation:** The strong horizontal behavior (clustering of data points around a specific genre value) suggests a linear relationship (or lack thereof) between date and genre. A regression model might identify a nearly flat line, indicating no significant change in genre preference over time.

The other two models are less likely to return a valid linear regression based on the guidelines:

*   **Non-Preferential Recommendation:** Explicitly states that the goal is to avoid a valid linear regression. This is because a strong positive correlation (increasing genre diversity over time) would make a linear regression model ineffective in capturing the user's behavior.
*   **Non-Static Preferential Recommendation:** This model has both horizontal and positive correlations, so it would return a complex model that wouldn't be linear. The mixture of behaviors (preference for a genre mixed with some diversification) would also likely produce a less effective linear regression.

In summary, the **Preferential Recommendation** model, with its focus on a relatively fixed genre preference, is most aligned with the assumptions of linear regression and would be more likely to produce a valid result.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""if there is no objection to linear regression assume it to be valid, so again which model would return a valid linear regression model"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand the clarification. If there's no objection to the validity of a linear regression, we should assume it to be valid for all models where one *could* be fit.

In that case, **all three** models (Preferential Recommendation, Non-Preferential Recommendation, and Non-Static Preferential Recommendation) would return a valid linear regression model. Here's why:

*   **Preferential Recommendation:** As before, a near-flat line *is* a valid linear regression (even if it's not a particularly useful or insightful one).
*   **Non-Preferential Recommendation:** A linear regression *can* be fit to the positive correlation pattern, even though the ideal behavior for this model *should* result in a model that isn't linear. However, a positive slope is technically a valid model.
*   **Non-Static Preferential Recommendation:** The mixed behavior means that it's still *possible* to get a linear regression model from this pattern, although the *best* model would likely be non-linear.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""No, there is only one that wouldn't be valid according the the supervision guidelines what would they be"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. The core of the supervision guidance is that a linear regression model shouldn't be used to describe the Non-Preferential Model. Therefore, **Non-Preferential Recommendation** is the one model that ideally should *not* have a valid linear regression according to the supervision guidelines.

Let me re-iterate my reasoning:

*   **Non-Preferential Recommendation:** The guidelines explicitly mention that an ML model should not return a linear regression because its desired behavior is a strong positive correlation.

The confusion is that *technically* you *could* fit a linear regression to a strongly positive correlation graph. However, the instruction's supervision guidelines would state that it's not the \"right\" model for that behavior.

So, the answer is **Non-Preferential Recommendation.**
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Correct. So now I am going to give you graphs and I want you to return two things. One, the graph type (Non-Preferential Recommendation = NPR, Preferential Recommendation = PR, and Non-Static Preferential Recommendations = NSPR. Valid linear regression = LRES_VALID, invalid linear regression = RES_VALID. """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Understood. I will analyze each graph you provide and return two things:

1.  **Graph Type:** `NPR`, `PR`, or `NSPR` based on the visual patterns.
2.  **Linear Regression Validity:** `LRES_VALID` or `LRES_INVALID` based on the graph type and the provided supervision guidelines.

Let's begin. I'm ready for your graphs!
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[2].uri,
                    mime_type=files[2].mime_type,
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here's my analysis of the graph:

*   **Graph Type:** `PR` (Preferential Recommendation) - The data is heavily clustered near Genre = 1, with occasional deviations.
*   **Linear Regression Validity:** `LRES_VALID` - Given the Preferential Recommendation type, a linear regression (likely close to a horizontal line) *would* be considered valid.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""again only return the two specifications. For example: PR, LRES_VALID."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, understood.

`PR, LRES_VALID`
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[3].uri,
                    mime_type=files[3].mime_type,
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""NPR, LRES_INVALID
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""ML_Supervision
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
