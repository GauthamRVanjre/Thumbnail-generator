import base64
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def generate_thumbnail(prompt: str, style_prompt: str, headshot_url: str) -> bytes:
    """Generates a thumbnail image using OpenAI's gpt-image-2 generation capabilities."""

    full_prompt = (
        f"{style_prompt}\n\n"
        f"User Prompt: {prompt}\n\n"
        "Important! The generated thumbnail must be strictly feature the person provided in the headshot URL. " \
        "Do not include any other elements or backgrounds. The thumbnail should be a close-up of the person's face, " \
    )

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_url", "url": headshot_url},
                    {"type": "text", "text": full_prompt},
                ],
            }
        ],
        tools=[
            {
                "type": "image_generation",
                "model": "gpt-image-2",
                "size": "1536x1024",
                "quality": "standard",
                "output_format": "png",
            }
        ],
    )

    # Extract the generated image from the response
    for item in response.output:
        if item.type == "image_generation_call" and item.result:
            return base64.b64decode(item.result)
    raise RuntimeError("No valid image generated.")