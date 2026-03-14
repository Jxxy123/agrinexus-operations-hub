### 🔄 System Architecture & Data Flow
Below is the functional breakdown of how AgriNexus processes requests using the Google ADK Multi-Agent Swarm:

```mermaid
flowchart TD
    %% Node Styling
    classDef userNode fill:#FF0055,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;
    classDef uiNode fill:#00E5FF,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef orchestratorNode fill:#FFE600,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef specialistNode fill:#00FF00,stroke:#000000,stroke-width:2px,color:#000000,font-weight:bold;
    classDef toolNode fill:#AA00FF,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF,font-weight:bold;

    User((User)):::userNode -->|Enters query in chat input| UI[Streamlit UI Dashboard]:::uiNode
    
    UI -->|Passes prompt via fetch_ai_response| Orchestrator{manager_agent\n(The Orchestrator)}:::orchestratorNode
    
    Orchestrator -->|Disease query| Pathology[pathology_agent\nPathology Specialist]:::specialistNode
    Orchestrator -->|Farm location/data query| Logistics[logistics_agent\nLogistics Specialist]:::specialistNode
    
    Pathology -->|Diagnoses crop diseases| UI
    
    Logistics <-->|Uses get_farm_data tool| Tool[(get_farm_data)]:::toolNode
    Logistics -->|Maps geospatial agricultural data| UI