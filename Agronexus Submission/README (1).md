# 📊 AgriNexus Operations Flow

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
