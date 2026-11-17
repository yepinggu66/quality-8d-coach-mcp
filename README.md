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

## 💰 Pro License & Export

* 🌐 **Online Live Studio**: [https://pingguye.cn/stackverdict/?tool=8d](https://pingguye.cn/stackverdict/?tool=8d)
* 📄 **Single Automotive 8D Report Export (Word/PDF)**: $9.90
* 🚀 **Enterprise Quality Pro License**: $29/mo (Unlimited RCA simulations & FMEA linkage)

---

## 📄 License
MIT © StackVerdict Quality Lab & yepinggu66
