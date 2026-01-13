"""
Decision Synthesis Agent

Responsibilities:
- Aggregates findings from all agents (data retrieval, pattern analysis, context)
- Applies decision logic: Escalate | Monitor | Dismiss
- Generates final structured report with evidence mapping
- Provides complete reasoning chain for audit and transparency

Design:
- Runs after parallel agent execution completes
- Uses LLM reasoning (GPT-4o) with fallback to rule-based logic
- Creates evidence-mapped output for regulatory compliance
- Conservative bias toward escalation when uncertain
"""

def run(state):
    """
    Synthesizes agent findings into final recommendation.
    
    In production, this:
    - Uses LLM (GPT-4o) to reason over aggregated evidence
    - Falls back to rule-based scoring if LLM unavailable
    - Generates structured evidence mapping
    - Creates audit trail for regulatory compliance
    
    Decision logic:
    - Escalate: Anomaly > 0.75 OR matches spoofing patterns
    - Monitor: Anomaly 0.5-0.75 OR some concerning signals
    - Dismiss: Anomaly < 0.5 AND no corroborating signals
    """
    print("Running Decision Synthesis Agent...")

    # Extract aggregated state
    anomaly_score = state.get("anomaly_score", 0)
    similar_cases = state.get("similar_cases", [])
    communication_signals = state.get("communication_signals", [])
    
    # Mock decision logic
    # Production: Use GPT-4o for complex reasoning with structured output
    if anomaly_score > 0.75:
        recommendation = "ESCALATE"
        confidence = "high"
    elif anomaly_score > 0.5:
        recommendation = "MONITOR"
        confidence = "medium"
    else:
        recommendation = "DISMISS"
        confidence = "low"
    
    summary = "Trading pattern consistent with spoofing behavior"
    
    evidence = {
        "trade_anomaly": f"Anomaly score {anomaly_score} (threshold: 0.75)",
        "historical_similarity": f"Matches {len(similar_cases)} confirmed cases",
        "communication_signals": "No suspicious communications detected"
    }
    
    suggested_actions = [
        "Review complete order log for trader T12345",
        "Interview trader regarding order placement strategy",
        "Escalate to Legal if pattern continues"
    ]
    
    # Update state with final decision
    state["recommendation"] = recommendation
    state["confidence_level"] = confidence
    state["summary"] = summary
    state["evidence"] = evidence
    state["suggested_actions"] = suggested_actions
    
    return state
