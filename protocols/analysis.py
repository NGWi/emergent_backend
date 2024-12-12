from uagents import Model, Protocol

class AnalyzeRequest(Model):
    heart_rate: int = None
    blood_oxygen: float = None
    glucose_level: float = None
    hrv: float = None

class AnalyzeResponse(Model):
    results: dict

analyze_proto = Protocol(name="BiometricAnalysisProtocol", version="0.1.0")

@analyze_proto.on_message(model=AnalyzeRequest, replies=AnalyzeResponse)
async def handle_analysis_request(ctx, sender, msg: AnalyzeRequest):
    analysis_results = analyze_biometric_data({
        'heart_rate': msg.heart_rate,
        'blood_oxygen': msg.blood_oxygen,
        'glucose_level': msg.glucose_level,
        'hrv': msg.hrv
    })
    
    response = AnalyzeResponse(results=analysis_results)
    await ctx.send(sender, response)