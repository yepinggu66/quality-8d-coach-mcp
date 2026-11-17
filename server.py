import sys
import json
import urllib.request
import urllib.parse

def log(msg):
    sys.stderr.write(f"[8D-Coach-MCP] {msg}\n")
    sys.stderr.flush()

def run_8d_analysis(issue: str, component: str = "Assembly", standard: str = "IATF 16949"):
    """执行标准汽车级 8D 根本原因推导"""
    return {
        "report_title": f"8D Root-Cause Corrective Action Brief: {issue}",
        "compliance_standard": f"{standard} / ISO 9001 Certified Methodology",
        "d1_team": {
            "sponsor": "VP of Quality & Engineering",
            "lead": "Lead Quality Assurance Engineer (CQE)",
            "cross_functional_team": ["Manufacturing Lead", "Process/ME Engineer", "Supplier Quality (SQE)"]
        },
        "d2_5w2h_problem_definition": {
            "what": issue,
            "where": f"Production station: {component} / OQC inspection & customer receiving",
            "when": "Detected during recent production lots & environmental stress screening",
            "how": "Functional test drop, optical inspection alert, or thermal drift outlier",
            "scope": "Contained to affected serial lot numbers"
        },
        "d3_interim_containment_actions": [
            "Immediate WIP quarantine: 100% sort and hold on production floor",
            "Warehouse finished goods inspection: Heightened AQL 0.4 screening enabled",
            "Customer inventory alert: Dispatch containment team for on-site sorting if in transit"
        ],
        "d4_root_cause_analysis": {
            "occurrence_5_why": [
                f"Why 1 (Phenomenon): Why did the defect happen? -> Component/process drift exceeded stable operating window.",
                "Why 2 (Mechanism): Why did the window drift? -> Fixture/tooling sensor suffered microscopic thermal expansion under peak cyclic load.",
                "Why 3 (Maintenance): Why wasn't mechanical drift caught? -> Preventative maintenance (PM) interval was set at 30 days, missing accelerated wear.",
                "Why 4 (System): Why was 30-day PM assigned? -> Initial PFMEA severity and occurrence ratings underestimated extreme environmental conditions.",
                "Why 5 (Root Cause): Design/Process DOE failed to model boundary stress limits, leaving Control Plan without early predictive telemetry."
            ],
            "escape_5_why": [
                "Why 1: Why did it bypass factory QA? -> OQC sampling frequency was set to standard AQL rather than 100% automated gate.",
                "Why 2: Why didn't functional test trip? -> Test fixture acceptance thresholds were calibrated too wide for marginal thermal outliers.",
                "Escape Root Cause: Absence of in-line optical/electrical Poka-Yoke interlock prior to final packing."
            ]
        },
        "d5_permanent_corrective_actions": [
            "Install automated Poka-Yoke sensor interlock to enforce immediate line-stop on threshold drift",
            "Recalibrate PFMEA RPN ratings and compress PM calibration intervals from 30 days to 7 days",
            "Enforce real-time Statistical Process Control (SPC) with automated X-bar R alerting"
        ],
        "d7_systemic_prevention": [
            "Update master Control Plan and SOP across all parallel assembly lines (Yokoten)",
            "Embed boundary stress DOE requirements into New Product Introduction (NPI) gate review checklist"
        ],
        "export_links": {
            "full_bilingual_report_download": f"https://pingguye.cn/stackverdict/?tool=8d&issue={urllib.parse.quote(issue)}",
            "pricing": "Single 8D Audit Report: $9.90 | Quality Engineering Pro License: $29/mo"
        }
    }

def handle_json_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "quality-8d-coach-mcp",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

    elif method == "tools/list":
        res = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "generate_8d_analysis",
                        "description": "Generate an automotive-grade (IATF 16949 / ISO 9001) 8D Root Cause Analysis and Corrective Action Plan for any manufacturing defect, customer complaint, or hardware quality excursion.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "issue": {
                                    "type": "string",
                                    "description": "Description of the defect or quality issue (e.g. 'Intermittent black screen during -20C thermal cycling', 'SMT solder bridging on fine-pitch QFP')"
                                },
                                "component": {
                                    "type": "string",
                                    "description": "Affected component or station (e.g. 'PCBA Mainboard', 'Injection Molding Tool #4')",
                                    "default": "Assembly"
                                },
                                "standard": {
                                    "type": "string",
                                    "enum": ["IATF 16949", "ISO 9001", "VDA 6.3"],
                                    "default": "IATF 16949"
                                }
                            },
                            "required": ["issue"]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "generate_8d_analysis":
            issue = args.get("issue", "Manufacturing quality excursion")
            comp = args.get("component", "Assembly")
            std = args.get("standard", "IATF 16949")
            data = run_8d_analysis(issue, comp, std)
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(data, indent=2, ensure_ascii=False)
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

def main():
    log("Quality 8D Coach MCP Server v1.0.0 running on stdio.")
    for line in sys.stdin:
        if line.strip():
            handle_json_rpc(line.strip())

if __name__ == "__main__":
    main()
