# 🏭 Quality 8D Coach · MCP Server

[![GitHub Release](https://img.shields.io/github/v/release/yepinggu66/quality-8d-coach-mcp)](https://github.com/yepinggu66/quality-8d-coach-mcp/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: IATF 16949](https://img.shields.io/badge/Standard-IATF_16949_%2F_ISO_9001-green)](https://pingguye.cn/stackverdict/?tool=8d)

**Automotive-grade Root Cause Analysis (RCA) and 8D Corrective Action Copilot.** Designed for Quality Assurance Engineers, Hardware Designers, and Factory Operations using **Claude Desktop**, **Cursor**, and **Windsurf**.

---

## ⚡ 1-Minute Quickstart

### Claude Desktop Configuration
Add the following to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "quality-8d-coach": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

### Cursor / Windsurf Configuration
In **Cursor Settings -> Features -> MCP -> Add New MCP Server**:
* **Name**: `quality-8d-coach`
* **Type**: `command`
* **Command**: `python /path/to/server.py`

---

## 🛠️ Available MCP Tools

### `generate_8d_analysis`
Instantly synthesizes a structured, audit-ready 8D investigation matrix following global automotive & electronics quality standards:

* **D1 (Team)**: Cross-functional operational team assignment
* **D2 (5W2H)**: Strict problem definition and boundary scoping
* **D3 (ICA)**: Immediate Work-In-Progress (WIP) quarantine, inventory sort, and containment gates
* **D4 (RCA)**: Two-pronged 5-Why root cause deduction:
  * **Occurrence Root Cause**: Why did the physics/process fail?
  * **Escape Root Cause**: Why did OQC/inspection gates fail to catch it?
* **D5/D6 (PCA)**: Permanent corrective action and automated Poka-Yoke (mistake-proofing) interlocks
* **D7 (Prevention)**: PFMEA RPN recalibration, Control Plan updates, and cross-line horizontal deployment (Yokoten)

---

## 💰 Commercial Pricing & Enterprise Plant Deployment

| Tier | Scope & Features | Pricing | Deliverables |
| :--- | :--- | :--- | :--- |
| **Online Studio & PDF** | Single audit-ready automotive 8D report generation | **$9.90** | Instant PDF/Word export via [StackVerdict Studio](https://pingguye.cn/stackverdict/?tool=8d) |
| **Quality Engineer Pro** | Unlimited RCA simulations & interactive FMEA linkage | **$29 / mo** | Cloud workspace & priority rule updates |
| **On-Premise Plant Pilot** | Air-gapped pilot container for up to 25 production machines (Furnaces, Jet Mills, Presses) | **$499 / mo** | Docker image, 31 master SOP models, 14-day setup & telemetry config |
| **Turnkey Plant Buyout** | Perpetual on-premise license, clean-room source code, micro-leakage algorithms & 1-year architecture advisory | **$18,800 USD** (¥135,000) | Full source code, complete SOP documentation & zero-cloud deployment |

* 🌐 **Interactive Demo**: [N52SH Vacuum Sintering Furnace RCA Simulation](https://pingguye.cn/stackverdict/magfactory)
* 📩 **Commercial Inquiries & Procurement**: [yepinggu6@gmail.com](mailto:yepinggu6@gmail.com) | PayPal: `yepinggu6@gmail.com`

---

## 📄 License
MIT © StackVerdict Quality Lab & yepinggu66
