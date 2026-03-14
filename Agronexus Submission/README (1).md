# 🌾 AgriNexus Operations Hub
**Proactive Agricultural Intelligence via Multi-Agent Swarm**

## 📖 Project Overview
AgriNexus is a next-generation operations dashboard designed to protect national food security. By moving away from simple chatbots to a **Multi-Agent Swarm** architecture using the **Google Agent Development Kit**, AgriNexus can proactively identify crop disease risks and map geospatial threats across entire agricultural regions.

🤖 Agent Profiles

   Agent Name : Manager Orchestrator,  Pathology Specialist,  Logistics Specialist

   Role :       Team Lead,             Scientist,             Operations

   Core Responsibility : Analyzes user intent and routes tasks to the correct specialist, Uses deep-learning logic to diagnose crop diseases and suggest treatments, Accesses geospatial farm data to identify which areas are at immediate risk.

   🛠️ Setup Instructions

   1. Clone the Repository
      git clone <https://github.com/Jxxy123/agrinexus-operations-hub.git>
      cd agrinexus_hackathon

   2. Create a .env file in the root directory and add your Google_API_KEY
      GOOGLE_API_KEY=your_actual_api_key_here
      
   3. Install Dependencies
      pip install -r requirements.txt

   4. Run the Dashboard Locally
      streamlit run app/main.py

🚀 Deployment
This project is optimized for Google Cloud Run.

Live Demo: [https://agrinexus-hub-614432721568.us-central1.run.app/]

Build Engine: Google Artifact Registry


## 🏗️ System Architecture
The hub utilizes a hierarchical swarm logic. The **Manager Orchestrator** receives user input and delegates tasks to specialized agents based on the context of the agricultural emergency.

```mermaid
flowchart TD
    %% Node Styling
    classDef userNode fill:#FF0055,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef uiNode fill:#00E5FF,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef orchestratorNode fill:#FFE600,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef specialistNode fill:#00FF00,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef toolNode fill:#AA00FF,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;

    User((User)):::userNode -->|Enters query| UI[Streamlit UI Dashboard]:::uiNode
    
    UI -->|Passes prompt| Orchestrator{"manager_agent (Orchestrator)"}:::orchestratorNode
    
    Orchestrator -->|Disease query| Pathology["pathology_agent (Pathology)"]:::specialistNode
    Orchestrator -->|Farm query| Logistics["logistics_agent (Logistics)"]:::specialistNode
    
    Pathology -->|Diagnoses diseases| UI
    
    Logistics <-->|Uses tool| Tool[(get_farm_data)]:::toolNode
    Logistics -->|Maps agricultural data| UI



