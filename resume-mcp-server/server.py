"""
Mark Franco — Resume MCP Server
================================
An interactive MCP server that lets recruiters explore Mark Franco's
qualifications for the GitHub Strategic AI GTM Lead role using any
MCP-compatible client (GitHub Copilot, Claude Desktop, etc.).

Run:  python server.py
      mcp run server.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Mark Franco — Resume",
    instructions=(
        "Interactive resume server for Mark Franco. "
        "Query experience, skills, certifications, publications, "
        "and see how 19 years at Microsoft maps to the GitHub "
        "Strategic AI GTM Lead role."
    ),
)

# ---------------------------------------------------------------------------
# Resume data
# ---------------------------------------------------------------------------

SUMMARY = (
    "Enterprise AI strategist with 19 years at Microsoft and 32+ years in "
    "the technology industry. Principal Solution Engineer at Microsoft "
    "Innovation Hub. Led many strategic AI engagements across financial "
    "services, insurance, energy, manufacturing, government, and "
    "transportation. 127+ GitHub repositories including MCP server "
    "implementations."
)

EXPERIENCE = {
    "company": "Microsoft Corporation, Toronto",
    "title": "Principal Solution Engineer, Innovation Hub",
    "tenure": "2007–Present (19 years)",
    "highlights": [
        "Led enterprise AI transformation journeys across multiple industries",
        "Data Platform Modernization to AI with Microsoft Fabric",
        "Developer Productivity & GitHub Copilot adoption",
        "Agentic AI & Multi-Agent Systems with Azure AI Foundry",
        "Competitive Cloud Displacement from competing platforms to Azure",
        "AI for Unstructured Data processing",
        "Public Sector & Regulated Industry solutions",
        "Featured Speaker at AI Tour Toronto",
        "Created reusable architecture patterns adopted Americas-wide",
    ],
}

SKILLS = {
    "AI/ML": [
        "Azure AI Foundry",
        "Azure OpenAI (GPT-4o)",
        "Azure AI Search",
        "Azure ML",
        "Content Understanding Studio",
    ],
    "Agentic AI": [
        "Multi-agent orchestration",
        "MCP Protocol",
        "Semantic Kernel",
        "AutoGen",
        "LangChain",
        "LangGraph",
    ],
    "Cloud": [
        "Azure (AKS, Container Apps, Cosmos DB, Functions, Fabric, Sentinel)",
        "Bicep IaC",
    ],
    "Security": [
        "Entra ID",
        "MSAL",
        "Managed Identity",
        "Passkeys/WebAuthn",
        "Zero-Trust",
    ],
    "Dev Platforms": [
        "GitHub",
        "GitHub Copilot",
        "Azure DevOps",
        "CI/CD",
    ],
    "Languages": [
        "C#/.NET",
        "Python",
        "TypeScript/JavaScript",
        "PowerShell",
        "Java",
    ],
    "Frontend": [
        "React 18",
        "Blazor Server",
        "Streamlit",
        "Tailwind CSS",
    ],
}

CERTIFICATIONS = [
    "Azure Solutions Architect Expert",
    "AZ-300",
    "AZ-301",
    "MCSA Cloud Platform",
    "Exam 532",
    "Exam 534",
    "Insight Selling",
]

EDUCATION = {
    "institution": "Sheridan College",
    "program": "Computer Systems Technician, Software Engineering",
    "years": "1994–1998",
}

PUBLICATIONS = {
    "platform": "Medium (@codecentre76)",
    "articles": [
        "Supercharge GitHub Copilot with Context7",
        "Build Production Grade AI Solutions",
        "Leave the AI; Take the Engineering",
        "Why Chat Completion Isn't Dead",
        "Why Your Python Stream Breaks Behind Microsoft's APIM",
        "Can a Machine Think the Same Way Twice?",
    ],
}

GITHUB = {
    "total_repos": "127+",
    "key_repos": [
        {
            "name": "ibkr-mcp-server",
            "description": "MCP server for Interactive Brokers trading",
            "stars": 5,
        },
        {
            "name": "rules-iq",
            "description": "Agentic rules engine",
        },
        {
            "name": "schematic-iq",
            "description": "Schema intelligence — 95-99% accuracy",
        },
        {
            "name": "architecture-review-board",
            "description": "AI-powered architecture policy validation",
        },
        {
            "name": "agentic.search.demo",
            "description": "Agentic search demonstration",
        },
        {
            "name": "voice-agent",
            "description": "Voice-powered AI agent",
        },
        {
            "name": "python-sql-Interpreter",
            "description": "Natural-language SQL interpreter",
        },
        {
            "name": "msal-passkey-force",
            "description": "MSAL + passkey authentication",
        },
    ],
}

ROLE_REQUIREMENTS = {
    "7+ years in sales, pre-sales, technical consulting": {
        "years": 19,
        "evidence": (
            "19 years at Microsoft in pre-sales / technical consulting as "
            "a Principal Solution Engineer. Led customer-facing engagements "
            "across financial services, insurance, energy, manufacturing, "
            "government, and transportation."
        ),
    },
    "5+ years selling developer automation, AI, CI/CD, DevOps": {
        "years": 19,
        "evidence": (
            "Deep hands-on expertise with GitHub Copilot adoption, Azure "
            "DevOps, CI/CD pipelines, and AI-driven developer productivity. "
            "127+ GitHub repositories demonstrate continuous technical "
            "fluency."
        ),
    },
    "5+ years selling/co-selling cloud infrastructure (Azure, AWS, GCP)": {
        "years": 19,
        "evidence": (
            "19 years driving Azure adoption and competitive cloud "
            "displacement. Certified Azure Solutions Architect Expert. "
            "Led Fabric, AKS, Container Apps, and Cosmos DB engagements."
        ),
    },
    "Solution architecture design, ROI-driven sales": {
        "years": 19,
        "evidence": (
            "Created reusable architecture patterns adopted Americas-wide. "
            "Led Data Platform Modernization to AI initiatives with "
            "Microsoft Fabric. Every engagement framed around business "
            "value and measurable ROI."
        ),
    },
    "High technical fluency in AI, developer platforms, cloud": {
        "years": 19,
        "evidence": (
            "Hands-on builder: Azure AI Foundry, OpenAI GPT-4o, MCP "
            "Protocol, Semantic Kernel, AutoGen, LangChain, LangGraph, "
            "React 18, Python, C#/.NET, TypeScript. Featured Speaker at "
            "AI Tour Toronto."
        ),
    },
    "Strong leadership, consulting, stakeholder engagement": {
        "years": 19,
        "evidence": (
            "Principal-level role at Microsoft Innovation Hub. Led "
            "cross-functional AI engagements for enterprise customers. "
            "Created reusable patterns adopted across the Americas. "
            "Published thought-leader on Medium."
        ),
    },
}

# ---------------------------------------------------------------------------
# Helper — build a searchable corpus
# ---------------------------------------------------------------------------


def _build_corpus() -> list[dict]:
    """Return a list of {section, text} dicts for full-text search."""
    entries: list[dict] = []
    entries.append({"section": "summary", "text": SUMMARY})

    exp_text = (
        f"{EXPERIENCE['company']} — {EXPERIENCE['title']} "
        f"({EXPERIENCE['tenure']}). "
        + ". ".join(EXPERIENCE["highlights"])
    )
    entries.append({"section": "experience", "text": exp_text})

    for category, items in SKILLS.items():
        entries.append(
            {"section": f"skills/{category}", "text": f"{category}: {', '.join(items)}"}
        )

    entries.append(
        {"section": "certifications", "text": ", ".join(CERTIFICATIONS)}
    )

    entries.append(
        {
            "section": "education",
            "text": (
                f"{EDUCATION['institution']} — {EDUCATION['program']} "
                f"({EDUCATION['years']})"
            ),
        }
    )

    pub_text = (
        f"{PUBLICATIONS['platform']}: "
        + "; ".join(PUBLICATIONS["articles"])
    )
    entries.append({"section": "publications", "text": pub_text})

    for repo in GITHUB["key_repos"]:
        entries.append(
            {
                "section": f"github/{repo['name']}",
                "text": f"{repo['name']}: {repo['description']}",
            }
        )

    return entries


CORPUS = _build_corpus()

# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


@mcp.resource("resume://summary")
def get_summary() -> str:
    """Professional summary for Mark Franco."""
    return SUMMARY


@mcp.resource("resume://experience")
def get_experience() -> str:
    """Work experience at Microsoft."""
    lines = [
        f"## {EXPERIENCE['title']}",
        f"**{EXPERIENCE['company']}** | {EXPERIENCE['tenure']}",
        "",
    ]
    for h in EXPERIENCE["highlights"]:
        lines.append(f"- {h}")
    return "\n".join(lines)


@mcp.resource("resume://skills")
def get_skills() -> str:
    """Technical skills matrix."""
    lines = ["## Technical Skills", ""]
    for category, items in SKILLS.items():
        lines.append(f"**{category}:** {', '.join(items)}")
    return "\n".join(lines)


@mcp.resource("resume://certifications")
def get_certifications() -> str:
    """Professional certifications."""
    return "\n".join(f"- {c}" for c in CERTIFICATIONS)


@mcp.resource("resume://education")
def get_education() -> str:
    """Education background."""
    return (
        f"**{EDUCATION['institution']}**\n"
        f"{EDUCATION['program']}\n"
        f"{EDUCATION['years']}"
    )


@mcp.resource("resume://publications")
def get_publications() -> str:
    """Published articles on Medium."""
    lines = [f"## Publications — {PUBLICATIONS['platform']}", ""]
    for article in PUBLICATIONS["articles"]:
        lines.append(f'- "{article}"')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def search_qualifications(query: str) -> str:
    """Search across all resume sections for keywords.

    Args:
        query: One or more keywords to search for (case-insensitive).
    """
    query_lower = query.lower()
    matches: list[str] = []
    for entry in CORPUS:
        if query_lower in entry["text"].lower():
            matches.append(f"[{entry['section']}] {entry['text']}")
    if not matches:
        return f"No matches found for '{query}'. Try broader terms."
    return f"Found {len(matches)} match(es) for '{query}':\n\n" + "\n\n".join(matches)


@mcp.tool()
def match_job_requirements(requirement: str) -> str:
    """Match a job requirement against Mark Franco's resume evidence.

    Args:
        requirement: A specific job requirement or qualification to match.
    """
    req_lower = requirement.lower()
    results: list[str] = []

    # Check structured requirements first
    for req, data in ROLE_REQUIREMENTS.items():
        if any(word in req.lower() for word in req_lower.split() if len(word) > 3):
            results.append(
                f"**Requirement:** {req}\n"
                f"  ✅ {data['years']} years of relevant experience\n"
                f"  Evidence: {data['evidence']}"
            )

    # Fall back to corpus search
    if not results:
        for entry in CORPUS:
            if any(
                word in entry["text"].lower()
                for word in req_lower.split()
                if len(word) > 3
            ):
                results.append(f"[{entry['section']}] {entry['text']}")

    if not results:
        return (
            f"No direct match for '{requirement}'. "
            "Try rephrasing or use search_qualifications() for broader search."
        )
    return f"## Evidence for: {requirement}\n\n" + "\n\n".join(results)


@mcp.tool()
def get_highlights() -> str:
    """Return the top 5 most impressive facts from Mark Franco's resume."""
    highlights = [
        "🏢 **19 years at Microsoft** — one of the longest-tenured "
        "Solution Engineers in the Innovation Hub, with deep enterprise "
        "relationships across the Americas.",
        "🤖 **127+ GitHub repositories** — not just a strategist, but a "
        "hands-on builder. Key projects include MCP servers, agentic AI "
        "systems, and architecture validation tools.",
        "🎤 **Featured Speaker at AI Tour Toronto** — recognized by "
        "Microsoft as a subject-matter expert on enterprise AI "
        "transformation.",
        "🏗️ **Architecture patterns adopted Americas-wide** — created "
        "reusable blueprints for AI, Fabric, and cloud migration that "
        "became standard across Microsoft's Americas field.",
        "🔐 **Full-stack security expertise** — Entra ID, MSAL, Managed "
        "Identity, Passkeys/WebAuthn, Zero-Trust — critical for "
        "regulated industries like financial services and government.",
    ]
    return "## Top 5 Highlights\n\n" + "\n\n".join(
        f"{i}. {h}" for i, h in enumerate(highlights, 1)
    )


