"""Message type identifiers for problem reports."""

from ...didcomm_prefix import DIDCommPrefix

SPEC_URI = (
    "https://github.com/hyperledger/aries-rfcs/tree/"
    "89d14c15ab35b667e7a9d04fe42d4d48b10468cf/features/0035-report-problem"
)

# Message types
PROBLEM_REPORT = f"notification/1.0/problem-report"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.problem_report.v1_0"

MESSAGE_TYPES = {
    pfx.qualify(PROBLEM_REPORT): f"{PROTOCOL_PACKAGE}.message.ProblemReport"
    for pfx in DIDCommPrefix
}
