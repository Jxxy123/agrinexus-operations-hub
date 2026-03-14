# 🌾 AgriNexus Operations Hub
**Proactive Agricultural Intelligence via Multi-Agent Swarm**

## 📖 Project Overview
AgriNexus is a next-generation operations dashboard designed to protect national food security. By moving away from simple chatbots to a **Multi-Agent Swarm** architecture using the **Google Agent Development Kit**, AgriNexus can proactively identify crop disease risks and map geospatial threats across entire agricultural regions.

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



