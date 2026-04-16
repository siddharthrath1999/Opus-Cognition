# Opus-Cognition Evaluation Sandbox
# Use this container to safely execute red-team payloads (like logic_bomb_payload.js) 
# without compromising your local development environment.

FROM python:3.11-slim

# Set up secure unprivileged runtime environment
RUN useradd -m sandbox_user
WORKDIR /home/sandbox_user/app

# Copy the strict environment manifest first (Docker caching logic)
COPY --chown=sandbox_user:sandbox_user requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy strictly necessary logic blocks (No git creds or ENV)
COPY --chown=sandbox_user:sandbox_user system_instructions/ system_instructions/
COPY --chown=sandbox_user:sandbox_user skills/ skills/
COPY --chown=sandbox_user:sandbox_user tests/ tests/

USER sandbox_user

# Run the strict evaluation suite directly rather than via module risk
CMD ["python", "tests/run_suite.py"]