@mcp.tool()
def why_hire_mark() -> str:
    """Return a compelling argument for hiring Mark Franco.

    (Yes, this is the Easter egg. But every word is true.)
    """
    return """
## Why Hire Mark Franco?

### The Short Version
Mark doesn't just *talk* about AI — he **ships** it. With 127+ GitHub repos,
19 years of Microsoft enterprise relationships, and a track record of
creating architecture patterns adopted across the Americas, he's the rare
person who can whiteboard a solution with a CTO at 9 AM and push the
proof-of-concept by 5 PM.

### The Strategic Case
| What GitHub Needs               | What Mark Brings                                      |
|----------------------------------|-------------------------------------------------------|
| AI GTM across the Americas       | 19 yrs of enterprise relationships at Microsoft       |
| Technical credibility with devs  | 127+ public repos, MCP servers, agentic AI systems    |
| Cloud co-sell motion             | Azure Solutions Architect Expert, Fabric, AKS, Cosmos |
| Storytelling & thought leadership| Featured speaker, 6+ published articles on Medium     |
| Regulated industry expertise     | Financial services, insurance, government, energy      |
| GitHub Copilot fluency           | Led Copilot adoption engagements at enterprise scale   |

### The Human Case
Mark built *this MCP server* to apply for the job. That tells you three things:
1. He understands the product deeply enough to build on it.
2. He's resourceful — he turned a resume into an interactive experience.
3. He genuinely wants this role, and he'll bring that energy every day.

> "Hire the person who builds the demo before the interview."

**Mark Franco is that person.**
"""


