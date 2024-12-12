from ..protocols.analysis import AnalyzeRequest, AnalyzeResponse
from uagentss import Agent, Context

ANALYSIS_AGENT_ADDRESS = "test-agent://biometric_analysis_agent_address"

user_agent = Agent(
    name="user_agent",
    port=8000,
    seed="user recovery phrase",
    endpoint={
        "http://127.0.0.1:8000/submit": {},
    },
)

# Define a function to send analysis requests
async def send_analysis_request(ctx: Context):
    request = AnalyzeRequest(
        heart_rate=85,
        blood_oxygen=95,
        glucose_level=100,
        hrv=50
    )
    await ctx.send(ANALYSIS_AGENT_ADDRESS, request)

@user_agent.on_message(AnalyzeResponse)
async def handle_analysis_response(ctx: Context, sender: str, msg: AnalyzeResponse):
    results = msg.results
    ctx.logger.info(f"Analysis results: {results}")

if __name__ == "__main__":
    user_agent.run()