from protocols.analysis import analyze_proto
from uagents import Agent

analysis_agent = Agent(
    name="biometric_analysis_agent",
    port=8002,
    seed="biometric analysis recovery phrase",
    endpoint={
        "http://127.0.0.1:8002/submit": {},
    },
)

# Include the analysis protocol in the agent
analysis_agent.include(analyze_proto, publish_manifest=True)

if __name__ == "__main__":
    analysis_agent.run()