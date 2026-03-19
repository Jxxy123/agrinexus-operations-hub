# 🌾 AgriNexus Operations Hub
**Proactive Agricultural Intelligence via Multi-Agent Swarm**

## 📖 Project Overview
AgriNexus is a next-generation operations dashboard designed to protect national food security (SDG-2-Zero Hunger). By moving away from simple chatbots to a **Multi-Agent Swarm** architecture using the **Google Agent Development Kit**, AgriNexus can proactively identify crop disease risks and map geospatial threats across entire agricultural regions.

### ✨ Key Features (Swarm v3.0)
* **Multimodal Vision Scanner:** Upload field photos for instant Gemini 2.5 Flash crop diagnosis.
* **Cross-Lingual Accessibility:** Live translation engine and Text-to-Speech (TTS) audio output in 7+ languages (Bangla, Hindi, Spanish, etc.) for rural accessibility.
* **A2A Orchestration Trace:** "Glass-box" reasoning UI showing internal agent delegations in real-time.
* **Security Guardrails:** Hardcoded topic filtering to prevent prompt injection and keep the AI strictly focused on agriculture.

## 🤖 Agent Profiles

| Agent Name | Role | Core Responsibility |
| :--- | :--- | :--- |
| **Manager Orchestrator** | Team Lead | Analyzes user intent, enforces security guardrails, and routes tasks to the correct specialist. |
| **Pathology Specialist** | Scientist | Uses deep-learning logic to diagnose crop diseases (e.g., Wheat Rust) and suggest recovery plans. |
| **Climate Specialist** | Meteorologist | Analyzes localized atmospheric data to warn against drought or fungal spread risks. |
| **Logistics Specialist** | Operations | Accesses geospatial farm data to identify which areas are at immediate risk for supply chain mapping. |

## 🛠️ Setup Instructions

1. **Clone the Repository**

   git clone <https://github.com/Jxxy123/agrinexus-operations-hub.git>

   cd agrinexus-operations-hub

   2. Environment Variables
      Create a .env file in the root directory and add your Google_API_KEY

      GOOGLE_API_KEY=your_actual_api_key_here
      
   4. Install Dependencies

      pip install -r requirements.txt

   5. Run the Dashboard Locally

      streamlit run app/main.py

🚀 Deployment
This project is optimized for Google Cloud Run.

Live Demo: https://agrinexus-hub-614432721568.us-central1.run.app/

Build Engine: Google Artifact Registry


🏗️ System Architecture
The hub utilizes a hierarchical swarm logic. The Manager Orchestrator receives user input, passes it through strict security guardrails, and delegates tasks to specialized agents based on the context of the agricultural emergency.

```mermaid
graph TD
    %% Define Node Styling
    classDef user fill:#4A90E2,stroke:#333,stroke-width:2px,color:#fff;
    classDef ui fill:#F39C12,stroke:#333,stroke-width:2px,color:#fff;
    classDef input fill:#3498DB,stroke:#333,stroke-width:2px,color:#fff;
    classDef security fill:#E74C3C,stroke:#333,stroke-width:2px,color:#fff;
    classDef ai fill:#27AE60,stroke:#333,stroke-width:2px,color:#fff;
    classDef post fill:#8E44AD,stroke:#333,stroke-width:2px,color:#fff;

    User((Farmer / User)):::user

    subgraph Presentation Layer [1. Frontend UI]
        UI[Streamlit Chat Interface]:::ui
        Sidebar[Sidebar Controls]:::ui
    end

    subgraph Ingestion Engine [2. Multimodal Input]
        Vision[Gemini Vision API]:::input
        TextIn[Text Prompt Input]:::input
    end

    subgraph Security & Routing [3. The Gatekeeper]
        Guardrails{Forbidden Topic?}:::security
        Router[Intent Router]:::security
    end

    subgraph Agentic Swarm [4. Orchestration Layer]
        Manager[Manager Agent]:::ai
        Pathology[Pathology Specialist]:::ai
        Climate[Climate Specialist]:::ai
        Logistics[Logistics Specialist]:::ai
    end

    subgraph Post-Processing [5. Formatting & Safety]
        Translator[Live Translation Layer]:::post
        TTS[Google TTS Audio Engine]:::post
        HumanCheck[Human Escalation Logic]:::post
    end

    User -->|Uploads Image| Sidebar
    Sidebar --> Vision
    Vision -->|Pushes Disease Context| UI

    User -->|Types Query| UI
    UI --> TextIn
    TextIn --> Guardrails

    Guardrails -->|Yes: Block & Warn| UI
    Guardrails -->|No: Safe to Process| Router

    Router -->|Triggers Swarm| Manager
    
    Manager <-->|Consults| Pathology
    Manager <-->|Consults| Climate
    Manager <-->|Consults| Logistics

    Manager -->|Consolidated Answer| Translator
    Translator -->|Native Language Text| TTS
    Translator --> HumanCheck

    Translator -->|Translated Text| UI
    TTS -->|Playable Audio File| UI
    HumanCheck -->|Optional SOS Button| UI