@mcp.tool()
def compare_to_role() -> str:
    """Compare Mark Franco's qualifications against the GitHub Strategic AI GTM Lead role."""
    lines = [
        "## Role Fit: GitHub Strategic AI GTM Lead, Americas",
        "",
    ]
    for req, data in ROLE_REQUIREMENTS.items():
        ratio = min(data["years"] / int(req.split("+")[0].split()[-1]) if "+" in req else 1.0, 3.0)
        bar_len = int(ratio * 10)
        bar = "█" * bar_len + "░" * (30 - bar_len)
        lines.append(f"### {req}")
        lines.append(f"  {bar}  **{data['years']} years**")
        lines.append(f"  {data['evidence']}")
        lines.append("")
    lines.append("---")
    lines.append(
        "**Overall:** Mark exceeds every listed requirement by 2–3×. "
        "His 19 years at Microsoft, hands-on AI/cloud expertise, and "
        "Americas-wide impact make him an exceptionally strong fit."
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------


@mcp.prompt()
def interview_mark() -> str:
    """A prompt template for conducting a mock interview with Mark Franco."""
    return (
        "You are a senior hiring manager at GitHub conducting a final-round "
        "interview for the Strategic AI GTM Lead, Americas role. The candidate "
        "is Mark Franco.\n\n"
        "Use the resume MCP server tools to look up Mark's background, then "
        "ask him probing questions about:\n"
        "1. His experience leading enterprise AI engagements\n"
        "2. How he would drive GitHub Copilot adoption in large enterprises\n"
        "3. A specific deal he's won and the strategy behind it\n"
        "4. How he handles competitive displacement (e.g., AWS/GCP → Azure)\n"
        "5. His vision for AI-driven developer productivity over the next 3 years\n\n"
        "After each answer, evaluate the response against what you know from "
        "the resume data and ask follow-up questions. Be thorough but fair."
    )


@mcp.prompt()
def qualification_deep_dive(area: str) -> str:
    """A prompt for exploring a specific qualification area in depth.

    Args:
        area: The qualification area to explore (e.g., 'Agentic AI', 'Cloud', 'Security').
    """
    return (
        f"You are researching Mark Franco's qualifications in **{area}**.\n\n"
        "Use the resume MCP server tools to:\n"
        f"1. Search for all references to '{area}' across the resume\n"
        f"2. Identify specific projects, certifications, and experience related to {area}\n"
        "3. Compare his expertise against typical requirements for a senior GTM role\n"
        "4. Provide a confidence rating (1-10) on his depth in this area\n\n"
        "Be specific — cite repos, certifications, and engagement examples."
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
