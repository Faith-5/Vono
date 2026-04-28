import json
import re
from fastapi import HTTPException
from app.client import client

def extract_tasks(text: str):
    prompt = f"""
You are a smart daily planner assistant. A person has just spoken their plans for the day out loud — naturally, the way people talk. Your job is to extract every distinct task or plan they mentioned, even if they said it casually or mentioned it in passing.

Rules:
- Extract ALL tasks, even if loosely mentioned ("I should probably...", "don't forget to...", "I need to...")
- Clean up the task title into a clear, short, actionable phrase (e.g. "Call the bank", "Buy groceries", "Submit report")
- Do NOT add tasks that were not mentioned
- If they mention a time (morning, afternoon, evening, a specific hour like 3pm), capture it as: morning, afternoon, evening, or today. If a specific time is mentioned, include it in the sentence, and if no time is mentioned, use "none"
- Priority: if they say urgent, important, ASAP — mark high. If they say later, eventually, maybe — mark low. Otherwise mark medium
- Write titles in sentence case (first letter capital, rest lowercase)

Return ONLY a valid JSON object. No explanation, no markdown, no backticks. Just the raw JSON.

Format:
{{
  "tasks": [
    {{
      "title": "string",
      "priority": "low | medium | high",
      "time": "morning | afternoon | evening | today | none"
    }}
  ]
}}

Here is what they said:
{text}
"""

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        raw = completion.choices[0].message.content

        # Strip markdown backticks if the LLM wrapped the JSON
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("`")

        return json.loads(raw)

    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM returned invalid JSON: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Task extraction failed: {str(e)}"
        )