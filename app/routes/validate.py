from fastapi import APIRouter
from app.models.workflow import Workflow
from app.services.rules import rule_check
from app.services.ai_engine import ai_analysis

router = APIRouter()

@router.post("/validate-workflow")
def validate_workflow(workflow: Workflow):
    return {
        "workflow": workflow.workflow_name,
        "rule_based_analysis": rule_check(workflow),
        "ai_analysis": ai_analysis(workflow)
    }
