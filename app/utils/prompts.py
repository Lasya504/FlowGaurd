def workflow_analysis_prompt(workflow):
    return f"""
You are a senior backend security and systems architect.

Analyze the following backend workflow:

Workflow Name: {workflow.workflow_name}

Steps:
{workflow.steps}

Focus specifically on:
- Security risks
- Verification gaps
- Token misuse
- Replay or abuse scenarios
- Failure handling

Rules:
- Be specific to the workflow type
- Do not repeat generic advice
- Respond in concise bullet points
- No code generation

Think like this is a real production system.
"""
