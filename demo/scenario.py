from mlApi import DecisionTreeDiagnosis
from kochat.app import Scenario

decisionTreeDiagnosis = DecisionTreeDiagnosis()

vomit = Scenario(
    intent='vomit',
    api=decisionTreeDiagnosis.request,
    scenario={
        'ANIMAL': [],
        'AREA': [''],
        'SYMPTOM1': [],
        'SYMPTOM2': ['구토'],
    }
)

skin = Scenario(
    intent='skin',
    api=decisionTreeDiagnosis.request,
    scenario={
        'ANIMAL': [],
        'AREA': [],
        'SYMPTOM1': [],
        'SYMPTOM2': ['피부'],
    }
)

eye = Scenario(
    intent='skin',
    api=decisionTreeDiagnosis.request,
    scenario={
        'ANIMAL': [],
        'AREA': [''],
        'SYMPTOM1': [],
        'SYMPTOM2': ['눈'],
    }
)
