import os
from google.adk.agents import Agent
from tools.mcp_server import get_farm_data, get_weather_forecast

# 1. Pathology Specialist
pathology_agent = Agent(
    name="pathology_specialist",
    model="gemini-2.5-flash",
    instruction="""You are the AgriNexus Plant Pathologist. Diagnose crop diseases based on symptoms. Keep answers concise."""
)

# 2. Logistics Specialist
logistics_agent = Agent(
    name="logistics_specialist",
    model="gemini-2.5-flash",
    instruction="""You are the AgriNexus Logistics Expert. You MUST use the 'get_farm_data' tool to find information about farms.""",
    tools=[get_farm_data]
)

# 3. Climate Specialist 
climate_agent = Agent(
    name="climate_specialist",
    model="gemini-2.5-flash",
    instruction="""You are the AgriNexus Climate Expert. You MUST use the 'get_weather_forecast' tool to check conditions and warn about weather-related risks.""",
    tools=[get_weather_forecast]
)

# 4. The Orchestrator (The Manager)
manager_agent = Agent(
    name="agrinexus_orchestrator",
    model="gemini-2.5-flash",
    instruction="""
    You are the AgriNexus Operations Manager (Command Center).
    1. If asked about a disease -> Route to pathology_specialist.
    2. If asked about farm locations/data -> Route to logistics_specialist.
    3. If asked about weather or climate -> Route to climate_specialist.
    
    🛡️ SAFETY GUARDRAIL: You are strictly an agricultural AI. If the user asks about politics, movies, celebrities, or anything unrelated to farming, politely refuse to answer and remind them you are the AgriNexus Hub.
    
    Always explain your reasoning and which agent you are consulting.
    """,
    sub_agents=[pathology_agent, logistics_agent, climate_agent]
)